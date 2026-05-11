> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux Pro V1 API

> API reference for Flux Pro V1. FLUX.1 [pro] Fill is a high-performance endpoint for the FLUX.1 [pro] model that enables rapid transformation of existing images, delivering high-quality style transfers

<Tabs>
  <Tab title="Fill">
    **Endpoint:** `POST https://fal.run/fal-ai/flux-pro/v1/fill`
    **Endpoint ID:** `fal-ai/flux-pro/v1/fill`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-pro/v1/fill/playground">
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
          "fal-ai/flux-pro/v1/fill",
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

      const result = await fal.subscribe("fal-ai/flux-pro/v1/fill", {
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
        --url https://fal.run/fal-ai/flux-pro/v1/fill \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A knight in shining armour holding a greatshield with \"FAL\" on it",
        "image_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/knight.jpeg",
        "mask_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/mask_knight.jpeg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to fill the masked part of the image.
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

    <ParamField body="image_url" type="string" required>
      The image URL to generate an image from. Needs to match the dimensions of the mask.
    </ParamField>

    <ParamField body="mask_url" type="string" required>
      The mask URL to inpaint the image. Needs to match the dimensions of the input image.
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

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A knight in shining armour holding a greatshield with \"FAL\" on it",
      "sync_mode": false,
      "num_images": 1,
      "output_format": "jpeg",
      "safety_tolerance": "2",
      "enhance_prompt": false,
      "image_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/knight.jpeg",
      "mask_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/mask_knight.jpeg"
    }
    ```

    ### Output Example

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
  </Tab>

  <Tab title="Fill Finetuned">
    **Endpoint:** `POST https://fal.run/fal-ai/flux-pro/v1/fill-finetuned`
    **Endpoint ID:** `fal-ai/flux-pro/v1/fill-finetuned`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-pro/v1/fill-finetuned/playground">
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
          "fal-ai/flux-pro/v1/fill-finetuned",
          arguments={
              "prompt": "A knight in shining armour holding a greatshield with \"FAL\" on it",
              "image_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/knight.jpeg",
              "mask_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/mask_knight.jpeg",
              "finetune_id": ""
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/flux-pro/v1/fill-finetuned", {
        input: {
            prompt: "A knight in shining armour holding a greatshield with \"FAL\" on it",
            image_url: "https://storage.googleapis.com/falserverless/flux-lora/example-images/knight.jpeg",
            mask_url: "https://storage.googleapis.com/falserverless/flux-lora/example-images/mask_knight.jpeg",
            finetune_id: ""
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
        --url https://fal.run/fal-ai/flux-pro/v1/fill-finetuned \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A knight in shining armour holding a greatshield with \"FAL\" on it",
        "image_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/knight.jpeg",
        "mask_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/mask_knight.jpeg",
        "finetune_id": ""
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to fill the masked part of the image.
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

    <ParamField body="image_url" type="string" required>
      The image URL to generate an image from. Needs to match the dimensions of the mask.
    </ParamField>

    <ParamField body="mask_url" type="string" required>
      The mask URL to inpaint the image. Needs to match the dimensions of the input image.
    </ParamField>

    <ParamField body="finetune_id" type="string" required>
      References your specific model
    </ParamField>

    <ParamField body="finetune_strength" type="float" required>
      Controls finetune influence.
      Increase this value if your target concept isn't showing up strongly enough.
      The optimal setting depends on your finetune and prompt

      Range: `0` to `2`
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

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A knight in shining armour holding a greatshield with \"FAL\" on it",
      "sync_mode": false,
      "num_images": 1,
      "output_format": "jpeg",
      "safety_tolerance": "2",
      "enhance_prompt": false,
      "image_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/knight.jpeg",
      "mask_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/mask_knight.jpeg",
      "finetune_id": ""
    }
    ```

    ### Output Example

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
  </Tab>
</Tabs>

Black Forest Labs' FLUX.1 \[pro] delivers professional-grade inpainting at \$0.05 per megapixel. Trading broad creative generation for surgical precision, this endpoint excels at targeted modifications, replacing objects, filling gaps, or seamlessly blending new elements into existing compositions without regenerating entire images.

**Use Cases:** Product photo editing | Architectural visualization refinement | E-commerce asset modification

***

## Performance

FLUX.1 \[pro] Fill operates at competitive inference speeds while maintaining the quality standards of the full FLUX.1 \[pro] architecture, with cost scaling directly to output resolution rather than flat per-inference pricing.

| Metric                 | Result                                                                                                                                               | Context                                              |
| :--------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------- |
| **Cost per Megapixel** | \$0.05                                                                                                                                               | Billed by rounding up to nearest megapixel           |
| **Output Range**       | 1-4 images                                                                                                                                           | Single API call supports batch generation            |
| **Safety Tolerance**   | 6 levels (1-6)                                                                                                                                       | Configurable content moderation strictness           |
| **Output Formats**     | JPEG, PNG                                                                                                                                            | Standard web-optimized formats                       |
| **Related Endpoints**  | [FLUX.1 Kontext \[pro\]](https://fal.ai/models/fal-ai/flux-pro/kontext), [FLUX.1 Kontext \[max\]](https://fal.ai/models/fal-ai/flux-pro/kontext/max) | Context-aware variants for multi-reference workflows |

***

## Precision Inpainting Without Full Regeneration

FLUX.1 \[pro] Fill operates through mask-based editing rather than full image regeneration, requiring three inputs: your base image, a mask defining the edit region, and a text prompt describing the desired fill content. This approach preserves everything outside the mask untouched while applying FLUX.1 \[pro]'s generation quality only where needed.

**What this means for you:**

* **Surgical precision:** Modify specific objects or regions without risking changes to surrounding elements, critical for product photography where brand consistency matters

* **Dual-input control:** Mask URL and image URL parameters enable programmatic workflows where masks are generated separately (edge detection, object segmentation, manual selection tools)

* **Prompt enhancement option:** Optional `enhance_prompt` parameter applies FLUX's prompt optimization to your instructions, improving interpretation of complex editing requests

* **Batch efficiency:** Generate up to 4 variations per API call with different seeds, useful for A/B testing edits or exploring alternative fills for the same masked region

***

## Technical Specifications

| Spec                    | Details                                                                 |
| :---------------------- | :---------------------------------------------------------------------- |
| **Architecture**        | FLUX.1 \[pro]                                                           |
| **Input Formats**       | Image URL (JPEG, PNG, WebP, GIF, AVIF) + Mask URL (matching dimensions) |
| **Output Formats**      | JPEG, PNG                                                               |
| **Resolution Handling** | Variable (billed per megapixel, rounded up)                             |
| **License**             | Commercial use permitted via fal partnership                            |

[API Documentation](https://fal.ai/models/fal-ai/flux-pro/v1/fill/api) | [Quickstart Guide](https://docs.fal.ai/model-apis/quickstart) | [Enterprise Pricing](https://fal.ai/pricing)

***

## How It Stacks Up

\*\*FLUX.1 Kontext \[pro] ($0.055/MP)** – FLUX.1 [pro] Fill ($0.05/MP) focuses on single-mask inpainting with straightforward prompt-based fills at 9% lower cost. [FLUX.1 Kontext \[pro\]](https://fal.ai/models/fal-ai/flux-pro/kontext) adds multi-reference image conditioning via URL arrays, enabling style transfer and context-aware fills for workflows requiring visual examples beyond text prompts.

\*\*FLUX.1 Kontext \[max] ($0.11/MP)** – FLUX.1 [pro] Fill delivers core inpainting functionality at 55% lower cost ($0.05 vs \$0.11 per megapixel). [FLUX.1 Kontext \[max\]](https://fal.ai/models/fal-ai/flux-pro/kontext/max) trades cost efficiency for maximum quality output and enhanced multi-reference capabilities, ideal for high-end commercial work where generation fidelity justifies premium pricing.

## Related

* [FLUX1.1 \[pro\] ultra](/model-api-reference/image-generation-api/flux1.1-ultra) — Image Generation
* [FLUX1.1 \[pro\]](/model-api-reference/image-generation-api/flux1.1) — Image Generation
* [FLUX1.1 \[pro\] Redux](/model-api-reference/image-generation-api/flux1.1-redux) — Image Generation
* [FLUX1.1 \[pro\] ultra Redux](/model-api-reference/image-generation-api/flux1.1-ultra-redux) — Image Generation
* [FLUX1.1 \[pro\] ultra Fine-tuned](/model-api-reference/image-generation-api/flux1.1-ultra-fine-tuned) — Image Generation
* [FLUX.1 \[pro\] Fill Fine-tuned](/model-api-reference/image-generation-api/flux.1-fill-fine-tuned) — Image Generation
* [FLUX.1 \[pro\] Fill](/model-api-reference/image-generation-api/flux.1-fill) — Image Generation

## Limitations

* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`, `6`
* `finetune_strength` range: 0 to 2
