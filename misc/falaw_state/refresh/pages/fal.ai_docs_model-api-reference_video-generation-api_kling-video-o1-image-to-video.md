> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video O1 Image To Video API

> API reference for Kling Video O1 Image To Video. Generate a video by taking a start frame and an end frame, animating the transition between them while following text-driven style and scene guidance.

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/o1/image-to-video`
**Endpoint ID:** `fal-ai/kling-video/o1/image-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/o1/image-to-video/playground">
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
      "fal-ai/kling-video/o1/image-to-video",
      arguments={
          "prompt": "Create a magical timelapse transition. The snow melts rapidly to reveal green grass, and the tree branches burst into bloom with pink flowers in real-time. The lighting shifts from cold winter light to warm spring sunshine. The camera pushes in slowly towards the tree. Disney-style magical transformation, cinematic, 8k.",
          "start_image_url": "https://v3b.fal.media/files/b/rabbit/NaslJIC7F2WodS6DFZRRJ.png"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/kling-video/o1/image-to-video", {
    input: {
        prompt: "Create a magical timelapse transition. The snow melts rapidly to reveal green grass, and the tree branches burst into bloom with pink flowers in real-time. The lighting shifts from cold winter light to warm spring sunshine. The camera pushes in slowly towards the tree. Disney-style magical transformation, cinematic, 8k.",
        start_image_url: "https://v3b.fal.media/files/b/rabbit/NaslJIC7F2WodS6DFZRRJ.png"
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
    --url https://fal.run/fal-ai/kling-video/o1/image-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "Create a magical timelapse transition. The snow melts rapidly to reveal green grass, and the tree branches burst into bloom with pink flowers in real-time. The lighting shifts from cold winter light to warm spring sunshine. The camera pushes in slowly towards the tree. Disney-style magical transformation, cinematic, 8k.",
    "start_image_url": "https://v3b.fal.media/files/b/rabbit/NaslJIC7F2WodS6DFZRRJ.png"
  }'
  ```
</CodeGroup>

Kuaishou's Kling O1 delivers first-frame-last-frame video generation at \$0.112 per second, animating precise transitions between two keyframes. Trading broad creative freedom for exact endpoint control, this specialized variant handles timelapse transformations, morphing sequences, and narrative scene transitions where both start and end states matter. Built for motion designers, creative studios, and developers who need deterministic video outputs rather than open-ended generation.

**Built for:** Timelapse animations | Product transformation sequences | Narrative scene transitions

***

## Dual-Keyframe Control Architecture

Kling O1's dual-keyframe approach inverts the standard image-to-video workflow by accepting both start and end images as constraints, then synthesizing the motion path between them. Where traditional image-to-video models extrapolate freely from a single frame, this variant interpolates along a defined trajectory while respecting prompt-driven style guidance.

**What this means for you:**

* **Deterministic endpoints:** Generate 5 or 10-second videos where both opening and closing frames match your exact specifications, critical for brand-consistent sequences or narrative continuity
* **Controlled transformation arcs:** Animate seasonal changes, product evolutions, or character state transitions with predictable motion paths rather than AI-improvised endings
* **Prompt-guided interpolation:** Reference start and end frames via `@Image1` and `@Image2` in prompts to direct style, camera movement, and scene dynamics during the transition
* **Flexible duration options:** Choose between 5-second ($0.56) or 10-second ($1.12) outputs to match pacing requirements for social media clips or longer editorial sequences

***

## Performance Scaling

Kling O1 operates within Kuaishou's broader Kling Video ecosystem, prioritizing frame-accurate transitions over generation speed.

| Metric                 | Result                            | Context                                                          |
| :--------------------- | :-------------------------------- | :--------------------------------------------------------------- |
| **Duration Options**   | 5s or 10s                         | Configurable via `duration` parameter                            |
| **Cost per Video**     | $0.56 (5s) or $1.12 (10s)         | Based on \$0.112 per second rate                                 |
| **Input Requirements** | Start + end frame (both required) | Min 300px dimensions, 0.40-2.50 aspect ratio, 10MB max per image |
| **Output Format**      | MP4 video                         | Single video file with synthesized motion path                   |

***

## Technical Specifications

| Spec                 | Details                                                                         |
| :------------------- | :------------------------------------------------------------------------------ |
| **Architecture**     | Kling O1                                                                        |
| **Input Formats**    | Start image (required), end image (required), text prompt with frame references |
| **Output Formats**   | MP4 video                                                                       |
| **Duration Options** | 5 seconds or 10 seconds                                                         |
| **Prompt Syntax**    | Use `@Image1` and `@Image2` to reference uploaded keyframes in prompts          |
| **License**          | Commercial use via fal partnership                                              |

[API Documentation](https://fal.ai/models/fal-ai/kling-video/o1/image-to-video/llms.txt)

***

## How It Stacks Up

**Kling Video Image to Video (v2.5-turbo)** - Kling O1 specializes in dual-keyframe interpolation for transformation sequences where endpoint precision matters, making it ideal for timelapse effects and morphing animations. [Kling Video v2.5-turbo](https://fal.ai/models/fal-ai/kling-video/v2.5-turbo/pro/image-to-video) emphasizes single-frame extrapolation with faster generation speeds for open-ended creative exploration.

**Kling 2.0 Master Image to Video** - Kling O1 trades generation flexibility for endpoint accuracy, constraining motion paths between two defined frames at a specialized price point. [Kling 2.0 Master](https://fal.ai/models/fal-ai/kling-video/v2/master/image-to-video) prioritizes maximum quality single-frame animation for premium production workflows requiring cinematic motion without endpoint constraints.

## Related

* [Kling O1 Edit Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-edit-video) — Video Generation
* [Kling O1 First Frame Last Frame to Video \[Standard\]](/model-api-reference/video-generation-api/kling-o1-first-frame-last-frame-to-video) — Video Generation
* [Kling O1 Reference Image to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-reference-image-to-video) — Video Generation
* [Kling O1 Reference Video to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-reference-video-to-video) — Video Generation

## Capabilities

* Text prompt input
* Duration control

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required>
  Use @Image1 to reference the start frame, @Image2 to reference the end frame.
</ParamField>

<ParamField body="start_image_url" type="string" required>
  Image to use as the first frame of the video.

  Max file size: 10.0MB, Min width: 300px, Min height: 300px, Min aspect ratio: 0.40, Max aspect ratio: 2.50, Timeout: 20.0s
</ParamField>

<ParamField body="end_image_url" type="string">
  Image to use as the last frame of the video.
</ParamField>

<ParamField body="duration" type="DurationEnum" default="5">
  Video duration in seconds. Default value: `"5"`

  Possible values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The generated video.
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "Create a magical timelapse transition. The snow melts rapidly to reveal green grass, and the tree branches burst into bloom with pink flowers in real-time. The lighting shifts from cold winter light to warm spring sunshine. The camera pushes in slowly towards the tree. Disney-style magical transformation, cinematic, 8k.",
  "start_image_url": "https://v3b.fal.media/files/b/rabbit/NaslJIC7F2WodS6DFZRRJ.png",
  "end_image_url": "https://v3b.fal.media/files/b/tiger/BwHi22qoQnqaTNMMhe533.png",
  "duration": "5"
}
```

## Output Example

```json theme={null}
{
  "video": {
    "content_type": "video/mp4",
    "file_name": "output.mp4",
    "file_size": 27588984,
    "url": "https://v3b.fal.media/files/b/koala/knryyyGF3ZVyMMrGr77CL_output.mp4"
  }
}
```

## Limitations

* `duration` restricted to: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`
