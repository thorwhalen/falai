"""Typed exceptions for falaw operations.

The bare ``fal_client`` exposes ``FalClientError``, ``FalClientHTTPError``, and
``FalClientTimeoutError``. These are correct but coarse — every 403, 429,
402, and timeout looks the same to a caller. This module wraps fal_client
errors in a more specific hierarchy so:

- An agent can catch :class:`FalAccountLocked` and surface a "go fix billing"
  message instead of debugging a generic 403.
- A retry layer can catch :class:`FalRateLimited` and back off, but let
  :class:`FalAccountLocked` propagate (no amount of retry will fix it).
- Scripts can catch :class:`FalDurationOutOfRange` to fall back to splitting
  a shot, instead of silently truncating to whatever the model produced.

Use :func:`translate` to convert a fal_client exception to the appropriate
typed subclass — :func:`falaw.core.call_fal` does this automatically.

Examples
--------

>>> err = FalAccountLocked(
...     "account locked",
...     status_code=403,
...     detail="Verify your email at fal.ai/settings",
...     url="https://fal.ai/dashboard/billing",
... )
>>> err.url
'https://fal.ai/dashboard/billing'
>>> isinstance(err, FalError)
True
"""

from __future__ import annotations

from typing import Any


class FalError(Exception):
    """Base for all falaw-raised exceptions."""


class FalHTTPError(FalError):
    """Wraps an HTTP error from fal.ai with the original status, body, and headers.

    Subclasses pick out specific status codes / patterns. Use this base when
    you want to catch any HTTP failure (e.g. for retry).
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        detail: str = "",
        body: Any = None,
        headers: dict[str, str] | None = None,
        application: str | None = None,
        url: str | None = None,
        cause: BaseException | None = None,
    ):
        super().__init__(message)
        self.status_code = status_code
        self.detail = detail
        self.body = body
        self.headers = headers or {}
        self.application = application
        self.url = url
        self.__cause__ = cause


class FalAccountLocked(FalHTTPError):
    """fal account is locked / suspended / awaiting verification.

    Typical 403 with a body indicating the account is not in good standing.
    No amount of retrying or model-switching will fix this — the user has
    to act (verify email, top up billing, contact support).
    """


class FalUnauthorized(FalHTTPError):
    """Missing or invalid API credentials — typical 401."""


class FalRateLimited(FalHTTPError):
    """fal is throttling requests — typical 429.

    ``retry_after_s`` is parsed from the ``Retry-After`` header if present,
    else ``None`` (caller decides backoff).
    """

    def __init__(
        self,
        message: str,
        *,
        retry_after_s: float | None = None,
        **kwargs,
    ):
        super().__init__(message, **kwargs)
        self.retry_after_s = retry_after_s


class FalInsufficientFunds(FalHTTPError):
    """Account balance is insufficient — typical 402."""


class FalBadRequest(FalHTTPError):
    """Server rejected the request payload — typical 400 / 422."""


class FalServerError(FalHTTPError):
    """fal-side server error — typical 5xx. Generally retryable."""


class FalTimeout(FalError):
    """The fal call timed out before producing a result."""

    def __init__(
        self, message: str, *, elapsed_s: float, application: str | None = None
    ):
        super().__init__(message)
        self.elapsed_s = elapsed_s
        self.application = application


class FalModelHung(FalError):
    """A model was queued but never returned — distinct from a network timeout.

    Raised by higher-level orchestration that sets a per-call wall-clock
    budget (e.g. "give up on this lipsync after 5 minutes and pick another model").
    """

    def __init__(self, message: str, *, model_id: str, elapsed_s: float):
        super().__init__(message)
        self.model_id = model_id
        self.elapsed_s = elapsed_s


class FalDurationOutOfRange(FalError):
    """The requested duration is outside what the model can produce.

    Raised by Plan/Execute when the caller asks for ``duration_s`` that the
    model's declared ``expected_duration_range`` cannot satisfy. Callers can
    catch this to split the shot, repeat it, or pick a different model.
    """

    def __init__(
        self,
        message: str,
        *,
        model_id: str,
        requested: float,
        valid_range: tuple[float, float],
    ):
        super().__init__(message)
        self.model_id = model_id
        self.requested = requested
        self.valid_range = valid_range


# --- Translation from fal_client errors --------------------------------------


_LOCK_PATTERNS = (
    "account is locked",
    "account locked",
    "account is suspended",
    "verify your email",
    "verify your account",
)


def translate(exc: BaseException, *, application: str | None = None) -> BaseException:
    """Convert an underlying fal_client / network exception to a typed falaw exception.

    Returns the original exception unchanged if no specific subclass applies
    (so callers always get *something* — never silently swallowed).

    Logic:

    - ``FalClientHTTPError`` with 403 + lock-pattern body → :class:`FalAccountLocked`
    - ``FalClientHTTPError`` with 401 → :class:`FalUnauthorized`
    - ``FalClientHTTPError`` with 402 → :class:`FalInsufficientFunds`
    - ``FalClientHTTPError`` with 429 → :class:`FalRateLimited` (parses Retry-After)
    - ``FalClientHTTPError`` with 4xx → :class:`FalBadRequest`
    - ``FalClientHTTPError`` with 5xx → :class:`FalServerError`
    - ``FalClientTimeoutError`` → :class:`FalTimeout`
    - anything else → returned unchanged
    """
    try:
        import fal_client  # type: ignore[import-untyped]
    except ImportError:
        return exc

    # Tests stub `fal_client` with a SimpleNamespace that may lack these
    # classes; use getattr to fall back to the bare exception type.
    timeout_cls = getattr(fal_client, "FalClientTimeoutError", None)
    http_cls = getattr(fal_client, "FalClientHTTPError", None)

    if timeout_cls is not None and isinstance(exc, timeout_cls):
        elapsed = getattr(exc, "elapsed_s", None) or 0.0
        return FalTimeout(
            f"call_fal({application!r}) timed out after {elapsed}s",
            elapsed_s=float(elapsed),
            application=application,
        )

    if http_cls is None or not isinstance(exc, http_cls):
        return exc

    status = exc.status_code
    headers = dict(exc.response_headers) if exc.response_headers else {}
    body_text, body_obj = _read_body(exc)
    body_lower = body_text.lower() if body_text else ""

    common = dict(
        status_code=status,
        detail=body_text,
        body=body_obj,
        headers=headers,
        application=application,
        cause=exc,
    )

    if status == 403 and any(p in body_lower for p in _LOCK_PATTERNS):
        return FalAccountLocked(
            f"fal account locked / unverified (HTTP 403): {body_text or exc.message}",
            url="https://fal.ai/dashboard/billing",
            **common,
        )
    if status == 401:
        return FalUnauthorized(
            f"unauthorized (HTTP 401) — check FAL_KEY: {body_text or exc.message}",
            **common,
        )
    if status == 402:
        return FalInsufficientFunds(
            f"insufficient funds (HTTP 402): {body_text or exc.message}",
            url="https://fal.ai/dashboard/billing",
            **common,
        )
    if status == 429:
        retry_after = _parse_retry_after(headers.get("retry-after"))
        return FalRateLimited(
            f"rate limited (HTTP 429): {body_text or exc.message}",
            retry_after_s=retry_after,
            **common,
        )
    if 400 <= status < 500:
        return FalBadRequest(
            f"bad request (HTTP {status}): {body_text or exc.message}",
            **common,
        )
    if 500 <= status < 600:
        return FalServerError(
            f"fal server error (HTTP {status}): {body_text or exc.message}",
            **common,
        )

    # Unknown status — wrap conservatively but still surface specifics.
    return FalHTTPError(
        f"HTTP {status}: {body_text or exc.message}",
        **common,
    )


def _read_body(exc) -> tuple[str, Any]:
    """Best-effort read of an httpx-backed FalClientHTTPError's body.

    fal_client swallows the JSON body in __str__; we go to .response directly.
    Returns (text, parsed-object-or-None). Both are best-effort.
    """
    response = getattr(exc, "response", None)
    if response is None:
        return ("", None)
    text = ""
    try:
        text = response.text or ""
    except Exception:
        pass
    parsed = None
    try:
        parsed = response.json()
        # Prefer the "detail" / "message" / "error" sub-field if present.
        if isinstance(parsed, dict):
            for key in ("detail", "message", "error"):
                if key in parsed and isinstance(parsed[key], str):
                    text = parsed[key]
                    break
    except Exception:
        pass
    return (text, parsed)


def _parse_retry_after(value: str | None) -> float | None:
    if not value:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        # Could be an HTTP-date; we don't bother parsing — None is fine.
        return None
