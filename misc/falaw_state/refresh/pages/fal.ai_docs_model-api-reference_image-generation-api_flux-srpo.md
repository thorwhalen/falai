> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux Srpo API

> API reference for Flux Srpo. FLUX.1 SRPO [dev] is a 12 billion parameter flow transformer that generates high-quality images from text with incredible aesthetics. It is suitable for personal and comme

<Tabs>
  <Tab title="Srpo">
    **Endpoint:** `POST https://fal.run/fal-ai/flux/srpo`
    **Endpoint ID:** `fal-ai/flux/srpo`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux/srpo/playground">
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
          "fal-ai/flux/srpo",
          arguments={
              "prompt": "Mountain guide, sturdy build, wilderness wisdom, alert gaze, technical outdoor gear with rope coils, snow-capped peaks background, crisp mountain lighting, leading pose, wind-swept hair with full beard, weather-worn face with quiet confidence, alpine expert presence"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/flux/srpo", {
        input: {
            prompt: "Mountain guide, sturdy build, wilderness wisdom, alert gaze, technical outdoor gear with rope coils, snow-capped peaks background, crisp mountain lighting, leading pose, wind-swept hair with full beard, weather-worn face with quiet confidence, alpine expert presence"
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
        --url https://fal.run/fal-ai/flux/srpo \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Mountain guide, sturdy build, wilderness wisdom, alert gaze, technical outdoor gear with rope coils, snow-capped peaks background, crisp mountain lighting, leading pose, wind-swept hair with full beard, weather-worn face with quiet confidence, alpine expert presence"
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

    <ParamField body="guidance_scale" type="float" default="4.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `4.5`

      Range: `1` to `20`
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

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`
    </ParamField>

    <ParamField body="acceleration" type="AccelerationEnum" default="none">
      The speed of the generation. The higher the speed, the faster the generation. Default value: `"none"`

      Possible values: `none`, `regular`, `high`
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
      The generated images.
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
      "prompt": "Mountain guide, sturdy build, wilderness wisdom, alert gaze, technical outdoor gear with rope coils, snow-capped peaks background, crisp mountain lighting, leading pose, wind-swept hair with full beard, weather-worn face with quiet confidence, alpine expert presence",
      "image_size": "landscape_4_3",
      "num_inference_steps": 28,
      "guidance_scale": 4.5,
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
          "content_type": "image/jpeg",
          "height": 768,
          "url": "https://storage.googleapis.com/falserverless/example_outputs/flux-srpo-output.jpeg",
          "width": 1024
        }
      ],
      "prompt": ""
    }
    ```
  </Tab>

  <Tab title="Image To Image">
    **Endpoint:** `POST https://fal.run/fal-ai/flux/srpo/image-to-image`
    **Endpoint ID:** `fal-ai/flux/srpo/image-to-image`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux/srpo/image-to-image/playground">
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
          "fal-ai/flux/srpo/image-to-image",
          arguments={
              "image_url": "https://fal.media/files/koala/Chls9L2ZnvuipUTEwlnJC.png",
              "prompt": "A cat dressed as a wizard with a background of a mystic forest."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/flux/srpo/image-to-image", {
        input: {
            image_url: "https://fal.media/files/koala/Chls9L2ZnvuipUTEwlnJC.png",
            prompt: "A cat dressed as a wizard with a background of a mystic forest."
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
        --url https://fal.run/fal-ai/flux/srpo/image-to-image \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://fal.media/files/koala/Chls9L2ZnvuipUTEwlnJC.png",
        "prompt": "A cat dressed as a wizard with a background of a mystic forest."
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The URL of the image to generate an image from.
    </ParamField>

    <ParamField body="strength" type="float" default="0.95">
      The strength of the initial image. Higher strength values are better for this model. Default value: `0.95`

      Range: `0.01` to `1`
    </ParamField>

    <ParamField body="num_inference_steps" type="integer" default="40">
      The number of inference steps to perform. Default value: `40`

      Range: `10` to `50`
    </ParamField>

    <ParamField body="prompt" type="string" required>
      The prompt to generate an image from.
    </ParamField>

    <ParamField body="seed" type="integer">
      The same seed and the same prompt given to the same version of the model
      will output the same image every time.
    </ParamField>

    <ParamField body="guidance_scale" type="float" default="4.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `4.5`

      Range: `1` to `20`
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

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`
    </ParamField>

    <ParamField body="acceleration" type="AccelerationEnum" default="none">
      The speed of the generation. The higher the speed, the faster the generation. Default value: `"none"`

      Possible values: `none`, `regular`, `high`
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
      "image_url": "https://fal.media/files/koala/Chls9L2ZnvuipUTEwlnJC.png",
      "strength": 0.95,
      "num_inference_steps": 40,
      "prompt": "A cat dressed as a wizard with a background of a mystic forest.",
      "guidance_scale": 4.5,
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

## Related

* [FLUX.1 SRPO \[dev\]](/model-api-reference/image-generation-api/flux.1-srpo) — Image Generation

## Limitations

* `image_size` restricted to: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
* `num_inference_steps` range: 1 to 50
* `guidance_scale` range: 1 to 20
* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`
* `acceleration` restricted to: `none`, `regular`, `high`
* Content moderation via safety checker
* `strength` range: 0.01 to 1
* `num_inference_steps` range: 10 to 50
