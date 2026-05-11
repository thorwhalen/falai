> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Nano Banana API

> API reference for Nano Banana. Google's famous original image generation and editing model

<Tabs>
  <Tab title="Nano Banana">
    **Endpoint:** `POST https://fal.run/fal-ai/nano-banana`
    **Endpoint ID:** `fal-ai/nano-banana`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/nano-banana/playground">
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
          "fal-ai/nano-banana",
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

      const result = await fal.subscribe("fal-ai/nano-banana", {
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
        --url https://fal.run/fal-ai/nano-banana \
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

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="1:1">
      The aspect ratio of the generated image. Default value: `"1:1"`

      Possible values: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`
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

    <ParamField body="limit_generations" type="boolean" default="false">
      Experimental parameter to limit the number of generations from each round of prompting to 1. Set to `True` to to disregard any instructions in the prompt regarding the number of images to generate.
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
      "limit_generations": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "content_type": "image/png",
          "file_name": "nano-banana-t2i-output.png",
          "url": "https://storage.googleapis.com/falserverless/example_outputs/nano-banana-t2i-output.png"
        }
      ],
      "description": ""
    }
    ```
  </Tab>

  <Tab title="Edit">
    **Endpoint:** `POST https://fal.run/fal-ai/nano-banana/edit`
    **Endpoint ID:** `fal-ai/nano-banana/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/nano-banana/edit/playground">
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
          "fal-ai/nano-banana/edit",
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

      const result = await fal.subscribe("fal-ai/nano-banana/edit", {
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
        --url https://fal.run/fal-ai/nano-banana/edit \
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
      <img src="https://v3b.fal.media/files/b/0a95c085/S0ExtNZpsp_6xygCJ3MKG_Bj98CiYt.png" alt="Generated image: make a photo of the man driving the car down the california coastline" />
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

    <ParamField body="limit_generations" type="boolean" default="false">
      Experimental parameter to limit the number of generations from each round of prompting to 1. Set to `True` to to disregard any instructions in the prompt regarding the number of images to generate.
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
      "limit_generations": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "content_type": "image/png",
          "file_name": "nano-banana-multi-edit-output.png",
          "url": "https://storage.googleapis.com/falserverless/example_outputs/nano-banana-multi-edit-output.png"
        }
      ],
      "description": ""
    }
    ```
  </Tab>
</Tabs>

## Related

* [Nano Banana](/model-api-reference/image-generation-api/nano-banana) — Image Generation

## Limitations

* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`, `webp`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`, `6`
