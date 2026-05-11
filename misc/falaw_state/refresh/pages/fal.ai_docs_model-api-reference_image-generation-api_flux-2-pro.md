> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux 2 Pro API

> API reference for Flux 2 Pro. Image editing with FLUX.2 [pro] from Black Forest Labs. Ideal for high-quality image manipulation, style transfer, and sequential editing workflows

<Tabs>
  <Tab title="Flux 2 Pro">
    **Endpoint:** `POST https://fal.run/fal-ai/flux-2-pro`
    **Endpoint ID:** `fal-ai/flux-2-pro`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-2-pro/playground">
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
          "fal-ai/flux-2-pro",
          arguments={
              "prompt": "An intense close-up of knight's visor reflecting battle, sword raised, flames in background, chiaroscuro helmet shadows, hyper-detailed armor, square medieval, cinematic lighting"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/flux-2-pro", {
        input: {
            prompt: "An intense close-up of knight's visor reflecting battle, sword raised, flames in background, chiaroscuro helmet shadows, hyper-detailed armor, square medieval, cinematic lighting"
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
        --url https://fal.run/fal-ai/flux-2-pro \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "An intense close-up of knight'\''s visor reflecting battle, sword raised, flames in background, chiaroscuro helmet shadows, hyper-detailed armor, square medieval, cinematic lighting"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to generate an image from.
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="landscape_4_3">
      The size of the generated image. Default value: `landscape_4_3`

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
    </ParamField>

    <ParamField body="seed" type="integer">
      The seed to use for the generation.
    </ParamField>

    <ParamField body="safety_tolerance" type="SafetyToleranceEnum" default="2">
      The safety tolerance level for the generated image. 1 being the most strict and 5 being the most permissive. Default value: `"2"`

      Possible values: `1`, `2`, `3`, `4`, `5`
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      Whether to enable the safety checker. Default value: `true`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<ImageFile>" required>
      The generated images.
    </ParamField>

    <ParamField body="seed" type="integer" required>
      The seed used for the generation.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "An intense close-up of knight's visor reflecting battle, sword raised, flames in background, chiaroscuro helmet shadows, hyper-detailed armor, square medieval, cinematic lighting",
      "image_size": "landscape_4_3",
      "safety_tolerance": "2",
      "enable_safety_checker": true,
      "output_format": "jpeg",
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://storage.googleapis.com/falserverless/example_outputs/flux2_pro_t2i_output.png"
        }
      ]
    }
    ```
  </Tab>

  <Tab title="Edit">
    **Endpoint:** `POST https://fal.run/fal-ai/flux-2-pro/edit`
    **Endpoint ID:** `fal-ai/flux-2-pro/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-2-pro/edit/playground">
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
          "fal-ai/flux-2-pro/edit",
          arguments={
              "prompt": "Place realistic flames emerging from the top of the coffee cup, dancing above the rim",
              "image_urls": [
                  "https://storage.googleapis.com/falserverless/example_inputs/flux2_pro_edit_input.png"
              ]
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/flux-2-pro/edit", {
        input: {
            prompt: "Place realistic flames emerging from the top of the coffee cup, dancing above the rim",
            image_urls: [
              "https://storage.googleapis.com/falserverless/example_inputs/flux2_pro_edit_input.png"
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
        --url https://fal.run/fal-ai/flux-2-pro/edit \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Place realistic flames emerging from the top of the coffee cup, dancing above the rim",
        "image_urls": [
          "https://storage.googleapis.com/falserverless/example_inputs/flux2_pro_edit_input.png"
        ]
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to generate an image from.
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="auto">
      The size of the generated image. If `auto`, the size will be determined by the model. Default value: `auto`

      Possible values: `auto`, `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
    </ParamField>

    <ParamField body="seed" type="integer">
      The seed to use for the generation.
    </ParamField>

    <ParamField body="safety_tolerance" type="SafetyToleranceEnum" default="2">
      The safety tolerance level for the generated image. 1 being the most strict and 5 being the most permissive. Default value: `"2"`

      Possible values: `1`, `2`, `3`, `4`, `5`
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      Whether to enable the safety checker. Default value: `true`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="image_urls" type="list<string>" required>
      List of URLs of input images for editing
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<ImageFile>" required>
      The generated images.
    </ParamField>

    <ParamField body="seed" type="integer" required>
      The seed used for the generation.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Place realistic flames emerging from the top of the coffee cup, dancing above the rim",
      "image_size": "auto",
      "safety_tolerance": "2",
      "enable_safety_checker": true,
      "output_format": "jpeg",
      "sync_mode": false,
      "image_urls": [
        "https://storage.googleapis.com/falserverless/example_inputs/flux2_pro_edit_input.png"
      ]
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://storage.googleapis.com/falserverless/example_outputs/flux2_pro_edit_output.png"
        }
      ]
    }
    ```
  </Tab>
</Tabs>

**Production-optimized generation** with professional quality out of the box. FLUX.2 \[pro] delivers studio-grade images through a streamlined pipeline that prioritizes consistency and speed over parameter tuning. No inference steps to configure, no guidance scales to adjust—just pure prompt-to-image conversion optimized for production workflows where reliability matters more than experimental control.

**Built for:** Production pipelines | High-volume generation | API integrations | Consistent brand outputs | Teams prioritizing speed over parameter experimentation

## Streamlined Professional Pipeline

FLUX.2 \[pro] removes generation complexity to focus on what matters: translating prompts into professional-quality images with predictable results. The model's fixed optimization delivers consistent output quality without requiring expertise in inference tuning.

**What this means for you:**

* **Zero-configuration quality**: Professional-grade outputs without tuning steps or guidance parameters. The model's internal optimization handles quality decisions
* **Production consistency**: Predictable results across batch generations make pro ideal for automated workflows and API integrations
* **Fast iteration cycles**: Streamlined pipeline prioritizes generation speed for teams moving quickly through creative development
* **Flexible output formats**: Choose between JPEG (optimized file sizes) or PNG (lossless quality) based on delivery requirements
* **Reproducible generations**: Seed control maintains consistency across variations without exposing low-level inference parameters
* **Prompt enhancement**: Automatic prompt upsampling refines instructions for optimal interpretation (enabled by default)

# Advanced Prompting Techniques

## JSON Structured Prompts

For precise control over complex generations, use structured JSON prompts instead of natural language. JSON prompting enables granular specification of scene elements, subjects, camera settings, and composition.

**Basic JSON structure:**

```json theme={null}
{
  "scene": "Overall setting description",
  "subjects": [
    {
      "type": "Subject category",
      "description": "Physical attributes and details",
      "pose": "Action or stance",
      "position": "foreground/midground/background"
    }
  ],
  "style": "Artistic rendering approach",
  "color_palette": ["color1", "color2", "color3"],
  "lighting": "Lighting conditions and direction",
  "mood": "Emotional atmosphere",
  "composition": "rule of thirds/centered/dynamic diagonal",
  "camera": {
    "angle": "eye level/low angle/high angle",
    "distance": "close-up/medium shot/wide shot",
    "lens": "35mm/50mm/85mm"
  }
}
```

JSON prompts excel at controlling multiple subjects, precise positioning, and maintaining specific attributes across complex compositions.

## HEX Color Code Control

Specify exact colors using HEX codes for precise color matching and brand consistency. Include the keyword "color" or "hex" before the code for best results.

**Examples:**

* `"a wall painted in color #2ECC71"`
* `"gradient from hex #FF6B6B to hex #4ECDC4"`
* `"the car in color #1A1A1A with accents in #FFD700"`

For enhanced accuracy, reference a color swatch image alongside the HEX code in your prompt.

## Image Referencing with @

Reference uploaded images directly in prompts using the `@` symbol for intuitive multi-image workflows.

**Usage patterns:**

* `"@image1 wearing the outfit from @image2"`
* `"combine the style of @image1 with the composition of @image2"`
* `"the person from @image1 in the setting from @image3"`

The `@` syntax provides a natural way to reference multiple images without explicit index notation, while maintaining support for traditional "image 1", "image 2" indexing.

## Related

* [Flux 2 Pro](/model-api-reference/image-generation-api/flux-2-pro) — Image Generation

## Limitations

* `image_size` restricted to: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`
* `output_format` restricted to: `jpeg`, `png`
* Content moderation via safety checker
* `image_size` restricted to: `auto`, `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
