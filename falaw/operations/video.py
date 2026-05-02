"""Video-generation operations: text-to-video and image-to-video."""

from __future__ import annotations

from typing import Optional

from ..core import call_fal
from ..registry import pick_model, register_tool
from ..results import Result, parse_response


@register_tool(
    name="text_to_video",
    description=(
        "Generate a video from a text prompt. Picks a tier-appropriate "
        "model (Veo 3 for ultra, Seedance Pro for high). Use `extra` to "
        "pass through model-specific knobs like duration, aspect_ratio, "
        "negative_prompt."
    ),
    tags=("video", "text_to_video", "generate"),
    input_schema={
        "type": "object",
        "required": ["prompt"],
        "properties": {
            "prompt": {"type": "string"},
            "quality": {
                "type": "string",
                "enum": ["fast", "balanced", "high", "ultra"],
                "default": "high",
            },
            "model_id": {"type": "string"},
            "extra": {"type": "object"},
        },
    },
    output_schema={"type": "object", "description": "falaw.Result"},
    examples=(
        {"prompt": "A drone shot over a misty pine forest at dawn"},
        {"prompt": "Macro: a single dewdrop on a spider web", "quality": "ultra"},
    ),
)
def text_to_video(
    prompt: str,
    *,
    quality: str = "high",
    model_id: Optional[str] = None,
    extra: Optional[dict] = None,
) -> Result:
    """Generate a video from a text prompt."""
    model = model_id or pick_model(category="text_to_video", quality_tier=quality).id
    arguments = {"prompt": prompt, **(extra or {})}
    raw = call_fal(model, arguments)
    return parse_response(raw, application=model, arguments=arguments)


@register_tool(
    name="image_to_video",
    description=(
        "Animate a still image into a short video. Optional prompt steers "
        "the motion. Picks a tier-appropriate i2v model (Kling Master for "
        "ultra, Seedance for high, Hailuo for balanced)."
    ),
    tags=("video", "image_to_video", "generate"),
    input_schema={
        "type": "object",
        "required": ["image_url"],
        "properties": {
            "image_url": {"type": "string"},
            "prompt": {"type": "string"},
            "quality": {
                "type": "string",
                "enum": ["balanced", "high", "ultra"],
                "default": "high",
            },
            "model_id": {"type": "string"},
            "extra": {"type": "object"},
        },
    },
    output_schema={"type": "object", "description": "falaw.Result"},
    examples=(
        {"image_url": "https://...", "prompt": "the camera slowly zooms in"},
        {"image_url": "https://...", "quality": "balanced"},
    ),
)
def image_to_video(
    image_url: str,
    prompt: str = "",
    *,
    quality: str = "high",
    model_id: Optional[str] = None,
    extra: Optional[dict] = None,
) -> Result:
    """Animate a still image into a video."""
    model = model_id or pick_model(category="image_to_video", quality_tier=quality).id
    arguments: dict = {"image_url": image_url, **(extra or {})}
    if prompt:
        arguments["prompt"] = prompt
    raw = call_fal(model, arguments)
    return parse_response(raw, application=model, arguments=arguments)
