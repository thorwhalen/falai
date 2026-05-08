"""Plan / Execute primitives — separate planning (data) from execution (effects).

Today every falaw operation is eager: ``generate_image(prompt)`` makes the
API call immediately. That means:

- A budget gate has to predict cost from outside the call and *hope* the
  prediction matches what the operation will actually do.
- Tests need a fake fal_client to exercise any code that touches an
  operation, even when the test is about composition or cost.
- A UI can't show "you're about to spend $4.12, click confirm" without
  a separate, parallel cost-prediction code path.

The fix is to give every operation two surfaces:

1. ``plan_X(...) -> CallPlan``: pure data describing the call that *would*
   happen — model_id, arguments, predicted cost, cache status. No API contact.
2. ``execute(plan, ...) -> list[Artifact]``: turns a Plan (one or more
   CallPlans) into materialized Artifacts. The eager wrappers
   (``generate_image``, etc.) are now thin: ``execute(plan_X(...))[0]``.

A higher-level orchestrator (a music-video render, a storyboard generation)
builds a Plan by composing CallPlans across multiple operations. The Plan
gets a typed ``total_cost_usd``, can be inspected, edited, dry-run, or
serialized — all without the network.

Examples
--------

>>> from falaw.plan import CallPlan, Plan
>>> p1 = CallPlan(
...     tool="generate_image",
...     application="fal-ai/flux/dev",
...     arguments={"prompt": "a tiger", "image_size": "landscape_4_3"},
...     output_kind="image",
...     estimated_cost_usd=0.025,
...     cache_status="miss",
... )
>>> p2 = CallPlan(
...     tool="image_to_video",
...     application="fal-ai/minimax/hailuo-02/pro/image-to-video",
...     arguments={"image_url": "<from p1>"},
...     output_kind="video",
...     estimated_cost_usd=0.50,
...     cache_status="miss",
... )
>>> plan = Plan(calls=(p1, p2))
>>> plan.total_cost_usd
0.525
>>> plan.cache_hit_savings_usd
0.0
>>> [c.tool for c in plan.calls]
['generate_image', 'image_to_video']

Plans concatenate, so an orchestrator can build one shot's Plan and then
append it to a scene-level Plan:

>>> shot_plan = Plan(calls=(p1,))
>>> scene_plan = Plan(calls=()) + shot_plan + Plan(calls=(p2,))
>>> len(scene_plan.calls)
2
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Any, Callable, Literal, Optional


CacheStatus = Literal["hit", "miss", "stale", "unknown"]
"""Whether the cache will short-circuit this call.

- ``hit``: A cached response exists and will be returned without an API call.
- ``miss``: No cache entry; the call will hit fal.
- ``stale``: An entry exists but is expected to be invalidated (e.g. a
  ``force=True`` re-render asked for it). Today we don't distinguish stale
  from miss for cost — both are billed.
- ``unknown``: Plan was built without consulting the cache.
"""


OutputKind = Literal["image", "video", "audio", "json", "text", "binary"]
"""Coarse class of what this call produces. Mirrors :class:`lacing.Artifact.kind`
so the producer knows what shape of Artifact to materialize."""


@dataclass(frozen=True, slots=True, kw_only=True)
class CallPlan:
    """A single planned fal call. Pure data — no API contact yet.

    ``application`` and ``arguments`` are the *exact* tuple
    ``cached_call_fal(application, arguments)`` would take, so a Plan can be
    cache-checked, executed, or replayed without ambiguity.
    """

    tool: str
    """High-level tool name — ``"generate_image"``, ``"image_to_video"``, etc.
    Distinct from ``application`` because one tool may dispatch to several
    fal models depending on quality tier."""

    application: str
    """The fal model id that will be invoked (e.g. ``"fal-ai/flux/dev"``)."""

    arguments: dict
    """Keyword arguments to pass to fal. Will be JSON-canonicalized for
    cache key computation; should be JSON-serializable."""

    output_kind: OutputKind
    """What kind of Artifact this call will produce."""

    estimated_cost_usd: Optional[float] = None
    """Predicted cost in USD. ``None`` when the model has no ``cost_estimate``
    populated (callers can distinguish "free" from "unknown")."""

    cache_status: CacheStatus = "unknown"
    """Whether the cache will short-circuit this call. ``"hit"`` means
    ``execute`` won't bill, so :attr:`Plan.total_cost_usd` and
    :attr:`Plan.cache_hit_savings_usd` reflect that."""

    expected_duration_s: Optional[tuple[float, float]] = None
    """``(min, max)`` duration the model can produce, or ``None`` if no
    duration contract is known. Plan-level validators can check that the
    requested duration fits this range and raise :class:`FalDurationOutOfRange`
    *before* the call instead of letting it silently truncate."""

    metadata: dict = field(default_factory=dict)
    """Free-form labels for downstream consumers. Conventional keys:
    ``shot_id``, ``beat_id``, ``character_name``, ``strategy``."""

    # -- predicted-billable cost --------------------------------------------

    @property
    def billable_cost_usd(self) -> float:
        """Cost that will actually be billed (0 on cache hit, estimate otherwise).

        Returns ``0.0`` (not ``None``) on cache hit or unknown estimate so
        sums are well-defined; use :attr:`estimated_cost_usd` ``is None`` to
        check unknown status explicitly.
        """
        if self.cache_status == "hit":
            return 0.0
        return self.estimated_cost_usd or 0.0


@dataclass(frozen=True, slots=True)
class Plan:
    """An ordered sequence of :class:`CallPlan` — a render plan, in essence.

    Plans compose: ``a + b`` returns a new Plan with ``a.calls`` followed by
    ``b.calls``. ``Plan(calls=())`` is the identity. Plans are frozen, so
    edits return new Plans (use :meth:`with_call_replaced` for in-place-feel).
    """

    calls: tuple[CallPlan, ...] = ()

    def __add__(self, other: "Plan") -> "Plan":
        if not isinstance(other, Plan):
            return NotImplemented
        return Plan(calls=self.calls + other.calls)

    def __len__(self) -> int:
        return len(self.calls)

    def __iter__(self):
        return iter(self.calls)

    def __getitem__(self, idx):
        return self.calls[idx]

    @property
    def total_cost_usd(self) -> float:
        """Sum of :attr:`CallPlan.billable_cost_usd` across all calls."""
        return sum((c.billable_cost_usd for c in self.calls), 0.0)

    @property
    def cache_hit_savings_usd(self) -> float:
        """USD that would have been spent without the cache.

        Equal to ``sum(c.estimated_cost_usd for c in calls if c.cache_status == "hit"
        and c.estimated_cost_usd is not None)``.
        """
        return sum(
            (
                c.estimated_cost_usd or 0.0
                for c in self.calls
                if c.cache_status == "hit"
            ),
            0.0,
        )

    @property
    def has_unknown_costs(self) -> bool:
        """True if any non-cache-hit call has no cost estimate.

        Use this to refuse to gate on a budget when the estimate is incomplete.
        """
        return any(
            c.estimated_cost_usd is None and c.cache_status != "hit"
            for c in self.calls
        )

    def with_call_replaced(self, index: int, new_call: CallPlan) -> "Plan":
        """Return a new Plan with ``calls[index]`` replaced."""
        new_calls = list(self.calls)
        new_calls[index] = new_call
        return Plan(calls=tuple(new_calls))


# --- planning helpers -------------------------------------------------------


def make_call_plan(
    *,
    tool: str,
    application: str,
    arguments: dict,
    output_kind: OutputKind,
    estimated_cost_usd: Optional[float] = None,
    expected_duration_s: Optional[tuple[float, float]] = None,
    metadata: Optional[dict] = None,
    consult_cache: bool = True,
) -> CallPlan:
    """Build a :class:`CallPlan` and (optionally) check the cache.

    When ``consult_cache=True`` (the default), the cache is peeked using the
    same key the eventual call would produce; ``cache_status`` is set to
    ``"hit"`` if a cached entry exists, ``"miss"`` otherwise. This makes
    ``Plan.total_cost_usd`` honest: a fully-cached Plan reports $0.

    When ``consult_cache=False`` (e.g. for unit tests or "what would a fresh
    run cost?" reporting), ``cache_status`` is ``"unknown"``.
    """
    status: CacheStatus = "unknown"
    if consult_cache:
        # Local import to avoid a cycle: cache imports from core, core imports
        # from errors, none of which need plan.
        try:
            from .cache import cache_get  # type: ignore[import-not-found]
            status = "hit" if cache_get(application, arguments) is not None else "miss"
        except Exception:
            # Cache lookup is best-effort — if it errors (corrupted manifest,
            # etc.) fall back to ``"unknown"`` rather than fail the planner.
            status = "unknown"
    return CallPlan(
        tool=tool,
        application=application,
        arguments=arguments,
        output_kind=output_kind,
        estimated_cost_usd=estimated_cost_usd,
        cache_status=status,
        expected_duration_s=expected_duration_s,
        metadata=metadata or {},
    )


# --- execution --------------------------------------------------------------


# Type for the per-call result-to-Artifact converter.
ResultToArtifact = Callable[[dict, CallPlan], "Artifact"]  # noqa: F821


def execute(
    plan: Plan,
    *,
    on_event: Optional[Callable] = None,
    dry_run: bool = False,
    use_cache: bool = True,
    artifact_converter: Optional[ResultToArtifact] = None,
) -> list:
    """Execute a Plan, returning a list of materialized :class:`lacing.Artifact`s.

    Args:
        plan: The Plan to execute.
        on_event: Optional per-call event subscriber (passed to ``call_fal``).
        dry_run: When True, no fal calls are made; synthetic Artifacts are
            returned with placeholder ``asset_id`` and ``url=None``. Useful
            for exercising downstream composition without an API key.
        use_cache: When True (default), executes via ``cached_call_fal`` so
            cache hits skip the network. When False, every call is fresh.
        artifact_converter: Per-CallPlan converter from raw fal response to
            :class:`lacing.Artifact`. When ``None`` (default), a built-in
            converter handles the common shapes (``{images: [{url}]}``,
            ``{video: {url}}``, ``{audio: {url}}``).

    Returns:
        One :class:`lacing.Artifact` per :class:`CallPlan` in ``plan.calls``,
        in the same order.
    """
    from lacing import Artifact

    if dry_run:
        return [_synthetic_artifact(c) for c in plan.calls]

    converter = artifact_converter or _default_artifact_converter

    artifacts: list[Artifact] = []
    for call in plan.calls:
        if use_cache:
            from .cache import cached_call_fal
            raw = cached_call_fal(call.application, call.arguments, on_event=on_event)
        else:
            from .core import call_fal
            raw = call_fal(call.application, call.arguments, on_event=on_event)
        artifacts.append(converter(raw, call))
    return artifacts


def _synthetic_artifact(call: CallPlan):
    """A placeholder Artifact for ``dry_run=True``. Not byte-stable across runs."""
    from lacing import Artifact, hash_bytes

    # Deterministic asset_id from the call's identity, so dry-run twice over
    # the same Plan yields the same Artifact.id pair (helpful for testing).
    import json as _json
    blob = _json.dumps(
        {"app": call.application, "args": call.arguments, "tool": call.tool},
        sort_keys=True, default=str,
    ).encode("utf-8")
    fake_id = hash_bytes(blob)
    return Artifact(
        asset_id=fake_id,
        kind=call.output_kind,
        path=None,
        url=None,
        bytes_size=0,
        duration_s=None,
        mime=None,
        provenance=_dry_run_provenance(call),
        cost_usd=0.0,
        producer_call_id=f"dry-run:{fake_id[:12]}",
    )


def _dry_run_provenance(call: CallPlan):
    from lacing.artifact import _now_rt
    from lacing.model import Provenance

    return Provenance(
        was_generated_by=f"agent:falaw-plan@{call.application}",
        was_attributed_to="dry-run",
        was_derived_from=[],
        generated_at_time=_now_rt(),
        activity="infer",
    )


def _default_artifact_converter(raw: dict, call: CallPlan):
    """Convert a fal response to an Artifact using the common response shapes.

    Handles these patterns observed across fal models:

    - ``{"images": [{"url": ..., "content_type": ...}, ...]}`` — flux family
    - ``{"image": {"url": ..., "content_type": ...}}``        — some edits
    - ``{"video": {"url": ..., "content_type": ...}}``        — i2v / t2v / lipsync
    - ``{"audio": {"url": ..., "content_type": ...}}``        — TTS
    - ``{"audio_url": "..."}``                                — voice-clone
    - ``{"output": "..."}`` (string)                          — some LLM endpoints

    The first matching pattern wins. For multi-asset responses (e.g. flux
    with ``num_images > 1``), only the first asset becomes an Artifact —
    callers wanting all assets should provide their own converter.

    The Artifact's ``asset_id`` is the SHA-256 of the URL (when present);
    ``bytes_size`` is 0 because we don't download by default. Callers who
    want byte-content addressing should download the asset and re-hash.
    """
    from lacing import Artifact, hash_bytes
    from lacing.artifact import _now_rt
    from lacing.model import Provenance

    url = _extract_first_url(raw)
    duration = _extract_duration_s(raw)
    mime = _extract_content_type(raw)

    # asset_id from URL when we don't have bytes — stable across re-runs of
    # the same fal response. When bytes are downloaded later, callers should
    # re-hash and produce a new Artifact.
    if url:
        fake_id = hash_bytes(url.encode("utf-8"))
    else:
        # Last-resort: hash the response itself.
        import json as _json
        fake_id = hash_bytes(_json.dumps(raw, sort_keys=True, default=str).encode("utf-8"))

    prov = Provenance(
        was_generated_by=f"agent:fal@{call.application}",
        was_attributed_to=call.metadata.get("attributed_to", "user:unknown"),
        was_derived_from=[],
        generated_at_time=_now_rt(),
        activity="create",
    )

    return Artifact(
        asset_id=fake_id,
        kind=call.output_kind,
        path=None,
        url=url,
        bytes_size=0,
        duration_s=duration,
        mime=mime,
        provenance=prov,
        cost_usd=call.billable_cost_usd or None,
        producer_call_id=None,  # set by orchestrators that thread through call_id
    )


def _extract_first_url(raw: dict) -> Optional[str]:
    """Find the first asset URL in a fal response, regardless of shape."""
    if not isinstance(raw, dict):
        return None
    images = raw.get("images")
    if isinstance(images, list) and images:
        first = images[0]
        if isinstance(first, dict):
            return first.get("url")
        if isinstance(first, str):
            return first
    for key in ("video", "audio", "image"):
        v = raw.get(key)
        if isinstance(v, dict) and "url" in v:
            return v["url"]
    if isinstance(raw.get("audio_url"), str):
        return raw["audio_url"]
    if isinstance(raw.get("video_url"), str):
        return raw["video_url"]
    if isinstance(raw.get("image_url"), str):
        return raw["image_url"]
    return None


def _extract_duration_s(raw: dict) -> Optional[float]:
    if not isinstance(raw, dict):
        return None
    for key in ("video", "audio"):
        v = raw.get(key)
        if isinstance(v, dict):
            d = v.get("duration") or v.get("duration_s")
            if isinstance(d, (int, float)):
                return float(d)
    return None


def _extract_content_type(raw: dict) -> Optional[str]:
    if not isinstance(raw, dict):
        return None
    for key in ("video", "audio", "image"):
        v = raw.get(key)
        if isinstance(v, dict) and isinstance(v.get("content_type"), str):
            return v["content_type"]
    images = raw.get("images")
    if isinstance(images, list) and images and isinstance(images[0], dict):
        return images[0].get("content_type")
    return None
