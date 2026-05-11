> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Video Stylize API

> API reference for Bytedance Video Stylize. Transform your images into stylized videos using this workflow.

**Endpoint:** `POST https://fal.run/fal-ai/bytedance/video-stylize`
**Endpoint ID:** `fal-ai/bytedance/video-stylize`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/video-stylize/playground">
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
      "fal-ai/bytedance/video-stylize",
      arguments={
          "style": "Manga style",
          "image_url": "https://v3.fal.media/files/kangaroo/-KmSPIcXeGA3Z_iiH4C75_tmph2ry_0_8.png"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/bytedance/video-stylize", {
    input: {
        style: "Manga style",
        image_url: "https://v3.fal.media/files/kangaroo/-KmSPIcXeGA3Z_iiH4C75_tmph2ry_0_8.png"
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
    --url https://fal.run/fal-ai/bytedance/video-stylize \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "style": "Manga style",
    "image_url": "https://v3.fal.media/files/kangaroo/-KmSPIcXeGA3Z_iiH4C75_tmph2ry_0_8.png"
  }'
  ```
</CodeGroup>

## Capabilities

* Image input

## API Reference

### Input Schema

<ParamField body="style" type="string" required>
  The style for your character in the video. Please use a short description.
</ParamField>

<ParamField body="image_url" type="string" required>
  URL of the image to make the stylized video from.
</ParamField>

## Input Example

```json theme={null}
{
  "style": "Manga style",
  "image_url": "https://v3.fal.media/files/kangaroo/-KmSPIcXeGA3Z_iiH4C75_tmph2ry_0_8.png"
}
```
