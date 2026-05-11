> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Seedance 2.0 Text To Video API

> API reference for Bytedance Seedance 2.0 Text To Video. ByteDance's most advanced text-to-video model. Cinematic output with native audio, multi-shot editing, real-world physics, and director-level ca

**Endpoint:** `POST https://fal.run/bytedance/seedance-2.0/text-to-video`
**Endpoint ID:** `bytedance/seedance-2.0/text-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bytedance/seedance-2.0/text-to-video/playground">
  Run this model interactively with your own prompts.
</Card>

## Quick Start

<CodeGroup>
  ```python title="Python" theme={null}
  import fal_client

  def on_queue_update(update):
      if isinstance(update, fal_client.InProgress):
          for log in update.logs:
             print(log["message"])

  result = fal_client.subscribe(
      "bytedance/seedance-2.0/text-to-video",
      arguments={
          "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("bytedance/seedance-2.0/text-to-video", {
    input: {
        prompt: "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."
      },
    logs: true,
    onQueueUpdate: (update) => {
      if (update.status === "IN_PROGRESS") {
        update.logs.map((log) => log.message).forEach(console.log);
      }
    },
  });
  console.log(result.data);
  console.log(result.requestId);
  ```

  ```bash title="cURL" theme={null}
  curl --request POST \
    --url https://fal.run/bytedance/seedance-2.0/text-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."
  }'
  ```
</CodeGroup>

## Examples

> ltra high-end editorial photography, photorealistic, 8K, razor-sharp detail, perfect skin texture with natural pores and subsurface scattering, cinematic lighting, shot on medium format, Portrait: 31-year-old Black British architect in a cream blazer, standing in a brutalist concrete stairwell, soft...

<video src="https://v3b.fal.media/files/b/0a959980/O8bR1l3Z8tvZiNDNVUBDM_video.mp4" controls width="100%" />

> A shimmering soap film stretches across a circular frame, catching the light. The secrets to achieving a perfectly spherical bubble are unveiled as the surface tension and air pressure work in harmony. This exploration reveals the simple yet elegant physics at play, creating fleeting moments of irid...

<video src="https://v3b.fal.media/files/b/0a948b06/f_MwnfesPZNuFJnIKra1i_video.mp4" controls width="100%" />

ByteDance's most advanced video generation model. Generate cinematic video with native audio, real-world physics, and director-level camera control, all in a single pass.

`bytedance/seedance-2.0`

***

## Overview

Seedance 2.0 is built on a unified multimodal architecture that accepts text, images, video clips, and audio as inputs and produces coherent, audio-synchronized video output. Audio and video are generated together natively, no post-production layering.

***

## API Endpoints

| Endpoint                  | Model ID                                         |
| ------------------------- | ------------------------------------------------ |
| Text to Video             | `bytedance/seedance-2.0/text-to-video`           |
| Text to Video (Fast)      | `bytedance/seedance-2.0/fast/text-to-video`      |
| Image to Video            | `bytedance/seedance-2.0/image-to-video`          |
| Image to Video (Fast)     | `bytedance/seedance-2.0/fast/image-to-video`     |
| Reference to Video        | `bytedance/seedance-2.0/reference-to-video`      |
| Reference to Video (Fast) | `bytedance/seedance-2.0/fast/reference-to-video` |

Standard endpoints prioritize maximum quality. Fast endpoints offer lower latency and cost for production workloads.

***

## Pricing

| Endpoint             | Price             |
| -------------------- | ----------------- |
| 720p with audio      | \$0.3034 / second |
| 720p fast with audio | \$0.2419 / second |

***

## What's new in 2.0

**Multimodal reference inputs.** Combine up to 9 images, 3 video clips, and 3 audio files in a single generation via the reference-to-video endpoint. Reference them in your prompt using `[Image1]`, `[Video1]`, `[Audio1]`, etc.

**Better motion and physics.** More realistic rendering of complex interactions — sports, dancing, fighting, object collisions, and more.

**Video editing and extension.** Provide a reference video and describe what to change, or describe what should happen next to extend it.

**Intelligent duration.** Set `duration` to `"auto"` and the model picks the optimal length for the content.

**Adaptive aspect ratio.** Set `aspect_ratio` to `"auto"` and the model chooses the best fit based on your inputs.

***

## Usage

Install the client:

```bash theme={null}
npm install --save @fal-ai/client
```

> **Note:** `@fal-ai/serverless-client` is deprecated. Use `@fal-ai/client` instead.

### Python

```python theme={null}
import fal_client

result = fal_client.subscribe(
    "bytedance/seedance-2.0/text-to-video",
    arguments={
        "prompt": "A spear-wielding warrior clashes with a dual-blade fighter in a maple leaf forest. Autumn leaves scatter on each impact.",
        "duration": "5",
        "resolution": "720p",
        "aspect_ratio": "16:9",
    }
)

print(result["video"]["url"])
```

### JavaScript

```javascript theme={null}
import { fal } from "@fal-ai/client";

const result = await fal.subscribe("bytedance/seedance-2.0/text-to-video", {
  input: {
    prompt: "A spear-wielding warrior clashes with a dual-blade fighter in a maple leaf forest. Autumn leaves scatter on each impact.",
    duration: "5",
    resolution: "720p",
    aspect_ratio: "16:9",
  },
  logs: true,
  onQueueUpdate: (update) => {
    if (update.status === "IN_PROGRESS") {
      update.logs.map((log) => log.message).forEach(console.log);
    }
  },
});

console.log(result.data);
```

### REST

```bash theme={null}
curl -X POST https://fal.run/bytedance/seedance-2.0/text-to-video \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A spear-wielding warrior clashes with a dual-blade fighter in a maple leaf forest.",
    "duration": "5",
    "resolution": "720p",
    "aspect_ratio": "16:9"
  }'
```

***

## Input schema

### Text to Video (`bytedance/seedance-2.0/text-to-video`)

| Parameter        | Type    | Default  | Description                                                                                 |
| ---------------- | ------- | -------- | ------------------------------------------------------------------------------------------- |
| `prompt`         | string  | —        | **Required.** Scene description. Put spoken dialogue in double quotes for lip-synced audio. |
| `resolution`     | string  | `"720p"` | `"480p"` or `"720p"`                                                                        |
| `duration`       | string  | `"auto"` | `"auto"`, or `"4"` through `"15"`                                                           |
| `aspect_ratio`   | string  | `"auto"` | `"auto"`, `"21:9"`, `"16:9"`, `"4:3"`, `"1:1"`, `"3:4"`, `"9:16"`                           |
| `generate_audio` | boolean | `true`   | Generate synchronized audio alongside video.                                                |
| `seed`           | integer | —        | Optional seed for reproducibility.                                                          |
| `end_user_id`    | string  | —        | Required for B2B access. Unique identifier for your end customer.                           |

### Image to Video (`bytedance/seedance-2.0/image-to-video`)

All text-to-video parameters, plus:

| Parameter       | Type   | Description                                                                     |
| --------------- | ------ | ------------------------------------------------------------------------------- |
| `image_url`     | string | **Required.** Start frame image URL. Accepted: jpg, jpeg, png, webp, gif, avif. |
| `end_image_url` | string | Optional end frame image to control where the video concludes.                  |

### Reference to Video (`bytedance/seedance-2.0/reference-to-video`)

Accepts text prompts combined with up to 9 images, 3 video clips, and 3 audio files. Reference inputs in your prompt as `[Image1]`, `[Video1]`, `[Audio1]`, etc.

***

## Output schema

```json theme={null}
{
  "video": {
    "url": "https://v3b.fal.media/files/...",
    "content_type": "video/mp4",
    "file_name": "video.mp4",
    "file_size": 4352150
  },
  "seed": 1094575694
}
```

Access the video URL at `result["video"]["url"]` (Python) or `result.data.video.url` (JavaScript).

***

## Supported resolutions

|          | 21:9     | 16:9     | 4:3      | 1:1     | 3:4      | 9:16     |
| -------- | -------- | -------- | -------- | ------- | -------- | -------- |
| **480p** | 992×432  | 864×496  | 752×560  | 640×640 | 560×752  | 496×864  |
| **720p** | 1470×630 | 1280×720 | 1112×834 | 960×960 | 834×1112 | 720×1280 |

***

## Capabilities

**Text to video.** Describe a scene and get video with matching audio. The model handles multi-subject interactions, camera movements, and emotional tone. For dialogue, put speech in double quotes — the model generates matching lip movements and voice.

**Image to video.** Animate a still image using it as the first frame. Optionally provide an end frame to control where the video concludes. The model preserves the look and style of your input image while adding natural motion.

**Multimodal reference.** Combine images, videos, and audio as references in a single generation via the reference-to-video endpoint. Provide a reference video for motion style, reference images for character appearance, and reference audio for rhythm — then describe how to combine them. Powerful for outfit-change videos, product showcases, and music-synced content.

**Video editing.** Provide a reference video and describe changes — replace an object, change a background, alter the style. The model preserves original motion and camera work while applying your edits.

**Video extension.** Provide a reference video and describe what should happen next. The model continues the scene with consistent characters, environment, and style.

***

## Tips

* **Be specific.** Describe camera movements, lighting, mood, and specific actions for best results.
* **Dialogue.** Wrap spoken lines in double quotes: `The man stopped and said: "Remember this moment."`
* **Referencing inputs.** Label them explicitly in your prompt: `"The character from [Image1] performs the dance from [Video1]."`
* **Video editing.** Describe what to change and what to preserve: `"Replace the perfume in [Video1] with the face cream from [Image1], keeping all original motion."`
* **Iterate fast.** Start with 5-second generations to nail the style, then increase duration.

## Related

* [Seedance 2 Image to Video](/model-api-reference/video-generation-api/seedance-2-image-to-video) — Video Generation
* [Seedance 2 Reference to Video](/model-api-reference/video-generation-api/seedance-2-reference-to-video) — Video Generation
* [Seedance 2.0 Fast Text to Video](/model-api-reference/video-generation-api/seedance-2.0-fast-text-to-video) — Video Generation
* [Seedance 2.0 Fast Image to Video](/model-api-reference/video-generation-api/seedance-2.0-fast-image-to-video) — Video Generation
* [Seedance 2.0 Fast Reference to Video](/model-api-reference/video-generation-api/seedance-2.0-fast-reference-to-video) — Video Generation

## Capabilities

* Text prompt input
* Duration control
* Aspect ratio control
* Reproducible generation (seed)

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required>
  The text prompt used to generate the video
</ParamField>

<ParamField body="resolution" type="ResolutionEnum" default="720p">
  Video resolution - 480p for faster generation, 720p for balance. Default value: `"720p"`

  Possible values: `480p`, `720p`
</ParamField>

<ParamField body="duration" type="DurationEnum" default="auto">
  Duration of the video in seconds. Supports 4 to 15 seconds, or auto to let the model decide based on the prompt. Default value: `"auto"`

  Possible values: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`
</ParamField>

<ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
  The aspect ratio of the generated video. Use 16:9 for landscape, 9:16 for portrait/vertical, 1:1 for square, 21:9 for ultrawide cinematic, or auto to let the model decide. Default value: `"auto"`

  Possible values: `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
</ParamField>

<ParamField body="generate_audio" type="boolean" default="true">
  Whether to generate synchronized audio for the video, including sound effects, ambient sounds, and lip-synced speech. The cost of video generation is the same regardless of whether audio is generated or not. Default value: `true`
</ParamField>

<ParamField body="seed" type="integer">
  Random seed for reproducibility. Note that results may still vary slightly even with the same seed.
</ParamField>

<ParamField body="end_user_id" type="string">
  The unique user ID of the end user.
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The generated video file.
</ParamField>

<ParamField body="seed" type="integer" required>
  The seed used for generation.
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea.",
  "resolution": "720p",
  "duration": "auto",
  "aspect_ratio": "auto",
  "generate_audio": true
}
```

## Output Example

```json theme={null}
{
  "video": {
    "url": "https://storage.googleapis.com/falserverless/example_outputs/bytedance/seedance_2/output.mp4"
  },
  "seed": 42
}
```

## Limitations

* `resolution` restricted to: `480p`, `720p`
* `aspect_ratio` restricted to: `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
