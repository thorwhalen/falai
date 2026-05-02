"""Render a Claude SKILL.md (and references) from the falaw tool registry.

The skill is the entry point that teaches Claude Code how to use falaw. It
is generated --- never hand-edited at the install location --- so adding a
new tool automatically updates the skill the next time we run
`write_skill_files()`.
"""

from __future__ import annotations

import os
from typing import Iterable, Optional

from ..base import ToolSpec
from ..registry import list_models, list_tools

_HEADER = """---
name: falaw
description: >-
  Generate and manage AI media (images, video, audio) via fal.ai. Use this
  skill whenever the user wants to generate, edit, upscale, or compose media,
  or asks about fal.ai or fal-client. Also use it for *directorial* workflows:
  the user defines a Scene as data (characters, beats, shots) and falaw renders
  it with caching, so a single edit re-renders only what changed.
---

# falaw

Two ways to use `falaw`:

1. **Single-shot operations** --- `generate_image`, `text_to_speech`, etc. for
   one-off media generation.
2. **Directorial workflow** --- author a Scene as data, render it, give notes
   that re-edit the Scene, re-render only the affected beats. This is the path
   to *direct* a film instead of just *generate* clips.

## Directorial workflow (when the user wants to "plan, parametrize, render")

The thesis: keep the film in *editable structure* all the way down to the
pixels. The creator authors a Scene as data; a directorial note becomes a
single IR edit; the renderer caches everything content-addressed so unchanged
beats don't re-render.

### Phase 1: Plan (LLM-assisted or hand-built)

```python
from falaw import parse_screenplay, Scene, Character, Environment, make_beat, make_shot

# Option A: feed prose / treatment text and let any-llm draft the structure.
scene = parse_screenplay(prose_text, title="Diner Encounter",
                         style="Wes-Anderson pastel")

# Option B: build the Scene directly.
scene = Scene(
    title="Diner Encounter",
    style="Wes-Anderson symmetrical pastel",
    characters=(Character(name="Sarah", description="mid-30s, dark curly hair"),),
    environments=(Environment(name="diner", description="1950s chrome diner",
                              time_of_day="midnight"),),
    shots=(make_shot("two-shot at the booth", framing="medium",
                     environment="diner", characters=("Sarah", "Tom"), index=0),),
    beats=(
        make_beat("Sarah", "Why are you here?",
                  shot_id="...", emotion="wary", index=0),
        make_beat("Tom", "I came to apologize.", index=1),
    ),
)
```

### Phase 2: Parametrize (set identity anchors)

Cast each character with a *canonical* face and voice. These anchors get
reused for every shot/beat that character appears in --- this is what gives
identity continuity.

```python
from falaw import cast_character, establish_environment

sarah = cast_character("Sarah", "mid-30s, dark curly hair, wary eyes",
                       reference_audio_url="https://.../sarah_sample.wav")
diner = establish_environment("diner",
                              "1950s chrome diner, neon outside, half-empty booths",
                              time_of_day="midnight", lighting="cool fluorescents")
scene = scene.with_character(sarah).with_environment(diner)
```

### Phase 3: Render (caches; re-edits are cheap)

```python
from falaw import render_scene, save_scene

manifest = render_scene(scene)             # all beats + shots
save_scene(scene, "out/diner_v1.json")     # snapshot the IR alongside
```

### Phase 4: Direct (notes -> IR edits -> re-render)

```python
from falaw import apply_note_to_beat

# Pick the beat to direct.
beat = scene.beat("002-tom-...")
edited = apply_note_to_beat(beat, "He cracks on this line; tries to hide it.")
scene2 = scene.with_beat(edited)
manifest2 = render_scene(scene2)   # only the edited beat re-renders;
                                   # the rest are cache hits.
```

For cross-cutting notes like "tighten the pacing", use
`apply_note_to_scene(scene, note)`. For non-LLM edits, just construct the
new dataclass yourself --- everything is frozen so `dataclasses.replace`
works.

### Local stitching

`falaw.local` (requires ffmpeg) stitches the per-beat lipsynced clips into
a watchable scene:

```python
from falaw.local import concatenate_clips
concatenate_clips([m["url"] for m in manifest["beats"]],
                  output_path="out/scene.mp4", transition_s=0.2)
```

## Read the journal first

Before novel work, glance at recent entries --- past sessions may have
left notes that save you time:

```python
from falaw import journal
for e in journal.recent(20):
    print(e.kind, '-', e.text[:120])
```

## Leave a journal entry when something surprises you

```python
from falaw import journal
journal.issue("FLUX dev returned NSFW=True for a benign prompt",
              suggestion="Try guidance_scale=2.0", tags=("flux", "safety"))
journal.improvement("Pass beat.emotion as a TTS prompt arg for emotion-aware models",
                    tags=("backlog", "directorial"))
journal.note("schnell at quality='fast' returns 1024x1024 by default")
```

## Pick a model without memorizing IDs

```python
from falaw import list_models, pick_model
[m.id for m in list_models(category='image_to_video')]
pick_model(category='image_edit', quality_tier='ultra').id
```

## Tools

Every function below is a registered tool; bridges (MCP server, HTTP
service, UI) derive their surfaces from the same registry.
"""

_FOOTER_TEMPLATE = """
## Models known to falaw

The model registry lives at `falaw/data/models.json`. Refresh it from
`misc/docs/fal_ai_docs_full.md` when fal ships new models. Quick view:

```
{model_lines}
```

## When you can't find what you need

* Check `falaw/misc/docs/llms-full.txt` for a structured fal.ai overview.
* Check `falaw/misc/docs/fal_ai_docs_full.md` for the full corpus (~3MB).
* Drop into `falaw.call_fal(application, arguments)` for any model not
  yet wrapped --- this is the escape hatch. Then leave a `journal.improvement`
  asking for a proper tool wrapper.
"""


def build_skill_md(tools: Optional[Iterable[ToolSpec]] = None) -> str:
    """Render the SKILL.md content from the tool registry."""
    tools = list(tools if tools is not None else list_tools())
    parts = [_HEADER]
    for t in tools:
        parts.append(f"\n### `falaw.{t.name}`\n")
        parts.append(t.description.strip())
        parts.append("")
        if t.examples:
            parts.append("Examples:")
            for ex in t.examples:
                parts.append(f"  - `falaw.{t.name}(**{dict(ex)!r})`")
            parts.append("")
    model_lines = "\n".join(
        f"  {m.category:20s} {m.quality_tier:10s} {m.id}"
        for m in sorted(list_models(), key=lambda x: (x.category, x.quality_tier))
    )
    parts.append(_FOOTER_TEMPLATE.format(model_lines=model_lines))
    return "\n".join(parts)


def write_skill_files(target_dir: str) -> str:
    """Write SKILL.md (and a small references/ folder) under `target_dir`.

    Returns the path written.
    """
    os.makedirs(os.path.join(target_dir, "references"), exist_ok=True)
    skill_path = os.path.join(target_dir, "SKILL.md")
    with open(skill_path, "w") as f:
        f.write(build_skill_md())
    return skill_path
