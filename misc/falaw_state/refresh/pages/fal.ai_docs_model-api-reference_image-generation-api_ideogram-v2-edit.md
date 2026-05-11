> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ideogram V2 Edit API

> API reference for Ideogram V2 Edit. Transform existing images with Ideogram V2's editing capabilities. Modify, adjust, and refine images while maintaining high fidelity and realistic outputs with prec

**Endpoint:** `POST https://fal.run/fal-ai/ideogram/v2/edit`
**Endpoint ID:** `fal-ai/ideogram/v2/edit`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/v2/edit/playground">
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
      "fal-ai/ideogram/v2/edit",
      arguments={
          "prompt": "A knight in shining armour holding a greatshield with \"FAL\" on it",
          "image_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/knight.jpeg",
          "mask_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/mask_knight.jpeg"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/ideogram/v2/edit", {
    input: {
        prompt: "A knight in shining armour holding a greatshield with \"FAL\" on it",
        image_url: "https://storage.googleapis.com/falserverless/flux-lora/example-images/knight.jpeg",
        mask_url: "https://storage.googleapis.com/falserverless/flux-lora/example-images/mask_knight.jpeg"
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
    --url https://fal.run/fal-ai/ideogram/v2/edit \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "A knight in shining armour holding a greatshield with \"FAL\" on it",
    "image_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/knight.jpeg",
    "mask_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/mask_knight.jpeg"
  }'
  ```
</CodeGroup>

## Related

* [Ideogram V2](/model-api-reference/image-generation-api/ideogram-v2) — Image Generation
* [Ideogram V2 Remix](/model-api-reference/image-generation-api/ideogram-v2-remix) — Image Generation

## Capabilities

* Text prompt input
* Image input
* Inpainting (mask support)
* Reproducible generation (seed)
* Synchronous mode

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required>
  The prompt to fill the masked part of the image.
</ParamField>

<ParamField body="image_url" type="string" required>
  The image URL to generate an image from. Needs to match the dimensions of the mask.
</ParamField>

<ParamField body="mask_url" type="string" required>
  The mask URL to inpaint the image. Needs to match the dimensions of the input image.
</ParamField>

<ParamField body="seed" type="integer">
  Seed for the random number generator
</ParamField>

<ParamField body="style" type="StyleEnum" default="auto">
  The style of the generated image Default value: `"auto"`

  Possible values: `auto`, `general`, `realistic`, `design`, `render_3D`, `anime`
</ParamField>

<ParamField body="expand_prompt" type="boolean" default="true">
  Whether to expand the prompt with MagicPrompt functionality. Default value: `true`
</ParamField>

<ParamField body="sync_mode" type="boolean" default="false">
  If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
</ParamField>

### Output Schema

<ParamField body="images" type="list<File>" required />

<ParamField body="seed" type="integer" required>
  Seed used for the random number generator
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "A knight in shining armour holding a greatshield with \"FAL\" on it",
  "image_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/knight.jpeg",
  "mask_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/mask_knight.jpeg",
  "style": "auto",
  "expand_prompt": true,
  "sync_mode": false
}
```

## Output Example

```json theme={null}
{
  "images": [
    {
      "url": "https://fal.media/files/monkey/cNaoxPl0YAWYb-QVBvO9F_image.png"
    }
  ],
  "seed": 123456
}
```

## Limitations

* `style` restricted to: `auto`, `general`, `realistic`, `design`, `render_3D`, `anime`
