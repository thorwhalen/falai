> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Seedream V4 API

> API reference for Bytedance Seedream V4. A new-generation image creation model ByteDance, Seedream 4.0 integrates image generation and image editing capabilities into a single, unified architecture.

<Tabs>
  <Tab title="Edit">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedream/v4/edit`
    **Endpoint ID:** `fal-ai/bytedance/seedream/v4/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedream/v4/edit/playground">
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
          "fal-ai/bytedance/seedream/v4/edit",
          arguments={
              "prompt": "Dress the model in the clothes and hat. Add a cat to the scene and change the background to a Victorian era building.",
              "image_urls": [
                  "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_1.png",
                  "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_2.png",
                  "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_3.png",
                  "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_4.png"
              ]
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/seedream/v4/edit", {
        input: {
            prompt: "Dress the model in the clothes and hat. Add a cat to the scene and change the background to a Victorian era building.",
            image_urls: [
              "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_1.png",
              "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_2.png",
              "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_3.png",
              "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_4.png"
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
        --url https://fal.run/fal-ai/bytedance/seedream/v4/edit \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Dress the model in the clothes and hat. Add a cat to the scene and change the background to a Victorian era building.",
        "image_urls": [
          "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_1.png",
          "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_2.png",
          "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_3.png",
          "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_4.png"
        ]
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt used to edit the image
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="[object Object]">
      The size of the generated image. The minimum total image area is 921600 pixels. Failing this, the image size will be adjusted to by scaling it up, while maintaining the aspect ratio.

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`, `auto`, `auto_2K`, `auto_4K`
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

    <ParamField body="enhance_prompt_mode" type="EnhancePromptModeEnum" default="standard">
      The mode to use for enhancing prompt enhancement. Standard mode provides higher quality results but takes longer to generate. Fast mode provides average quality results but takes less time to generate. Default value: `"standard"`

      Possible values: `standard`, `fast`
    </ParamField>

    <ParamField body="image_urls" type="list<string>" required>
      List of URLs of input images for editing. Presently, up to 10 image inputs are allowed. If over 10 images are sent, only the last 10 will be used.
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
      "prompt": "Dress the model in the clothes and hat. Add a cat to the scene and change the background to a Victorian era building.",
      "image_size": {
        "height": 2160,
        "width": 3840
      },
      "num_images": 1,
      "max_images": 1,
      "sync_mode": false,
      "enable_safety_checker": true,
      "enhance_prompt_mode": "standard",
      "image_urls": [
        "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_1.png",
        "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_2.png",
        "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_3.png",
        "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_4.png"
      ]
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://storage.googleapis.com/falserverless/example_outputs/seedream4_edit_output.png"
        }
      ],
      "seed": 746406749
    }
    ```
  </Tab>

  <Tab title="Text To Image">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedream/v4/text-to-image`
    **Endpoint ID:** `fal-ai/bytedance/seedream/v4/text-to-image`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedream/v4/text-to-image/playground">
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
          "fal-ai/bytedance/seedream/v4/text-to-image",
          arguments={
              "prompt": "A trendy restaurant with a digital menu board displaying \"Seedream 4.0 is available on fal\" in elegant script, with diners enjoying their meals."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/seedream/v4/text-to-image", {
        input: {
            prompt: "A trendy restaurant with a digital menu board displaying \"Seedream 4.0 is available on fal\" in elegant script, with diners enjoying their meals."
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
        --url https://fal.run/fal-ai/bytedance/seedream/v4/text-to-image \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A trendy restaurant with a digital menu board displaying \"Seedream 4.0 is available on fal\" in elegant script, with diners enjoying their meals."
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt used to generate the image
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="[object Object]">
      The size of the generated image. Total pixels must be between 960x960 and 4096x4096.

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`, `auto`, `auto_2K`, `auto_4K`
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

    <ParamField body="enhance_prompt_mode" type="EnhancePromptModeEnum" default="standard">
      The mode to use for enhancing prompt enhancement. Standard mode provides higher quality results but takes longer to generate. Fast mode provides average quality results but takes less time to generate. Default value: `"standard"`

      Possible values: `standard`, `fast`
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
      "prompt": "A trendy restaurant with a digital menu board displaying \"Seedream 4.0 is available on fal\" in elegant script, with diners enjoying their meals.",
      "image_size": {
        "height": 4096,
        "width": 4096
      },
      "num_images": 1,
      "max_images": 1,
      "sync_mode": false,
      "enable_safety_checker": true,
      "enhance_prompt_mode": "standard"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://storage.googleapis.com/falserverless/example_outputs/seedream4_t2i_output.png"
        }
      ],
      "seed": 746406749
    }
    ```
  </Tab>
</Tabs>

## Related

* [Bytedance Seedream v4](/model-api-reference/image-generation-api/bytedance-seedream-v4) — Image Generation
* [Bytedance](/model-api-reference/image-generation-api/bytedance) — Image Generation
* [Bytedance Seedream v4 Edit](/model-api-reference/image-generation-api/bytedance-seedream-v4-edit) — Image Generation

## Limitations

* `num_images` range: 1 to 6
* `max_images` range: 1 to 6
* `enhance_prompt_mode` restricted to: `standard`, `fast`
* Content moderation via safety checker
