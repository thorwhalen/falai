> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Gpt Image 1.5 API

> API reference for Gpt Image 1.5. GPT Image 1.5 generates high-fidelity images with strong prompt adherence, preserving composition, lighting, and fine-grained detail.

<Tabs>
  <Tab title="Gpt Image 1.5">
    **Endpoint:** `POST https://fal.run/fal-ai/gpt-image-1.5`
    **Endpoint ID:** `fal-ai/gpt-image-1.5`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/gpt-image-1.5/playground">
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
          "fal-ai/gpt-image-1.5",
          arguments={
              "prompt": "create a realistic image taken with iphone at these coordinates 41°43′32″N 49°56′49″W 15 April 1912"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/gpt-image-1.5", {
        input: {
            prompt: "create a realistic image taken with iphone at these coordinates 41°43′32″N 49°56′49″W 15 April 1912"
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
        --url https://fal.run/fal-ai/gpt-image-1.5 \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "create a realistic image taken with iphone at these coordinates 41°43′32″N 49°56′49″W 15 April 1912"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt for image generation
    </ParamField>

    <ParamField body="image_size" type="ImageSizeEnum" default="1024x1024">
      Aspect ratio for the generated image Default value: `"1024x1024"`

      Possible values: `1024x1024`, `1536x1024`, `1024x1536`
    </ParamField>

    <ParamField body="background" type="BackgroundEnum" default="auto">
      Background for the generated image Default value: `"auto"`

      Possible values: `auto`, `transparent`, `opaque`
    </ParamField>

    <ParamField body="quality" type="QualityEnum" default="high">
      Quality for the generated image Default value: `"high"`

      Possible values: `low`, `medium`, `high`
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      Number of images to generate Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="png">
      Output format for the images Default value: `"png"`

      Possible values: `jpeg`, `png`, `webp`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<ImageFile>" required>
      The generated images.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "create a realistic image taken with iphone at these coordinates 41°43′32″N 49°56′49″W 15 April 1912",
      "image_size": "1024x1024",
      "background": "auto",
      "quality": "high",
      "num_images": 1,
      "output_format": "png",
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "content_type": "image/png",
          "file_name": "EnWrO3XWjPE0nxBDpaQrj.png",
          "height": 1024,
          "url": "https://v3b.fal.media/files/b/0a869129/EnWrO3XWjPE0nxBDpaQrj.png",
          "width": 1024
        }
      ]
    }
    ```
  </Tab>

  <Tab title="Edit">
    **Endpoint:** `POST https://fal.run/fal-ai/gpt-image-1.5/edit`
    **Endpoint ID:** `fal-ai/gpt-image-1.5/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/gpt-image-1.5/edit/playground">
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
          "fal-ai/gpt-image-1.5/edit",
          arguments={
              "prompt": "Same workers, same beam, same lunch boxes - but they're all on their phones now. One is taking a selfie. One is on a call looking annoyed. Same danger, new priorities. A hard hat has AirPods.",
              "image_urls": [
                  "https://v3b.fal.media/files/b/0a8691af/9Se_1_VX1wzTjjTOpWbs9_bb39c2eb-1a41-4749-b1d0-cf134abc8bbf.png"
              ]
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/gpt-image-1.5/edit", {
        input: {
            prompt: "Same workers, same beam, same lunch boxes - but they're all on their phones now. One is taking a selfie. One is on a call looking annoyed. Same danger, new priorities. A hard hat has AirPods.",
            image_urls: [
              "https://v3b.fal.media/files/b/0a8691af/9Se_1_VX1wzTjjTOpWbs9_bb39c2eb-1a41-4749-b1d0-cf134abc8bbf.png"
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
        --url https://fal.run/fal-ai/gpt-image-1.5/edit \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Same workers, same beam, same lunch boxes - but they'\''re all on their phones now. One is taking a selfie. One is on a call looking annoyed. Same danger, new priorities. A hard hat has AirPods.",
        "image_urls": [
          "https://v3b.fal.media/files/b/0a8691af/9Se_1_VX1wzTjjTOpWbs9_bb39c2eb-1a41-4749-b1d0-cf134abc8bbf.png"
        ]
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt for image generation
    </ParamField>

    <ParamField body="image_urls" type="list<string>" required>
      The URLs of the images to use as a reference for the generation.
    </ParamField>

    <ParamField body="image_size" type="ImageSizeEnum" default="auto">
      Aspect ratio for the generated image Default value: `"auto"`

      Possible values: `auto`, `1024x1024`, `1536x1024`, `1024x1536`
    </ParamField>

    <ParamField body="background" type="BackgroundEnum" default="auto">
      Background for the generated image Default value: `"auto"`

      Possible values: `auto`, `transparent`, `opaque`
    </ParamField>

    <ParamField body="quality" type="QualityEnum" default="high">
      Quality for the generated image Default value: `"high"`

      Possible values: `low`, `medium`, `high`
    </ParamField>

    <ParamField body="input_fidelity" type="InputFidelityEnum" default="high">
      Input fidelity for the generated image Default value: `"high"`

      Possible values: `low`, `high`
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      Number of images to generate Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="png">
      Output format for the images Default value: `"png"`

      Possible values: `jpeg`, `png`, `webp`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="mask_image_url" type="string">
      The URL of the mask image to use for the generation. This indicates what part of the image to edit.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<ImageFile>" required>
      The generated images.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Same workers, same beam, same lunch boxes - but they're all on their phones now. One is taking a selfie. One is on a call looking annoyed. Same danger, new priorities. A hard hat has AirPods.",
      "image_urls": [
        "https://v3b.fal.media/files/b/0a8691af/9Se_1_VX1wzTjjTOpWbs9_bb39c2eb-1a41-4749-b1d0-cf134abc8bbf.png"
      ],
      "image_size": "auto",
      "background": "auto",
      "quality": "high",
      "input_fidelity": "high",
      "num_images": 1,
      "output_format": "png",
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "content_type": "image/png",
          "file_name": "yUt7tifLSbg1WzWWgfj2o.png",
          "height": 1024,
          "url": "https://v3b.fal.media/files/b/0a8691b0/yUt7tifLSbg1WzWWgfj2o.png",
          "width": 1024
        }
      ]
    }
    ```
  </Tab>
</Tabs>

## Related

* [GPT-Image 1.5](/model-api-reference/image-generation-api/gpt-image-1.5) — Image Generation

## Limitations

* `image_size` restricted to: `1024x1024`, `1536x1024`, `1024x1536`
* `background` restricted to: `auto`, `transparent`, `opaque`
* `quality` restricted to: `low`, `medium`, `high`
* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`, `webp`
* `image_size` restricted to: `auto`, `1024x1024`, `1536x1024`, `1024x1536`
* `input_fidelity` restricted to: `low`, `high`
