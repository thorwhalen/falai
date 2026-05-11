> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Xai Grok Imagine Image API

> API reference for Xai Grok Imagine Image. Generate highly aesthetic images with xAI's Grok Imagine Image generation model.

<Tabs>
  <Tab title="Grok Imagine Image">
    **Endpoint:** `POST https://fal.run/xai/grok-imagine-image`
    **Endpoint ID:** `xai/grok-imagine-image`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/xai/grok-imagine-image/playground">
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
          "xai/grok-imagine-image",
          arguments={
              "prompt": "Abstract human silhouette, golden particles ready to burst outward representing joy, data visualization style, emotional expression through particles, artistic scientific"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("xai/grok-imagine-image", {
        input: {
            prompt: "Abstract human silhouette, golden particles ready to burst outward representing joy, data visualization style, emotional expression through particles, artistic scientific"
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
        --url https://fal.run/xai/grok-imagine-image \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Abstract human silhouette, golden particles ready to burst outward representing joy, data visualization style, emotional expression through particles, artistic scientific"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      Text description of the desired image.
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      Number of images to generate. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="1:1">
      Aspect ratio of the generated image. Default value: `"1:1"`

      Possible values: `2:1`, `20:9`, `19.5:9`, `16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16`, `9:19.5`, `9:20`, `1:2`
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="1k">
      Resolution of the generated image. `1k` for standard resolution, `2k` for high resolution. Default value: `"1k"`

      Possible values: `1k`, `2k`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`, `webp`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<ImageFile>" required>
      The URL of the generated image.
    </ParamField>

    <ParamField body="revised_prompt" type="string" required>
      The enhanced prompt that was used to generate the image.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Abstract human silhouette, golden particles ready to burst outward representing joy, data visualization style, emotional expression through particles, artistic scientific",
      "num_images": 1,
      "aspect_ratio": "1:1",
      "resolution": "1k",
      "output_format": "jpeg",
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://v3b.fal.media/files/b/0a8b90b7/9avg_nKJmcVinjQHJR_Ja.jpg"
        }
      ],
      "revised_prompt": ""
    }
    ```
  </Tab>

  <Tab title="Edit">
    **Endpoint:** `POST https://fal.run/xai/grok-imagine-image/edit`
    **Endpoint ID:** `xai/grok-imagine-image/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/xai/grok-imagine-image/edit/playground">
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
          "xai/grok-imagine-image/edit",
          arguments={
              "prompt": "Make this scene more realistic but still keep the game vibes"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("xai/grok-imagine-image/edit", {
        input: {
            prompt: "Make this scene more realistic but still keep the game vibes"
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
        --url https://fal.run/xai/grok-imagine-image/edit \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Make this scene more realistic but still keep the game vibes"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      Text description of the desired image.
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      Number of images to generate. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="1k">
      Resolution of the generated image. `1k` for standard resolution, `2k` for high resolution. Default value: `"1k"`

      Possible values: `1k`, `2k`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`, `webp`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="image_urls" type="list<string>">
      List of URLs of the images to edit. A maximum of 3 images are supported.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<ImageFile>" required>
      The URL of the edited image.
    </ParamField>

    <ParamField body="revised_prompt" type="string" required>
      The enhanced prompt that was used to generate the image.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Make this scene more realistic but still keep the game vibes",
      "num_images": 1,
      "resolution": "1k",
      "output_format": "jpeg",
      "sync_mode": false,
      "image_urls": [
        "https://v3b.fal.media/files/b/0a8b911d/Abk8vStrvmSPlzUqI_NN3_image_043.png"
      ]
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://v3b.fal.media/files/b/0a8b911d/XMqiVoO2ECXUZEUYmPl2l.jpg"
        }
      ],
      "revised_prompt": ""
    }
    ```
  </Tab>
</Tabs>

## Related

* [Grok Imagine Image](/model-api-reference/image-generation-api/grok-imagine-image) — Image Generation

## Limitations

* `num_images` range: 1 to 4
* `resolution` restricted to: `1k`, `2k`
* `output_format` restricted to: `jpeg`, `png`, `webp`
