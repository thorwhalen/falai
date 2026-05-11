> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bria Product Shot API

> API reference for Bria Product Shot. Place any product in any scenery with just a prompt or reference image while maintaining high integrity of the product. Trained exclusively on licensed data for sa

**Endpoint:** `POST https://fal.run/fal-ai/bria/product-shot`
**Endpoint ID:** `fal-ai/bria/product-shot`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bria/product-shot/playground">
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
      "fal-ai/bria/product-shot",
      arguments={
          "image_url": "https://storage.googleapis.com/falserverless/bria/bria_product_fg.jpg"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/bria/product-shot", {
    input: {
        image_url: "https://storage.googleapis.com/falserverless/bria/bria_product_fg.jpg"
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
    --url https://fal.run/fal-ai/bria/product-shot \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "image_url": "https://storage.googleapis.com/falserverless/bria/bria_product_fg.jpg"
  }'
  ```
</CodeGroup>

## Related

* [Bria RMBG 2.0](/model-api-reference/image-generation-api/bria-rmbg-2.0) — Image Generation
* [Bria Expand Image](/model-api-reference/image-generation-api/bria-expand-image) — Image Generation
* [Bria Eraser](/model-api-reference/image-generation-api/bria-eraser) — Image Generation
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
* Synchronous mode

## API Reference

### Input Schema

<ParamField body="image_url" type="string" required>
  The URL of the product shot to be placed in a lifestyle shot. If both image\_url and image\_file are provided, image\_url will be used. Accepted formats are jpeg, jpg, png, webp. Maximum file size 12MB.
</ParamField>

<ParamField body="scene_description" type="string">
  Text description of the new scene or background for the provided product shot. Bria currently supports prompts in English only, excluding special characters.
</ParamField>

<ParamField body="ref_image_url" type="string" default="">
  The URL of the reference image to be used for generating the new scene or background for the product shot. Use "" to leave empty.Either ref\_image\_url or scene\_description has to be provided but not both. If both ref\_image\_url and ref\_image\_file are provided, ref\_image\_url will be used. Accepted formats are jpeg, jpg, png, webp. Default value: `""`
</ParamField>

<ParamField body="optimize_description" type="boolean" default="true">
  Whether to optimize the scene description Default value: `true`
</ParamField>

<ParamField body="num_results" type="integer" default="1">
  The number of lifestyle product shots you would like to generate. You will get num\_results x 10 results when placement\_type=automatic and according to the number of required placements x num\_results if placement\_type=manual\_placement. Default value: `1`

  Range: `1` to `4`
</ParamField>

<ParamField body="fast" type="boolean" default="true">
  Whether to use the fast model Default value: `true`
</ParamField>

<ParamField body="placement_type" type="PlacementTypeEnum" default="manual_placement">
  This parameter allows you to control the positioning of the product in the image. Choosing 'original' will preserve the original position of the product in the image. Choosing 'automatic' will generate results with the 10 recommended positions for the product. Choosing 'manual\_placement' will allow you to select predefined positions (using the parameter 'manual\_placement\_selection'). Selecting 'manual\_padding' will allow you to control the position and size of the image by defining the desired padding in pixels around the product. Default value: `"manual_placement"`

  Possible values: `original`, `automatic`, `manual_placement`, `manual_padding`
</ParamField>

<ParamField body="original_quality" type="boolean" default="false">
  This flag is only relevant when placement\_type=original. If true, the output image retains the original input image's size; otherwise, the image is scaled to 1 megapixel (1MP) while preserving its aspect ratio.
</ParamField>

<ParamField body="shot_size" type="list<integer>" default="1000,1000">
  The desired size of the final product shot. For optimal results, the total number of pixels should be around 1,000,000. This parameter is only relevant when placement\_type=automatic or placement\_type=manual\_placement.
</ParamField>

<ParamField body="manual_placement_selection" type="ManualPlacementSelectionEnum" default="bottom_center">
  If you've selected placement\_type=manual\_placement, you should use this parameter to specify which placements/positions you would like to use from the list. You can select more than one placement in one request. Default value: `"bottom_center"`

  Possible values: `upper_left`, `upper_right`, `bottom_left`, `bottom_right`, `right_center`, `left_center`, `upper_center`, `bottom_center`, `center_vertical`, `center_horizontal`
</ParamField>

<ParamField body="padding_values" type="list<integer>">
  The desired padding in pixels around the product, when using placement\_type=manual\_padding. The order of the values is \[left, right, top, bottom]. For optimal results, the total number of pixels, including padding, should be around 1,000,000. It is recommended to first use the product cutout API, get the cutout and understand the size of the result, and then define the required padding and use the cutout as an input for this API.
</ParamField>

<ParamField body="sync_mode" type="boolean" default="false">
  If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
</ParamField>

### Output Schema

<ParamField body="images" type="list<Image>" required>
  The generated images
</ParamField>

## Input Example

```json theme={null}
{
  "image_url": "https://storage.googleapis.com/falserverless/bria/bria_product_fg.jpg",
  "scene_description": "on a rock, next to the ocean, dark theme",
  "ref_image_url": "https://storage.googleapis.com/falserverless/bria/bria_product_bg.jpg",
  "optimize_description": true,
  "num_results": 1,
  "fast": true,
  "placement_type": "manual_placement",
  "original_quality": false,
  "shot_size": [
    1000,
    1000
  ],
  "manual_placement_selection": "bottom_center",
  "sync_mode": false
}
```

## Output Example

```json theme={null}
{
  "images": [
    {
      "content_type": "image/png",
      "url": "https://storage.googleapis.com/falserverless/bria/bria_product_res.png"
    }
  ]
}
```

## Limitations

* `num_results` range: 1 to 4
* `placement_type` restricted to: `original`, `automatic`, `manual_placement`, `manual_padding`
