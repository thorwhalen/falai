"""Avatar / lip-sync operations and composers.

Lip-sync is a primitive (image + audio → talking video). The composer
``talking_avatar_from_text`` chains TTS → lipsync, demonstrating the
pattern for multi-step workflows.
"""

from __future__ import annotations

from typing import Optional

from ..core import call_fal
from ..registry import pick_model, register_tool
from ..results import Result, parse_response
from .audio import text_to_speech


@register_tool(
    name="lipsync",
    description=(
        "Generate a lip-synced talking-head video from a face image and an "
        "audio track. Returns a falaw.Result whose .first asset is the "
        "synced video URL."
    ),
    tags=("video", "lipsync", "generate"),
    input_schema={
        "type": "object",
        "required": ["image_url", "audio_url"],
        "properties": {
            "image_url": {"type": "string"},
            "audio_url": {"type": "string"},
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
    examples=({"image_url": "https://...", "audio_url": "https://..."},),
)
def lipsync(
    image_url: str,
    audio_url: str,
    *,
    quality: str = "high",
    model_id: Optional[str] = None,
    extra: Optional[dict] = None,
) -> Result:
    """Lip-sync an audio track to a face image."""
    model = model_id or pick_model(category="lipsync", quality_tier=quality).id
    arguments = {"image_url": image_url, "audio_url": audio_url, **(extra or {})}
    raw = call_fal(model, arguments)
    return parse_response(raw, application=model, arguments=arguments)


@register_tool(
    name="talking_avatar_from_text",
    description=(
        "Composer: text + face image → lip-synced talking video. Internally "
        "runs `text_to_speech(text)` then `lipsync(image_url, audio_url)`. "
        "Returns the lipsync Result. Use this when you have text and a "
        "portrait but no pre-recorded audio."
    ),
    tags=("video", "avatar", "compose"),
    input_schema={
        "type": "object",
        "required": ["text", "image_url"],
        "properties": {
            "text": {"type": "string"},
            "image_url": {"type": "string"},
            "voice": {"type": "string"},
            "tts_quality": {"type": "string", "default": "balanced"},
            "lipsync_quality": {"type": "string", "default": "high"},
        },
    },
    output_schema={"type": "object", "description": "falaw.Result (the lipsync video)"},
    examples=(
        {"text": "Welcome to the demo.", "image_url": "https://example.com/host.jpg"},
    ),
)
def talking_avatar_from_text(
    text: str,
    image_url: str,
    *,
    voice: Optional[str] = None,
    tts_quality: str = "balanced",
    lipsync_quality: str = "high",
) -> Result:
    """text + face image → lip-synced video. Two fal calls, one Result."""
    tts_result = text_to_speech(text, voice=voice, quality=tts_quality)
    if not tts_result.first:
        raise RuntimeError(
            f"talking_avatar_from_text: TTS produced no audio asset; "
            f"raw response: {tts_result.raw!r}"
        )
    return lipsync(image_url, tts_result.first.url, quality=lipsync_quality)
