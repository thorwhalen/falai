"""falaw: agent-friendly Python facade over fal.ai for AI media generation.

Quick start (single-shot generation):

    >>> from falaw import generate_image  # doctest: +SKIP
    >>> r = generate_image("a tiger eye, macro, 35mm", quality="fast")
    >>> r.first.download(to="./tiger.png")

Directorial workflow (Scene IR + caching):

    >>> from falaw import Scene, cast_character, render_scene  # doctest: +SKIP
    >>> sarah = cast_character("Sarah", "mid-30s, dark curly hair")
    >>> # ... build a Scene with characters/beats/shots ...
    >>> manifest = render_scene(scene)            # caches per-beat
    >>> # edit one beat, re-render: only that beat re-fires.

Leave notes for future sessions:

    >>> from falaw import journal  # doctest: +SKIP
    >>> journal.note("Sarah's voice clone needs ~10s reference for stability")
"""

from . import corpus as _corpus  # noqa: F401  (registers refresh_models_from_corpus)
from . import journal, operations  # noqa: F401  (operations registers tools)
from . import refresh as _refresh  # noqa: F401  (refresh registers tools too)
from .base import ModelRecord, ToolSpec
from .cache import cached_call_fal, cache_get, cache_put, cache_stats, materialize_asset
from .core import call_fal
from .events import (
    ProgressEvent,
    clear_subscribers,
    subscribe,
    unsubscribe,
)
from .corpus import extract_models_from_corpus, refresh_models_from_corpus
from .operations import (
    animate_face,
    apply_note_to_beat,
    apply_note_to_scene,
    cast_character,
    cast_voice,
    edit_image,
    establish_environment,
    generate_image,
    image_to_video,
    lipsync,
    llm_complete,
    parse_screenplay,
    remove_background,
    render_beat,
    render_scene,
    render_shot,
    storyboard_shot,
    talking_avatar_from_text,
    text_to_speech,
    text_to_video,
    upscale_image,
    voice_clone,
)
from .refresh import refresh_full_docs, refresh_llms, refresh_state
from .registry import (
    get_model,
    get_tool,
    list_models,
    list_tools,
    pick_model,
    register_tool,
)
from .results import Asset, Result, parse_response
from .scene import (
    Beat,
    Character,
    Environment,
    Scene,
    Shot,
    Voice,
    beat_content_hash,
    load_scene,
    make_beat,
    make_shot,
    save_scene,
    scene_from_dict,
    scene_to_dict,
    shot_content_hash,
)
from .session import Session

__all__ = [
    "Asset",
    "Beat",
    "Character",
    "Environment",
    "ModelRecord",
    "Result",
    "ProgressEvent",
    "Scene",
    "Session",
    "Shot",
    "ToolSpec",
    "Voice",
    "clear_subscribers",
    "subscribe",
    "unsubscribe",
    "animate_face",
    "apply_note_to_beat",
    "apply_note_to_scene",
    "beat_content_hash",
    "cache_get",
    "cache_put",
    "cache_stats",
    "cached_call_fal",
    "call_fal",
    "cast_character",
    "cast_voice",
    "edit_image",
    "establish_environment",
    "extract_models_from_corpus",
    "generate_image",
    "get_model",
    "get_tool",
    "image_to_video",
    "journal",
    "lipsync",
    "list_models",
    "list_tools",
    "llm_complete",
    "load_scene",
    "make_beat",
    "make_shot",
    "materialize_asset",
    "parse_response",
    "parse_screenplay",
    "pick_model",
    "refresh_full_docs",
    "refresh_llms",
    "refresh_models_from_corpus",
    "refresh_state",
    "register_tool",
    "remove_background",
    "render_beat",
    "render_scene",
    "render_shot",
    "save_scene",
    "scene_from_dict",
    "scene_to_dict",
    "shot_content_hash",
    "storyboard_shot",
    "talking_avatar_from_text",
    "text_to_speech",
    "text_to_video",
    "upscale_image",
    "voice_clone",
]
