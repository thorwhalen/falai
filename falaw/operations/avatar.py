"""Avatar / lip-sync operations and composers.

Two distinct primitives, often confused:

* ``animate_face`` --- image + audio → talking video. The face is a still;
  the model animates lips/expressions over the audio. Backed by ai-avatar
  / omnihuman ("avatar" registry category).
* ``lipsync`` --- video + audio → re-synced video. The body and motion
  come from an existing video; only the mouth is replaced to match new
  audio. Backed by sync-lipsync / kling-lipsync ("lipsync" category).

Use ``animate_face`` when you only have a portrait. Use ``lipsync`` when
you already have a video clip.

The composer ``talking_avatar_from_text`` chains TTS → ``animate_face``.
"""

from __future__ import annotations

from typing import Optional

from ..core import call_fal
from ..registry import pick_model, register_tool
from ..results import Result, parse_response
from .audio import text_to_speech


@register_tool(
    name="animate_face",
    description=(
        "Animate a still face image to speak an audio track. Returns a "
        "falaw.Result whose .first asset is the talking-head video URL. "
        "Use this when you have a portrait + audio but NOT an existing "
        "video. Picks ai-avatar (balanced) or omnihuman v1.5 (high)."
    ),
    tags=("video", "avatar", "generate"),
    input_schema={
        "type": "object",
        "required": ["image_url", "audio_url"],
        "properties": {
            "image_url": {"type": "string"},
            "audio_url": {"type": "string"},
            "prompt": {
                "type": "string",
                "description": "Direction (expression / acting note); "
                "ai-avatar requires it, omnihuman uses it as a hint.",
            },
            "quality": {
                "type": "string",
                "enum": ["balanced", "high"],
                "default": "balanced",
            },
            "model_id": {"type": "string"},
            "extra": {"type": "object"},
        },
    },
    output_schema={"type": "object", "description": "falaw.Result"},
    examples=(
        {
            "image_url": "https://...",
            "audio_url": "https://...",
            "prompt": "warm, attentive listener",
        },
    ),
)
def animate_face(
    image_url: str,
    audio_url: str,
    *,
    prompt: str = "",
    quality: str = "balanced",
    model_id: Optional[str] = None,
    extra: Optional[dict] = None,
) -> Result:
    """Animate a still face from audio. Image + audio → talking video."""
    model = model_id or pick_model(category="avatar", quality_tier=quality).id
    arguments: dict = {"image_url": image_url, "audio_url": audio_url}
    # ai-avatar requires `prompt`; omnihuman accepts but doesn't require it.
    # Pass an empty-but-present prompt so ai-avatar's schema is happy.
    arguments["prompt"] = prompt or "neutral expression, natural delivery"
    arguments.update(extra or {})
    raw = call_fal(model, arguments)
    return parse_response(raw, application=model, arguments=arguments)


@register_tool(
    name="lipsync",
    description=(
        "Re-sync an existing VIDEO clip to a new audio track. Pass "
        "`video_url` (NOT a still image) and `audio_url`. The model "
        "replaces mouth motion to match the audio while keeping body "
        "and motion from the original video. Use `animate_face` if you "
        "only have a still image."
    ),
    tags=("video", "lipsync", "generate"),
    input_schema={
        "type": "object",
        "required": ["video_url", "audio_url"],
        "properties": {
            "video_url": {"type": "string"},
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
    examples=({"video_url": "https://...", "audio_url": "https://..."},),
)
def lipsync(
    video_url: str,
    audio_url: str,
    *,
    quality: str = "high",
    model_id: Optional[str] = None,
    extra: Optional[dict] = None,
) -> Result:
    """Re-sync mouth motion in an existing video to a new audio track."""
    model = model_id or pick_model(category="lipsync", quality_tier=quality).id
    arguments = {"video_url": video_url, "audio_url": audio_url, **(extra or {})}
    raw = call_fal(model, arguments)
    return parse_response(raw, application=model, arguments=arguments)


@register_tool(
    name="talking_avatar_from_text",
    description=(
        "Composer: text + face IMAGE → talking-head video. Internally runs "
        "`text_to_speech(text)` then `animate_face(image_url, audio_url, "
        "prompt)`. Returns the animate_face Result. Use this when you "
        "have text and a portrait but no audio."
    ),
    tags=("video", "avatar", "compose"),
    input_schema={
        "type": "object",
        "required": ["text", "image_url"],
        "properties": {
            "text": {"type": "string"},
            "image_url": {"type": "string"},
            "voice": {"type": "string"},
            "prompt": {"type": "string"},
            "tts_quality": {"type": "string", "default": "balanced"},
            "avatar_quality": {"type": "string", "default": "balanced"},
        },
    },
    output_schema={
        "type": "object",
        "description": "falaw.Result (talking-head video)",
    },
    examples=(
        {"text": "Welcome to the demo.", "image_url": "https://example.com/host.jpg"},
    ),
)
def talking_avatar_from_text(
    text: str,
    image_url: str,
    *,
    voice: Optional[str] = None,
    prompt: str = "",
    tts_quality: str = "balanced",
    avatar_quality: str = "balanced",
) -> Result:
    """text + face image → talking video. Two fal calls, one Result."""
    tts_result = text_to_speech(text, voice=voice, quality=tts_quality)
    if not tts_result.first:
        raise RuntimeError(
            f"talking_avatar_from_text: TTS produced no audio asset; "
            f"raw response: {tts_result.raw!r}"
        )
    return animate_face(
        image_url,
        tts_result.first.url,
        prompt=prompt,
        quality=avatar_quality,
    )
