> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Seedream V3 API

> API reference for Bytedance Seedream V3. Seedream 3.0 is a bilingual (Chinese and English) text-to-image model that excels at text-to-image generation.

**Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedream/v3/text-to-image`
**Endpoint ID:** `fal-ai/bytedance/seedream/v3/text-to-image`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedream/v3/text-to-image/playground">
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
      "fal-ai/bytedance/seedream/v3/text-to-image",
      arguments={
          "prompt": "Fisheye lens, the head of a cat, the image shows the effect that the facial features of the cat are distorted due to the shooting method."
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/bytedance/seedream/v3/text-to-image", {
    input: {
        prompt: "Fisheye lens, the head of a cat, the image shows the effect that the facial features of the cat are distorted due to the shooting method."
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
    --url https://fal.run/fal-ai/bytedance/seedream/v3/text-to-image \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "Fisheye lens, the head of a cat, the image shows the effect that the facial features of the cat are distorted due to the shooting method."
  }'
  ```
</CodeGroup>

### Input Schema

<ParamField body="prompt" type="string" required>
  The text prompt used to generate the image
</ParamField>

<ParamField body="image_size" type="ImageSize | Enum">
  Use for finer control over the output image size. Will be used over aspect\_ratio, if both are provided. Width and height must be between 512 and 2048.

  Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
</ParamField>

<ParamField body="guidance_scale" type="float" default="2.5">
  Controls how closely the output image aligns with the input prompt. Higher values mean stronger prompt correlation. Default value: `2.5`

  Range: `1` to `10`
</ParamField>

<ParamField body="num_images" type="integer" default="1">
  Number of images to generate Default value: `1`

  Range: `1` to `4`
</ParamField>

<ParamField body="seed" type="integer">
  Random seed to control the stochasticity of image generation.
</ParamField>

<ParamField body="enable_safety_checker" type="boolean" default="true">
  If set to true, the safety checker will be enabled. Default value: `true`
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
  "prompt": "Fisheye lens, the head of a cat, the image shows the effect that the facial features of the cat are distorted due to the shooting method.",
  "guidance_scale": 2.5,
  "num_images": 1,
  "enable_safety_checker": true,
  "sync_mode": false
}
```

### Output Example

```json theme={null}
{
  "images": [
    {
      "url": "https://v3.fal.media/files/rabbit/EJqemc4hQlHKAtkkfTJqB_a2aaccab7ff84740b6323da580146087.png"
    }
  ],
  "seed": 42
}
```

## Limitations

* `image_size` restricted to: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
* `guidance_scale` range: 1 to 10
* `num_images` range: 1 to 4
* Content moderation via safety checker
