> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bria Text To Image API

> API reference for Bria Text To Image. Bria's Text-to-Image model for HD images. Trained exclusively on licensed data for safe and risk-free commercial use. Available also as source code and weights. F

<Tabs>
  <Tab title="Hd">
    **Endpoint:** `POST https://fal.run/fal-ai/bria/text-to-image/hd`
    **Endpoint ID:** `fal-ai/bria/text-to-image/hd`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bria/text-to-image/hd/playground">
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
          "fal-ai/bria/text-to-image/hd",
          arguments={
              "prompt": "A lone figure stands on the edge of a serene cliff at sunset, gazing out over a vast, mystical valley. The figure is clad in flowing robes that ripple in the gentle breeze, silhouetted against the golden and lavender hues of the sky. Below, a cascading waterfall pours into a sparkling river winding through a forest of bioluminescent trees. The scene blends the awe of nature with a touch of otherworldly wonder, inviting reflection and imagination."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bria/text-to-image/hd", {
        input: {
            prompt: "A lone figure stands on the edge of a serene cliff at sunset, gazing out over a vast, mystical valley. The figure is clad in flowing robes that ripple in the gentle breeze, silhouetted against the golden and lavender hues of the sky. Below, a cascading waterfall pours into a sparkling river winding through a forest of bioluminescent trees. The scene blends the awe of nature with a touch of otherworldly wonder, inviting reflection and imagination."
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
        --url https://fal.run/fal-ai/bria/text-to-image/hd \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A lone figure stands on the edge of a serene cliff at sunset, gazing out over a vast, mystical valley. The figure is clad in flowing robes that ripple in the gentle breeze, silhouetted against the golden and lavender hues of the sky. Below, a cascading waterfall pours into a sparkling river winding through a forest of bioluminescent trees. The scene blends the awe of nature with a touch of otherworldly wonder, inviting reflection and imagination."
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt you would like to use to generate images.
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="">
      The negative prompt you would like to use to generate images. Default value: `""`
    </ParamField>

    <ParamField body="num_images" type="integer" default="4">
      How many images you would like to generate. When using any Guidance Method, Value is set to 1. Default value: `4`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="1:1">
      The aspect ratio of the image. When a guidance method is being used, the aspect ratio is defined by the guidance image and this parameter is ignored. Default value: `"1:1"`

      Possible values: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`
    </ParamField>

    <ParamField body="seed" type="integer">
      The same seed and the same prompt given to the same version of the model
      will output the same image every time.

      Range: `0` to `2147483647`
    </ParamField>

    <ParamField body="num_inference_steps" type="integer" default="30">
      The number of iterations the model goes through to refine the generated image. This parameter is optional. Default value: `30`

      Range: `20` to `50`
    </ParamField>

    <ParamField body="guidance_scale" type="float" default="5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `5`

      Range: `0` to `20`
    </ParamField>

    <ParamField body="prompt_enhancement" type="boolean" default="false">
      When set to true, enhances the provided prompt by generating additional, more descriptive variations, resulting in more diverse and creative output images.
    </ParamField>

    <ParamField body="medium" type="MediumEnum">
      Which medium should be included in your generated images. This parameter is optional.

      Possible values: `photography`, `art`
    </ParamField>

    <ParamField body="guidance" type="list<GuidanceInput>" default="">
      Guidance images to use for the generation. Up to 4 guidance methods can be combined during a single inference.
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
      The generated images
    </ParamField>

    <ParamField body="seed" type="integer" required>
      Seed value used for generation.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A lone figure stands on the edge of a serene cliff at sunset, gazing out over a vast, mystical valley. The figure is clad in flowing robes that ripple in the gentle breeze, silhouetted against the golden and lavender hues of the sky. Below, a cascading waterfall pours into a sparkling river winding through a forest of bioluminescent trees. The scene blends the awe of nature with a touch of otherworldly wonder, inviting reflection and imagination.",
      "negative_prompt": "",
      "num_images": 4,
      "aspect_ratio": "1:1",
      "num_inference_steps": 30,
      "guidance_scale": 5,
      "prompt_enhancement": false,
      "guidance": [],
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "content_type": "image/png",
          "file_name": "257cf8e7bd3a47c2959396343d5b38cf.png",
          "file_size": 3731290,
          "height": 1536,
          "url": "https://v3.fal.media/files/tiger/48e63e0K6C9XQYBuomoU-_257cf8e7bd3a47c2959396343d5b38cf.png",
          "width": 1536
        }
      ]
    }
    ```
  </Tab>

  <Tab title="Base">
    **Endpoint:** `POST https://fal.run/fal-ai/bria/text-to-image/base`
    **Endpoint ID:** `fal-ai/bria/text-to-image/base`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bria/text-to-image/base/playground">
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
          "fal-ai/bria/text-to-image/base",
          arguments={
              "prompt": "A lone figure stands on the edge of a serene cliff at sunset, gazing out over a vast, mystical valley. The figure is clad in flowing robes that ripple in the gentle breeze, silhouetted against the golden and lavender hues of the sky. Below, a cascading waterfall pours into a sparkling river winding through a forest of bioluminescent trees. The scene blends the awe of nature with a touch of otherworldly wonder, inviting reflection and imagination."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bria/text-to-image/base", {
        input: {
            prompt: "A lone figure stands on the edge of a serene cliff at sunset, gazing out over a vast, mystical valley. The figure is clad in flowing robes that ripple in the gentle breeze, silhouetted against the golden and lavender hues of the sky. Below, a cascading waterfall pours into a sparkling river winding through a forest of bioluminescent trees. The scene blends the awe of nature with a touch of otherworldly wonder, inviting reflection and imagination."
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
        --url https://fal.run/fal-ai/bria/text-to-image/base \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A lone figure stands on the edge of a serene cliff at sunset, gazing out over a vast, mystical valley. The figure is clad in flowing robes that ripple in the gentle breeze, silhouetted against the golden and lavender hues of the sky. Below, a cascading waterfall pours into a sparkling river winding through a forest of bioluminescent trees. The scene blends the awe of nature with a touch of otherworldly wonder, inviting reflection and imagination."
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt you would like to use to generate images.
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="">
      The negative prompt you would like to use to generate images. Default value: `""`
    </ParamField>

    <ParamField body="num_images" type="integer" default="4">
      How many images you would like to generate. When using any Guidance Method, Value is set to 1. Default value: `4`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="1:1">
      The aspect ratio of the image. When a guidance method is being used, the aspect ratio is defined by the guidance image and this parameter is ignored. Default value: `"1:1"`

      Possible values: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`
    </ParamField>

    <ParamField body="seed" type="integer">
      The same seed and the same prompt given to the same version of the model
      will output the same image every time.

      Range: `0` to `2147483647`
    </ParamField>

    <ParamField body="num_inference_steps" type="integer" default="30">
      The number of iterations the model goes through to refine the generated image. This parameter is optional. Default value: `30`

      Range: `20` to `50`
    </ParamField>

    <ParamField body="guidance_scale" type="float" default="5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `5`

      Range: `0` to `20`
    </ParamField>

    <ParamField body="prompt_enhancement" type="boolean" default="false">
      When set to true, enhances the provided prompt by generating additional, more descriptive variations, resulting in more diverse and creative output images.
    </ParamField>

    <ParamField body="medium" type="MediumEnum">
      Which medium should be included in your generated images. This parameter is optional.

      Possible values: `photography`, `art`
    </ParamField>

    <ParamField body="guidance" type="list<GuidanceInput>" default="">
      Guidance images to use for the generation. Up to 4 guidance methods can be combined during a single inference.
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
      The generated images
    </ParamField>

    <ParamField body="seed" type="integer" required>
      Seed value used for generation.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A lone figure stands on the edge of a serene cliff at sunset, gazing out over a vast, mystical valley. The figure is clad in flowing robes that ripple in the gentle breeze, silhouetted against the golden and lavender hues of the sky. Below, a cascading waterfall pours into a sparkling river winding through a forest of bioluminescent trees. The scene blends the awe of nature with a touch of otherworldly wonder, inviting reflection and imagination.",
      "negative_prompt": "",
      "num_images": 4,
      "aspect_ratio": "1:1",
      "num_inference_steps": 30,
      "guidance_scale": 5,
      "prompt_enhancement": false,
      "guidance": [],
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "content_type": "image/png",
          "file_name": "257cf8e7bd3a47c2959396343d5b38cf.png",
          "file_size": 3731290,
          "height": 1536,
          "url": "https://v3.fal.media/files/tiger/48e63e0K6C9XQYBuomoU-_257cf8e7bd3a47c2959396343d5b38cf.png",
          "width": 1536
        }
      ]
    }
    ```
  </Tab>

  <Tab title="Fast">
    **Endpoint:** `POST https://fal.run/fal-ai/bria/text-to-image/fast`
    **Endpoint ID:** `fal-ai/bria/text-to-image/fast`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bria/text-to-image/fast/playground">
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
          "fal-ai/bria/text-to-image/fast",
          arguments={
              "prompt": "A lone figure stands on the edge of a serene cliff at sunset, gazing out over a vast, mystical valley. The figure is clad in flowing robes that ripple in the gentle breeze, silhouetted against the golden and lavender hues of the sky. Below, a cascading waterfall pours into a sparkling river winding through a forest of bioluminescent trees. The scene blends the awe of nature with a touch of otherworldly wonder, inviting reflection and imagination."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bria/text-to-image/fast", {
        input: {
            prompt: "A lone figure stands on the edge of a serene cliff at sunset, gazing out over a vast, mystical valley. The figure is clad in flowing robes that ripple in the gentle breeze, silhouetted against the golden and lavender hues of the sky. Below, a cascading waterfall pours into a sparkling river winding through a forest of bioluminescent trees. The scene blends the awe of nature with a touch of otherworldly wonder, inviting reflection and imagination."
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
        --url https://fal.run/fal-ai/bria/text-to-image/fast \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A lone figure stands on the edge of a serene cliff at sunset, gazing out over a vast, mystical valley. The figure is clad in flowing robes that ripple in the gentle breeze, silhouetted against the golden and lavender hues of the sky. Below, a cascading waterfall pours into a sparkling river winding through a forest of bioluminescent trees. The scene blends the awe of nature with a touch of otherworldly wonder, inviting reflection and imagination."
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt you would like to use to generate images.
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="">
      The negative prompt you would like to use to generate images. Default value: `""`
    </ParamField>

    <ParamField body="num_images" type="integer" default="4">
      How many images you would like to generate. When using any Guidance Method, Value is set to 1. Default value: `4`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="1:1">
      The aspect ratio of the image. When a guidance method is being used, the aspect ratio is defined by the guidance image and this parameter is ignored. Default value: `"1:1"`

      Possible values: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`
    </ParamField>

    <ParamField body="seed" type="integer">
      The same seed and the same prompt given to the same version of the model
      will output the same image every time.

      Range: `0` to `2147483647`
    </ParamField>

    <ParamField body="num_inference_steps" type="integer" default="8">
      The number of iterations the model goes through to refine the generated image. This parameter is optional. Default value: `8`

      Range: `4` to `10`
    </ParamField>

    <ParamField body="guidance_scale" type="float" default="5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `5`

      Range: `0` to `20`
    </ParamField>

    <ParamField body="prompt_enhancement" type="boolean" default="false">
      When set to true, enhances the provided prompt by generating additional, more descriptive variations, resulting in more diverse and creative output images.
    </ParamField>

    <ParamField body="medium" type="MediumEnum">
      Which medium should be included in your generated images. This parameter is optional.

      Possible values: `photography`, `art`
    </ParamField>

    <ParamField body="guidance" type="list<GuidanceInput>" default="">
      Guidance images to use for the generation. Up to 4 guidance methods can be combined during a single inference.
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
      The generated images
    </ParamField>

    <ParamField body="seed" type="integer" required>
      Seed value used for generation.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A lone figure stands on the edge of a serene cliff at sunset, gazing out over a vast, mystical valley. The figure is clad in flowing robes that ripple in the gentle breeze, silhouetted against the golden and lavender hues of the sky. Below, a cascading waterfall pours into a sparkling river winding through a forest of bioluminescent trees. The scene blends the awe of nature with a touch of otherworldly wonder, inviting reflection and imagination.",
      "negative_prompt": "",
      "num_images": 4,
      "aspect_ratio": "1:1",
      "num_inference_steps": 8,
      "guidance_scale": 5,
      "prompt_enhancement": false,
      "guidance": [],
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "content_type": "image/png",
          "file_name": "257cf8e7bd3a47c2959396343d5b38cf.png",
          "file_size": 3731290,
          "height": 1536,
          "url": "https://v3.fal.media/files/tiger/48e63e0K6C9XQYBuomoU-_257cf8e7bd3a47c2959396343d5b38cf.png",
          "width": 1536
        }
      ]
    }
    ```
  </Tab>
</Tabs>

## Related

* [Bria RMBG 2.0](/model-api-reference/image-generation-api/bria-rmbg-2.0) — Image Generation
* [Bria Expand Image](/model-api-reference/image-generation-api/bria-expand-image) — Image Generation
* [Bria Eraser](/model-api-reference/image-generation-api/bria-eraser) — Image Generation
* [Bria Product Shot](/model-api-reference/image-generation-api/bria-product-shot) — Image Generation
* [Bria Background Replace](/model-api-reference/image-generation-api/bria-background-replace) — Image Generation
* [Video](/model-api-reference/video-generation-api/video) — Video Generation
* [Bria GenFill](/model-api-reference/image-generation-api/bria-genfill) — Image Generation
* [Replace Background](/model-api-reference/image-generation-api/replace-background) — Image Generation
* [Bria Text-to-Image Base](/model-api-reference/image-generation-api/bria-text-to-image-base) — Image Generation
* [Embed Product](/model-api-reference/image-generation-api/embed-product) — Image Generation
* [Bria Text-to-Image Fast](/model-api-reference/image-generation-api/bria-text-to-image-fast) — Image Generation
* [Bria Text-to-Image HD](/model-api-reference/image-generation-api/bria-text-to-image-hd) — Image Generation

## Limitations

* `num_images` range: 1 to 4
* `seed` range: 0 to 2147483647
* `num_inference_steps` range: 20 to 50
* `guidance_scale` range: 0 to 20
* `medium` restricted to: `photography`, `art`
* `num_inference_steps` range: 4 to 10
