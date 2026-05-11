> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video V1 Pro API

> API reference for Kling Video V1 Pro. Kling AI Avatar Pro: The premium endpoint for creating avatar videos with realistic humans, animals, cartoons, or stylized characters

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/v1/pro/ai-avatar`
**Endpoint ID:** `fal-ai/kling-video/v1/pro/ai-avatar`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v1/pro/ai-avatar/playground">
  Run this model interactively with your own prompts.
</Card>

### Quick Start

<CodeGroup>
  ```python title="Python" theme={null}
  import fal_client

  def on_queue_update(update):
      if isinstance(update, fal_client.InProgress):
          for log in update.logs:
             print(log["message"])

  result = fal_client.subscribe(
      "fal-ai/kling-video/v1/pro/ai-avatar",
      arguments={
          "image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling_ai_avatar_input.jpg",
          "audio_url": "https://v3.fal.media/files/rabbit/9_0ZG_geiWjZOmn9yscO6_output.mp3"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/kling-video/v1/pro/ai-avatar", {
    input: {
        image_url: "https://storage.googleapis.com/falserverless/example_inputs/kling_ai_avatar_input.jpg",
        audio_url: "https://v3.fal.media/files/rabbit/9_0ZG_geiWjZOmn9yscO6_output.mp3"
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
    --url https://fal.run/fal-ai/kling-video/v1/pro/ai-avatar \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling_ai_avatar_input.jpg",
    "audio_url": "https://v3.fal.media/files/rabbit/9_0ZG_geiWjZOmn9yscO6_output.mp3"
  }'
  ```
</CodeGroup>

### Input Schema

<ParamField body="image_url" type="string" required>
  The URL of the image to use as your avatar
</ParamField>

<ParamField body="audio_url" type="string" required>
  The URL of the audio file.
</ParamField>

<ParamField body="prompt" type="string" default=".">
  The prompt to use for the video generation. Default value: `"."`
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The generated video
</ParamField>

<ParamField body="duration" type="float" required>
  Duration of the output video in seconds.
</ParamField>

### Input Example

```json theme={null}
{
  "image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling_ai_avatar_input.jpg",
  "audio_url": "https://v3.fal.media/files/rabbit/9_0ZG_geiWjZOmn9yscO6_output.mp3",
  "prompt": "."
}
```

### Output Example

```json theme={null}
{
  "video": {
    "url": "https://v3.fal.media/files/penguin/ln3x7H1p1jL0Pwo7675NI_output.mp4"
  }
}
```

## Related

* [Kling AI Avatar v2 Pro](/model-api-reference/video-generation-api/kling-ai-avatar-v2-pro) — Video Generation
* [Kling AI Avatar v2 Standard](/model-api-reference/video-generation-api/kling-ai-avatar-v2-standard) — Video Generation
* [Kling AI Avatar](/model-api-reference/video-generation-api/kling-ai-avatar) — Video Generation
* [Kling TTS](/model-api-reference/audio-api/kling-tts) — Audio
