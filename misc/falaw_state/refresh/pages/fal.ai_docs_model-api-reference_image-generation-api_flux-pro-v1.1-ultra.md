> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux Pro V1.1 Ultra API

> API reference for Flux Pro V1.1 Ultra. FLUX1.1 [pro] ultra is the newest version of FLUX1.1 [pro], maintaining professional-grade image quality while delivering up to 2K resolution with improved photo

<Tabs>
  <Tab title="V1.1 Ultra">
    **Endpoint:** `POST https://fal.run/fal-ai/flux-pro/v1.1-ultra`
    **Endpoint ID:** `fal-ai/flux-pro/v1.1-ultra`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-pro/v1.1-ultra/playground">
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
          "fal-ai/flux-pro/v1.1-ultra",
          arguments={
              "prompt": "Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"FLUX\" is painted over it in big, white brush strokes with visible texture."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/flux-pro/v1.1-ultra", {
        input: {
            prompt: "Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"FLUX\" is painted over it in big, white brush strokes with visible texture."
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
        --url https://fal.run/fal-ai/flux-pro/v1.1-ultra \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"FLUX\" is painted over it in big, white brush strokes with visible texture."
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to generate an image from.
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

    <ParamField body="image_url" type="string">
      The image URL to generate an image from.
    </ParamField>

    <ParamField body="image_prompt_strength" type="float" default="0.1">
      The strength of the image prompt, between 0 and 1. Default value: `0.1`

      Range: `0` to `1`
    </ParamField>

    <ParamField body="aspect_ratio" type="Enum | string" default="16:9">
      The aspect ratio of the generated image. Default value: `16:9`

      Possible values: `21:9`, `16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16`, `9:21`
    </ParamField>

    <ParamField body="raw" type="boolean" default="false">
      Generate less processed, more natural-looking images.
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
      "prompt": "Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"FLUX\" is painted over it in big, white brush strokes with visible texture.",
      "sync_mode": false,
      "num_images": 1,
      "output_format": "jpeg",
      "safety_tolerance": "2",
      "enhance_prompt": false,
      "image_prompt_strength": 0.1,
      "aspect_ratio": "16:9",
      "raw": false
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

  <Tab title="Redux">
    **Endpoint:** `POST https://fal.run/fal-ai/flux-pro/v1.1-ultra/redux`
    **Endpoint ID:** `fal-ai/flux-pro/v1.1-ultra/redux`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-pro/v1.1-ultra/redux/playground">
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
          "fal-ai/flux-pro/v1.1-ultra/redux",
          arguments={
              "image_url": "https://fal.media/files/kangaroo/acQvq-Kmo2lajkgvcEHdv.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/flux-pro/v1.1-ultra/redux", {
        input: {
            image_url: "https://fal.media/files/kangaroo/acQvq-Kmo2lajkgvcEHdv.png"
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
        --url https://fal.run/fal-ai/flux-pro/v1.1-ultra/redux \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://fal.media/files/kangaroo/acQvq-Kmo2lajkgvcEHdv.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" default="">
      The prompt to generate an image from. Default value: `""`
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

    <ParamField body="image_prompt_strength" type="float" default="0.1">
      The strength of the image prompt, between 0 and 1. Default value: `0.1`

      Range: `0` to `1`
    </ParamField>

    <ParamField body="aspect_ratio" type="Enum | string" default="16:9">
      The aspect ratio of the generated image. Default value: `16:9`

      Possible values: `21:9`, `16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16`, `9:21`
    </ParamField>

    <ParamField body="raw" type="boolean" default="false">
      Generate less processed, more natural-looking images.
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
      "prompt": "",
      "sync_mode": false,
      "num_images": 1,
      "output_format": "jpeg",
      "safety_tolerance": "2",
      "enhance_prompt": false,
      "image_url": "https://fal.media/files/kangaroo/acQvq-Kmo2lajkgvcEHdv.png",
      "image_prompt_strength": 0.1,
      "aspect_ratio": "16:9",
      "raw": false
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

Black Forest Labs' FLUX1.1 \[pro] ultra delivers up to 2K resolution (4 megapixels) image generation at \$0.06 per image. With **4x the resolution detail**, this model extends FLUX1.1 \[pro]'s capabilities with enhanced photorealism while maintaining \~10 second generation times. Built for production workflows where resolution and visual fidelity directly impact deliverables.

**Use Cases:** High-resolution marketing assets | Product photography | Editorial illustrations

***

## Performance

At \$0.06 per image with 4-megapixel output capability, FLUX1.1 \[pro] ultra positions between standard-resolution alternatives and premium high-res solutions.

| Metric                | Result                                                                                                                                               | Context                                           |
| :-------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------ |
| **Max Resolution**    | 4 megapixels (2048×2048)                                                                                                                             | 4x standard FLUX1.1 \[pro] resolution             |
| **Inference Speed**   | \~10 seconds per sample                                                                                                                              | Ultra mode generation time from Black Forest Labs |
| **Cost per Image**    | \$0.06                                                                                                                                               | 16.7 images per \$1.00                            |
| **Batch Generation**  | Up to 4 images                                                                                                                                       | Parallel generation via `num_images` parameter    |
| **Related Endpoints** | [FLUX1.1 \[pro\]](https://fal.ai/models/fal-ai/flux-pro/v1.1), [FLUX.1 Kontext \[pro\]](https://fal.ai/models/fal-ai/flux-pro/kontext/text-to-image) | Standard resolution and context-aware variants    |

***

## Professional-Grade Resolution Without Compromise

FLUX1.1 \[pro] ultra extends Black Forest Labs' architecture to 4-megapixel generation while maintaining the **prompt interpretation and photorealism** that defined the standard version. Where most high-resolution models sacrifice inference speed or introduce quality degradation, ultra mode processes at comparable latency to standard-resolution alternatives.

**What this means for you:**

* **True 2K output:** Generate up to 2048×2048 images without upscaling artifacts or post-processing, delivering **print-ready assets** directly from the API

* **Optional image conditioning:** Use `image_url` and `image_prompt_strength` (0-1 range) to guide generation with reference images, enabling style transfer and composition control

* **Flexible aspect ratios:** Support for multiple aspect ratios with automatic megapixel-based billing, pay only for the resolution you actually use

* **Granular safety controls:** Six-level `safety_tolerance` parameter (1-6) lets you calibrate content filtering for your specific use case, from strict (1) to permissive (6)

***

## Technical Specifications

| Spec               | Details                                         |
| :----------------- | :---------------------------------------------- |
| **Architecture**   | FLUX1.1 \[pro] ultra                            |
| **Input Formats**  | Text prompts, optional reference images via URL |
| **Output Formats** | JPEG, PNG                                       |
| **Max Resolution** | 4 megapixels (up to 2048×2048)                  |
| **License**        | Commercial use enabled via fal partnership      |

[API Documentation](https://fal.ai/models/fal-ai/flux-pro/v1.1-ultra/api) | [Quickstart Guide](https://fal.ai/docs) | [Enterprise Pricing](https://fal.ai/pricing)

***

## How It Stacks Up

\*\*FLUX1.1 \[pro] ($0.05)** – FLUX1.1 [pro] ultra trades cost efficiency for 4x resolution at $0.06 vs \$0.05 (20% premium). Standard [FLUX1.1 \[pro\]](https://fal.ai/models/fal-ai/flux-pro/v1.1) remains ideal for **high-volume workflows** where 1-megapixel output meets requirements and cost per image is the primary constraint.

**FLUX.1 Kontext \[pro] (\$0.05)** – FLUX1.1 \[pro] ultra prioritizes maximum resolution and photorealism for single-image generation. [FLUX.1 Kontext \[pro\]](https://fal.ai/models/fal-ai/flux-pro/kontext/text-to-image) emphasizes **multi-image context understanding** (up to 5 reference images) at standard resolution, optimized for workflows requiring consistent style or character preservation across generations.

\*\*AuraFlow ($0.012)** – FLUX1.1 [pro] ultra delivers professional-grade photorealism and 4-megapixel output at 5x the cost ($0.06 vs \$0.012). [AuraFlow](https://fal.ai/models/fal-ai/aura-flow) offers **open-weight flexibility** and cost efficiency for rapid iteration workflows where resolution and photorealism requirements are secondary to generation volume.

## Related

* [FLUX1.1 \[pro\]](/model-api-reference/image-generation-api/flux1.1) — Image Generation
* [FLUX.1 \[pro\] Fill](/model-api-reference/image-generation-api/flux.1-fill) — Image Generation
* [FLUX1.1 \[pro\] Redux](/model-api-reference/image-generation-api/flux1.1-redux) — Image Generation
* [FLUX1.1 \[pro\] ultra Redux](/model-api-reference/image-generation-api/flux1.1-ultra-redux) — Image Generation
* [FLUX1.1 \[pro\] ultra Fine-tuned](/model-api-reference/image-generation-api/flux1.1-ultra-fine-tuned) — Image Generation
* [FLUX.1 \[pro\] Fill Fine-tuned](/model-api-reference/image-generation-api/flux.1-fill-fine-tuned) — Image Generation
* [FLUX1.1 \[pro\] ultra](/model-api-reference/image-generation-api/flux1.1-ultra) — Image Generation

## Limitations

* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`, `6`
* `image_prompt_strength` range: 0 to 1
