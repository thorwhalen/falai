> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Imageutils API

> API reference for Imageutils. Predict the probability of an image being NSFW.

**Endpoint:** `POST https://fal.run/fal-ai/imageutils/nsfw`
**Endpoint ID:** `fal-ai/imageutils/nsfw`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/imageutils/nsfw/playground">
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
      "fal-ai/imageutils/nsfw",
      arguments={
          "image_url": "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/imageutils/nsfw", {
    input: {
        image_url: "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg"
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
    --url https://fal.run/fal-ai/imageutils/nsfw \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "image_url": "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg"
  }'
  ```
</CodeGroup>

### Input Schema

<ParamField body="image_url" type="string" required>
  Input image url.
</ParamField>

### Output Schema

<ParamField body="nsfw_probability" type="float" required>
  The probability of the image being NSFW.
</ParamField>

### Input Example

```json theme={null}
{
  "image_url": "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg"
}
```
