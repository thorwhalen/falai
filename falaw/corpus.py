"""Extract model records from `misc/docs/llms-full.txt`.

The fal.ai llms-full.txt has a regular structure:

    ## <Section heading>
    <paragraph>

    ### <Model name>
    - **Model**: `fal-ai/<id>`
    - **Purpose**: <one-liner>
    - **Features**: <details>

We map the section to a category, infer a quality tier from the model
name, and emit ModelRecord-shaped dicts the registry can consume. The
`refresh_models_from_corpus` tool merges these into `data/models.json`,
adding new models without overwriting hand-curated entries.
"""

from __future__ import annotations

import json
import os
import re
from typing import Iterator, Optional

from .journal import _default_journal
from .registry import _load_models, _models_path, register_tool

# Section heading -> category for our registry.
_SECTION_TO_CATEGORY = {
    "high quality image generation models": "image",
    "fast and quality image generation models": "image",
    "image editing tools": "image_edit",
    "ready-to-go image editing pipelines": "image_edit",
    "video generation models": "video",
    "audio processing & enhancement tools": "audio",
    "avatar & lip sync tools": "lipsync",
    "text-to-speech tools": "tts",
    "large language models (llms)": "llm",
    "background removal & image tools": "background_removal",
    "music & audio generation": "music",
    "training & personalization": "training",
}

# Tier inference from heading keywords (longest-match wins via order below).
_TIER_KEYWORDS = (
    ("ultra", "ultra"),
    (" max", "ultra"),
    ("master", "ultra"),
    (" pro", "high"),
    (" hd", "high"),
    ("schnell", "fast"),
    ("sprint", "fast"),
    (" fast", "fast"),
    (" flash", "fast"),
    (" dev", "balanced"),
    (" turbo", "fast"),
)


def _infer_tier(name: str) -> str:
    n = " " + name.lower() + " "
    for kw, tier in _TIER_KEYWORDS:
        if kw in n:
            return tier
    return "balanced"


def _refine_video_category(model_id: str, name: str) -> str:
    blob = (model_id + " " + name).lower()
    if "image-to-video" in blob or "image to video" in blob:
        return "image_to_video"
    if "text-to-video" in blob or "text to video" in blob:
        return "text_to_video"
    return "video"


def _parse_entry_block(block: str) -> Optional[dict]:
    """Parse one ``### Name\n- **Model**: ...`` block."""
    lines = block.split("\n")
    name = lines[0].strip()
    if not name:
        return None
    metadata: dict = {}
    for line in lines[1:]:
        m = re.match(r"^\s*-\s*\*\*([^*]+)\*\*:\s*(.+?)\s*$", line)
        if m:
            metadata[m.group(1).strip().lower()] = m.group(2).strip()
    model_id_text = metadata.get("model", "")
    m = re.match(r"`(fal-ai/[^`]+)`", model_id_text)
    if not m:
        return None
    return {
        "name": name,
        "id": m.group(1),
        "purpose": metadata.get("purpose", ""),
        "features": metadata.get("features", ""),
    }


def extract_models_from_corpus(path: str) -> Iterator[dict]:
    """Yield ModelRecord-shaped dicts parsed from llms-full.txt."""
    with open(path) as f:
        text = f.read()
    sections = re.split(r"^## ", text, flags=re.MULTILINE)
    for sec in sections[1:]:  # skip preamble before the first ##
        head_end = sec.find("\n")
        heading = sec[:head_end].strip().lower() if head_end != -1 else ""
        category = _SECTION_TO_CATEGORY.get(heading)
        if not category:
            continue
        body = sec[head_end:] if head_end != -1 else ""
        for entry in re.split(r"\n### ", body)[1:]:
            parsed = _parse_entry_block(entry)
            if not parsed:
                continue
            cat = category
            if cat == "video":
                cat = _refine_video_category(parsed["id"], parsed["name"])
            yield {
                "id": parsed["id"],
                "category": cat,
                "description": parsed["purpose"]
                or parsed["features"]
                or parsed["name"],
                "aliases": [],
                "quality_tier": _infer_tier(parsed["name"]),
                "cost_hint": "",
                "docs_url": f"https://fal.ai/models/{parsed['id']}",
            }


def _default_corpus_path() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(here, "..", "misc", "docs", "llms-full.txt"))


@register_tool(
    name="refresh_models_from_corpus",
    description=(
        "Parse `misc/docs/llms-full.txt` and merge any newly-discovered "
        "models into `falaw/data/models.json`. Hand-curated entries are "
        "preserved; only previously-unknown ids are added. Pass "
        "`write=True` to persist; otherwise returns a dry-run summary."
    ),
    tags=("refresh", "maintenance", "registry"),
    input_schema={
        "type": "object",
        "properties": {
            "path": {"type": "string"},
            "write": {"type": "boolean", "default": False},
        },
    },
    output_schema={"type": "object"},
)
def refresh_models_from_corpus(
    *,
    path: Optional[str] = None,
    write: bool = False,
) -> dict:
    """Merge corpus-discovered models into models.json (additive).

    Returns ``{added, total, from_corpus, write}`` summary. Setting
    ``write=False`` (the default) reports what *would* change without
    touching the file.
    """
    path = path or _default_corpus_path()
    if not os.path.exists(path):
        return {"error": f"corpus not found: {path}"}
    new_records = list(extract_models_from_corpus(path))

    seed_path = _models_path()
    with open(seed_path) as f:
        existing = {r["id"]: r for r in json.load(f)}

    added_ids: list[str] = []
    for rec in new_records:
        if rec["id"] not in existing:
            existing[rec["id"]] = rec
            added_ids.append(rec["id"])

    summary = {
        "added": len(added_ids),
        "added_ids": added_ids[:20],
        "total": len(existing),
        "from_corpus": len(new_records),
        "write": write,
    }

    if write and added_ids:
        merged = sorted(
            existing.values(),
            key=lambda r: (r.get("category", ""), r.get("quality_tier", ""), r["id"]),
        )
        with open(seed_path, "w") as f:
            json.dump(merged, f, indent=2, ensure_ascii=False)
            f.write("\n")
        _load_models.cache_clear()
        _default_journal().append(
            kind="note",
            text=f"refresh_models_from_corpus: added {len(added_ids)} models",
            tags=("refresh", "registry"),
            context={"sample_added": added_ids[:10]},
        )

    return summary
