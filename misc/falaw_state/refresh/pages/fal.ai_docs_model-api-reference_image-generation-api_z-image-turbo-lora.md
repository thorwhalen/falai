> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Z Image Turbo Lora API

> API reference for Z Image Turbo Lora. Text-to-Image endpoint with LoRA support for Z-Image Turbo, a super fast text-to-image model of 6B parameters developed by Tongyi-MAI.

**Endpoint:** `POST https://fal.run/fal-ai/z-image/turbo/lora`
**Endpoint ID:** `fal-ai/z-image/turbo/lora`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/z-image/turbo/lora/playground">
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
      "fal-ai/z-image/turbo/lora",
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

  const result = await fal.subscribe("fal-ai/z-image/turbo/lora", {
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
    --url https://fal.run/fal-ai/z-image/turbo/lora \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "A hyper-realistic, close-up portrait of a tribal elder from the Omo Valley, painted with intricate white chalk patterns and adorned with a headdress made of dried flowers, seed pods, and rusted bottle caps. The focus is razor-sharp on the texture of the skin, showing every pore, wrinkle, and scar that tells a story of survival. The background is a blurred, smoky hut interior, with the warm glow of a cooking fire reflecting in the subject'\''s dark, soulful eyes. Shot on a Leica M6 with Kodak Portra 400 film grain aesthetic."
  }'
  ```
</CodeGroup>

Tongyi-MAI's Z-Image Turbo with LoRA support delivers 6B-parameter text-to-image generation at \$0.0085 per megapixel with 8-step inference. Apply up to 3 custom LoRA weights at inference time without retraining, enabling style consistency and brand adaptation at approximately 118 generations per dollar on fal.

**Built for:** Custom style application | Brand-consistent generation | Character consistency workflows | Rapid design iteration

***

## LoRA Flexibility Without Training Overhead

Z-Image Turbo LoRA adds inference-time style customization to the base model's speed advantages. Apply pre-trained LoRA adapters directly through the API, combining multiple style influences in a single generation call without touching the underlying model weights.

**What this means for you:**

* **Apply up to 3 LoRA weights simultaneously:** Combine custom styles, character adapters, and brand guidelines in a single generation request through the `loras` parameter
* **Batch generation at scale:** Generate up to 4 images per request with configurable inference steps (1-8 range), optimizing the speed-quality tradeoff for your use case
* **Acceleration options:** Choose between "none", "regular", or "high" acceleration modes to balance generation speed against output fidelity
* **Production-ready safety:** Built-in safety checker (enabled by default) filters NSFW content automatically, with optional prompt expansion for enhanced detail at +\$0.0025 per request
* **Flexible output formats:** Generate images in JPEG, PNG, or WebP with landscape (4:3), portrait (3:4), or square (1:1) aspect ratios

***

## Performance That Scales

Z-Image Turbo LoRA adds minimal overhead to base model pricing while enabling custom style application at inference time.

| Metric                 | Result                     | Context                                           |
| :--------------------- | :------------------------- | :------------------------------------------------ |
| **Cost per Megapixel** | \$0.0085                   | \~118 generations per \$1.00 on fal               |
| **Inference Steps**    | 1-8 configurable           | Default 8 steps balances speed and quality        |
| **Batch Capability**   | Up to 4 images             | Single API call generates multiple variants       |
| **LoRA Support**       | Up to 3 concurrent weights | Apply custom styles without base model retraining |
| **Base Model Cost**    | \$0.005/MP                 | LoRA adds \$0.0035/MP for style flexibility       |

***

## Technical Specifications

| Spec                   | Details                                                                                  |
| :--------------------- | :--------------------------------------------------------------------------------------- |
| **Architecture**       | Z-Image Turbo (6B parameters) with LoRA inference                                        |
| **Input Formats**      | Text prompts, optional LoRA weights (up to 3)                                            |
| **Output Formats**     | JPEG, PNG, WebP                                                                          |
| **Image Sizes**        | Landscape 4:3, Portrait 3:4, Square 1:1                                                  |
| **Acceleration Modes** | None, Regular, High                                                                      |
| **Training**           | [Z-Image Trainer](https://fal.ai/models/fal-ai/z-image-trainer) for custom LoRA creation |
| **License**            | Commercial use permitted                                                                 |

[API Documentation](https://fal.ai/models/fal-ai/z-image/turbo/lora/api) | [Quickstart Guide](https://docs.fal.ai/model-apis/quickstart)

***

## How It Stacks Up

**[Z-Image Turbo](https://fal.ai/models/fal-ai/z-image/turbo)** – The base Z-Image Turbo endpoint runs at $0.005/MP for maximum cost efficiency when style customization isn't required. The LoRA variant adds $0.0035/MP overhead to enable custom style application, character consistency, and brand adaptation at inference time.

**[AuraFlow](https://fal.ai/models/fal-ai/aura-flow)** – Z-Image Turbo LoRA prioritizes cost efficiency at \$0.0085/MP with 8-step inference and runtime style customization. [AuraFlow](https://fal.ai/models/fal-ai/aura-flow) emphasizes open-source flexibility and longer inference paths for applications requiring maximum creative control and community-driven development.

**[FLUX.2 \[dev\] LoRA](https://fal.ai/models/fal-ai/flux-2/lora)** – Z-Image Turbo LoRA delivers comparable style customization at $0.0085/MP versus FLUX.2 [dev] LoRA's $0.021/MP, making it 2.5x more cost-efficient for high-volume workflows. [FLUX.2 \[dev\] LoRA](https://fal.ai/models/fal-ai/flux-2/lora) offers higher resolution outputs and more sophisticated prompt interpretation for applications where output quality justifies the premium.

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
* LoRA support

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

<ParamField body="loras" type="list<LoRAInput>" default="">
  List of LoRA weights to apply (maximum 3).
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
  "enable_prompt_expansion": false,
  "loras": []
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
