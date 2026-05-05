---
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


### `falaw.refresh_models_from_corpus`

Parse `misc/docs/llms-full.txt` and merge any newly-discovered models into `falaw/data/models.json`. Hand-curated entries are preserved; only previously-unknown ids are added. Pass `write=True` to persist; otherwise returns a dry-run summary.


### `falaw.text_to_speech`

Synthesize speech from text. Picks a TTS model by quality tier; pass `voice` and `extra` for model-specific knobs. Returns a falaw.Result whose .first asset is the audio URL.

Examples:
  - `falaw.text_to_speech(**{'text': 'Hello world', 'quality': 'balanced'})`
  - `falaw.text_to_speech(**{'text': 'Bonjour le monde', 'quality': 'high', 'voice': 'fr-FR-female-1'})`


### `falaw.voice_clone`

Synthesize speech in a cloned voice. Provide a `reference_audio_url` (a few seconds of the target voice) and the text to speak. Returns a falaw.Result whose .first asset is the cloned-voice audio URL.

Examples:
  - `falaw.voice_clone(**{'reference_audio_url': 'https://example.com/me.wav', 'text': 'Hello, this is in my voice.'})`


### `falaw.lipsync`

Generate a lip-synced talking-head video from a face image and an audio track. Returns a falaw.Result whose .first asset is the synced video URL.

Examples:
  - `falaw.lipsync(**{'image_url': 'https://...', 'audio_url': 'https://...'})`


### `falaw.talking_avatar_from_text`

Composer: text + face image → lip-synced talking video. Internally runs `text_to_speech(text)` then `lipsync(image_url, audio_url)`. Returns the lipsync Result. Use this when you have text and a portrait but no pre-recorded audio.

Examples:
  - `falaw.talking_avatar_from_text(**{'text': 'Welcome to the demo.', 'image_url': 'https://example.com/host.jpg'})`


### `falaw.generate_image`

Generate an image from a text prompt. Picks a sensible FLUX model based on the requested quality tier ('fast', 'balanced', 'high', 'ultra'). Returns a falaw.Result whose .first asset has a URL you can .download(to=...).

Examples:
  - `falaw.generate_image(**{'prompt': 'A red panda eating bamboo', 'quality': 'fast'})`
  - `falaw.generate_image(**{'prompt': 'Cinematic portrait, 35mm film', 'quality': 'ultra'})`


### `falaw.edit_image`

Edit an image using a natural-language instruction. Picks a FLUX Kontext / SeedEdit model by quality tier. Returns a falaw.Result with the edited image.

Examples:
  - `falaw.edit_image(**{'image_url': 'https://...', 'prompt': 'make the sky orange'})`
  - `falaw.edit_image(**{'image_url': 'https://...', 'prompt': 'remove the person on the left', 'quality': 'ultra'})`


### `falaw.upscale_image`

Upscale an image to higher resolution while preserving fidelity. Defaults to clarity-upscaler. Returns a falaw.Result with the upscaled image.

Examples:
  - `falaw.upscale_image(**{'image_url': 'https://...', 'scale': 2.0})`
  - `falaw.upscale_image(**{'image_url': 'https://...', 'scale': 4.0, 'extra': {'creativity': 0.35}})`


### `falaw.remove_background`

Remove the background from an image, returning a transparent PNG. Defaults to BiRefNet v2 (quality='high') or Bria (quality='balanced'). Returns a falaw.Result.

Examples:
  - `falaw.remove_background(**{'image_url': 'https://example.com/photo.jpg'})`


### `falaw.llm_complete`

Run a single LLM completion via fal-ai/any-llm. Returns the raw text output. Use `system` for instruction prompts, `prompt` for the user message. Cached by content.

Examples:
  - `falaw.llm_complete(**{'prompt': 'summarize this scene in one line', 'system': 'you are a script consultant'})`


### `falaw.parse_screenplay`

Parse prose screenplay/treatment text into a structured Scene (via any-llm). Returns a falaw.Scene you can render directly. Use `model_hint` to pick a stronger LLM for nuanced material.


### `falaw.apply_note_to_beat`

Apply a directorial note to a single Beat using an LLM. Returns an updated Beat (same id; modified content fields). Use this to implement 'he cracks on this line; she softens but hides it' without manually rewriting the structure.

Examples:
  - `falaw.apply_note_to_beat(**{'beat': {'id': '001-john-abcd', 'speaker': 'John', 'line': "It's fine.", 'emotion': ''}, 'note': 'He cracks on this line --- voice goes up.'})`


### `falaw.apply_note_to_scene`

Apply a directorial note to the whole Scene by asking the LLM for a JSON patch (which beats/shots to edit, with new content). Returns a new Scene. Use for cross-cutting notes like 'tighten the pacing in the middle' or 'add a reaction shot after beat 5'.


### `falaw.cast_character`

Generate or attach a canonical face image for a character, plus an optional voice. Returns an updated Character with `reference_image_url` set --- the anchor used by every later lipsync render. Pass an existing image_url to skip generation.

Examples:
  - `falaw.cast_character(**{'name': 'Sarah', 'description': 'mid-30s, sharp features, dark curly hair, wary eyes'})`


### `falaw.cast_voice`

Attach or refine a Voice for an existing Character. Provide a `reference_audio_url` (for cloning) or a `voice_id` (model-side preset). Returns the updated Character.


### `falaw.establish_environment`

Generate or attach a canonical establishing image for a location. Used as visual anchor and lighting reference for every shot in that environment. Returns an Environment.

Examples:
  - `falaw.establish_environment(**{'name': 'diner', 'description': '1950s American chrome diner, neon outside, half-empty booths', 'time_of_day': 'midnight'})`


### `falaw.storyboard_shot`

Render a still preview (storyboard frame) for a single Shot, composited with its Environment and the Characters in view. Returns the URL of the still --- use it as a reference image for downstream image-to-video.


### `falaw.render_beat`

Render one Beat: TTS (using the speaker's Voice) → lipsync to the speaker's reference image. Cached by content hash --- re-rendering an unchanged Beat is a no-op. Returns {url, cache_hit, hash, audio_url}.


### `falaw.render_shot`

Render a Shot: a still (storyboard) or short clip if `as_video=True` (image-to-video). Cached by content hash. Returns {url, cache_hit, hash, kind}.


### `falaw.render_scene`

Render an entire Scene: every Shot + every Beat, with caching so unchanged units are no-ops. Returns a manifest dict with per-beat and per-shot results, plus aggregate counts. Pass `force=True` to bypass the cache. `concurrency=N` (default 1) runs N units in parallel through a thread pool. For live progress, use `iter_render_scene(scene, concurrency=N)` which yields `(kind, result)` pairs as each unit completes.

Subscribe to progress events with `falaw.subscribe(callback)` (callback gets `ProgressEvent(kind, application, call_id, message, pct, elapsed_s)`); kinds include `queued`, `progress`, `log`, `done`, `error`, and `cache_hit`. Use `estimate_scene_cost(scene)` to get a USD `CostRollup` before kicking off a render — useful for budget gating.


### `falaw.text_to_video`

Generate a video from a text prompt. Picks a tier-appropriate model (Veo 3 for ultra, Seedance Pro for high). Use `extra` to pass through model-specific knobs like duration, aspect_ratio, negative_prompt.

Examples:
  - `falaw.text_to_video(**{'prompt': 'A drone shot over a misty pine forest at dawn'})`
  - `falaw.text_to_video(**{'prompt': 'Macro: a single dewdrop on a spider web', 'quality': 'ultra'})`


### `falaw.image_to_video`

Animate a still image into a short video. Optional prompt steers the motion. Picks a tier-appropriate i2v model (Kling Master for ultra, Seedance for high, Hailuo for balanced).

Examples:
  - `falaw.image_to_video(**{'image_url': 'https://...', 'prompt': 'the camera slowly zooms in'})`
  - `falaw.image_to_video(**{'image_url': 'https://...', 'quality': 'balanced'})`


### `falaw.refresh_llms`

Refresh `llms.txt` and `llms-full.txt` from fal.ai using conditional GETs (ETag-based). Cheap: returns immediately if nothing changed. On change, snapshots the previous version and journals the diff. Returns a summary dict like {'llms': {'changed': False}, ...}.


### `falaw.refresh_full_docs`

Re-crawl every per-page .md endpoint listed in `fal_ai_docs_index.md` with conditional GETs, then reassemble `fal_ai_docs_full.md`. Heavy. Gated on `is_stale(llms-full)` by default --- pass `force=True` to skip the gate. Pages that 304 are skipped; only changed pages re-download. Logs a single journal entry summarizing the run.


## Models known to falaw

The model registry lives at `falaw/data/models.json`. Refresh it from
`misc/docs/fal_ai_docs_full.md` when fal ships new models. Quick view:

```
  audio                balanced   fal-ai/elevenlabs/audio-isolation
  audio                balanced   fal-ai/playai/inpaint/diffusion
  avatar               balanced   fal-ai/ai-avatar
  background_removal   balanced   fal-ai/bria/background/remove
  background_removal   balanced   fal-ai/ideogram/v3/reframe
  background_removal   high       fal-ai/birefnet/v2
  image                balanced   fal-ai/flux/dev
  image                balanced   fal-ai/ideogram/v3
  image                balanced   fal-ai/recraft/v3/text-to-image
  image                fast       fal-ai/flux/schnell
  image                fast       fal-ai/hidream-i1-fast
  image                fast       fal-ai/sana/sprint
  image                high       fal-ai/flux-pro/v1.1
  image                ultra      fal-ai/flux-pro/v1.1-ultra
  image                ultra      fal-ai/imagen4/preview/ultra
  image_edit           balanced   fal-ai/flux-kontext/dev
  image_edit           balanced   fal-ai/omnigen-v2
  image_edit           high       fal-ai/bytedance/seededit/v3/edit-image
  image_edit           ultra      fal-ai/flux-pro/kontext/max
  image_to_video       balanced   fal-ai/minimax/hailuo-02/pro/image-to-video
  image_to_video       balanced   fal-ai/pixverse/v4.5/image-to-video
  image_to_video       high       fal-ai/bytedance/seedance/v1/pro/image-to-video
  image_to_video       ultra      fal-ai/kling-video/v2.1/master/image-to-video
  lipsync              balanced   fal-ai/ai-avatar/multi
  lipsync              balanced   fal-ai/kling-video/lipsync/audio-to-video
  lipsync              high       fal-ai/sync-lipsync/v2
  llm                  balanced   fal-ai/any-llm
  llm                  balanced   fal-ai/any-llm/vision
  music                balanced   fal-ai/diffrhythm
  music                balanced   fal-ai/mmaudio-v2/text-to-audio
  music                high       fal-ai/lyria2
  text_to_video        high       fal-ai/bytedance/seedance/v1/pro/text-to-video
  text_to_video        ultra      fal-ai/veo3
  training             balanced   fal-ai/flux-lora-portrait-trainer
  training             fast       fal-ai/flux-lora-fast-training
  training             high       fal-ai/flux-pro-trainer
  tts                  balanced   fal-ai/playai/tts/dialog
  tts                  balanced   fal-ai/playai/tts/v3
  tts                  high       fal-ai/elevenlabs/tts/multilingual-v2
  tts                  high       fal-ai/minimax/speech-02-hd
  upscale              high       fal-ai/clarity-upscaler
  voice_clone          high       fal-ai/minimax/voice-clone
```

## When you can't find what you need

* Check `falaw/misc/docs/llms-full.txt` for a structured fal.ai overview.
* Check `falaw/misc/docs/fal_ai_docs_full.md` for the full corpus (~3MB).
* Drop into `falaw.call_fal(application, arguments)` for any model not
  yet wrapped --- this is the escape hatch. Then leave a `journal.improvement`
  asking for a proper tool wrapper.
