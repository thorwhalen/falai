> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux Lora API

> API reference for Flux Lora. Super fast endpoint for the FLUX.1 [dev] model with LoRA support, enabling rapid and high-quality image generation using pre-trained LoRA adaptations for personalization, 

<Tabs>
  <Tab title="Flux Lora">
    **Endpoint:** `POST https://fal.run/fal-ai/flux-lora`
    **Endpoint ID:** `fal-ai/flux-lora`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-lora/playground">
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
          "fal-ai/flux-lora",
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

      const result = await fal.subscribe("fal-ai/flux-lora", {
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
        --url https://fal.run/fal-ai/flux-lora \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"FLUX\" is painted over it in big, white brush strokes with visible texture."
      }'
      ```
    </CodeGroup>

    ## Examples

    > Gal gadot, wearing jacket and tie

    <Frame>
      <img src="https://fal.media/files/penguin/hHhmyazpcSq_W8c0TzXl4_14015fe83e3541848e6b2e2e1c7e4968.jpg" alt="Generated image: Gal gadot, wearing jacket and tie" />
    </Frame>

    > a trtcrd of a person on a computer, on the computer you see a meme being made with an ancient looking trollface, "the shitposter" arcana, in the style of TOK a trtcrd, tarot style

    <Frame>
      <img src="https://fal.media/files/penguin/82xiDnqE_nRov7s5GuOAM_2654d4ddc62e4e2490207d2d8f115583.jpg" alt="Generated image: a trtcrd of a person on a computer, on the computer you see a meme being made wi" />
    </Frame>

    > two warriors fighting, in the middle, white background

    <Frame>
      <img src="https://fal.media/files/tiger/j48DGzlaA5ai3CmjDYkJ5_1b5ad1d0b6974989a196738d8c01211f.jpg" alt="Generated image: two warriors fighting, in the middle, white background" />
    </Frame>

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

    <ParamField body="loras" type="list<LoraWeight>" default="">
      The LoRAs to use for the image generation. You can use any number of LoRAs
      and they will be merged together to generate the final image.
    </ParamField>

    <ParamField body="guidance_scale" type="float" default="3.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `3.5`

      Range: `0` to `35`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      The number of images to generate. This is always set to 1 for streaming output. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`
    </ParamField>

    <ParamField body="acceleration" type="AccelerationEnum" default="none">
      Acceleration level for image generation. 'regular' balances speed and quality. Default value: `"none"`

      Possible values: `none`, `regular`
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
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
      "image_size": "landscape_4_3",
      "num_inference_steps": 28,
      "guidance_scale": 3.5,
      "sync_mode": false,
      "num_images": 1,
      "enable_safety_checker": true,
      "output_format": "jpeg",
      "acceleration": "none"
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

  <Tab title="Image To Image">
    **Endpoint:** `POST https://fal.run/fal-ai/flux-lora/image-to-image`
    **Endpoint ID:** `fal-ai/flux-lora/image-to-image`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-lora/image-to-image/playground">
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
          "fal-ai/flux-lora/image-to-image",
          arguments={
              "prompt": "A photo of a lion sitting on a stone bench",
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/dog.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/flux-lora/image-to-image", {
        input: {
            prompt: "A photo of a lion sitting on a stone bench",
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/dog.png"
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
        --url https://fal.run/fal-ai/flux-lora/image-to-image \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A photo of a lion sitting on a stone bench",
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/dog.png"
      }'
      ```
    </CodeGroup>

    ## Examples

    > Gal gadot looking at the camera

    <Frame>
      <img src="https://fal.media/files/penguin/W1MCCCS1mShfWJcGUadZ7_0feb0b615bb549ed9cd968069938e5e5.jpg" alt="Generated image: Gal gadot looking at the camera" />
    </Frame>

    > Bald man giving conference talk

    <Frame>
      <img src="https://fal.media/files/kangaroo/YWwOfoIP2uNd1C0_Smnd8_62166b4abd164f9794b651038c86c012.jpg" alt="Generated image: Bald man giving conference talk" />
    </Frame>

    > eh\_style, The image showcases a tiger

    <Frame>
      <img src="https://fal.media/files/zebra/--Ktg0V5aJPxKUFvHfyo1_a4b9ae4678a045189c1f4b5f9742511f.jpg" alt="Generated image: eh_style, The image showcases a tiger" />
    </Frame>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to generate an image from.
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum">
      The size of the generated image.

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

    <ParamField body="loras" type="list<LoraWeight>" default="">
      The LoRAs to use for the image generation. You can use any number of LoRAs
      and they will be merged together to generate the final image.
    </ParamField>

    <ParamField body="guidance_scale" type="float" default="3.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `3.5`

      Range: `0` to `35`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      The number of images to generate. This is always set to 1 for streaming output. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`
    </ParamField>

    <ParamField body="acceleration" type="AccelerationEnum" default="none">
      Acceleration level for image generation. 'regular' balances speed and quality. Default value: `"none"`

      Possible values: `none`, `regular`
    </ParamField>

    <ParamField body="image_url" type="string" required>
      URL of image to use for inpainting. or img2img
    </ParamField>

    <ParamField body="strength" type="float" default="0.85">
      The strength to use for inpainting/image-to-image. Only used if the image\_url is provided. 1.0 is completely remakes the image while 0.0 preserves the original. Default value: `0.85`

      Range: `0.01` to `1`
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
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
      "prompt": "A photo of a lion sitting on a stone bench",
      "num_inference_steps": 28,
      "guidance_scale": 3.5,
      "sync_mode": false,
      "num_images": 1,
      "enable_safety_checker": true,
      "output_format": "jpeg",
      "acceleration": "none",
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/dog.png",
      "strength": 0.85
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

  <Tab title="Inpainting">
    **Endpoint:** `POST https://fal.run/fal-ai/flux-lora/inpainting`
    **Endpoint ID:** `fal-ai/flux-lora/inpainting`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-lora/inpainting/playground">
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
          "fal-ai/flux-lora/inpainting",
          arguments={
              "prompt": "A photo of a lion sitting on a stone bench",
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/dog.png",
              "mask_url": "https://storage.googleapis.com/falserverless/example_inputs/dog_mask.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/flux-lora/inpainting", {
        input: {
            prompt: "A photo of a lion sitting on a stone bench",
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/dog.png",
            mask_url: "https://storage.googleapis.com/falserverless/example_inputs/dog_mask.png"
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
        --url https://fal.run/fal-ai/flux-lora/inpainting \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A photo of a lion sitting on a stone bench",
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/dog.png",
        "mask_url": "https://storage.googleapis.com/falserverless/example_inputs/dog_mask.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to generate an image from.
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum">
      The size of the generated image.

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

    <ParamField body="loras" type="list<LoraWeight>" default="">
      The LoRAs to use for the image generation. You can use any number of LoRAs
      and they will be merged together to generate the final image.
    </ParamField>

    <ParamField body="guidance_scale" type="float" default="3.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `3.5`

      Range: `0` to `35`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      The number of images to generate. This is always set to 1 for streaming output. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`
    </ParamField>

    <ParamField body="acceleration" type="AccelerationEnum" default="none">
      Acceleration level for image generation. 'regular' balances speed and quality. Default value: `"none"`

      Possible values: `none`, `regular`
    </ParamField>

    <ParamField body="image_url" type="string" required>
      URL of image to use for inpainting. or img2img
    </ParamField>

    <ParamField body="strength" type="float" default="0.85">
      The strength to use for inpainting/image-to-image. Only used if the image\_url is provided. 1.0 is completely remakes the image while 0.0 preserves the original. Default value: `0.85`

      Range: `0.01` to `1`
    </ParamField>

    <ParamField body="mask_url" type="string" required>
      The mask to area to Inpaint in.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
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
      "prompt": "A photo of a lion sitting on a stone bench",
      "num_inference_steps": 28,
      "guidance_scale": 3.5,
      "sync_mode": false,
      "num_images": 1,
      "enable_safety_checker": true,
      "output_format": "jpeg",
      "acceleration": "none",
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/dog.png",
      "strength": 0.85,
      "mask_url": "https://storage.googleapis.com/falserverless/example_inputs/dog_mask.png"
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

  <Tab title="Stream">
    **Endpoint:** `POST https://fal.run/fal-ai/flux-lora/stream`
    **Endpoint ID:** `fal-ai/flux-lora/stream`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-lora/stream/playground">
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
          "fal-ai/flux-lora/stream",
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

      const result = await fal.subscribe("fal-ai/flux-lora/stream", {
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
        --url https://fal.run/fal-ai/flux-lora/stream \
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

    <ParamField body="loras" type="list<LoraWeight>" default="">
      The LoRAs to use for the image generation. You can use any number of LoRAs
      and they will be merged together to generate the final image.
    </ParamField>

    <ParamField body="guidance_scale" type="float" default="3.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `3.5`

      Range: `0` to `35`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      The number of images to generate. This is always set to 1 for streaming output. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`
    </ParamField>

    <ParamField body="acceleration" type="AccelerationEnum" default="none">
      Acceleration level for image generation. 'regular' balances speed and quality. Default value: `"none"`

      Possible values: `none`, `regular`
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
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
      "image_size": "landscape_4_3",
      "num_inference_steps": 28,
      "guidance_scale": 3.5,
      "sync_mode": false,
      "num_images": 1,
      "enable_safety_checker": true,
      "output_format": "jpeg",
      "acceleration": "none"
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

## FLUX.1 \[dev] with LoRAs - High-Performance Text-to-Image Generation

Transform your text descriptions into stunning images with FLUX.1 \[dev] with LoRA support, enabling rapid and high-quality image generation using pre-trained LoRA adaptations for personalization, specific styles, brand identities, and product-specific outputs.

### Overview

FLUX.1 \[dev] with LoRAs is a super fast endpoint powered by a 12 billion parameter flow transformer architecture that delivers exceptional image generation capabilities with LoRA support. Whether you're creating personalized content, generating marketing assets with specific styles, or exploring creative ideas with custom adaptations, FLUX LoRA provides the perfect balance of speed, quality, and customization.

### Key Features

Experience industry-leading capabilities designed for both personal and commercial projects:

#### Advanced LoRA Integration

Transform your vision with precise control over image generation through pre-trained LoRA adaptations. Apply custom styles, brand identities, and personalized elements seamlessly.

#### Lightning-Fast Generation

Generate high-quality images in seconds with our optimized inference pipeline, leveraging the power of the FLUX.1 \[dev] model architecture.

#### Commercial-Ready Output

All generated images are cleared for commercial use, making FLUX LoRA ideal for professional creative workflows and business applications.

### Getting Started

Getting started with FLUX LoRA is straightforward. Here's how to begin:

1. **Install the SDK**
   Choose your preferred language:

```bash theme={null}
# For JavaScript/TypeScript
npm install --save @fal-ai/client

# For Python
pip install fal-client
```

2. **Configure Authentication**

```typescript theme={null}
import { fal } from '@fal-ai/client'

fal.config({
  credentials: 'YOUR_FAL_KEY'
})
```

3. **Generate Your First Image**

```typescript theme={null}
const result = await fal.subscribe('fal-ai/flux-lora', {
  input: {
    prompt: 'A serene landscape at sunset, painted in watercolor style',
    loras: [
      {
        path: 'https://example.com/watercolor-style-lora.safetensors',
        scale: 1.0
      }
    ]
  }
})
```

### Best Practices

Maximize your results with these proven approaches:

#### Prompt Engineering

Write detailed, specific prompts that describe both content and style. For example, instead of "a cat," try "a Persian cat sitting in a sunlit window, painted in soft watercolor style."

#### LoRA Configuration

* Use appropriate LoRA scales (typically 0.5-1.5) to balance style application
* Combine multiple LoRAs for complex styling effects
* Test different LoRA combinations for unique results

#### Parameter Optimization

Start with default parameters and adjust based on your needs. The model is optimized for rapid generation while maintaining high quality output.

### Technical Specifications

#### Model Architecture

* 12 billion parameter FLUX.1 \[dev] model
* Flow transformer architecture
* LoRA adaptation support
* Support for multiple image dimensions
* Commercial use licensing

#### Input Capabilities

* Text prompts with detailed descriptions
* Multiple LoRA model support
* Negative prompts for content exclusion
* Resolution control and customization

#### Performance

* Super fast inference optimized for speed
* Concurrent request handling
* Reliable uptime and availability

### API Reference

The FLUX LoRA API accepts the following core parameters:

```typescript theme={null}
interface FluxLoRAParameters {
  prompt: string;              // Your detailed text description
  loras?: Array<{             // LoRA models to apply
    path: string;             // URL to LoRA model file
    scale: number;            // Application strength (0-2)
  }>;
  negative_prompt?: string;    // Elements to avoid in generation
  width?: number;             // Output image width
  height?: number;            // Output image height
  num_inference_steps?: number; // Generation steps
  guidance_scale?: number;     // Prompt adherence strength
  seed?: number;              // For reproducible results
}
```

### Pricing and Usage

Your request will cost \$0.035 per megapixel. Images are billed by rounding up to the nearest megapixel. Our transparent, usage-based pricing scales with your needs:

* Pay-per-use model based on image resolution
* No subscription fees or minimum commitments
* Commercial usage rights included
* Competitive rates for high-volume usage

[View detailed pricing](https://fal.ai/pricing) or [contact sales](mailto:support@fal.ai) for enterprise solutions.

### Support and Resources

Take advantage of our comprehensive support system:

#### Documentation

Access detailed guides and reference materials at our documentation portal at [https://docs.fal.ai/](https://docs.fal.ai/)

#### Community Support

Join our active developer community for tips, tricks, and troubleshooting help.

#### Professional Support

Enterprise users receive dedicated support channels and priority assistance.

Ready to transform your creative workflow with FLUX LoRA? Sign up for an API key and start generating stunning, personalized images today. Visit our dashboard to begin your journey with one of the most powerful text-to-image models with LoRA support available.

## Related

* [FLUX.1 \[dev\] with LoRAs](/model-api-reference/image-generation-api/flux.1-with-loras) — Image Generation
* [FLUX.1 \[dev\] Inpainting with LoRAs](/model-api-reference/image-generation-api/flux.1-inpainting-with-loras) — Image Generation

## Limitations

* `image_size` restricted to: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
* `num_inference_steps` range: 1 to 50
* `guidance_scale` range: 0 to 35
* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`
* `acceleration` restricted to: `none`, `regular`
* Content moderation via safety checker
* `strength` range: 0.01 to 1
