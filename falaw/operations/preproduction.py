"""Pre-production: produce reusable identity anchors for a Scene.

The downstream renderer reuses Character.reference_image_url for every
shot featuring that character, and Character.voice for every line they
speak. So the quality of the *anchors* set here propagates everywhere.

Each function returns an updated entity (Character / Environment) you
can feed back into the Scene via `scene.with_character(...)` etc.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from ..cache import cached_call_fal, materialize_asset
from ..registry import pick_model, register_tool
from ..results import Result, parse_response
from ..scene import Character, Environment, Shot, Voice


@register_tool(
    name="cast_character",
    description=(
        "Generate or attach a canonical face image for a character, plus "
        "an optional voice. Returns an updated Character with "
        "`reference_image_url` set --- the anchor used by every later "
        "lipsync render. Pass an existing image_url to skip generation."
    ),
    tags=("preproduction", "character"),
    input_schema={
        "type": "object",
        "required": ["name", "description"],
        "properties": {
            "name": {"type": "string"},
            "description": {"type": "string",
                            "description": "Visual description used to generate the face."},
            "image_url": {"type": "string",
                          "description": "Skip generation and use this image as the face."},
            "style": {"type": "string",
                      "description": "Visual style applied to the face image (joined to description)."},
            "quality": {"type": "string",
                        "enum": ["fast", "balanced", "high", "ultra"],
                        "default": "high"},
            "voice_id": {"type": "string"},
            "reference_audio_url": {"type": "string"},
            "voice_style": {"type": "string"},
        },
    },
    output_schema={"type": "object", "description": "falaw.Character"},
    examples=(
        {"name": "Sarah", "description": "mid-30s, sharp features, dark curly hair, wary eyes"},
    ),
)
def cast_character(
    name: str,
    description: str,
    *,
    image_url: str = "",
    style: str = "",
    quality: str = "high",
    voice_id: str = "",
    reference_audio_url: str = "",
    voice_style: str = "",
) -> Character:
    """Create a Character with a canonical face (and optional voice).

    If ``image_url`` is given, we skip face generation and use that
    image directly. Otherwise we run text-to-image with the description
    (+ optional ``style`` suffix), cache the result, and use the URL.
    """
    if not image_url:
        prompt = description
        if style:
            prompt = f"{description} | style: {style}"
        model = pick_model(category="image", quality_tier=quality).id
        raw = cached_call_fal(model, {"prompt": prompt, "image_size": "portrait_4_3"})
        result = parse_response(raw, application=model, arguments={"prompt": prompt})
        if not result.first:
            raise RuntimeError(
                f"cast_character: face generation produced no asset for {name!r}"
            )
        image_url = result.first.url

    voice: Optional[Voice] = None
    if voice_id or reference_audio_url:
        voice = Voice(
            name=name,
            voice_id=voice_id,
            reference_audio_url=reference_audio_url,
            style_notes=voice_style,
        )

    return Character(
        name=name,
        description=description,
        reference_image_url=image_url,
        voice=voice,
    )


@register_tool(
    name="cast_voice",
    description=(
        "Attach or refine a Voice for an existing Character. Provide a "
        "`reference_audio_url` (for cloning) or a `voice_id` (model-side "
        "preset). Returns the updated Character."
    ),
    tags=("preproduction", "voice"),
    input_schema={
        "type": "object",
        "required": ["character"],
        "properties": {
            "character": {"type": "object", "description": "falaw.Character"},
            "voice_id": {"type": "string"},
            "reference_audio_url": {"type": "string"},
            "style_notes": {"type": "string"},
            "model_id": {"type": "string"},
        },
    },
    output_schema={"type": "object", "description": "falaw.Character"},
    examples=(),
)
def cast_voice(
    character: Character,
    *,
    voice_id: str = "",
    reference_audio_url: str = "",
    style_notes: str = "",
    model_id: str = "",
) -> Character:
    """Attach or update the Voice on a Character."""
    voice = Voice(
        name=character.name,
        voice_id=voice_id,
        reference_audio_url=reference_audio_url,
        style_notes=style_notes,
        model_id=model_id,
    )
    return replace(character, voice=voice)


@register_tool(
    name="establish_environment",
    description=(
        "Generate or attach a canonical establishing image for a "
        "location. Used as visual anchor and lighting reference for "
        "every shot in that environment. Returns an Environment."
    ),
    tags=("preproduction", "environment"),
    input_schema={
        "type": "object",
        "required": ["name", "description"],
        "properties": {
            "name": {"type": "string"},
            "description": {"type": "string"},
            "time_of_day": {"type": "string"},
            "lighting": {"type": "string"},
            "image_url": {"type": "string"},
            "quality": {"type": "string",
                        "enum": ["fast", "balanced", "high", "ultra"],
                        "default": "high"},
        },
    },
    output_schema={"type": "object", "description": "falaw.Environment"},
    examples=(
        {"name": "diner", "description": "1950s American chrome diner, "
         "neon outside, half-empty booths", "time_of_day": "midnight"},
    ),
)
def establish_environment(
    name: str,
    description: str,
    *,
    time_of_day: str = "",
    lighting: str = "",
    image_url: str = "",
    quality: str = "high",
) -> Environment:
    """Create an Environment with a canonical establishing image."""
    if not image_url:
        prompt_parts = [description]
        if time_of_day:
            prompt_parts.append(f"time of day: {time_of_day}")
        if lighting:
            prompt_parts.append(f"lighting: {lighting}")
        prompt = " | ".join(prompt_parts)
        model = pick_model(category="image", quality_tier=quality).id
        raw = cached_call_fal(model, {"prompt": prompt, "image_size": "landscape_16_9"})
        result = parse_response(raw, application=model, arguments={"prompt": prompt})
        if not result.first:
            raise RuntimeError(
                f"establish_environment: generation produced no asset for {name!r}"
            )
        image_url = result.first.url

    return Environment(
        name=name,
        description=description,
        time_of_day=time_of_day,
        lighting=lighting,
        reference_image_url=image_url,
    )


@register_tool(
    name="storyboard_shot",
    description=(
        "Render a still preview (storyboard frame) for a single Shot, "
        "composited with its Environment and the Characters in view. "
        "Returns the URL of the still --- use it as a reference image "
        "for downstream image-to-video."
    ),
    tags=("preproduction", "storyboard"),
    input_schema={
        "type": "object",
        "required": ["shot"],
        "properties": {
            "shot": {"type": "object", "description": "falaw.Shot"},
            "environment": {"type": "object", "description": "falaw.Environment"},
            "characters": {"type": "array", "description": "list of falaw.Character"},
            "style": {"type": "string"},
            "quality": {"type": "string",
                        "enum": ["fast", "balanced", "high", "ultra"],
                        "default": "balanced"},
        },
    },
    output_schema={"type": "object", "description": "falaw.Result (the still)"},
    examples=(),
)
def storyboard_shot(
    shot: Shot,
    *,
    environment: Optional[Environment] = None,
    characters: tuple = (),
    style: str = "",
    quality: str = "balanced",
) -> Result:
    """Render a storyboard still for a Shot."""
    parts: list[str] = [shot.description or "shot"]
    if shot.framing:
        parts.append(f"framing: {shot.framing}")
    if environment is not None:
        parts.append(f"location: {environment.description}")
        if environment.time_of_day:
            parts.append(f"time: {environment.time_of_day}")
        if environment.lighting:
            parts.append(f"lighting: {environment.lighting}")
    if characters:
        names = ", ".join(c.name for c in characters)
        parts.append(f"characters: {names}")
        for c in characters:
            if c.description:
                parts.append(f"{c.name}: {c.description}")
    if shot.camera:
        parts.append(f"camera: {shot.camera}")
    if style:
        parts.append(f"style: {style}")
    prompt = " | ".join(parts)

    model = pick_model(category="image", quality_tier=quality).id
    raw = cached_call_fal(model, {"prompt": prompt, "image_size": "landscape_16_9"})
    return parse_response(raw, application=model, arguments={"prompt": prompt})
