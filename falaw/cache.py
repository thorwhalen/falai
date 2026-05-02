"""Content-addressed cache for fal calls.

Why this exists: the directorial workflow ("a single edit, the scene
re-renders around it") only works if unchanged beats *don't* re-render.
A cache hit is the difference between a 30-second edit-and-preview
loop and a 5-minute one.

Design:

* Key = SHA256 of (model_id, sorted(arguments_json)). Two structurally
  identical fal calls collapse to the same key.
* Value = the raw fal response, plus optional locally-downloaded asset
  paths. We persist both the JSON manifest and the binary downloads.
* Cache root: ``$FALAW_CACHE_DIR`` or ``$FALAW_DATA_DIR/cache`` or
  ``~/.config/falaw/cache``.
* The cache is *per-process* aware via lru_cache for hot lookups;
  on-disk for persistence across runs.

Usage:

    from falaw.cache import cached_call_fal
    raw = cached_call_fal("fal-ai/flux/dev", {"prompt": "..."})

The wrapped variant has the same signature as `core.call_fal` but skips
the network when the (model_id, arguments) tuple was seen before.
"""

from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.request
from typing import Any, Mapping, Optional

from .core import call_fal


# --- cache root -----------------------------------------------------------


def _cache_dir() -> str:
    base = (
        os.environ.get("FALAW_CACHE_DIR")
        or (os.environ.get("FALAW_DATA_DIR") and
            os.path.join(os.environ["FALAW_DATA_DIR"], "cache"))
        or os.path.expanduser("~/.config/falaw/cache")
    )
    os.makedirs(base, exist_ok=True)
    return base


def _key(application: str, arguments: Mapping[str, Any]) -> str:
    blob = json.dumps(
        {"app": application, "args": dict(arguments)},
        sort_keys=True,
        default=str,
    ).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def _entry_dir(key: str) -> str:
    # Two-char shard so the cache directory listing stays manageable.
    d = os.path.join(_cache_dir(), key[:2], key)
    os.makedirs(d, exist_ok=True)
    return d


def _manifest_path(key: str) -> str:
    return os.path.join(_entry_dir(key), "manifest.json")


# --- public API -----------------------------------------------------------


def cache_get(application: str, arguments: Mapping[str, Any]) -> Optional[dict]:
    """Return the raw fal response if cached, else None."""
    path = _manifest_path(_key(application, arguments))
    if not os.path.exists(path):
        return None
    with open(path) as f:
        manifest = json.load(f)
    return manifest.get("raw")


def cache_put(
    application: str,
    arguments: Mapping[str, Any],
    raw: dict,
    *,
    note: str = "",
) -> str:
    """Persist a fal response. Returns the entry directory path."""
    key = _key(application, arguments)
    d = _entry_dir(key)
    manifest = {
        "key": key,
        "application": application,
        "arguments": dict(arguments),
        "raw": raw,
        "note": note,
        "stored_at": time.time(),
    }
    with open(_manifest_path(key), "w") as f:
        json.dump(manifest, f, indent=2, default=str)
    return d


def cached_call_fal(
    application: str,
    arguments: Mapping[str, Any],
    *,
    refresh: bool = False,
) -> dict:
    """Call a fal model, but reuse the cached response when present.

    Args:
        application: fal model id.
        arguments: model input dict.
        refresh: if True, bypass the cache and overwrite it with a fresh result.

    Returns:
        Raw fal response (whether from cache or network).
    """
    if not refresh:
        hit = cache_get(application, arguments)
        if hit is not None:
            return hit
    raw = call_fal(application, arguments)
    cache_put(application, arguments, raw)
    return raw


def materialize_asset(url: str, *, key_hint: str = "") -> str:
    """Download a remote asset to the cache and return the local path.

    The local filename is content-addressed by the URL, so calling this
    twice for the same URL is free.
    """
    h = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
    ext = _infer_ext_from_url(url)
    fname = f"{key_hint + '-' if key_hint else ''}{h}{ext}"
    path = os.path.join(_cache_dir(), "assets", fname)
    if os.path.exists(path):
        return path
    os.makedirs(os.path.dirname(path), exist_ok=True)
    urllib.request.urlretrieve(url, path)
    return path


def _infer_ext_from_url(url: str) -> str:
    base = url.split("?", 1)[0]
    for ext in (".mp4", ".mov", ".webm", ".mp3", ".wav", ".m4a",
                ".png", ".jpg", ".jpeg", ".webp"):
        if base.lower().endswith(ext):
            return ext
    return ".bin"


def cache_stats() -> dict:
    """Quick summary of the cache: entry count and disk usage."""
    root = _cache_dir()
    entries = 0
    total_bytes = 0
    for dirpath, _dirs, files in os.walk(root):
        for f in files:
            entries += int(f == "manifest.json")
            total_bytes += os.path.getsize(os.path.join(dirpath, f))
    return {
        "root": root,
        "manifest_entries": entries,
        "size_bytes": total_bytes,
        "size_mb": round(total_bytes / 1_000_000, 2),
    }
