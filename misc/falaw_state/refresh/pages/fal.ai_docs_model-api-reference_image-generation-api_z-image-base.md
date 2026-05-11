> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Z Image Base API

> API reference for Z Image Base. Z-Image is the foundation model of the Z- Image family, engineered for good quality, robust generative diversity, broad stylistic coverage, and precise prompt adherence

<Tabs>
  <Tab title="Base">
    **Endpoint:** `POST https://fal.run/fal-ai/z-image/base`
    **Endpoint ID:** `fal-ai/z-image/base`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/z-image/base/playground">
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
          "fal-ai/z-image/base",
          arguments={
              "prompt": "Grandmother knitting by a window, an empty chair by her"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/z-image/base", {
        input: {
            prompt: "Grandmother knitting by a window, an empty chair by her"
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
        --url https://fal.run/fal-ai/z-image/base \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Grandmother knitting by a window, an empty chair by her"
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

    <ParamField body="num_inference_steps" type="integer" default="28">
      The number of inference steps to perform. Default value: `28`

      Range: `1` to `50`
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

    <ParamField body="guidance_scale" type="float" default="4">
      The guidance scale to use for the image generation. Default value: `4`

      Range: `1` to `20`
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="">
      The negative prompt to use for the image generation. Default value: `""`
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

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Grandmother knitting by a window, an empty chair by her",
      "image_size": "landscape_4_3",
      "num_inference_steps": 28,
      "sync_mode": false,
      "num_images": 1,
      "enable_safety_checker": true,
      "output_format": "png",
      "acceleration": "regular",
      "guidance_scale": 4,
      "negative_prompt": ""
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "content_type": "image/png",
          "height": 768,
          "url": "https://v3b.fal.media/files/b/0a8c18a5/1z0k9F1YLgz4qCr64jCBa_r2uqRyDg.png",
          "width": 1024
        }
      ],
      "prompt": ""
    }
    ```
  </Tab>

  <Tab title="Lora">
    **Endpoint:** `POST https://fal.run/fal-ai/z-image/base/lora`
    **Endpoint ID:** `fal-ai/z-image/base/lora`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/z-image/base/lora/playground">
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
          "fal-ai/z-image/base/lora",
          arguments={
              "prompt": "Grandmother knitting by a window, an empty chair by her"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/z-image/base/lora", {
        input: {
            prompt: "Grandmother knitting by a window, an empty chair by her"
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
        --url https://fal.run/fal-ai/z-image/base/lora \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Grandmother knitting by a window, an empty chair by her"
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

    <ParamField body="num_inference_steps" type="integer" default="28">
      The number of inference steps to perform. Default value: `28`

      Range: `1` to `50`
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

    <ParamField body="guidance_scale" type="float" default="4">
      The guidance scale to use for the image generation. Default value: `4`

      Range: `1` to `20`
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="">
      The negative prompt to use for the image generation. Default value: `""`
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

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Grandmother knitting by a window, an empty chair by her",
      "image_size": "landscape_4_3",
      "num_inference_steps": 28,
      "sync_mode": false,
      "num_images": 1,
      "enable_safety_checker": true,
      "output_format": "png",
      "acceleration": "regular",
      "guidance_scale": 4,
      "negative_prompt": "",
      "loras": []
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "content_type": "image/png",
          "height": 768,
          "url": "https://v3b.fal.media/files/b/0a8c18a5/1z0k9F1YLgz4qCr64jCBa_r2uqRyDg.png",
          "width": 1024
        }
      ],
      "prompt": ""
    }
    ```
  </Tab>
</Tabs>

## Related

* [Z-Image Turbo](/model-api-reference/image-generation-api/z-image-turbo) — Image Generation
* [Z Image Base (LoRA)](/model-api-reference/image-generation-api/z-image-base-lora) — Image Generation
* [Z-Image Turbo Seamless Tiling](/model-api-reference/image-generation-api/z-image-turbo-seamless-tiling) — Image Generation
* [Z Image Base](/model-api-reference/image-generation-api/z-image-base) — Image Generation

## Limitations

* `image_size` restricted to: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
* `num_inference_steps` range: 1 to 50
* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`, `webp`
* `acceleration` restricted to: `none`, `regular`, `high`
* `guidance_scale` range: 1 to 20
* Content moderation via safety checker
