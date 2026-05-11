> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux Pro Kontext Multi API

> API reference for Flux Pro Kontext Multi. Experimental version of FLUX.1 Kontext [pro] with multi image handling capabilities

**Endpoint:** `POST https://fal.run/fal-ai/flux-pro/kontext/multi`
**Endpoint ID:** `fal-ai/flux-pro/kontext/multi`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-pro/kontext/multi/playground">
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
      "fal-ai/flux-pro/kontext/multi",
      arguments={
          "prompt": "Put the little duckling on top of the woman's t-shirt.",
          "image_urls": [
              "https://v3.fal.media/files/penguin/XoW0qavfF-ahg-jX4BMyL_image.webp",
              "https://v3.fal.media/files/tiger/bml6YA7DWJXOigadvxk75_image.webp"
          ]
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/flux-pro/kontext/multi", {
    input: {
        prompt: "Put the little duckling on top of the woman's t-shirt.",
        image_urls: [
          "https://v3.fal.media/files/penguin/XoW0qavfF-ahg-jX4BMyL_image.webp",
          "https://v3.fal.media/files/tiger/bml6YA7DWJXOigadvxk75_image.webp"
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
    --url https://fal.run/fal-ai/flux-pro/kontext/multi \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "Put the little duckling on top of the woman'\''s t-shirt.",
    "image_urls": [
      "https://v3.fal.media/files/penguin/XoW0qavfF-ahg-jX4BMyL_image.webp",
      "https://v3.fal.media/files/tiger/bml6YA7DWJXOigadvxk75_image.webp"
    ]
  }'
  ```
</CodeGroup>

## Related

* [FLUX.1 Kontext \[pro\]](/model-api-reference/image-generation-api/flux.1-kontext) — Image Generation

## Capabilities

* Text prompt input
* Reproducible generation (seed)
* CFG guidance scale
* Synchronous mode
* Batch generation
* Aspect ratio control

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required>
  The prompt to generate an image from.
</ParamField>

<ParamField body="seed" type="integer">
  The same seed and the same prompt given to the same version of the model
  will output the same image every time.
</ParamField>

<ParamField body="guidance_scale" type="float" default="3.5">
  The CFG (Classifier Free Guidance) scale is a measure of how close you want
  the model to stick to your prompt when looking for a related image to show you. Default value: `3.5`

  Range: `1` to `20`
</ParamField>

<ParamField body="sync_mode" type="boolean" default="false">
  If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
</ParamField>

<ParamField body="num_images" type="integer" default="1">
  The number of images to generate. Default value: `1`

  Range: `1` to `4`
</ParamField>

<ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
  The format of the generated image. Default value: `"jpeg"`

  Possible values: `jpeg`, `png`
</ParamField>

<ParamField body="safety_tolerance" type="SafetyToleranceEnum" default="2">
  The safety tolerance level for the generated image. 1 being the most strict and 5 being the most permissive. Default value: `"2"`

  Possible values: `1`, `2`, `3`, `4`, `5`, `6`
</ParamField>

<ParamField body="enhance_prompt" type="boolean" default="false">
  Whether to enhance the prompt for better results.
</ParamField>

<ParamField body="aspect_ratio" type="Enum">
  The aspect ratio of the generated image.

  Possible values: `21:9`, `16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16`, `9:21`
</ParamField>

<ParamField body="image_urls" type="list<string>" required>
  Image prompt for the omni model.
</ParamField>

### Output Schema

<ParamField body="images" type="list<registry__image__fast_sdxl__models__Image>" required>
  The generated image files info.
</ParamField>

<ParamField body="timings" type="Timings" required />

<ParamField body="seed" type="integer" required>
  Seed of the generated Image. It will be the same value of the one passed in the
  input or the randomly generated that was used in case none was passed.
</ParamField>

<ParamField body="has_nsfw_concepts" type="list<boolean>" required>
  Whether the generated images contain NSFW concepts.
</ParamField>

<ParamField body="prompt" type="string" required>
  The prompt used for generating the image.
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "Put the little duckling on top of the woman's t-shirt.",
  "guidance_scale": 3.5,
  "sync_mode": false,
  "num_images": 1,
  "output_format": "jpeg",
  "safety_tolerance": "2",
  "enhance_prompt": false,
  "image_urls": [
    "https://v3.fal.media/files/penguin/XoW0qavfF-ahg-jX4BMyL_image.webp",
    "https://v3.fal.media/files/tiger/bml6YA7DWJXOigadvxk75_image.webp"
  ]
}
```

## Output Example

```json theme={null}
{
  "images": [
    {
      "url": "",
      "content_type": "image/jpeg"
    }
  ],
  "prompt": ""
}
```

## Limitations

* `guidance_scale` range: 1 to 20
* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`, `6`
