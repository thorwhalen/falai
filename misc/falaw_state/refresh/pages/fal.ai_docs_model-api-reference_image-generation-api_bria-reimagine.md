> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bria Reimagine API

> API reference for Bria Reimagine. Structure Reference allows generating new images while preserving the structure of an input image, guided by text prompts. Perfect for transforming sketches, illustra

**Endpoint:** `POST https://fal.run/fal-ai/bria/reimagine`
**Endpoint ID:** `fal-ai/bria/reimagine`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bria/reimagine/playground">
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
      "fal-ai/bria/reimagine",
      arguments={
          "prompt": "A 2d illustration of a dog in a vibrant park"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/bria/reimagine", {
    input: {
        prompt: "A 2d illustration of a dog in a vibrant park"
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
    --url https://fal.run/fal-ai/bria/reimagine \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "A 2d illustration of a dog in a vibrant park"
  }'
  ```
</CodeGroup>

## Capabilities

* Text prompt input
* Reproducible generation (seed)
* Adjustable inference steps
* Synchronous mode

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required>
  The prompt you would like to use to generate images.
</ParamField>

<ParamField body="structure_image_url" type="string" default="">
  The URL of the structure reference image. Use "" to leave empty. Accepted formats are jpeg, jpg, png, webp. Default value: `""`
</ParamField>

<ParamField body="structure_ref_influence" type="float" default="0.75">
  The influence of the structure reference on the generated image. Default value: `0.75`
</ParamField>

<ParamField body="num_results" type="integer" default="1">
  How many images you would like to generate. When using any Guidance Method, Value is set to 1. Default value: `1`

  Range: `1` to `4`
</ParamField>

<ParamField body="seed" type="integer">
  The same seed and the same prompt given to the same version of the model
  will output the same image every time.

  Range: `0` to `2147483647`
</ParamField>

<ParamField body="fast" type="boolean" default="true">
  Whether to use the fast model Default value: `true`
</ParamField>

<ParamField body="num_inference_steps" type="integer" default="30">
  The number of iterations the model goes through to refine the generated image. This parameter is optional. Default value: `30`

  Range: `20` to `50`
</ParamField>

<ParamField body="sync_mode" type="boolean" default="false">
  If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
</ParamField>

### Output Schema

<ParamField body="images" type="list<Image>" required>
  The generated images
</ParamField>

<ParamField body="seed" type="integer" required>
  Seed value used for generation.
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "A 2d illustration of a dog in a vibrant park",
  "structure_image_url": "https://storage.googleapis.com/falserverless/bria/bria_reimagine_input.png",
  "structure_ref_influence": 0.15,
  "num_results": 1,
  "fast": true,
  "num_inference_steps": 30,
  "sync_mode": false
}
```

## Output Example

```json theme={null}
{
  "images": [
    {
      "content_type": "image/png",
      "url": "https://storage.googleapis.com/falserverless/bria/bria_reimagine_output.png"
    }
  ]
}
```

## Limitations

* `num_results` range: 1 to 4
* `seed` range: 0 to 2147483647
* `num_inference_steps` range: 20 to 50
