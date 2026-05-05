"""Structured progress events for fal calls.

Replaces the implicit "stream raw log strings to stdout" model with a
small, machine-readable event stream that orchestrators can subscribe
to (UI progress bars, cost telemetry, billing dashboards, etc.).

A ``ProgressEvent`` is emitted at every major lifecycle transition of
a single ``call_fal`` invocation:

- ``queued``      — call submitted to fal
- ``progress``    — fal pushed an InProgress update with no message body
- ``log``         — fal pushed an InProgress update with a log line
- ``done``        — call returned a result
- ``error``       — call raised
- ``cache_hit``   — :func:`falaw.cached_call_fal` found a hit and skipped the network

Subscribers can be registered globally via :func:`subscribe` or
per-call via the ``on_event=`` argument on :func:`call_fal` /
:func:`cached_call_fal`. The ``on_log`` parameter still works
(legacy: a string-only stream); see :func:`call_fal` for compatibility
notes.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, Literal, Optional


EventKind = Literal["queued", "progress", "log", "done", "error", "cache_hit"]

EventCallback = Callable[["ProgressEvent"], None]


@dataclass(frozen=True, slots=True, kw_only=True)
class ProgressEvent:
    """One step in the lifecycle of a fal call.

    Attributes:
        kind: Lifecycle stage. See :data:`EventKind`.
        application: fal model id (e.g. ``"fal-ai/flux/dev"``).
        call_id: A short hex string that uniquely identifies the call.
            All events for one ``call_fal`` invocation share the same
            ``call_id``.
        message: Free-form text. For ``"log"`` events this is the log
            line; for ``"error"`` it's ``repr(exc)``; otherwise empty.
        pct: Optional progress percentage in [0.0, 100.0]. fal's
            current API doesn't surface this; included for forward
            compatibility.
        elapsed_s: Seconds since the call started.
    """

    kind: EventKind
    application: str
    call_id: str
    message: str = ""
    pct: Optional[float] = None
    elapsed_s: float = 0.0


# --- subscriber registry ---------------------------------------------------

_subscribers: list[EventCallback] = []


def subscribe(callback: EventCallback) -> EventCallback:
    """Register ``callback`` to receive every emitted ProgressEvent.

    Returns the callback unchanged so it can be used as a decorator::

        @subscribe
        def log_to_file(ev: ProgressEvent) -> None:
            ...
    """
    if callback not in _subscribers:
        _subscribers.append(callback)
    return callback


def unsubscribe(callback: EventCallback) -> None:
    """Remove a previously :func:`subscribe`'d callback. No-op if absent."""
    try:
        _subscribers.remove(callback)
    except ValueError:
        pass


def clear_subscribers() -> None:
    """Drop all registered subscribers. Mostly for tests."""
    _subscribers.clear()


def emit(event: ProgressEvent, *, also: Iterable[EventCallback] = ()) -> None:
    """Send ``event`` to every registered subscriber + the ``also`` list.

    Subscriber exceptions are swallowed (with a printed warning) so a
    misbehaving UI hook can't bring the rendering pipeline down.
    """
    for cb in list(_subscribers) + list(also):
        try:
            cb(event)
        except Exception as exc:  # pragma: no cover — defensive
            import warnings

            warnings.warn(f"falaw progress subscriber {cb!r} raised: {exc!r}")
