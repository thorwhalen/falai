> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Dreamina V3.1 API

> API reference for Bytedance Dreamina V3.1. Dreamina showcases superior picture effects, with significant improvements in picture aesthetics, precise and diverse styles, and rich details.

**Endpoint:** `POST https://fal.run/fal-ai/bytedance/dreamina/v3.1/text-to-image`
**Endpoint ID:** `fal-ai/bytedance/dreamina/v3.1/text-to-image`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/dreamina/v3.1/text-to-image/playground">
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
      "fal-ai/bytedance/dreamina/v3.1/text-to-image",
      arguments={
          "prompt": "A 25-year-old korean woman selfie, front facing camera, lighting is soft and natural. If background is visible, it's a clean, modern apartment interior. The clothing color is clearly visible and distinct, adding a hint of color contrast"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/bytedance/dreamina/v3.1/text-to-image", {
    input: {
        prompt: "A 25-year-old korean woman selfie, front facing camera, lighting is soft and natural. If background is visible, it's a clean, modern apartment interior. The clothing color is clearly visible and distinct, adding a hint of color contrast"
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
    --url https://fal.run/fal-ai/bytedance/dreamina/v3.1/text-to-image \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "A 25-year-old korean woman selfie, front facing camera, lighting is soft and natural. If background is visible, it'\''s a clean, modern apartment interior. The clothing color is clearly visible and distinct, adding a hint of color contrast"
  }'
  ```
</CodeGroup>

### Input Schema

<ParamField body="prompt" type="string" required>
  The text prompt used to generate the image
</ParamField>

<ParamField body="image_size" type="ImageSize | Enum" default="[object Object]">
  The size of the generated image. Width and height must be between 512 and 2048.

  Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
</ParamField>

<ParamField body="enhance_prompt" type="boolean" default="false">
  Whether to use an LLM to enhance the prompt
</ParamField>

<ParamField body="num_images" type="integer" default="1">
  Number of images to generate Default value: `1`

  Range: `1` to `4`
</ParamField>

<ParamField body="seed" type="integer">
  Random seed to control the stochasticity of image generation.
</ParamField>

<ParamField body="sync_mode" type="boolean" default="false">
  If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
</ParamField>

### Output Schema

<ParamField body="images" type="list<Image>" required>
  Generated images
</ParamField>

<ParamField body="seed" type="integer" required>
  Seed used for generation
</ParamField>

### Input Example

```json theme={null}
{
  "prompt": "A 25-year-old korean woman selfie, front facing camera, lighting is soft and natural. If background is visible, it's a clean, modern apartment interior. The clothing color is clearly visible and distinct, adding a hint of color contrast",
  "image_size": {
    "width": 2048,
    "height": 1536
  },
  "enhance_prompt": false,
  "num_images": 1,
  "sync_mode": false
}
```

### Output Example

```json theme={null}
{
  "images": [
    {
      "url": "https://v3.fal.media/files/panda/4mddd7PmDvbbBZDs-xnUW_4294a9041c9d46eaa7b98d15ce6300fb.png"
    }
  ],
  "seed": 746406749
}
```

## Related

* [Bytedance Seedream v4 Edit](/model-api-reference/image-generation-api/bytedance-seedream-v4-edit) — Image Generation
* [Bytedance Seedream v4](/model-api-reference/image-generation-api/bytedance-seedream-v4) — Image Generation

## Limitations

* `image_size` restricted to: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
* `num_images` range: 1 to 4
