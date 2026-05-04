"""Wrapper over `fal_client.subscribe` with progress events and auto-journaling.

Operations should call `call_fal` rather than `fal_client.subscribe` directly,
so we get one place to:

* publish structured progress events to subscribers (UI, telemetry),
* auto-journal failures (so the next agent learns from them),
* layer retries / backoff later without changing call sites.

See :mod:`falaw.events` for the event model. ``on_log`` (a
string-only callback) still works for backward compatibility — when
both ``on_log`` and ``on_event`` are given, both fire.
"""

from __future__ import annotations

import time
import uuid
from typing import Any, Callable, Mapping, Optional

from .events import EventCallback, ProgressEvent, emit
from .journal import _default_journal


def call_fal(
    application: str,
    arguments: Mapping[str, Any],
    *,
    on_log: Optional[Callable[[str], None]] = None,
    on_event: Optional[EventCallback] = None,
    with_logs: bool = True,
    journal_errors: bool = True,
) -> dict:
    """Call a fal model via fal_client.subscribe.

    Args:
        application: fal model id (e.g. ``"fal-ai/flux/dev"``).
        arguments: Input arguments. Keys depend on the model.
        on_log: Legacy log callback — receives raw log lines as strings.
            Defaults to no-op (use ``on_event`` for structured access).
        on_event: Per-call subscriber for :class:`ProgressEvent`s. Fires
            in addition to the global subscribers registered via
            :func:`falaw.events.subscribe`.
        with_logs: Pass through to fal_client; when True the model streams logs.
        journal_errors: When True, exceptions are recorded as journal issues
            before being re-raised. The journal entry includes the application
            id and arguments so future agents can recognize the same trap.

    Returns:
        The raw response dict from the model.
    """
    import fal_client  # lazy: keep import out of `from falaw import ...`

    call_id = uuid.uuid4().hex[:12]
    started = time.time()

    def _ev(kind: str, *, message: str = "", pct: float | None = None) -> None:
        emit(
            ProgressEvent(
                kind=kind,  # type: ignore[arg-type]
                application=application,
                call_id=call_id,
                message=message,
                pct=pct,
                elapsed_s=time.time() - started,
            ),
            also=(on_event,) if on_event else (),
        )

    log = on_log if on_log is not None else (lambda _msg: None)

    def _on_queue_update(update):
        if isinstance(update, fal_client.InProgress):
            entries = update.logs or ()
            if not entries:
                _ev("progress")
                return
            for entry in entries:
                msg = entry.get("message") if isinstance(entry, dict) else None
                if msg:
                    log(msg)
                    _ev("log", message=msg)

    _ev("queued")
    try:
        result = fal_client.subscribe(
            application,
            arguments=dict(arguments),
            with_logs=with_logs,
            on_queue_update=_on_queue_update,
        )
    except Exception as exc:
        _ev("error", message=repr(exc))
        if journal_errors:
            _default_journal().append(
                kind="issue",
                text=f"call_fal({application!r}) failed: {exc!r}",
                tags=("call_fal", "error"),
                context={
                    "application": application,
                    "arguments": dict(arguments),
                    "duration_s": time.time() - started,
                },
            )
        raise
    _ev("done")
    return result
