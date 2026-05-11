> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video Video To Audio API

> API reference for Kling Video Video To Audio. Generate audio from input videos using Kling

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/video-to-audio`
**Endpoint ID:** `fal-ai/kling-video/video-to-audio`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/video-to-audio/playground">
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
      "fal-ai/kling-video/video-to-audio",
      arguments={
          "video_url": "https://storage.googleapis.com/falserverless/model_tests/kling/kling-v2.5-turbo-pro-image-to-video-output.mp4"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/kling-video/video-to-audio", {
    input: {
        video_url: "https://storage.googleapis.com/falserverless/model_tests/kling/kling-v2.5-turbo-pro-image-to-video-output.mp4"
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
    --url https://fal.run/fal-ai/kling-video/video-to-audio \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "video_url": "https://storage.googleapis.com/falserverless/model_tests/kling/kling-v2.5-turbo-pro-image-to-video-output.mp4"
  }'
  ```
</CodeGroup>

## Examples

<video src="https://v3b.fal.media/files/b/zebra/SrjZVk4yqjXSLWOdq7p6P_output.mp4" controls width="100%" />

## Capabilities

* Video input

## API Reference

### Input Schema

<ParamField body="video_url" type="string" required>
  The video URL to extract audio from. Only .mp4/.mov formats are supported. File size does not exceed 100MB. Video duration between 3.0s and 20.0s.
</ParamField>

<ParamField body="sound_effect_prompt" type="string" default="Car tires screech as they accelerate in a drag race">
  Sound effect prompt. Cannot exceed 200 characters. Default value: `"Car tires screech as they accelerate in a drag race"`
</ParamField>

<ParamField body="background_music_prompt" type="string" default="intense car race">
  Background music prompt. Cannot exceed 200 characters. Default value: `"intense car race"`
</ParamField>

<ParamField body="asmr_mode" type="boolean" default="false">
  Enable ASMR mode. This mode enhances detailed sound effects and is suitable for highly immersive content scenarios.
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The original video with dubbed audio applied
</ParamField>

<ParamField body="audio" type="File" required>
  The extracted/generated audio from the video in MP3 format
</ParamField>

## Input Example

```json theme={null}
{
  "video_url": "https://storage.googleapis.com/falserverless/model_tests/kling/kling-v2.5-turbo-pro-image-to-video-output.mp4",
  "sound_effect_prompt": "Car tires screech as they accelerate in a drag race",
  "background_music_prompt": "intense car race",
  "asmr_mode": false
}
```

## Output Example

```json theme={null}
{
  "video": {
    "url": "https://v3.fal.media/files/monkey/O-ekVTtYqeDblD1oSf2uv_dubbed_video.mp4"
  },
  "audio": {
    "url": "https://v3.fal.media/files/monkey/O-ekVTtYqeDblD1oSf2uv_extracted_audio.mp3"
  }
}
```
