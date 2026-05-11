> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bria Genfill API

> API reference for Bria Genfill. Bria GenFill enables high-quality object addition or visual transformation. Trained exclusively on licensed data for safe and risk-free commercial use. Access the model

**Endpoint:** `POST https://fal.run/fal-ai/bria/genfill`
**Endpoint ID:** `fal-ai/bria/genfill`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bria/genfill/playground">
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
      "fal-ai/bria/genfill",
      arguments={
          "image_url": "https://storage.googleapis.com/falserverless/bria/bria_genfill_img.png",
          "mask_url": "https://storage.googleapis.com/falserverless/bria/bria_genfill_mask.png",
          "prompt": "A red delicious cherry"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/bria/genfill", {
    input: {
        image_url: "https://storage.googleapis.com/falserverless/bria/bria_genfill_img.png",
        mask_url: "https://storage.googleapis.com/falserverless/bria/bria_genfill_mask.png",
        prompt: "A red delicious cherry"
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
    --url https://fal.run/fal-ai/bria/genfill \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "image_url": "https://storage.googleapis.com/falserverless/bria/bria_genfill_img.png",
    "mask_url": "https://storage.googleapis.com/falserverless/bria/bria_genfill_mask.png",
    "prompt": "A red delicious cherry"
  }'
  ```
</CodeGroup>

## Related

* [Bria RMBG 2.0](/model-api-reference/image-generation-api/bria-rmbg-2.0) — Image Generation
* [Bria Expand Image](/model-api-reference/image-generation-api/bria-expand-image) — Image Generation
* [Bria Eraser](/model-api-reference/image-generation-api/bria-eraser) — Image Generation
* [Bria Product Shot](/model-api-reference/image-generation-api/bria-product-shot) — Image Generation
* [Bria Background Replace](/model-api-reference/image-generation-api/bria-background-replace) — Image Generation
* [Video](/model-api-reference/video-generation-api/video) — Video Generation
* [Replace Background](/model-api-reference/image-generation-api/replace-background) — Image Generation
* [Bria Text-to-Image HD](/model-api-reference/image-generation-api/bria-text-to-image-hd) — Image Generation
* [Bria Text-to-Image Base](/model-api-reference/image-generation-api/bria-text-to-image-base) — Image Generation
* [Embed Product](/model-api-reference/image-generation-api/embed-product) — Image Generation
* [Bria Text-to-Image Fast](/model-api-reference/image-generation-api/bria-text-to-image-fast) — Image Generation

## Capabilities

* Image input
* Inpainting (mask support)
* Text prompt input
* Negative prompts
* Reproducible generation (seed)
* Batch generation
* Synchronous mode

## API Reference

### Input Schema

<ParamField body="image_url" type="string" required>
  Input Image to erase from
</ParamField>

<ParamField body="mask_url" type="string" required>
  The URL of the binary mask image that represents the area that will be cleaned.
</ParamField>

<ParamField body="prompt" type="string" required>
  The prompt you would like to use to generate images.
</ParamField>

<ParamField body="negative_prompt" type="string" default="">
  The negative prompt you would like to use to generate images. Default value: `""`
</ParamField>

<ParamField body="seed" type="integer">
  The same seed and the same prompt given to the same version of the model
  will output the same image every time.

  Range: `0` to `2147483647`
</ParamField>

<ParamField body="num_images" type="integer" default="1">
  Number of Images to generate. Default value: `1`

  Range: `1` to `4`
</ParamField>

<ParamField body="sync_mode" type="boolean" default="false">
  If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
</ParamField>

### Output Schema

<ParamField body="images" type="list<Image>" required>
  Generated Images
</ParamField>

<ParamField body="seed" type="integer" required>
  Seed value used for generation.
</ParamField>

## Input Example

```json theme={null}
{
  "image_url": "https://storage.googleapis.com/falserverless/bria/bria_genfill_img.png",
  "mask_url": "https://storage.googleapis.com/falserverless/bria/bria_genfill_mask.png",
  "prompt": "A red delicious cherry",
  "negative_prompt": "",
  "num_images": 1,
  "sync_mode": false
}
```

## Output Example

```json theme={null}
{
  "images": [
    {
      "content_type": "image/png",
      "file_name": "a0d138e6820c4ad58f1fd3c758f16047.png",
      "file_size": 1064550,
      "height": 768,
      "url": "https://storage.googleapis.com/falserverless/bria/bria_genfill_res.png",
      "width": 1024
    }
  ]
}
```

## Limitations

* `seed` range: 0 to 2147483647
* `num_images` range: 1 to 4
