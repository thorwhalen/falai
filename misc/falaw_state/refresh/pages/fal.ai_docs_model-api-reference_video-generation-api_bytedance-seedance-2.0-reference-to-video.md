> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Seedance 2.0 Reference To Video API

> API reference for Bytedance Seedance 2.0 Reference To Video. ByteDance's most advanced reference-to-video model. Generate video from up to 9 images, 3 videos, and 3 audio clips with native audio and c

**Endpoint:** `POST https://fal.run/bytedance/seedance-2.0/reference-to-video`
**Endpoint ID:** `bytedance/seedance-2.0/reference-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bytedance/seedance-2.0/reference-to-video/playground">
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
      "bytedance/seedance-2.0/reference-to-video",
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

  const result = await fal.subscribe("bytedance/seedance-2.0/reference-to-video", {
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
    --url https://fal.run/bytedance/seedance-2.0/reference-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."
  }'
  ```
</CodeGroup>

## Examples

> Room is slowly getting filled from empty state to fully organized with furnitures. Camera is fixed timelapse.

<video src="https://v3b.fal.media/files/b/0a959a18/ojveMSkwmwthBKa4b-lIF_video.mp4" controls width="100%" />

> Sunlight filters into a crystalline cave, illuminating formations that hum softly. Air currents brush through the formations, their gentle vibrations creating ethereal melodies throughout the cavern. The serene simplicity of the cave reveals nature's delicate, musical architecture where tiny cleaner...

<video src="https://v3b.fal.media/files/b/0a948aed/kLlLreInOcDz2BkoGxtxb_video.mp4" controls width="100%" />

## Related

* [Seedance 2.0 Text to Video API](/model-api-reference/video-generation-api/seedance-2.0-text-to-video-api) — Video Generation
* [Seedance 2 Image to Video](/model-api-reference/video-generation-api/seedance-2-image-to-video) — Video Generation
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
  The text prompt used to generate the video.
</ParamField>

<ParamField body="image_urls" type="list<string>">
  Reference images to guide video generation. Refer to them in the prompt as @Image1, @Image2, etc. Supported formats: JPEG, PNG, WebP. Max 30 MB per image. Up to 9 images. Total files across all modalities must not exceed 12.
</ParamField>

<ParamField body="video_urls" type="list<string>">
  Reference videos to guide video generation. Refer to them in the prompt as @Video1, @Video2, etc. Supported formats: MP4, MOV. Up to 3 videos, combined duration must be between 2 and 15 seconds, total size under 50 MB. Each video must be between \~480p (640x640) and \~720p (834x1112) in resolution.
</ParamField>

<ParamField body="audio_urls" type="list<string>">
  Reference audio to guide video generation. Refer to them in the prompt as @Audio1, @Audio2, etc. Supported formats: MP3, WAV. Up to 3 files, combined duration must not exceed 15 seconds. Max 15 MB per file.If audio is provided, at least one reference image or video is required.
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
  "image_urls": [
    "https://v3b.fal.media/files/b/0a8eba37/Cqg-4Uwzyz4DELfceT1CF_a17e588773ec45b1a9e6f100a787b80b.jpg"
  ],
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
