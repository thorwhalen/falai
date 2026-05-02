"""Task-level verbs: stable, agent-friendly entry points.

Each submodule registers its functions via the `register_tool` decorator,
so importing this package populates the ToolRegistry as a side effect.
"""

from .audio import text_to_speech, voice_clone  # noqa: F401
from .avatar import lipsync, talking_avatar_from_text  # noqa: F401
from .images import (  # noqa: F401
    edit_image,
    generate_image,
    remove_background,
    upscale_image,
)
from .llm import (  # noqa: F401
    apply_note_to_beat,
    apply_note_to_scene,
    llm_complete,
    parse_screenplay,
)
from .preproduction import (  # noqa: F401
    cast_character,
    cast_voice,
    establish_environment,
    storyboard_shot,
)
from .render import render_beat, render_scene, render_shot  # noqa: F401
from .video import image_to_video, text_to_video  # noqa: F401
