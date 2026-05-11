> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedvr Upscale Image API

> API reference for Seedvr Upscale Image. Use SeedVR2 to upscale your images

<Tabs>
  <Tab title="Image">
    **Endpoint:** `POST https://fal.run/fal-ai/seedvr/upscale/image`
    **Endpoint ID:** `fal-ai/seedvr/upscale/image`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/seedvr/upscale/image/playground">
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
          "fal-ai/seedvr/upscale/image",
          arguments={
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/seedvr2/image_in.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/seedvr/upscale/image", {
        input: {
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/seedvr2/image_in.png"
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
        --url https://fal.run/fal-ai/seedvr/upscale/image \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/seedvr2/image_in.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The input image to be processed
    </ParamField>

    <ParamField body="upscale_mode" type="UpscaleModeEnum" default="factor">
      The mode to use for the upscale. If 'target', the upscale factor will be calculated based on the target resolution. If 'factor', the upscale factor will be used directly. Default value: `"factor"`

      Possible values: `target`, `factor`
    </ParamField>

    <ParamField body="upscale_factor" type="float" default="2">
      Upscaling factor to be used. Will multiply the dimensions with this factor when `upscale_mode` is `factor`. Default value: `2`

      Range: `1` to `10`
    </ParamField>

    <ParamField body="target_resolution" type="TargetResolutionEnum" default="1080p">
      The target resolution to upscale to when `upscale_mode` is `target`. Default value: `"1080p"`

      Possible values: `720p`, `1080p`, `1440p`, `2160p`
    </ParamField>

    <ParamField body="seed" type="integer">
      The random seed used for the generation process.
    </ParamField>

    <ParamField body="noise_scale" type="float" default="0.1">
      The noise scale to use for the generation process. Default value: `0.1`

      Range: `0` to `1`, step: `0.001`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="jpg">
      The format of the output image. Default value: `"jpg"`

      Possible values: `png`, `jpg`, `webp`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="ImageFile" required>
      Upscaled image file after processing
    </ParamField>

    <ParamField body="seed" type="integer" required>
      The random seed used for the generation process.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/seedvr2/image_in.png",
      "upscale_mode": "factor",
      "upscale_factor": 2,
      "target_resolution": "1080p",
      "noise_scale": 0.1,
      "output_format": "jpg",
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "content_type": "image/png",
        "url": "https://storage.googleapis.com/falserverless/example_outputs/seedvr2/image_out.png"
      }
    }
    ```
  </Tab>

  <Tab title="Seamless">
    **Endpoint:** `POST https://fal.run/fal-ai/seedvr/upscale/image/seamless`
    **Endpoint ID:** `fal-ai/seedvr/upscale/image/seamless`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/seedvr/upscale/image/seamless/playground">
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
          "fal-ai/seedvr/upscale/image/seamless",
          arguments={
              "image_url": "https://v3b.fal.media/files/b/0a93eb33/dQ_ZwLyeu8P2UJYsa8RDW_seamless_image_in.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/seedvr/upscale/image/seamless", {
        input: {
            image_url: "https://v3b.fal.media/files/b/0a93eb33/dQ_ZwLyeu8P2UJYsa8RDW_seamless_image_in.png"
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
        --url https://fal.run/fal-ai/seedvr/upscale/image/seamless \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://v3b.fal.media/files/b/0a93eb33/dQ_ZwLyeu8P2UJYsa8RDW_seamless_image_in.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The input image to be processed
    </ParamField>

    <ParamField body="upscale_mode" type="UpscaleModeEnum" default="factor">
      The mode to use for the upscale. If 'target', the upscale factor will be calculated based on the target resolution. If 'factor', the upscale factor will be used directly. Default value: `"factor"`

      Possible values: `target`, `factor`
    </ParamField>

    <ParamField body="upscale_factor" type="float" default="2">
      Upscaling factor to be used. Will multiply the dimensions with this factor when `upscale_mode` is `factor`. Default value: `2`

      Range: `1` to `10`
    </ParamField>

    <ParamField body="target_resolution" type="TargetResolutionEnum" default="1080p">
      The target resolution to upscale to when `upscale_mode` is `target`. Default value: `"1080p"`

      Possible values: `720p`, `1080p`, `1440p`, `2160p`
    </ParamField>

    <ParamField body="seed" type="integer">
      The random seed used for the generation process.
    </ParamField>

    <ParamField body="noise_scale" type="float" default="0.1">
      The noise scale to use for the generation process. Default value: `0.1`

      Range: `0` to `1`, step: `0.001`
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="png">
      The format of the output image. Default value: `"png"`

      Possible values: `png`, `jpeg`, `webp`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="ImageFile" required>
      Upscaled image file after processing
    </ParamField>

    <ParamField body="seed" type="integer" required>
      The random seed used for the generation process.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://v3b.fal.media/files/b/0a93eb33/dQ_ZwLyeu8P2UJYsa8RDW_seamless_image_in.png",
      "upscale_mode": "factor",
      "upscale_factor": 2,
      "target_resolution": "1080p",
      "noise_scale": 0.1,
      "enable_safety_checker": true,
      "output_format": "png",
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "content_type": "image/png",
        "url": "https://storage.googleapis.com/falserverless/example_outputs/seedvr2/image_out.png"
      }
    }
    ```
  </Tab>
</Tabs>

## Related

* [SeedVR2](/model-api-reference/video-generation-api/seedvr2) — Video Generation

## Limitations

* `upscale_mode` restricted to: `target`, `factor`
* `upscale_factor` range: 1 to 10
* `target_resolution` restricted to: `720p`, `1080p`, `1440p`, `2160p`
* `noise_scale` range: 0 to 1 (step 0.001)
* `output_format` restricted to: `png`, `jpg`, `webp`
* `output_format` restricted to: `png`, `jpeg`, `webp`
* Content moderation via safety checker
