> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Seedance 2.0 Image To Video API

> API reference for Bytedance Seedance 2.0 Image To Video. ByteDance's most advanced image-to-video model. Animate still images into cinematic video with synchronized audio, start and end frame control,

**Endpoint:** `POST https://fal.run/bytedance/seedance-2.0/image-to-video`
**Endpoint ID:** `bytedance/seedance-2.0/image-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bytedance/seedance-2.0/image-to-video/playground">
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
      "bytedance/seedance-2.0/image-to-video",
      arguments={
          "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea.",
          "image_url": "https://v3b.fal.media/files/b/0a8eba37/Cqg-4Uwzyz4DELfceT1CF_a17e588773ec45b1a9e6f100a787b80b.jpg"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("bytedance/seedance-2.0/image-to-video", {
    input: {
        prompt: "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea.",
        image_url: "https://v3b.fal.media/files/b/0a8eba37/Cqg-4Uwzyz4DELfceT1CF_a17e588773ec45b1a9e6f100a787b80b.jpg"
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
    --url https://fal.run/bytedance/seedance-2.0/image-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea.",
    "image_url": "https://v3b.fal.media/files/b/0a8eba37/Cqg-4Uwzyz4DELfceT1CF_a17e588773ec45b1a9e6f100a787b80b.jpg"
  }'
  ```
</CodeGroup>

## Examples

> Ultra high-end commercial product shot, photorealistic, 8K, cinematic lighting, macro detail, shallow depth of field, premium advertising aesthetic, VR headset suspended by invisible wires against a deep navy backdrop, slow vertical tilt down across the visor, magenta and cyan accent lighting, studi...

<video src="https://v3b.fal.media/files/b/0a95998b/Y2JKGGVWMyjhMKf_FoqS5_video.mp4" controls width="100%" />

> Glimpses of light illuminate Jupiter's polar regions, showcasing the auroras. The visuals simply present the glowing displays, revealing their location and radiant nature. It is a direct view of space phenomena on Jupiter's poles.

<video src="https://v3b.fal.media/files/b/0a948ae5/wUeGPTJd_2zh_5MAPeSDh_video.mp4" controls width="100%" />

## Related

* [Seedance 2.0 Text to Video API](/model-api-reference/video-generation-api/seedance-2.0-text-to-video-api) — Video Generation
* [Seedance 2 Reference to Video](/model-api-reference/video-generation-api/seedance-2-reference-to-video) — Video Generation
* [Seedance 2.0 Fast Text to Video](/model-api-reference/video-generation-api/seedance-2.0-fast-text-to-video) — Video Generation
* [Seedance 2.0 Fast Image to Video](/model-api-reference/video-generation-api/seedance-2.0-fast-image-to-video) — Video Generation
* [Seedance 2.0 Fast Reference to Video](/model-api-reference/video-generation-api/seedance-2.0-fast-reference-to-video) — Video Generation

## Capabilities

* Text prompt input
* Image input
* Duration control
* Aspect ratio control
* Reproducible generation (seed)

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required>
  The text prompt describing the desired motion and action for the video.
</ParamField>

<ParamField body="image_url" type="string" required>
  The URL of the starting frame image to animate. Supported formats: JPEG, PNG, WebP. Max 30 MB.
</ParamField>

<ParamField body="end_image_url" type="string">
  The URL of the image to use as the last frame of the video. When provided, the generated video will transition from the starting image to this ending image. Supported formats: JPEG, PNG, WebP. Max 30 MB.
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
  The aspect ratio of the generated video. Use 16:9 for landscape, 9:16 for portrait/vertical, 1:1 for square, 21:9 for ultrawide cinematic, or auto to infer from the input image. Default value: `"auto"`

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
  "image_url": "https://v3b.fal.media/files/b/0a8eba37/Cqg-4Uwzyz4DELfceT1CF_a17e588773ec45b1a9e6f100a787b80b.jpg",
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
