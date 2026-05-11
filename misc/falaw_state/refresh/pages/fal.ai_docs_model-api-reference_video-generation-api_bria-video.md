> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bria Video API

> API reference for Bria Video. Automatically remove backgrounds from videos -perfect for creating clean, professional content without a green screen.

<Tabs>
  <Tab title="Background Removal">
    **Endpoint:** `POST https://fal.run/bria/video/background-removal`
    **Endpoint ID:** `bria/video/background-removal`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/video/background-removal/playground">
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
          "bria/video/background-removal",
          arguments={
              "video_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/rmbg_tests/videos/5586521-uhd_3840_2160_25fps_original.mp4"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bria/video/background-removal", {
        input: {
            video_url: "https://bria-datasets.s3.us-east-1.amazonaws.com/rmbg_tests/videos/5586521-uhd_3840_2160_25fps_original.mp4"
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
        --url https://fal.run/bria/video/background-removal \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "video_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/rmbg_tests/videos/5586521-uhd_3840_2160_25fps_original.mp4"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="video_url" type="string" required>
      Input video to remove background from. Size should be less than 4000x4000 and duration less than 30s.
    </ParamField>

    <ParamField body="background_color" type="BackgroundColorEnum" default="Black">
      Background color. Options: Transparent, Black, White, Gray, Red, Green, Blue, Yellow, Cyan, Magenta, Orange. Default value: `"Black"`

      Possible values: `Transparent`, `Black`, `White`, `Gray`, `Red`, `Green`, `Blue`, `Yellow`, `Cyan`, `Magenta`, `Orange`
    </ParamField>

    <ParamField body="output_container_and_codec" type="OutputContainerAndCodecEnum" default="webm_vp9">
      Output container and codec. Options: mp4\_h265, mp4\_h264, webm\_vp9, mov\_h265, mov\_proresks, mkv\_h265, mkv\_h264, mkv\_vp9, gif. Default value: `"webm_vp9"`

      Possible values: `mp4_h265`, `mp4_h264`, `webm_vp9`, `mov_h265`, `mov_proresks`, `mkv_h265`, `mkv_h264`, `mkv_vp9`, `gif`
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="Video | File" required>
      Video with removed background and audio.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "video_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/rmbg_tests/videos/5586521-uhd_3840_2160_25fps_original.mp4",
      "background_color": "Black",
      "output_container_and_codec": "webm_vp9"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019
      }
    }
    ```
  </Tab>

  <Tab title="Increase Resolution">
    **Endpoint:** `POST https://fal.run/bria/video/increase-resolution`
    **Endpoint ID:** `bria/video/increase-resolution`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/video/increase-resolution/playground">
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
          "bria/video/increase-resolution",
          arguments={
              "video_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/video_increase_res/3446608-sd_426_240_25fps.mp4"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bria/video/increase-resolution", {
        input: {
            video_url: "https://bria-datasets.s3.us-east-1.amazonaws.com/video_increase_res/3446608-sd_426_240_25fps.mp4"
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
        --url https://fal.run/bria/video/increase-resolution \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "video_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/video_increase_res/3446608-sd_426_240_25fps.mp4"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="video_url" type="string" required>
      Input video to increase resolution. Size should be less than 7680,4320 and duration less than 30s.
    </ParamField>

    <ParamField body="desired_increase" type="DesiredIncreaseEnum" default="2">
      desired\_increase factor. Options: 2x, 4x. Default value: `"2"`

      Possible values: `2`, `4`
    </ParamField>

    <ParamField body="output_container_and_codec" type="OutputContainerAndCodecEnum" default="webm_vp9">
      Output container and codec. Options: mp4\_h265, mp4\_h264, webm\_vp9, mov\_h265, mov\_proresks, mkv\_h265, mkv\_h264, mkv\_vp9, gif. Default value: `"webm_vp9"`

      Possible values: `mp4_h265`, `mp4_h264`, `webm_vp9`, `mov_h265`, `mov_proresks`, `mkv_h265`, `mkv_h264`, `mkv_vp9`, `gif`
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="Video | File" required>
      Video with removed background and audio.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "video_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/video_increase_res/3446608-sd_426_240_25fps.mp4",
      "desired_increase": "2",
      "output_container_and_codec": "webm_vp9"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019
      }
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
* [Bria GenFill](/model-api-reference/image-generation-api/bria-genfill) — Image Generation
* [Replace Background](/model-api-reference/image-generation-api/replace-background) — Image Generation
* [Video](/model-api-reference/video-generation-api/video) — Video Generation
* [Bria Text-to-Image HD](/model-api-reference/image-generation-api/bria-text-to-image-hd) — Image Generation
* [Bria Text-to-Image Base](/model-api-reference/image-generation-api/bria-text-to-image-base) — Image Generation
* [Embed Product](/model-api-reference/image-generation-api/embed-product) — Image Generation
* [Bria Text-to-Image Fast](/model-api-reference/image-generation-api/bria-text-to-image-fast) — Image Generation

## Limitations

* `desired_increase` restricted to: `2`, `4`
