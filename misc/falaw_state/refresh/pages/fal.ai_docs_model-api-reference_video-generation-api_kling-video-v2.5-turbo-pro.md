> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video V2.5 Turbo Pro API

> API reference for Kling Video V2.5 Turbo Pro. Kling 2.5 Turbo Pro: Top-tier image-to-video generation with unparalleled motion fluidity, cinematic visuals, and exceptional prompt precision.

<Tabs>
  <Tab title="Image To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/v2.5-turbo/pro/image-to-video`
    **Endpoint ID:** `fal-ai/kling-video/v2.5-turbo/pro/image-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v2.5-turbo/pro/image-to-video/playground">
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
          "fal-ai/kling-video/v2.5-turbo/pro/image-to-video",
          arguments={
              "prompt": "A stark starting line divides two powerful cars, engines revving for the challenge ahead. They surge forward in the heat of competition, a blur of speed and chrome. The finish line looms as they vie for victory.",
              "image_url": "https://v3.fal.media/files/panda/HnY2yf-BbzlrVQxR-qP6m_9912d0932988453aadf3912fc1901f52.jpg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/v2.5-turbo/pro/image-to-video", {
        input: {
            prompt: "A stark starting line divides two powerful cars, engines revving for the challenge ahead. They surge forward in the heat of competition, a blur of speed and chrome. The finish line looms as they vie for victory.",
            image_url: "https://v3.fal.media/files/panda/HnY2yf-BbzlrVQxR-qP6m_9912d0932988453aadf3912fc1901f52.jpg"
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
        --url https://fal.run/fal-ai/kling-video/v2.5-turbo/pro/image-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A stark starting line divides two powerful cars, engines revving for the challenge ahead. They surge forward in the heat of competition, a blur of speed and chrome. The finish line looms as they vie for victory.",
        "image_url": "https://v3.fal.media/files/panda/HnY2yf-BbzlrVQxR-qP6m_9912d0932988453aadf3912fc1901f52.jpg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required />

    <ParamField body="image_url" type="string" required>
      URL of the image to be used for the video
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="5">
      The duration of the generated video in seconds Default value: `"5"`

      Possible values: `5`, `10`
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="blur, distort, and low quality">
      Default value: `"blur, distort, and low quality"`
    </ParamField>

    <ParamField body="cfg_scale" type="float" default="0.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt. Default value: `0.5`

      Range: `0` to `1`
    </ParamField>

    <ParamField body="tail_image_url" type="string">
      URL of the image to be used for the end of the video
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A stark starting line divides two powerful cars, engines revving for the challenge ahead. They surge forward in the heat of competition, a blur of speed and chrome. The finish line looms as they vie for victory.",
      "image_url": "https://v3.fal.media/files/panda/HnY2yf-BbzlrVQxR-qP6m_9912d0932988453aadf3912fc1901f52.jpg",
      "duration": "5",
      "negative_prompt": "blur, distort, and low quality",
      "cfg_scale": 0.5
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://storage.googleapis.com/falserverless/model_tests/kling/kling-v2.5-turbo-pro-image-to-video-output.mp4"
      }
    }
    ```
  </Tab>

  <Tab title="Text To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/v2.5-turbo/pro/text-to-video`
    **Endpoint ID:** `fal-ai/kling-video/v2.5-turbo/pro/text-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v2.5-turbo/pro/text-to-video/playground">
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
          "fal-ai/kling-video/v2.5-turbo/pro/text-to-video",
          arguments={
              "prompt": "A noble lord walks among his people, his presence a comforting reassurance. He greets them with a gentle smile, embodying their hopes and earning their respect through simple interactions. The atmosphere is intimate and sincere, highlighting the bond between the leader and community."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/v2.5-turbo/pro/text-to-video", {
        input: {
            prompt: "A noble lord walks among his people, his presence a comforting reassurance. He greets them with a gentle smile, embodying their hopes and earning their respect through simple interactions. The atmosphere is intimate and sincere, highlighting the bond between the leader and community."
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
        --url https://fal.run/fal-ai/kling-video/v2.5-turbo/pro/text-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A noble lord walks among his people, his presence a comforting reassurance. He greets them with a gentle smile, embodying their hopes and earning their respect through simple interactions. The atmosphere is intimate and sincere, highlighting the bond between the leader and community."
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required />

    <ParamField body="duration" type="DurationEnum" default="5">
      The duration of the generated video in seconds Default value: `"5"`

      Possible values: `5`, `10`
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="16:9">
      The aspect ratio of the generated video frame Default value: `"16:9"`

      Possible values: `16:9`, `9:16`, `1:1`
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="blur, distort, and low quality">
      Default value: `"blur, distort, and low quality"`
    </ParamField>

    <ParamField body="cfg_scale" type="float" default="0.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt. Default value: `0.5`

      Range: `0` to `1`
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A noble lord walks among his people, his presence a comforting reassurance. He greets them with a gentle smile, embodying their hopes and earning their respect through simple interactions. The atmosphere is intimate and sincere, highlighting the bond between the leader and community.",
      "duration": "5",
      "aspect_ratio": "16:9",
      "negative_prompt": "blur, distort, and low quality",
      "cfg_scale": 0.5
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://storage.googleapis.com/falserverless/model_tests/kling/kling-v2.5-turbo-pro-text-to-video-output.mp4"
      }
    }
    ```
  </Tab>
</Tabs>

## Related

* [Kling v2.5 Text to Video](/model-api-reference/video-generation-api/kling-v2.5-text-to-video) — Video Generation
* [Kling Video](/model-api-reference/video-generation-api/kling-video) — Video Generation

## Limitations

* `duration` restricted to: `5`, `10`
* `cfg_scale` range: 0 to 1
* `aspect_ratio` restricted to: `16:9`, `9:16`, `1:1`
