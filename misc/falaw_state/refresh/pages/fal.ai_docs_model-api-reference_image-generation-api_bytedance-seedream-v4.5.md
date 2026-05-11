> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Seedream V4.5 API

> API reference for Bytedance Seedream V4.5. A new-generation image creation model ByteDance, Seedream 4.5 integrates image generation and image editing capabilities into a single, unified architecture.

<Tabs>
  <Tab title="Edit">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedream/v4.5/edit`
    **Endpoint ID:** `fal-ai/bytedance/seedream/v4.5/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedream/v4.5/edit/playground">
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
          "fal-ai/bytedance/seedream/v4.5/edit",
          arguments={
              "prompt": "Replace the product in Figure 1 with that in Figure 2. For the title copy the text in Figure 3 to the top of the screen, the title should have a clear contrast with the background but not be overly eye-catching.",
              "image_urls": [
                  "https://storage.googleapis.com/falserverless/example_inputs/seedreamv45/seedream_v45_edit_input_1.png",
                  "https://storage.googleapis.com/falserverless/example_inputs/seedreamv45/seedream_v45_edit_input_2.png",
                  "https://storage.googleapis.com/falserverless/example_inputs/seedreamv45/seedream_v45_edit_input_3.png"
              ]
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/seedream/v4.5/edit", {
        input: {
            prompt: "Replace the product in Figure 1 with that in Figure 2. For the title copy the text in Figure 3 to the top of the screen, the title should have a clear contrast with the background but not be overly eye-catching.",
            image_urls: [
              "https://storage.googleapis.com/falserverless/example_inputs/seedreamv45/seedream_v45_edit_input_1.png",
              "https://storage.googleapis.com/falserverless/example_inputs/seedreamv45/seedream_v45_edit_input_2.png",
              "https://storage.googleapis.com/falserverless/example_inputs/seedreamv45/seedream_v45_edit_input_3.png"
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
        --url https://fal.run/fal-ai/bytedance/seedream/v4.5/edit \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Replace the product in Figure 1 with that in Figure 2. For the title copy the text in Figure 3 to the top of the screen, the title should have a clear contrast with the background but not be overly eye-catching.",
        "image_urls": [
          "https://storage.googleapis.com/falserverless/example_inputs/seedreamv45/seedream_v45_edit_input_1.png",
          "https://storage.googleapis.com/falserverless/example_inputs/seedreamv45/seedream_v45_edit_input_2.png",
          "https://storage.googleapis.com/falserverless/example_inputs/seedreamv45/seedream_v45_edit_input_3.png"
        ]
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt used to edit the image
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="[object Object]">
      The size of the generated image. Width and height must be between 1920 and 4096, or total number of pixels must be between 2560*1440 and 4096*4096.

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`, `auto_2K`, `auto_4K`
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      Number of separate model generations to be run with the prompt. Default value: `1`

      Range: `1` to `6`
    </ParamField>

    <ParamField body="max_images" type="integer" default="1">
      If set to a number greater than one, enables multi-image generation. The model will potentially return up to `max_images` images every generation, and in total, `num_images` generations will be carried out. In total, the number of images generated will be between `num_images` and `max_images*num_images`. The total number of images (image inputs + image outputs) must not exceed 15 Default value: `1`

      Range: `1` to `6`
    </ParamField>

    <ParamField body="seed" type="integer">
      Random seed to control the stochasticity of image generation.
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    <ParamField body="image_urls" type="list<string>" required>
      List of URLs of input images for editing. Presently, up to 10 image inputs are allowed. If over 10 images are sent, only the last 10 will be used.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
      Generated images
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Replace the product in Figure 1 with that in Figure 2. For the title copy the text in Figure 3 to the top of the screen, the title should have a clear contrast with the background but not be overly eye-catching.",
      "image_size": "auto_4K",
      "num_images": 1,
      "max_images": 1,
      "sync_mode": false,
      "enable_safety_checker": true,
      "image_urls": [
        "https://storage.googleapis.com/falserverless/example_inputs/seedreamv45/seedream_v45_edit_input_1.png",
        "https://storage.googleapis.com/falserverless/example_inputs/seedreamv45/seedream_v45_edit_input_2.png",
        "https://storage.googleapis.com/falserverless/example_inputs/seedreamv45/seedream_v45_edit_input_3.png"
      ]
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://storage.googleapis.com/falserverless/example_outputs/seedreamv45/seedream_v45_edit_output.png"
        }
      ]
    }
    ```
  </Tab>

  <Tab title="Text To Image">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedream/v4.5/text-to-image`
    **Endpoint ID:** `fal-ai/bytedance/seedream/v4.5/text-to-image`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedream/v4.5/text-to-image/playground">
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
          "fal-ai/bytedance/seedream/v4.5/text-to-image",
          arguments={
              "prompt": "A selfie of a cat, with the cat as the protagonist. The setting is twilight at the Eiffel Tower. The cat is happy, holding a piece of baklava in its paw. The photo has a slight motion blur and is slightly overexposed. From a selfie angle, with a bit of motion blur, the overall image presents a sense of calm madness. The text \"Seedream 4.5 is on fal\" should be written on the picture at the top in clearly visible font and crisp lettering. The image has a 4:3 aspect ratio"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/seedream/v4.5/text-to-image", {
        input: {
            prompt: "A selfie of a cat, with the cat as the protagonist. The setting is twilight at the Eiffel Tower. The cat is happy, holding a piece of baklava in its paw. The photo has a slight motion blur and is slightly overexposed. From a selfie angle, with a bit of motion blur, the overall image presents a sense of calm madness. The text \"Seedream 4.5 is on fal\" should be written on the picture at the top in clearly visible font and crisp lettering. The image has a 4:3 aspect ratio"
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
        --url https://fal.run/fal-ai/bytedance/seedream/v4.5/text-to-image \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A selfie of a cat, with the cat as the protagonist. The setting is twilight at the Eiffel Tower. The cat is happy, holding a piece of baklava in its paw. The photo has a slight motion blur and is slightly overexposed. From a selfie angle, with a bit of motion blur, the overall image presents a sense of calm madness. The text \"Seedream 4.5 is on fal\" should be written on the picture at the top in clearly visible font and crisp lettering. The image has a 4:3 aspect ratio"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt used to generate the image
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="[object Object]">
      The size of the generated image. Width and height must be between 1920 and 4096, or total number of pixels must be between 2560*1440 and 4096*4096.

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`, `auto_2K`, `auto_4K`
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      Number of separate model generations to be run with the prompt. Default value: `1`

      Range: `1` to `6`
    </ParamField>

    <ParamField body="max_images" type="integer" default="1">
      If set to a number greater than one, enables multi-image generation. The model will potentially return up to `max_images` images every generation, and in total, `num_images` generations will be carried out. In total, the number of images generated will be between `num_images` and `max_images*num_images`. Default value: `1`

      Range: `1` to `6`
    </ParamField>

    <ParamField body="seed" type="integer">
      Random seed to control the stochasticity of image generation.
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
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
      "prompt": "A selfie of a cat, with the cat as the protagonist. The setting is twilight at the Eiffel Tower. The cat is happy, holding a piece of baklava in its paw. The photo has a slight motion blur and is slightly overexposed. From a selfie angle, with a bit of motion blur, the overall image presents a sense of calm madness. The text \"Seedream 4.5 is on fal\" should be written on the picture at the top in clearly visible font and crisp lettering. The image has a 4:3 aspect ratio",
      "image_size": "auto_2K",
      "num_images": 1,
      "max_images": 1,
      "sync_mode": false,
      "enable_safety_checker": true
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://storage.googleapis.com/falserverless/example_outputs/seedreamv45/seedream_v45_t2i_output.png"
        }
      ],
      "seed": 42
    }
    ```
  </Tab>
</Tabs>

ByteDance's Seedream 4.5 transforms existing images through natural language instructions at \$0.04 per edit, processing up to 10 reference images simultaneously for complex multi-source compositions. Trading simple single-image workflows for sophisticated context-aware editing, this unified architecture references multiple sources, copies specific elements between images, and maintains spatial relationships without manual masking. Built for e-commerce teams assembling product composites, designers prototyping layout variations, and marketing workflows requiring consistent brand element integration across visuals.

**Built for:** Multi-image product composites | Layout prototyping with text overlays | Brand asset integration workflows

***

## Natural Language Editing Without Layers

Seedream 4.5 consolidates image generation and editing into a single architecture that interprets spatial references directly from your prompt. Instead of requiring layer masks or selection tools, you describe edits using natural language - "replace the product in Figure 1 with that in Figure 2" or "copy the text from Figure 3 to the top with clear contrast."

**What this means for you:**

* **Multi-source composition:** Reference up to 10 images per edit, enabling complex workflows like product swaps, text overlay copying, and element positioning across multiple source files
* **Context-aware transformations:** The model maintains depth, perspective, and lighting consistency when integrating elements from different sources - no manual blending required
* **Resolution flexibility:** Output up to 4 megapixels (2048x2048 maximum) with configurable dimensions between 1920px and 4096px on either axis
* **Batch generation control:** Run 1-6 separate generations per request, with optional multi-image output (up to 6 images per generation) for exploring variations

***

## Performance That Scales

Seedream 4.5 processes edits in approximately 60 seconds on [fal infrastructure](https://fal.ai/models/fal-ai/bytedance/seedream/v4.5/edit), with pricing structured for production workflows requiring multiple reference images.

| Metric                   | Result          | Context                                                             |
| :----------------------- | :-------------- | :------------------------------------------------------------------ |
| **Inference Speed**      | \~60 seconds    | Standard processing time per edit on fal                            |
| **Cost per Edit**        | \$0.04          | 25 edits per \$1.00 on fal                                          |
| **Max Reference Images** | 10 images       | Multi-source composition capability (last 10 used if more provided) |
| **Max Resolution**       | 4MP (2048x2048) | Configurable dimensions between 1920-4096px per axis                |

***

## Technical Specifications

| Spec                 | Details                                                   |
| :------------------- | :-------------------------------------------------------- |
| **Architecture**     | Seedream 4.5                                              |
| **Input Formats**    | Image URLs (up to 10), text prompt                        |
| **Output Formats**   | PNG images via URL or data URI                            |
| **Resolution Range** | 1920-4096px per axis, 2560×1440 to 4096×4096 total pixels |
| **License**          | Commercial use via fal Partner agreement                  |

[API Documentation](https://fal.ai/models/fal-ai/bytedance/seedream/v4.5/edit/api)

***

## How It Stacks Up

**[Bytedance Seedream v4 Edit](https://fal.ai/models/fal-ai/bytedance/seedream/v4/edit)** - Seedream 4.5 expands multi-image input capacity from v4's baseline while maintaining the unified editing architecture. Both versions handle natural language spatial instructions, with v4.5 prioritizing higher reference image limits for complex composition workflows.

**[Bytedance Seededit v3](https://fal.ai/models/fal-ai/bytedance/seededit/v3/edit-image)** - Seedream 4.5 consolidates generation and editing into a single model architecture, trading v3's specialized editing focus for broader capability coverage. Seededit v3 remains purpose-built for pure image-to-image transformation workflows without generation requirements.

**[NAFNet-deblur](https://fal.ai/models/fal-ai/nafnet/deblur)** - Seedream 4.5 handles multi-image composition and semantic editing through natural language, making it ideal for layout assembly and element integration. NAFNet-deblur specializes in single-image restoration tasks like blur removal and artifact correction where semantic understanding isn't required.

## Related

* [Bytedance](/model-api-reference/image-generation-api/bytedance) — Image Generation

## Limitations

* `image_size` restricted to: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`, `auto_2K`, `auto_4K`
* `num_images` range: 1 to 6
* `max_images` range: 1 to 6
* Content moderation via safety checker
