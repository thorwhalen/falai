> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video Create Voice API

> API reference for Kling Video Create Voice. Create Voices to be used with Kling Models Voice Control

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/create-voice`
**Endpoint ID:** `fal-ai/kling-video/create-voice`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/create-voice/playground">
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
      "fal-ai/kling-video/create-voice",
      arguments={
          "voice_url": "https://v3b.fal.media/files/b/0a867736/_Wo19V-XrOVYZt6jKE8t5_kling_video.wav"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/kling-video/create-voice", {
    input: {
        voice_url: "https://v3b.fal.media/files/b/0a867736/_Wo19V-XrOVYZt6jKE8t5_kling_video.wav"
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
    --url https://fal.run/fal-ai/kling-video/create-voice \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "voice_url": "https://v3b.fal.media/files/b/0a867736/_Wo19V-XrOVYZt6jKE8t5_kling_video.wav"
  }'
  ```
</CodeGroup>

## API Reference

### Input Schema

<ParamField body="voice_url" type="string" required>
  URL of the voice audio file. Supports .mp3/.wav audio or .mp4/.mov video. Duration must be 5-30 seconds with clean, single-voice audio.
</ParamField>

### Output Schema

<ParamField body="voice_id" type="string" required>
  Unique identifier for the created voice
</ParamField>

## Input Example

```json theme={null}
{
  "voice_url": "https://v3b.fal.media/files/b/0a867736/_Wo19V-XrOVYZt6jKE8t5_kling_video.wav"
}
```

## Output Example

```json theme={null}
{
  "voice_id": "829877809978941442"
}
```
