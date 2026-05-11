> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bria Expand API

> API reference for Bria Expand. Bria Expand expands images beyond their borders in high quality. Trained exclusively on licensed data for safe and risk-free commercial use. Access the model's source co

**Endpoint:** `POST https://fal.run/fal-ai/bria/expand`
**Endpoint ID:** `fal-ai/bria/expand`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bria/expand/playground">
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
      "fal-ai/bria/expand",
      arguments={
          "image_url": "https://storage.googleapis.com/falserverless/model_tests/orange.png",
          "canvas_size": [
              1200,
              674
          ]
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/bria/expand", {
    input: {
        image_url: "https://storage.googleapis.com/falserverless/model_tests/orange.png",
        canvas_size: [
          1200,
          674
        ]
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
    --url https://fal.run/fal-ai/bria/expand \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "image_url": "https://storage.googleapis.com/falserverless/model_tests/orange.png",
    "canvas_size": [
      1200,
      674
    ]
  }'
  ```
</CodeGroup>

## Related

* [Bria RMBG 2.0](/model-api-reference/image-generation-api/bria-rmbg-2.0) — Image Generation
* [Bria Eraser](/model-api-reference/image-generation-api/bria-eraser) — Image Generation
* [Bria Product Shot](/model-api-reference/image-generation-api/bria-product-shot) — Image Generation
* [Bria Background Replace](/model-api-reference/image-generation-api/bria-background-replace) — Image Generation
* [Video](/model-api-reference/video-generation-api/video) — Video Generation
* [Bria GenFill](/model-api-reference/image-generation-api/bria-genfill) — Image Generation
* [Replace Background](/model-api-reference/image-generation-api/replace-background) — Image Generation
* [Bria Text-to-Image HD](/model-api-reference/image-generation-api/bria-text-to-image-hd) — Image Generation
* [Bria Text-to-Image Base](/model-api-reference/image-generation-api/bria-text-to-image-base) — Image Generation
* [Embed Product](/model-api-reference/image-generation-api/embed-product) — Image Generation
* [Bria Text-to-Image Fast](/model-api-reference/image-generation-api/bria-text-to-image-fast) — Image Generation

## Capabilities

* Image input
* Aspect ratio control
* Text prompt input
* Reproducible generation (seed)
* Negative prompts
* Synchronous mode

## API Reference

### Input Schema

<ParamField body="image_url" type="string" required>
  The URL of the input image.
</ParamField>

<ParamField body="canvas_size" type="list<integer>" required>
  The desired size of the final image, after the expansion. should have an area of less than 5000x5000 pixels.
</ParamField>

<ParamField body="aspect_ratio" type="Enum">
  The desired aspect ratio of the final image. Will be used over original\_image\_size and original\_image\_location if provided.

  Possible values: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`
</ParamField>

<ParamField body="original_image_size" type="list<integer>">
  The desired size of the original image, inside the full canvas. Ensure that the ratio of input image foreground or main subject to the canvas area is greater than 15% to achieve optimal results. Will be ignored if aspect\_ratio is provided.
</ParamField>

<ParamField body="original_image_location" type="list<integer>">
  The desired location of the original image, inside the full canvas. Provide the location of the upper left corner of the original image. The location can also be outside the canvas (the original image will be cropped). Will be ignored if aspect\_ratio is provided.
</ParamField>

<ParamField body="prompt" type="string" default="">
  Text on which you wish to base the image expansion. This parameter is optional. Bria currently supports prompts in English only, excluding special characters. Default value: `""`
</ParamField>

<ParamField body="seed" type="integer">
  You can choose whether you want your generated expension to be random or predictable. You can recreate the same result in the future by using the seed value of a result from the response. You can exclude this parameter if you are not interested in recreating your results. This parameter is optional.

  Range: `0` to `2147483647`
</ParamField>

<ParamField body="negative_prompt" type="string" default="">
  The negative prompt you would like to use to generate images. Default value: `""`
</ParamField>

<ParamField body="sync_mode" type="boolean" default="false">
  If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
</ParamField>

### Output Schema

<ParamField body="image" type="Image" required>
  The generated image
</ParamField>

<ParamField body="seed" type="integer" required>
  Seed value used for generation.
</ParamField>

## Input Example

```json theme={null}
{
  "image_url": "https://storage.googleapis.com/falserverless/model_tests/orange.png",
  "canvas_size": [
    1200,
    674
  ],
  "original_image_size": [
    610,
    855
  ],
  "original_image_location": [
    301,
    -66
  ],
  "prompt": "",
  "negative_prompt": "",
  "sync_mode": false
}
```

## Output Example

```json theme={null}
{
  "image": {
    "content_type": "image/png",
    "file_name": "afa402a35ea742cdb5c3e219b2b19bfb.png",
    "file_size": 1471342,
    "height": 674,
    "url": "https://v3.fal.media/files/koala/8np-spgxxG-I1r3cjthRV_afa402a35ea742cdb5c3e219b2b19bfb.png",
    "width": 1200
  }
}
```

## Limitations

* `seed` range: 0 to 2147483647
