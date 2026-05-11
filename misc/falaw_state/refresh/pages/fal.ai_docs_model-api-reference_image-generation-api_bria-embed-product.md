> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bria Embed Product API

> API reference for Bria Embed Product. Seamlessly integrate one or more products into a predefined scene with pixel-perfect control.

**Endpoint:** `POST https://fal.run/bria/embed-product`
**Endpoint ID:** `bria/embed-product`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/embed-product/playground">
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
      "bria/embed-product",
      arguments={},
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("bria/embed-product", {
    input: {},
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
    --url https://fal.run/bria/embed-product \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{}'
  ```
</CodeGroup>

## Related

* [Bria RMBG 2.0](/model-api-reference/image-generation-api/bria-rmbg-2.0) — Image Generation
* [Bria Expand Image](/model-api-reference/image-generation-api/bria-expand-image) — Image Generation
* [Bria Eraser](/model-api-reference/image-generation-api/bria-eraser) — Image Generation
* [Bria Product Shot](/model-api-reference/image-generation-api/bria-product-shot) — Image Generation
* [Bria Background Replace](/model-api-reference/image-generation-api/bria-background-replace) — Image Generation
* [Video](/model-api-reference/video-generation-api/video) — Video Generation
* [Bria GenFill](/model-api-reference/image-generation-api/bria-genfill) — Image Generation
* [Replace Background](/model-api-reference/image-generation-api/replace-background) — Image Generation
* [Bria Text-to-Image HD](/model-api-reference/image-generation-api/bria-text-to-image-hd) — Image Generation
* [Bria Text-to-Image Base](/model-api-reference/image-generation-api/bria-text-to-image-base) — Image Generation
* [Bria Text-to-Image Fast](/model-api-reference/image-generation-api/bria-text-to-image-fast) — Image Generation

## Capabilities

* Reproducible generation (seed)
* Synchronous mode

## API Reference

### Input Schema

<ParamField body="image_source" type="string">
  URL of the image.
</ParamField>

<ParamField body="products" type="list<EmbedItem>">
  List of products to embed in the image.
</ParamField>

<ParamField body="seed" type="integer" default="5555">
  Random seed for reproducibility. Default value: `5555`
</ParamField>

<ParamField body="sync_mode" type="boolean" default="false">
  If true, returns the image directly in the response (increases latency).
</ParamField>

### Output Schema

<ParamField body="image" type="Image" required>
  Generated image with products embedded.
</ParamField>

<ParamField body="seed" type="integer" required>
  Seed used for generation.
</ParamField>

## Input Example

```json theme={null}
{
  "image_source": "https://bria-datasets.s3.us-east-1.amazonaws.com/embed-product/an_empty_living_room_0.png",
  "products": [
    {
      "coordinates": {
        "height": 300,
        "width": 100,
        "x": 300,
        "y": 317
      },
      "image_source": "https://bria-datasets.s3.us-east-1.amazonaws.com/embed-product/a_standing_lamp_over_white_background_0.png"
    },
    {
      "coordinates": {
        "height": 156,
        "width": 120,
        "x": 646,
        "y": 287
      },
      "image_source": "https://bria-datasets.s3.us-east-1.amazonaws.com/embed-product/a_wall_picture_on_white_background_0.png"
    }
  ],
  "seed": 5555,
  "sync_mode": false
}
```

## Output Example

```json theme={null}
{
  "image": {
    "url": "",
    "content_type": "image/png",
    "file_name": "z9RV14K95DvU.png",
    "file_size": 4404019,
    "width": 1024,
    "height": 1024
  }
}
```
