"""Image-generation and image-manipulation operations."""

from __future__ import annotations

from typing import Optional

from ..core import call_fal
from ..registry import pick_model, register_tool
from ..results import Result, parse_response


@register_tool(
    name="generate_image",
    description=(
        "Generate an image from a text prompt. Picks a sensible FLUX model "
        "based on the requested quality tier ('fast', 'balanced', 'high', "
        "'ultra'). Returns a falaw.Result whose .first asset has a URL you "
        "can .download(to=...)."
    ),
    tags=("image", "generate"),
    input_schema={
        "type": "object",
        "required": ["prompt"],
        "properties": {
            "prompt": {"type": "string"},
            "quality": {
                "type": "string",
                "enum": ["fast", "balanced", "high", "ultra"],
                "default": "balanced",
            },
            "image_size": {"type": "string", "default": "landscape_4_3"},
            "model_id": {"type": "string"},
            "extra": {"type": "object"},
        },
    },
    output_schema={"type": "object", "description": "falaw.Result"},
    examples=(
        {"prompt": "A red panda eating bamboo", "quality": "fast"},
        {"prompt": "Cinematic portrait, 35mm film", "quality": "ultra"},
    ),
)
def generate_image(
    prompt: str,
    *,
    quality: str = "balanced",
    image_size: str = "landscape_4_3",
    model_id: Optional[str] = None,
    extra: Optional[dict] = None,
) -> Result:
    """Generate an image from a text prompt."""
    model = model_id or pick_model(category="image", quality_tier=quality).id
    arguments = {"prompt": prompt, "image_size": image_size, **(extra or {})}
    raw = call_fal(model, arguments)
    return parse_response(raw, application=model, arguments=arguments)


@register_tool(
    name="edit_image",
    description=(
        "Edit an image using a natural-language instruction. Picks a FLUX "
        "Kontext / SeedEdit model by quality tier. Returns a falaw.Result "
        "with the edited image."
    ),
    tags=("image", "edit"),
    input_schema={
        "type": "object",
        "required": ["image_url", "prompt"],
        "properties": {
            "image_url": {"type": "string"},
            "prompt": {"type": "string"},
            "quality": {
                "type": "string",
                "enum": ["fast", "balanced", "high", "ultra"],
                "default": "balanced",
            },
            "model_id": {"type": "string"},
            "extra": {"type": "object"},
        },
    },
    output_schema={"type": "object", "description": "falaw.Result"},
    examples=(
        {"image_url": "https://...", "prompt": "make the sky orange"},
        {
            "image_url": "https://...",
            "prompt": "remove the person on the left",
            "quality": "ultra",
        },
    ),
)
def edit_image(
    image_url: str,
    prompt: str,
    *,
    quality: str = "balanced",
    model_id: Optional[str] = None,
    extra: Optional[dict] = None,
) -> Result:
    """Edit an image with a natural-language instruction."""
    model = model_id or pick_model(category="image_edit", quality_tier=quality).id
    arguments = {"image_url": image_url, "prompt": prompt, **(extra or {})}
    raw = call_fal(model, arguments)
    return parse_response(raw, application=model, arguments=arguments)


@register_tool(
    name="upscale_image",
    description=(
        "Upscale an image to higher resolution while preserving fidelity. "
        "Defaults to clarity-upscaler. Returns a falaw.Result with the "
        "upscaled image."
    ),
    tags=("image", "upscale"),
    input_schema={
        "type": "object",
        "required": ["image_url"],
        "properties": {
            "image_url": {"type": "string"},
            "scale": {"type": "number", "default": 2.0},
            "model_id": {"type": "string"},
            "extra": {"type": "object"},
        },
    },
    output_schema={"type": "object", "description": "falaw.Result"},
    examples=(
        {"image_url": "https://...", "scale": 2.0},
        {"image_url": "https://...", "scale": 4.0, "extra": {"creativity": 0.35}},
    ),
)
def upscale_image(
    image_url: str,
    *,
    scale: float = 2.0,
    model_id: Optional[str] = None,
    extra: Optional[dict] = None,
) -> Result:
    """Upscale an image."""
    model = model_id or pick_model(category="upscale", quality_tier="high").id
    arguments = {"image_url": image_url, "scale": scale, **(extra or {})}
    raw = call_fal(model, arguments)
    return parse_response(raw, application=model, arguments=arguments)


@register_tool(
    name="remove_background",
    description=(
        "Remove the background from an image, returning a transparent PNG. "
        "Defaults to BiRefNet v2 (quality='high') or Bria (quality='balanced'). "
        "Returns a falaw.Result."
    ),
    tags=("image", "background_removal"),
    input_schema={
        "type": "object",
        "required": ["image_url"],
        "properties": {
            "image_url": {"type": "string"},
            "quality": {
                "type": "string",
                "enum": ["balanced", "high"],
                "default": "high",
            },
            "model_id": {"type": "string"},
            "extra": {"type": "object"},
        },
    },
    output_schema={"type": "object", "description": "falaw.Result"},
    examples=({"image_url": "https://example.com/photo.jpg"},),
)
def remove_background(
    image_url: str,
    *,
    quality: str = "high",
    model_id: Optional[str] = None,
    extra: Optional[dict] = None,
) -> Result:
    """Remove the background from an image."""
    model = (
        model_id or pick_model(category="background_removal", quality_tier=quality).id
    )
    arguments = {"image_url": image_url, **(extra or {})}
    raw = call_fal(model, arguments)
    return parse_response(raw, application=model, arguments=arguments)
