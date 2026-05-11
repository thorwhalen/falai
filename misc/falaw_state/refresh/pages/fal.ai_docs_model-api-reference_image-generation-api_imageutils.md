> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Imageutils API

> API reference for Imageutils. Remove the background from an image.

<Tabs>
  <Tab title="Rembg">
    **Endpoint:** `POST https://fal.run/fal-ai/imageutils/rembg`
    **Endpoint ID:** `fal-ai/imageutils/rembg`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/imageutils/rembg/playground">
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
          "fal-ai/imageutils/rembg",
          arguments={
              "image_url": "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/imageutils/rembg", {
        input: {
            image_url: "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg"
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
        --url https://fal.run/fal-ai/imageutils/rembg \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      Input image url.
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="crop_to_bbox" type="boolean" default="false">
      If set to true, the resulting image be cropped to a bounding box around the subject
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      Background removed image.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg",
      "sync_mode": false,
      "crop_to_bbox": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      }
    }
    ```
  </Tab>

  <Tab title="Depth">
    **Endpoint:** `POST https://fal.run/fal-ai/imageutils/depth`
    **Endpoint ID:** `fal-ai/imageutils/depth`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/imageutils/depth/playground">
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
          "fal-ai/imageutils/depth",
          arguments={
              "image_url": "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/imageutils/depth", {
        input: {
            image_url: "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg"
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
        --url https://fal.run/fal-ai/imageutils/depth \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      Input image url.
    </ParamField>

    <ParamField body="a" type="float" default="6.283185307179586">
      a Default value: `6.283185307179586`
    </ParamField>

    <ParamField body="bg_th" type="float" default="0.1">
      bg\_th Default value: `0.1`
    </ParamField>

    <ParamField body="depth_and_normal" type="boolean" default="false">
      depth\_and\_normal
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      The depth map.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg",
      "a": 6.283185307179586,
      "bg_th": 0.1,
      "depth_and_normal": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      }
    }
    ```
  </Tab>

  <Tab title="Marigold Depth">
    **Endpoint:** `POST https://fal.run/fal-ai/imageutils/marigold-depth`
    **Endpoint ID:** `fal-ai/imageutils/marigold-depth`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/imageutils/marigold-depth/playground">
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
          "fal-ai/imageutils/marigold-depth",
          arguments={
              "image_url": "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/imageutils/marigold-depth", {
        input: {
            image_url: "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg"
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
        --url https://fal.run/fal-ai/imageutils/marigold-depth \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg"
      }'
      ```
    </CodeGroup>

    ## Examples

    <Frame>
      <img src="https://v3.fal.media/files/rabbit/N0GgfUE25qCp850ji09pY_209fe579ff1045889f7f3513e5a6401f.png" alt="Example output from Marigold Depth Estimation" />
    </Frame>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      Input image url.
    </ParamField>

    <ParamField body="num_inference_steps" type="integer" default="10">
      Number of denoising steps. Defaults to `10`. The higher the number, the more accurate the result, but the slower the inference. Default value: `10`

      Range: `2` to `50`
    </ParamField>

    <ParamField body="ensemble_size" type="integer" default="10">
      Number of predictions to average over. Defaults to `10`. The higher the number, the more accurate the result, but the slower the inference. Default value: `10`

      Range: `2` to `50`
    </ParamField>

    <ParamField body="processing_res" type="integer" default="0">
      Maximum processing resolution. Defaults `0` which means it uses the size of the input image.

      Range: `0` to `2048`
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      The depth map.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://storage.googleapis.com/falserverless/model_tests/remove_background/elephant.jpg",
      "num_inference_steps": 10,
      "ensemble_size": 10,
      "processing_res": 0
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      }
    }
    ```
  </Tab>
</Tabs>

## Limitations

* `num_inference_steps` range: 2 to 50
* `ensemble_size` range: 2 to 50
* `processing_res` range: 0 to 2048
