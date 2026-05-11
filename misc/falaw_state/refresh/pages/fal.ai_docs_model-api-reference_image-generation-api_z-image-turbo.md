> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Z Image Turbo API

> API reference for Z Image Turbo. Z-Image Turbo is a super fast text-to-image model of 6B parameters developed by Tongyi-MAI.

**Endpoint:** `POST https://fal.run/fal-ai/z-image/turbo`
**Endpoint ID:** `fal-ai/z-image/turbo`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/z-image/turbo/playground">
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
      "fal-ai/z-image/turbo",
      arguments={
          "prompt": "A hyper-realistic, close-up portrait of a tribal elder from the Omo Valley, painted with intricate white chalk patterns and adorned with a headdress made of dried flowers, seed pods, and rusted bottle caps. The focus is razor-sharp on the texture of the skin, showing every pore, wrinkle, and scar that tells a story of survival. The background is a blurred, smoky hut interior, with the warm glow of a cooking fire reflecting in the subject's dark, soulful eyes. Shot on a Leica M6 with Kodak Portra 400 film grain aesthetic."
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/z-image/turbo", {
    input: {
        prompt: "A hyper-realistic, close-up portrait of a tribal elder from the Omo Valley, painted with intricate white chalk patterns and adorned with a headdress made of dried flowers, seed pods, and rusted bottle caps. The focus is razor-sharp on the texture of the skin, showing every pore, wrinkle, and scar that tells a story of survival. The background is a blurred, smoky hut interior, with the warm glow of a cooking fire reflecting in the subject's dark, soulful eyes. Shot on a Leica M6 with Kodak Portra 400 film grain aesthetic."
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
    --url https://fal.run/fal-ai/z-image/turbo \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "A hyper-realistic, close-up portrait of a tribal elder from the Omo Valley, painted with intricate white chalk patterns and adorned with a headdress made of dried flowers, seed pods, and rusted bottle caps. The focus is razor-sharp on the texture of the skin, showing every pore, wrinkle, and scar that tells a story of survival. The background is a blurred, smoky hut interior, with the warm glow of a cooking fire reflecting in the subject'\''s dark, soulful eyes. Shot on a Leica M6 with Kodak Portra 400 film grain aesthetic."
  }'
  ```
</CodeGroup>

Tongyi-MAI's Z-Image Turbo delivers 6B-parameter text-to-image generation at \$0.005 per megapixel. Trading model size for raw speed through an 8-step inference pipeline, it optimizes for high-volume applications where cost efficiency and throughput matter more than maximum detail fidelity.

**Built for:** Rapid prototyping | Content variation testing | High-volume asset generation

***

## Speed-First Architecture for Volume Workflows

Z-Image Turbo compresses inference to 8 steps maximum (configurable down to 1), contrasting with standard diffusion models that typically require 20-50 steps for comparable output quality. The 6B parameter count keeps memory footprint lean while maintaining prompt adherence.

**What this means for you:**

* **Flexible resolution up to 4 megapixels:** Generate images from portrait to landscape orientations without resolution caps limiting your workflow
* **Batch generation up to 4 images:** Test multiple variations in a single API call for faster iteration cycles
* **Configurable inference steps (1-8):** Trade quality for speed based on your specific use case, use 1-step for thumbnails, 8-step for final assets
* **Optional prompt expansion:** Automatically enhance brief prompts with descriptive detail when you need richer outputs (adds \$0.0025 per request)

***

## Performance That Scales

Z-Image Turbo optimizes for cost-per-image economics in production environments where you're generating hundreds or thousands of assets.

| Metric                 | Result           | Context                                                  |
| :--------------------- | :--------------- | :------------------------------------------------------- |
| **Cost per Megapixel** | \$0.005          | 200 megapixels per \$1.00 on fal                         |
| **Inference Steps**    | 1-8 configurable | Default 8 steps balances speed/quality                   |
| **Max Resolution**     | Up to 4MP        | Supports standard aspect ratios from square to ultrawide |
| **Batch Size**         | 1-4 images       | Generate variations in single request                    |

***

## Technical Specifications

| Spec               | Details                                                                                        |
| :----------------- | :--------------------------------------------------------------------------------------------- |
| **Architecture**   | Z-Image Turbo (6B parameters)                                                                  |
| **Input Formats**  | Text prompts with optional seed control                                                        |
| **Output Formats** | JPEG, PNG, WebP                                                                                |
| **Max Resolution** | 4 megapixels (configurable aspect ratios)                                                      |
| **Training**       | [Z-Image Trainer](https://fal.ai/models/fal-ai/z-image-trainer) available for LoRA fine-tuning |
| **License**        | Commercial use permitted                                                                       |

[API Documentation](https://fal.ai/models/fal-ai/z-image/turbo/api) | [Quickstart Guide](https://docs.fal.ai/model-apis/quickstart)

***

## How It Stacks Up

**[AuraFlow](https://fal.ai/models/fal-ai/aura-flow)** – Z-Image Turbo prioritizes inference speed and cost efficiency through its 8-step maximum pipeline, making it ideal for high-volume generation workflows where throughput matters. [AuraFlow](https://fal.ai/models/fal-ai/aura-flow) emphasizes prompt interpretation depth for complex creative briefs requiring nuanced understanding.

**[FLUX.2 \[dev\]](https://fal.ai/models/fal-ai/flux-2)** – Z-Image Turbo trades parameter count (6B vs FLUX.2's larger architecture) for faster inference and lower cost per megapixel ($0.005 vs $0.012), positioning it for production environments generating thousands of assets. [FLUX.2 \[dev\]](https://fal.ai/models/fal-ai/flux-2) offers higher detail fidelity and more sophisticated prompt following for applications where output quality justifies higher per-image costs.

**[FLUX.2 \[pro\]](https://fal.ai/models/fal-ai/flux-2-pro)** – Z-Image Turbo delivers 8-step generation at $0.005/MP for rapid iteration workflows. [FLUX.2 [pro]](https://fal.ai/models/fal-ai/flux-2-pro) provides enhanced photorealism and detail preservation at $0.03 for the first megapixel, designed for final production assets where maximum quality matters more than generation speed.

## Related

* [Z-Image Turbo](/model-api-reference/image-generation-api/z-image-turbo) — Image Generation
* [Z Image Base](/model-api-reference/image-generation-api/z-image-base) — Image Generation
* [Z Image Base (LoRA)](/model-api-reference/image-generation-api/z-image-base-lora) — Image Generation
* [Z-Image Turbo Seamless Tiling](/model-api-reference/image-generation-api/z-image-turbo-seamless-tiling) — Image Generation

## Capabilities

* Text prompt input
* Configurable resolution
* Adjustable inference steps
* Reproducible generation (seed)
* Synchronous mode
* Batch generation
* Safety checker

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required>
  The prompt to generate an image from.
</ParamField>

<ParamField body="image_size" type="ImageSize | Enum" default="landscape_4_3">
  The size of the generated image. Default value: `landscape_4_3`

  Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
</ParamField>

<ParamField body="num_inference_steps" type="integer" default="8">
  The number of inference steps to perform. Default value: `8`

  Range: `1` to `8`
</ParamField>

<ParamField body="seed" type="integer">
  The same seed and the same prompt given to the same version of the model
  will output the same image every time.
</ParamField>

<ParamField body="sync_mode" type="boolean" default="false">
  If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
</ParamField>

<ParamField body="num_images" type="integer" default="1">
  The number of images to generate. Default value: `1`

  Range: `1` to `4`
</ParamField>

<ParamField body="enable_safety_checker" type="boolean" default="true">
  If set to true, the safety checker will be enabled. Default value: `true`
</ParamField>

<ParamField body="output_format" type="OutputFormatEnum" default="png">
  The format of the generated image. Default value: `"png"`

  Possible values: `jpeg`, `png`, `webp`
</ParamField>

<ParamField body="acceleration" type="AccelerationEnum" default="regular">
  The acceleration level to use. Default value: `"regular"`

  Possible values: `none`, `regular`, `high`
</ParamField>

<ParamField body="enable_prompt_expansion" type="boolean" default="false">
  Whether to enable prompt expansion. Note: this will increase the price by 0.0025 credits per request.
</ParamField>

### Output Schema

<ParamField body="images" type="list<ImageFile>" required>
  The generated image files info.
</ParamField>

<ParamField body="timings" type="Timings" required>
  The timings of the generation process.
</ParamField>

<ParamField body="seed" type="integer" required>
  Seed of the generated Image. It will be the same value of the one passed in the input or the randomly generated that was used in case none was passed.
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
  "prompt": "A hyper-realistic, close-up portrait of a tribal elder from the Omo Valley, painted with intricate white chalk patterns and adorned with a headdress made of dried flowers, seed pods, and rusted bottle caps. The focus is razor-sharp on the texture of the skin, showing every pore, wrinkle, and scar that tells a story of survival. The background is a blurred, smoky hut interior, with the warm glow of a cooking fire reflecting in the subject's dark, soulful eyes. Shot on a Leica M6 with Kodak Portra 400 film grain aesthetic.",
  "image_size": "landscape_4_3",
  "num_inference_steps": 8,
  "sync_mode": false,
  "num_images": 1,
  "enable_safety_checker": true,
  "output_format": "png",
  "acceleration": "regular",
  "enable_prompt_expansion": false
}
```

## Output Example

```json theme={null}
{
  "images": [
    {
      "content_type": "image/png",
      "height": 768,
      "url": "https://storage.googleapis.com/falserverless/example_outputs/z-image-turbo-output.png",
      "width": 1024
    }
  ],
  "prompt": ""
}
```

## Limitations

* `image_size` restricted to: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
* `num_inference_steps` range: 1 to 8
* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`, `webp`
* `acceleration` restricted to: `none`, `regular`, `high`
* Content moderation via safety checker
