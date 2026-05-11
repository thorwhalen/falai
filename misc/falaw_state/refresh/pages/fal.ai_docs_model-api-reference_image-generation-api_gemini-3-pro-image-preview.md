> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Gemini 3 Pro Image Preview API

> API reference for Gemini 3 Pro Image Preview. Gemini 3 Pro Image (a.k.a Nano Banana Pro) is Google's state-of-the-art high-fidelity image generation and editing model

<Tabs>
  <Tab title="Gemini 3 Pro Image Preview">
    **Endpoint:** `POST https://fal.run/fal-ai/gemini-3-pro-image-preview`
    **Endpoint ID:** `fal-ai/gemini-3-pro-image-preview`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/gemini-3-pro-image-preview/playground">
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
          "fal-ai/gemini-3-pro-image-preview",
          arguments={
              "prompt": "An action shot of a black lab swimming in an inground suburban swimming pool. The camera is placed meticulously on the water line, dividing the image in half, revealing both the dogs head above water holding a tennis ball in it's mouth, and it's paws paddling underwater."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/gemini-3-pro-image-preview", {
        input: {
            prompt: "An action shot of a black lab swimming in an inground suburban swimming pool. The camera is placed meticulously on the water line, dividing the image in half, revealing both the dogs head above water holding a tennis ball in it's mouth, and it's paws paddling underwater."
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
        --url https://fal.run/fal-ai/gemini-3-pro-image-preview \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "An action shot of a black lab swimming in an inground suburban swimming pool. The camera is placed meticulously on the water line, dividing the image in half, revealing both the dogs head above water holding a tennis ball in it'\''s mouth, and it'\''s paws paddling underwater."
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt to generate an image from.
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      The number of images to generate. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="seed" type="integer">
      The seed for the random number generator.
    </ParamField>

    <ParamField body="aspect_ratio" type="Enum" default="1:1">
      The aspect ratio of the generated image. Default value: `1:1`

      Possible values: `auto`, `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="png">
      The format of the generated image. Default value: `"png"`

      Possible values: `jpeg`, `png`, `webp`
    </ParamField>

    <ParamField body="safety_tolerance" type="SafetyToleranceEnum" default="4">
      The safety tolerance level for content moderation. 1 is the most strict (blocks most content), 6 is the least strict. Default value: `"4"`

      Possible values: `1`, `2`, `3`, `4`, `5`, `6`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="1K">
      The resolution of the image to generate. Default value: `"1K"`

      Possible values: `1K`, `2K`, `4K`
    </ParamField>

    <ParamField body="limit_generations" type="boolean" default="false">
      Experimental parameter to limit the number of generations from each round of prompting to 1. Set to `True` to to disregard any instructions in the prompt regarding the number of images to generate.
    </ParamField>

    <ParamField body="enable_web_search" type="boolean" default="false">
      Enable web search for the image generation task. This will allow the model to use the latest information from the web to generate the image.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<ImageFile>" required>
      The generated images.
    </ParamField>

    <ParamField body="description" type="string" required>
      The description of the generated images.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "An action shot of a black lab swimming in an inground suburban swimming pool. The camera is placed meticulously on the water line, dividing the image in half, revealing both the dogs head above water holding a tennis ball in it's mouth, and it's paws paddling underwater.",
      "num_images": 1,
      "aspect_ratio": "1:1",
      "output_format": "png",
      "safety_tolerance": "4",
      "sync_mode": false,
      "resolution": "1K",
      "limit_generations": false,
      "enable_web_search": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "content_type": "image/png",
          "file_name": "nano-banana-pro-t2i-output.png",
          "url": "https://storage.googleapis.com/falserverless/example_outputs/nano-banana-pro-t2i-output.png"
        }
      ],
      "description": ""
    }
    ```
  </Tab>

  <Tab title="Edit">
    **Endpoint:** `POST https://fal.run/fal-ai/gemini-3-pro-image-preview/edit`
    **Endpoint ID:** `fal-ai/gemini-3-pro-image-preview/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/gemini-3-pro-image-preview/edit/playground">
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
          "fal-ai/gemini-3-pro-image-preview/edit",
          arguments={
              "prompt": "make a photo of the man driving the car down the california coastline",
              "image_urls": [
                  "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input.png",
                  "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input-2.png"
              ]
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/gemini-3-pro-image-preview/edit", {
        input: {
            prompt: "make a photo of the man driving the car down the california coastline",
            image_urls: [
              "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input.png",
              "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input-2.png"
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
        --url https://fal.run/fal-ai/gemini-3-pro-image-preview/edit \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "make a photo of the man driving the car down the california coastline",
        "image_urls": [
          "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input.png",
          "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input-2.png"
        ]
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt for image editing.
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      The number of images to generate. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="seed" type="integer">
      The seed for the random number generator.
    </ParamField>

    <ParamField body="aspect_ratio" type="Enum" default="auto">
      The aspect ratio of the generated image. Default value: `auto`

      Possible values: `auto`, `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="png">
      The format of the generated image. Default value: `"png"`

      Possible values: `jpeg`, `png`, `webp`
    </ParamField>

    <ParamField body="safety_tolerance" type="SafetyToleranceEnum" default="4">
      The safety tolerance level for content moderation. 1 is the most strict (blocks most content), 6 is the least strict. Default value: `"4"`

      Possible values: `1`, `2`, `3`, `4`, `5`, `6`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="image_urls" type="list<string>" required>
      The URLs of the images to use for image-to-image generation or image editing.
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="1K">
      The resolution of the image to generate. Default value: `"1K"`

      Possible values: `1K`, `2K`, `4K`
    </ParamField>

    <ParamField body="limit_generations" type="boolean" default="false">
      Experimental parameter to limit the number of generations from each round of prompting to 1. Set to `True` to to disregard any instructions in the prompt regarding the number of images to generate.
    </ParamField>

    <ParamField body="enable_web_search" type="boolean" default="false">
      Enable web search for the image generation task. This will allow the model to use the latest information from the web to generate the image.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<ImageFile>" required>
      The edited images.
    </ParamField>

    <ParamField body="description" type="string" required>
      The description of the generated images.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "make a photo of the man driving the car down the california coastline",
      "num_images": 1,
      "aspect_ratio": "auto",
      "output_format": "png",
      "safety_tolerance": "4",
      "sync_mode": false,
      "image_urls": [
        "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input.png",
        "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input-2.png"
      ],
      "resolution": "1K",
      "limit_generations": false,
      "enable_web_search": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "content_type": "image/png",
          "file_name": "nano-banana-pro-edit-output.png",
          "url": "https://storage.googleapis.com/falserverless/example_outputs/nano-banana-pro-edit-output.png"
        }
      ],
      "description": ""
    }
    ```
  </Tab>
</Tabs>

Google's Nano Banana Pro (2) Preview delivers state-of-the-art image generation at \$0.15 per image, trading cost efficiency for advanced reasoning capabilities and prompt understanding. Built on Gemini 3 Pro's multimodal architecture, it handles complex natural language instructions that would trip up traditional diffusion models.

**Use Cases:** Complex Scene Composition | Typography-Heavy Designs | Natural Language-Driven Editing

***

## Performance

Nano Banana Pro prioritizes semantic understanding over raw speed, making it ideal for projects where prompt accuracy matters more than generation volume.

| Metric                     | Result            | Context                                                |
| :------------------------- | :---------------- | :----------------------------------------------------- |
| **Resolution Range**       | Up to 4K (4096px) | 4K outputs charged at 2x standard rate                 |
| **Cost per Image**         | \$0.15            | 6-7 generations per \$1.00 on fal                      |
| **Batch Generation**       | 1-4 images        | Per request via `num_images` parameter                 |
| **Web Search Integration** | Optional          | Enable via `enable_web_search` for current information |

***

## Advanced Prompt Understanding Through Gemini 3 Architecture

Gemini 3 Pro Image leverages Google's latest foundation model to interpret complex, conversational prompts rather than requiring carefully crafted keyword strings.

**What this means for you:**

* **Natural Language Processing:** Describe scenes conversationally ("meticulously placed camera on the water line, dividing the image in half") instead of keyword stuffing

* **Typography Excellence:** Tagged for realism and typography, making it particularly strong for text-heavy designs where letter accuracy matters

* **Flexible Output Control:** Generate up to 4 images per request with selectable aspect ratios (21:9 to 9:16) and formats (JPEG, PNG, WebP)

* **Resolution Scaling:** Choose 1K, 2K, or 4K output based on your quality-versus-cost tradeoff, with transparent 2x pricing for 4K

***

## Technical Specifications

| Spec                   | Details                                         |
| :--------------------- | :---------------------------------------------- |
| **Architecture**       | Gemini 3 Pro Image                              |
| **Input Formats**      | Text prompts with optional web search grounding |
| **Output Formats**     | JPEG, PNG, WebP                                 |
| **Resolution Options** | 1K, 2K, 4K (4K at 2x cost)                      |
| **License**            | Commercial use via partnership                  |

[API Documentation](https://fal.ai/models/fal-ai/gemini-3-pro-image-preview/api) | [Quickstart Guide](https://docs.fal.ai/model-apis/quickstart) | [Enterprise Pricing](https://fal.ai/pricing)

***

## How It Stacks Up

**[Gemini 2.5 Flash Image](https://fal.ai/models/fal-ai/gemini-25-flash-image)** – Nano Banana Pro trades speed and cost efficiency for advanced reasoning and complex instruction following at 4x the cost ($0.15 vs $0.039). Gemini 2.5 Flash Image remains ideal for high-volume workflows where rapid iteration matters more than nuanced prompt interpretation.

\*\*[AuraFlow](https://fal.ai/models/fal-ai/aura-flow) ($0.012)** – Nano Banana Pro prioritizes semantic understanding and typography accuracy at 12.5x the cost ($0.15 vs \$0.012). AuraFlow offers maximum cost efficiency for straightforward text-to-image generation where natural language complexity isn't critical.

## Related

* [Gemini 3 Pro Image Preview](/model-api-reference/image-generation-api/gemini-3-pro-image-preview) — Image Generation

## Limitations

* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`, `webp`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`, `6`
* `resolution` restricted to: `1K`, `2K`, `4K`
