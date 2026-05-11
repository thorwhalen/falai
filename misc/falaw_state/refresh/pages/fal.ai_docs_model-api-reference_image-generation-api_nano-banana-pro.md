> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Nano Banana Pro API

> API reference for Nano Banana Pro. Nano Banana Pro is Google's new state-of-the-art image generation and editing model

<Tabs>
  <Tab title="Nano Banana Pro">
    **Endpoint:** `POST https://fal.run/fal-ai/nano-banana-pro`
    **Endpoint ID:** `fal-ai/nano-banana-pro`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/nano-banana-pro/playground">
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
          "fal-ai/nano-banana-pro",
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

      const result = await fal.subscribe("fal-ai/nano-banana-pro", {
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
        --url https://fal.run/fal-ai/nano-banana-pro \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "An action shot of a black lab swimming in an inground suburban swimming pool. The camera is placed meticulously on the water line, dividing the image in half, revealing both the dogs head above water holding a tennis ball in it'\''s mouth, and it'\''s paws paddling underwater."
      }'
      ```
    </CodeGroup>

    ## Examples

    > An action shot of a black lab swimming in an inground suburban swimming pool. The camera is placed meticulously on the water line, dividing the image in half, revealing both the dogs head above water holding a tennis ball in it's mouth, and it's paws paddling underwater.

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a95c094/qGn_Uhoer-pmZ280bBLIl_uT30LWIl.png" alt="Generated image: An action shot of a black lab swimming in an inground suburban swimming pool. Th" />
    </Frame>

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
    **Endpoint:** `POST https://fal.run/fal-ai/nano-banana-pro/edit`
    **Endpoint ID:** `fal-ai/nano-banana-pro/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/nano-banana-pro/edit/playground">
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
          "fal-ai/nano-banana-pro/edit",
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

      const result = await fal.subscribe("fal-ai/nano-banana-pro/edit", {
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
        --url https://fal.run/fal-ai/nano-banana-pro/edit \
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

    ## Examples

    > make a photo of the man driving the car down the california coastline

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a95c097/cwrciOok_QqVLvkoEM3wp_Dj7uMWzg.png" alt="Generated image: make a photo of the man driving the car down the california coastline" />
    </Frame>

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

Google's Gemini 3 Pro Image architecture delivers production-quality visuals at \$0.15 per image—understanding context like a multimodal foundation model, not keyword matching like traditional diffusion systems. Trading raw speed for sophisticated semantic interpretation and enhanced reasoning capabilities, it transforms complex creative direction into accurate visuals without prompt engineering gymnastics, making it ideal for teams that need studio-quality results with advanced text rendering and character consistency.

**Built for:** Marketing campaign generation | Product visualization workflows | Creative content production requiring text accuracy | Infographic and diagram creation at scale

## Beyond CLIP: Multimodal Understanding

Built on Google's Gemini 3 Pro foundation, Nano Banana Pro processes prompts through the same multimodal architecture that powers conversational AI understanding nuance, context, and creative intent rather than simple keyword matching. Where traditional diffusion models treat prompts as collections of weighted tokens, this approach interprets your creative direction holistically, capturing relationships between concepts that single-modality systems miss.

**What this means for you:**

* **Semantic accuracy**: Generates images that match creative intent, not just literal prompt keywords understanding "1960s aesthetic" means grain, color palette, and composition choices
* **Reduced iteration cycles**: First-generation outputs align with complex briefs, cutting revision rounds compared to keyword-dependent models
* **Batch efficiency**: Process approximately 7 generations per dollar with consistent quality across variations, making A/B testing and campaign asset creation economically viable
* **Natural language control**: Direct the model with conversational prompts describing mood, style, and context without mastering prompt engineering syntax
* **Advanced text rendering**: Industry-leading text generation capabilities for creating legible text in multiple languages, fonts, and calligraphy styles directly within images

## Performance Optimized for Quality

Google's multimodal foundation prioritizes quality and reasoning depth over raw speed, optimized for production workflows requiring sophisticated outputs.

| Metric                    | Result                    | Context                                                                                     |
| ------------------------- | ------------------------- | ------------------------------------------------------------------------------------------- |
| **Cost per Image**        | \$0.15                    | \~7 generations per \$1.00 on fal.ai 4K outputs will be charged at double the standard rate |
| **Architecture**          | Gemini 3 Pro Image        | Multimodal foundation model with enhanced reasoning                                         |
| **Generation Philosophy** | Quality-first             | Prioritizes complex compositions and accuracy over speed                                    |
| **Batch Processing**      | Multiple images supported | Via `num_images` parameter in API                                                           |
| **Resolution Options**    | 1K, 2K, 4K                | Configurable via API                                                                        |

*Note: Generation times not publicly benchmarked by Google; model optimized for quality rather than speed metrics*

## Technical Specifications

| Spec                      | Details                                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| **Architecture**          | Gemini 3 Pro Image (Nano Banana Pro)                                                     |
| **Input Formats**         | Text prompts with natural language support; multi-image blending (up to 14 images)       |
| **Output Formats**        | PNG, JPEG, WebP image files                                                              |
| **Resolution Options**    | Multiple aspect ratios including 21:9, 16:9, 3:2, 4:3, 5:4, 1:1, 4:5, 3:4, 2:3, 9:16     |
| **Character Consistency** | Maintains consistency and resemblance for up to 5 people across generations              |
| **Watermarking**          | SynthID digital watermarking on all outputs; visible watermark for non-Ultra subscribers |
| **License**               | Commercial use enabled through fal.ai                                                    |
| **Launch Date**           | November 20, 2025                                                                        |

[API Documentation](https://fal.ai/models/fal-ai/nano-banana-pro/api)

## How It Stacks Up

**vs. FLUX.1 \[dev]**: Nano Banana Pro achieves semantic-aware generation with industry-leading text rendering through Gemini 3 Pro's multimodal reasoning, making it ideal for marketing materials requiring accurate typography. FLUX.1 \[dev] prioritizes maximum resolution control and fine detail preservation for technical illustration workflows.

**vs. Stable Diffusion 3.5**: Nano Banana Pro achieves natural language interpretation and real-world knowledge integration through Gemini architecture, making it ideal for teams creating infographics and data visualizations without prompt engineering expertise. Stable Diffusion 3.5 prioritizes open-source flexibility for custom fine-tuning and on-premise deployment scenarios.

**vs. Original Nano Banana (Gemini 2.5 Flash Image)**: Nano Banana Pro trades speed for quality, offering enhanced reasoning, superior text rendering, better character consistency, and advanced composition capabilities. Original Nano Banana remains available for rapid iterations and simple edits at lower cost (\$0.039/image).

## Related

* [Nano Banana Pro](/model-api-reference/image-generation-api/nano-banana-pro) — Image Generation

## Limitations

* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`, `webp`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`, `6`
* `resolution` restricted to: `1K`, `2K`, `4K`
