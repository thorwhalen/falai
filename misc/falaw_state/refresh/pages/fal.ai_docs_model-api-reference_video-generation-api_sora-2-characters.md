> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sora 2 Characters API

> API reference for Sora 2 Characters. Generate character ids to use with Sora 2 generations

**Endpoint:** `POST https://fal.run/fal-ai/sora-2/characters`
**Endpoint ID:** `fal-ai/sora-2/characters`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/sora-2/characters/playground">
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
      "fal-ai/sora-2/characters",
      arguments={
          "video_url": "",
          "name": ""
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/sora-2/characters", {
    input: {
        video_url: "",
        name: ""
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
    --url https://fal.run/fal-ai/sora-2/characters \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "video_url": "",
    "name": ""
  }'
  ```
</CodeGroup>

## Related

* [Sora 2](/model-api-reference/video-generation-api/sora-2) — Video Generation

## Capabilities

* Video input

## API Reference

### Input Schema

<ParamField body="video_url" type="string" required>
  URL of an MP4 video (minimum 720p, max \~2.67:1 aspect ratio) to define the character. Videos exceeding 1080p are automatically scaled down. Non-standard aspect ratios are automatically padded to 16:9 (landscape) or 9:16 (portrait). Videos longer than 4 seconds are trimmed to the first 4 seconds.
</ParamField>

<ParamField body="name" type="string" required>
  Name for the character (1–80 characters). Refer to this name in prompts when using the character.
</ParamField>

### Output Schema

<ParamField body="id" type="string" required>
  API character ID (format char\_...). Use this in character\_ids when generating video.
</ParamField>

<ParamField body="name" type="string" required>
  The character name
</ParamField>

## Input Example

```json theme={null}
{
  "video_url": "",
  "name": ""
}
```

## Output Example

```json theme={null}
{
  "id": "char_123",
  "name": ""
}
```
