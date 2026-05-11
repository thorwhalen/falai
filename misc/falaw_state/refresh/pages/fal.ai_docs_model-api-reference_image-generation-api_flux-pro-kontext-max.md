> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux Pro Kontext Max API

> API reference for Flux Pro Kontext Max. FLUX.1 Kontext [max] is a model with greatly improved prompt adherence and typography generation meet premium consistency for editing without compromise on spee

<Tabs>
  <Tab title="Max">
    **Endpoint:** `POST https://fal.run/fal-ai/flux-pro/kontext/max`
    **Endpoint ID:** `fal-ai/flux-pro/kontext/max`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-pro/kontext/max/playground">
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
          "fal-ai/flux-pro/kontext/max",
          arguments={
              "prompt": "Put a donut next to the flour.",
              "image_url": "https://v3.fal.media/files/rabbit/rmgBxhwGYb2d3pl3x9sKf_output.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/flux-pro/kontext/max", {
        input: {
            prompt: "Put a donut next to the flour.",
            image_url: "https://v3.fal.media/files/rabbit/rmgBxhwGYb2d3pl3x9sKf_output.png"
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
        --url https://fal.run/fal-ai/flux-pro/kontext/max \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Put a donut next to the flour.",
        "image_url": "https://v3.fal.media/files/rabbit/rmgBxhwGYb2d3pl3x9sKf_output.png"
      }'
      ```
    </CodeGroup>

    ## Examples

    > Restyle to Claymation style

    <Frame>
      <img src="https://fal.media/files/tiger/NxnvoLdxc1p_3ljO7vMfo_dd512383bc0b40f482e3d69c29eee7dd.jpg" alt="Generated image: Restyle to Claymation style" />
    </Frame>

    > Change the car color to green

    <Frame>
      <img src="https://fal.media/files/monkey/DhxZDjTxGUjSWm0Av-uf2_d6fdab7825624bfd940fa26b6a739ac0.jpg" alt="Generated image: Change the car color to green" />
    </Frame>

    > replace ‘joy’ by ‘fal"

    <Frame>
      <img src="https://fal.media/files/koala/-hqPr8EPFnQjOKAx8qpBr_472b0b363e8d451aad4737b85fa67cfc.jpg" alt="Generated image: replace ‘joy’ by ‘fal'" />
    </Frame>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to generate an image from.
    </ParamField>

    <ParamField body="seed" type="integer">
      The same seed and the same prompt given to the same version of the model
      will output the same image every time.
    </ParamField>

    <ParamField body="guidance_scale" type="float" default="3.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `3.5`

      Range: `1` to `20`
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

    <ParamField body="aspect_ratio" type="Enum">
      The aspect ratio of the generated image.

      Possible values: `21:9`, `16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16`, `9:21`
    </ParamField>

    <ParamField body="image_url" type="string" required>
      Image prompt for the omni model.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<fal__toolkit__image__image__Image>" required>
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
      "prompt": "Put a donut next to the flour.",
      "guidance_scale": 3.5,
      "sync_mode": false,
      "num_images": 1,
      "output_format": "jpeg",
      "safety_tolerance": "2",
      "enhance_prompt": false,
      "image_url": "https://v3.fal.media/files/rabbit/rmgBxhwGYb2d3pl3x9sKf_output.png"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "height": 1024,
          "url": "https://fal.media/files/tiger/7dSJbIU_Ni-0Zp9eaLsvR_fe56916811d84ac69c6ffc0d32dca151.jpg",
          "width": 1024
        }
      ],
      "prompt": ""
    }
    ```
  </Tab>

  <Tab title="Multi">
    **Endpoint:** `POST https://fal.run/fal-ai/flux-pro/kontext/max/multi`
    **Endpoint ID:** `fal-ai/flux-pro/kontext/max/multi`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-pro/kontext/max/multi/playground">
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
          "fal-ai/flux-pro/kontext/max/multi",
          arguments={
              "prompt": "Put the little duckling on top of the woman's t-shirt.",
              "image_urls": [
                  "https://v3.fal.media/files/penguin/XoW0qavfF-ahg-jX4BMyL_image.webp",
                  "https://v3.fal.media/files/tiger/bml6YA7DWJXOigadvxk75_image.webp"
              ]
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/flux-pro/kontext/max/multi", {
        input: {
            prompt: "Put the little duckling on top of the woman's t-shirt.",
            image_urls: [
              "https://v3.fal.media/files/penguin/XoW0qavfF-ahg-jX4BMyL_image.webp",
              "https://v3.fal.media/files/tiger/bml6YA7DWJXOigadvxk75_image.webp"
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
        --url https://fal.run/fal-ai/flux-pro/kontext/max/multi \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Put the little duckling on top of the woman'\''s t-shirt.",
        "image_urls": [
          "https://v3.fal.media/files/penguin/XoW0qavfF-ahg-jX4BMyL_image.webp",
          "https://v3.fal.media/files/tiger/bml6YA7DWJXOigadvxk75_image.webp"
        ]
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

    <ParamField body="guidance_scale" type="float" default="3.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `3.5`

      Range: `1` to `20`
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

    <ParamField body="aspect_ratio" type="Enum">
      The aspect ratio of the generated image.

      Possible values: `21:9`, `16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16`, `9:21`
    </ParamField>

    <ParamField body="image_urls" type="list<string>" required>
      Image prompt for the omni model.
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
      "prompt": "Put the little duckling on top of the woman's t-shirt.",
      "guidance_scale": 3.5,
      "sync_mode": false,
      "num_images": 1,
      "output_format": "jpeg",
      "safety_tolerance": "2",
      "enhance_prompt": false,
      "image_urls": [
        "https://v3.fal.media/files/penguin/XoW0qavfF-ahg-jX4BMyL_image.webp",
        "https://v3.fal.media/files/tiger/bml6YA7DWJXOigadvxk75_image.webp"
      ]
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

  <Tab title="Text To Image">
    **Endpoint:** `POST https://fal.run/fal-ai/flux-pro/kontext/max/text-to-image`
    **Endpoint ID:** `fal-ai/flux-pro/kontext/max/text-to-image`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-pro/kontext/max/text-to-image/playground">
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
          "fal-ai/flux-pro/kontext/max/text-to-image",
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

      const result = await fal.subscribe("fal-ai/flux-pro/kontext/max/text-to-image", {
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
        --url https://fal.run/fal-ai/flux-pro/kontext/max/text-to-image \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"FLUX\" is painted over it in big, white brush strokes with visible texture."
      }'
      ```
    </CodeGroup>

    ## Examples

    > A solo figure sits on a wooden stool in a dimly lit virtual reality dive bar with textured concrete walls and neon art by Nick Knight.

    <Frame>
      <img src="https://fal.media/files/rabbit/K-A-imOTZKtaWboFHPKTj_74805e96dd464edc901bcddd5ce07269.jpg" alt="Generated image: A solo figure sits on a wooden stool in a dimly lit virtual reality dive bar wit" />
    </Frame>

    > In the mystical realm of Aethereia, where moonlit rivers flowed with stardust and crystal forests pierced the sky, a serene marble bath tub sat at the river's edge, surrounded by luxury decor that shimmered with an ethereal glow, as if infused with the soft, sensual light of sun rays dancing through...

    <Frame>
      <img src="https://fal.media/files/kangaroo/WiEFDKf38mGbnJo37QUHy_84694c7394b54c23b99a9f082c1792d2.jpg" alt="Generated image: In the mystical realm of Aethereia, where moonlit rivers flowed with stardust an" />
    </Frame>

    > A woman stands centered in a secret underground city, surrounded by blurred foliage and a creek, under an overcast sky with natural light.

    <Frame>
      <img src="https://fal.media/files/panda/oDah6AfQ4PZBqPfVYYXxH_43189bb6989d47eaa994cee66829178f.jpg" alt="Generated image: A woman stands centered in a secret underground city, surrounded by blurred foli" />
    </Frame>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to generate an image from.
    </ParamField>

    <ParamField body="seed" type="integer">
      The same seed and the same prompt given to the same version of the model
      will output the same image every time.
    </ParamField>

    <ParamField body="guidance_scale" type="float" default="3.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `3.5`

      Range: `1` to `20`
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

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="1:1">
      The aspect ratio of the generated image. Default value: `"1:1"`

      Possible values: `21:9`, `16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16`, `9:21`
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
      "guidance_scale": 3.5,
      "sync_mode": false,
      "num_images": 1,
      "output_format": "jpeg",
      "safety_tolerance": "2",
      "enhance_prompt": false,
      "aspect_ratio": "1:1"
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

## Related

* [FLUX.1 Kontext \[pro\]](/model-api-reference/image-generation-api/flux.1-kontext) — Image Generation

## Limitations

* `guidance_scale` range: 1 to 20
* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`, `6`
