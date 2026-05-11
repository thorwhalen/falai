> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Veo3.1 Extend Video API

> API reference for Veo3.1 Extend Video. Extend Veo-Created Videos up to 30 seconds

**Endpoint:** `POST https://fal.run/fal-ai/veo3.1/extend-video`
**Endpoint ID:** `fal-ai/veo3.1/extend-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/veo3.1/extend-video/playground">
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
      "fal-ai/veo3.1/extend-video",
      arguments={
          "prompt": "Continue the scene naturally, maintaining the same style and motion.",
          "video_url": "https://v3b.fal.media/files/b/0a8670fe/pY8UGl4_C452wOm9XUBYO_9ae04df8771c4f3f979fa5cabeca6ada.mp4"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/veo3.1/extend-video", {
    input: {
        prompt: "Continue the scene naturally, maintaining the same style and motion.",
        video_url: "https://v3b.fal.media/files/b/0a8670fe/pY8UGl4_C452wOm9XUBYO_9ae04df8771c4f3f979fa5cabeca6ada.mp4"
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
    --url https://fal.run/fal-ai/veo3.1/extend-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "Continue the scene naturally, maintaining the same style and motion.",
    "video_url": "https://v3b.fal.media/files/b/0a8670fe/pY8UGl4_C452wOm9XUBYO_9ae04df8771c4f3f979fa5cabeca6ada.mp4"
  }'
  ```
</CodeGroup>

## Related

* [Veo 3.1](/model-api-reference/video-generation-api/veo-3.1) — Video Generation
* [Veo 3.1 Fast](/model-api-reference/video-generation-api/veo-3.1-fast) — Video Generation
* [Veo3.1 Lite Image to Video](/model-api-reference/video-generation-api/veo3.1-lite-image-to-video) — Video Generation
* [Veo3.1 Lite FLF](/model-api-reference/video-generation-api/veo3.1-lite-flf) — Video Generation
* [Veo3.1 Lite Text to Video](/model-api-reference/video-generation-api/veo3.1-lite-text-to-video) — Video Generation

## Capabilities

* Text prompt input
* Aspect ratio control
* Duration control
* Negative prompts
* Reproducible generation (seed)
* Video input

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required>
  The text prompt describing how the video should be extended
</ParamField>

<ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
  The aspect ratio of the generated video. Default value: `"auto"`

  Possible values: `auto`, `16:9`, `9:16`
</ParamField>

<ParamField body="duration" type="string" default="7s">
  The duration of the generated video. Default value: `"7s"`
</ParamField>

<ParamField body="negative_prompt" type="string">
  A negative prompt to guide the video generation.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  The resolution of the generated video. Default value: `"720p"`
</ParamField>

<ParamField body="generate_audio" type="boolean" default="true">
  Whether to generate audio for the video. Default value: `true`
</ParamField>

<ParamField body="seed" type="integer">
  The seed for the random number generator.
</ParamField>

<ParamField body="auto_fix" type="boolean" default="false">
  Whether to automatically attempt to fix prompts that fail content policy or other validation checks by rewriting them.
</ParamField>

<ParamField body="safety_tolerance" type="SafetyToleranceEnum" default="4">
  The safety tolerance level for content moderation. 1 is the most strict (blocks most content), 6 is the least strict. Default value: `"4"`

  Possible values: `1`, `2`, `3`, `4`, `5`, `6`
</ParamField>

<ParamField body="video_url" type="string" required>
  URL of the video to extend. The video should be 720p or 1080p resolution in 16:9 or 9:16 aspect ratio.
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The extended video.
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "Continue the scene naturally, maintaining the same style and motion.",
  "aspect_ratio": "auto",
  "duration": "7s",
  "resolution": "720p",
  "generate_audio": true,
  "auto_fix": false,
  "safety_tolerance": "4",
  "video_url": "https://v3b.fal.media/files/b/0a8670fe/pY8UGl4_C452wOm9XUBYO_9ae04df8771c4f3f979fa5cabeca6ada.mp4"
}
```

## Output Example

```json theme={null}
{
  "video": {
    "url": "https://v3b.fal.media/files/b/0a86711b/B_Z96VS4X9Dfd4M5ArB4H_c666e63f729f4a8fa1145c6727cef97d.mp4"
  }
}
```

## Limitations

* `aspect_ratio` restricted to: `auto`, `16:9`, `9:16`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`, `6`
