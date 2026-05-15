"""``plan_*`` siblings of the eager operations.

Every eager op in ``falaw.operations`` does the same dance:

1. Resolve a model id from ``(category, quality_tier)``.
2. Build the ``arguments`` dict.
3. Hand off to ``call_fal``.

The eager wrapper does all three. The ``plan_*`` sibling does steps 1 and 2,
then returns a :class:`falaw.plan.CallPlan` describing what *would* happen.
A planner can compose many ``plan_*`` results into a :class:`falaw.plan.Plan`,
inspect the cost, swap models, and only then call ``execute(plan)``.

The five ops covered here are the ones nw needs first:
``generate_image``, ``edit_image``, ``image_to_video``, ``animate_face``,
``lipsync``. Other ops can be ported later — the eager wrappers continue
to work in the meantime.
"""

from __future__ import annotations

from typing import Optional

from ..cost import estimate_call_cost
from ..plan import CallPlan, make_call_plan
from ..registry import get_model, pick_model


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _resolve_model_id_and_record(
    *, model_id: Optional[str], category: str, quality_tier: str
):
    """Mirror the eager-op model-resolution pattern; return ``(id, ModelRecord)``.

    Eager ops do ``model = model_id or pick_model(category, quality_tier).id``.
    For planning we need the full :class:`ModelRecord` (to read ``cost_estimate``
    and any future duration contracts), so this resolves both at once.
    """
    if model_id:
        # Allow alias resolution via get_model.
        record = get_model(model_id)
        return record.id, record
    record = pick_model(category=category, quality_tier=quality_tier)
    return record.id, record


def _estimate_cost_with_record(
    record,
    *,
    seconds: Optional[float] = None,
    megapixels: Optional[float] = None,
    tokens: Optional[int] = None,
) -> Optional[float]:
    """Thin wrapper around :func:`estimate_call_cost` for planner use."""
    return estimate_call_cost(
        record, count=1, seconds=seconds, megapixels=megapixels, tokens=tokens
    )


# ---------------------------------------------------------------------------
# generate_image
# ---------------------------------------------------------------------------


def plan_generate_image(
    prompt: str,
    *,
    quality: str = "balanced",
    image_size: str = "landscape_4_3",
    model_id: Optional[str] = None,
    extra: Optional[dict] = None,
    metadata: Optional[dict] = None,
    consult_cache: bool = True,
) -> CallPlan:
    """Plan a :func:`falaw.generate_image` call without executing it."""
    application, record = _resolve_model_id_and_record(
        model_id=model_id, category="image", quality_tier=quality
    )
    arguments = {"prompt": prompt, "image_size": image_size, **(extra or {})}
    return make_call_plan(
        tool="generate_image",
        application=application,
        arguments=arguments,
        output_kind="image",
        estimated_cost_usd=_estimate_cost_with_record(record),
        metadata=metadata,
        consult_cache=consult_cache,
    )


# ---------------------------------------------------------------------------
# edit_image
# ---------------------------------------------------------------------------


def plan_edit_image(
    image_url: str,
    prompt: str,
    *,
    quality: str = "balanced",
    model_id: Optional[str] = None,
    extra: Optional[dict] = None,
    metadata: Optional[dict] = None,
    consult_cache: bool = True,
) -> CallPlan:
    """Plan a :func:`falaw.edit_image` call (Flux Kontext / SeedEdit / OmniGen)."""
    application, record = _resolve_model_id_and_record(
        model_id=model_id, category="image_edit", quality_tier=quality
    )
    arguments = {"image_url": image_url, "prompt": prompt, **(extra or {})}
    return make_call_plan(
        tool="edit_image",
        application=application,
        arguments=arguments,
        output_kind="image",
        estimated_cost_usd=_estimate_cost_with_record(record),
        metadata=metadata,
        consult_cache=consult_cache,
    )


# ---------------------------------------------------------------------------
# composite_character_in_environment (multi-reference image edit)
# ---------------------------------------------------------------------------


_DEFAULT_COMPOSITE_PROMPT = (
    "Place the person from the first image into the scene from the second image. "
    "Preserve the person's identity exactly (face, hair, build, age, clothing). "
    "Match the environment's lighting, palette, and atmosphere. Photorealistic "
    "composition; the person looks like they belong there."
)


def plan_composite_character_in_environment(
    character_image_url: str,
    environment_image_url: str,
    *,
    prompt: str = "",
    quality: str = "balanced",
    model_id: Optional[str] = None,
    extra: Optional[dict] = None,
    metadata: Optional[dict] = None,
    consult_cache: bool = True,
) -> CallPlan:
    """Plan a :func:`falaw.composite_character_in_environment` call.

    The character image anchors identity; the environment image anchors
    location, lighting, palette. The default model is Flux Kontext dev.
    """
    application, record = _resolve_model_id_and_record(
        model_id=model_id, category="image_edit", quality_tier=quality
    )
    arguments: dict = {
        "image_url": character_image_url,
        "image_urls": [character_image_url, environment_image_url],
        "prompt": prompt or _DEFAULT_COMPOSITE_PROMPT,
        **(extra or {}),
    }
    return make_call_plan(
        tool="composite_character_in_environment",
        application=application,
        arguments=arguments,
        output_kind="image",
        estimated_cost_usd=_estimate_cost_with_record(record),
        metadata=metadata,
        consult_cache=consult_cache,
    )


# ---------------------------------------------------------------------------
# image_to_video
# ---------------------------------------------------------------------------


def plan_image_to_video(
    image_url: str,
    prompt: str = "",
    *,
    quality: str = "high",
    model_id: Optional[str] = None,
    duration_s: Optional[float] = None,
    extra: Optional[dict] = None,
    metadata: Optional[dict] = None,
    consult_cache: bool = True,
) -> CallPlan:
    """Plan a :func:`falaw.image_to_video` call.

    ``duration_s`` is used only for cost estimation when the model is priced
    ``per_second``; it does not get passed to fal unless the caller puts it
    in ``extra`` (different models have different argument names).
    """
    application, record = _resolve_model_id_and_record(
        model_id=model_id, category="image_to_video", quality_tier=quality
    )
    arguments: dict = {"image_url": image_url, **(extra or {})}
    if prompt:
        arguments["prompt"] = prompt
    return make_call_plan(
        tool="image_to_video",
        application=application,
        arguments=arguments,
        output_kind="video",
        estimated_cost_usd=_estimate_cost_with_record(record, seconds=duration_s),
        metadata=metadata,
        consult_cache=consult_cache,
    )


# ---------------------------------------------------------------------------
# animate_face (avatar from image + audio)
# ---------------------------------------------------------------------------


def plan_animate_face(
    image_url: str,
    audio_url: str,
    *,
    prompt: str = "",
    quality: str = "balanced",
    model_id: Optional[str] = None,
    duration_s: Optional[float] = None,
    extra: Optional[dict] = None,
    metadata: Optional[dict] = None,
    consult_cache: bool = True,
) -> CallPlan:
    """Plan a :func:`falaw.animate_face` call (image + audio → talking video).

    Note: the default avatar model is known to hang. For production-grade
    behavior, callers should pass ``model_id="fal-ai/bytedance/omnihuman/v1.5"``
    or set ``quality="high"`` (which picks omnihuman).
    """
    application, record = _resolve_model_id_and_record(
        model_id=model_id, category="avatar", quality_tier=quality
    )
    arguments: dict = {"image_url": image_url, "audio_url": audio_url}
    if prompt:
        arguments["prompt"] = prompt
    elif "ai-avatar" in application:
        # ai-avatar requires non-empty prompt by contract.
        arguments["prompt"] = "natural delivery"
    if extra:
        arguments.update(extra)
    return make_call_plan(
        tool="animate_face",
        application=application,
        arguments=arguments,
        output_kind="video",
        estimated_cost_usd=_estimate_cost_with_record(record, seconds=duration_s),
        metadata=metadata,
        consult_cache=consult_cache,
    )


# ---------------------------------------------------------------------------
# lipsync (re-sync existing video to new audio)
# ---------------------------------------------------------------------------


def plan_lipsync(
    video_url: str,
    audio_url: str,
    *,
    quality: str = "high",
    model_id: Optional[str] = None,
    duration_s: Optional[float] = None,
    extra: Optional[dict] = None,
    metadata: Optional[dict] = None,
    consult_cache: bool = True,
) -> CallPlan:
    """Plan a :func:`falaw.lipsync` call (existing video + new audio → re-synced video)."""
    application, record = _resolve_model_id_and_record(
        model_id=model_id, category="lipsync", quality_tier=quality
    )
    arguments = {"video_url": video_url, "audio_url": audio_url, **(extra or {})}
    return make_call_plan(
        tool="lipsync",
        application=application,
        arguments=arguments,
        output_kind="video",
        estimated_cost_usd=_estimate_cost_with_record(record, seconds=duration_s),
        metadata=metadata,
        consult_cache=consult_cache,
    )


# ---------------------------------------------------------------------------
# text_to_speech (TTS: text → audio Artifact)
# ---------------------------------------------------------------------------


def plan_text_to_speech(
    text: str,
    *,
    quality: str = "balanced",
    voice: Optional[str] = None,
    model_id: Optional[str] = None,
    duration_s: Optional[float] = None,
    extra: Optional[dict] = None,
    metadata: Optional[dict] = None,
    consult_cache: bool = True,
) -> CallPlan:
    """Plan a :func:`falaw.text_to_speech` call (text → audio Artifact).

    Mirrors the eager :func:`falaw.text_to_speech` signature so a planned
    call and an eager call with identical inputs collapse to the same
    cache entry. ``voice`` semantics are model-specific.

    ``duration_s`` is an *optional* hint used only by the cost estimator
    — the produced audio's actual duration comes back on the materialized
    Artifact.
    """
    application, record = _resolve_model_id_and_record(
        model_id=model_id, category="tts", quality_tier=quality
    )
    arguments: dict = {"text": text}
    if voice:
        arguments["voice"] = voice
    if extra:
        arguments.update(extra)
    return make_call_plan(
        tool="text_to_speech",
        application=application,
        arguments=arguments,
        output_kind="audio",
        estimated_cost_usd=_estimate_cost_with_record(record, seconds=duration_s),
        metadata=metadata,
        consult_cache=consult_cache,
    )


# ---------------------------------------------------------------------------
# llm_complete  (the planning sibling of falaw.llm_complete)
# ---------------------------------------------------------------------------


def plan_llm_complete(
    prompt: str,
    *,
    system: str = "",
    model: Optional[str] = None,
    temperature: float = 0.7,
    output_kind: str = "text",
    extra: Optional[dict] = None,
    metadata: Optional[dict] = None,
    consult_cache: bool = True,
) -> CallPlan:
    """Plan a :func:`falaw.llm_complete` call without executing it.

    Routes through ``fal-ai/any-llm`` with the *exact same* application id and
    argument shape as the eager :func:`falaw.llm_complete`, so a planned call
    and an eager call with identical inputs collapse to the same cache entry.

    ``output_kind`` is ``"text"`` for a free-form completion or ``"json"`` when
    the prompt asks for a strict-JSON response — it tells :func:`falaw.execute`
    what kind of :class:`lacing.Artifact` to materialize. Either way the LLM
    response is materialized to a content-addressed cache *file*
    (``Artifact.path``), because LLM output is text, not a URL.

    Cost is the ``fal-ai/any-llm`` per-call estimate (``source="approximate"``
    — real pricing is per-token); pass ``model`` to pick the underlying model.
    """
    from .llm import _DEFAULT_LLM, _DEFAULT_MODEL

    application = _DEFAULT_LLM
    record = get_model(application)
    arguments: dict = {
        "model": model or _DEFAULT_MODEL,
        "prompt": prompt,
        "temperature": temperature,
    }
    if system:
        arguments["system_prompt"] = system
    arguments.update(extra or {})
    return make_call_plan(
        tool="llm_complete",
        application=application,
        arguments=arguments,
        output_kind=output_kind,  # type: ignore[arg-type]  # "text" | "json"
        estimated_cost_usd=_estimate_cost_with_record(record),
        metadata=metadata,
        consult_cache=consult_cache,
    )
