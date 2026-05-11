> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Veo3.1 Lite API

> API reference for Veo3.1 Lite. Veo 3.1 Lite balances practical utility with professional capabilities, supporting Text-to-Video and Image-to-Video

<Tabs>
  <Tab title="Lite">
    **Endpoint:** `POST https://fal.run/fal-ai/veo3.1/lite`
    **Endpoint ID:** `fal-ai/veo3.1/lite`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/veo3.1/lite/playground">
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
          "fal-ai/veo3.1/lite",
          arguments={
              "prompt": "A massive blue whale glides through crystal-clear deep ocean water, sunlight rays piercing through the surface above, bioluminescent plankton scattered around, cinematic slow motion"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/veo3.1/lite", {
        input: {
            prompt: "A massive blue whale glides through crystal-clear deep ocean water, sunlight rays piercing through the surface above, bioluminescent plankton scattered around, cinematic slow motion"
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
        --url https://fal.run/fal-ai/veo3.1/lite \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A massive blue whale glides through crystal-clear deep ocean water, sunlight rays piercing through the surface above, bioluminescent plankton scattered around, cinematic slow motion"
      }'
      ```
    </CodeGroup>

    ## Examples

    > A ballerina performing an elegant pirouette on a moonlit outdoor stage. She wears a flowing white tutu that catches the silver light. Rose petals swirl around her in slow motion. The background is a dark forest with fireflies. Camera orbits slowly around her as she spins. Ethereal, dreamlike, cinema...

    <video src="https://v3b.fal.media/files/b/0a946855/rR-4fWeyUoQgo8g32Y1gy_8263e382d6734cfcb6f9b7160f127065.mp4" controls width="100%" />

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt describing the video you want to generate
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="16:9">
      Aspect ratio of the generated video Default value: `"16:9"`

      Possible values: `16:9`, `9:16`
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="8s">
      The duration of the generated video. Default value: `"8s"`

      Possible values: `4s`, `6s`, `8s`
    </ParamField>

    <ParamField body="negative_prompt" type="string">
      A negative prompt to guide the video generation.
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="720p">
      The resolution of the generated video. Default value: `"720p"`

      Possible values: `720p`, `1080p`
    </ParamField>

    <ParamField body="generate_audio" type="boolean" default="true">
      Whether to generate audio for the video. Default value: `true`
    </ParamField>

    <ParamField body="seed" type="integer">
      The seed for the random number generator.
    </ParamField>

    <ParamField body="auto_fix" type="boolean" default="true">
      Whether to automatically attempt to fix prompts that fail content policy or other validation checks by rewriting them. Default value: `true`
    </ParamField>

    <ParamField body="safety_tolerance" type="SafetyToleranceEnum" default="4">
      The safety tolerance level for content moderation. 1 is the most strict (blocks most content), 6 is the least strict. Default value: `"4"`

      Possible values: `1`, `2`, `3`, `4`, `5`, `6`
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A massive blue whale glides through crystal-clear deep ocean water, sunlight rays piercing through the surface above, bioluminescent plankton scattered around, cinematic slow motion",
      "aspect_ratio": "16:9",
      "duration": "8s",
      "resolution": "720p",
      "generate_audio": true,
      "auto_fix": true,
      "safety_tolerance": "4"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://v3b.fal.media/files/b/0a94683f/r4vLtNmFDi_qpglfEX_q9_0a7258527ac84509a0997639765f5c79.mp4"
      }
    }
    ```
  </Tab>

  <Tab title="Image To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/veo3.1/lite/image-to-video`
    **Endpoint ID:** `fal-ai/veo3.1/lite/image-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/veo3.1/lite/image-to-video/playground">
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
          "fal-ai/veo3.1/lite/image-to-video",
          arguments={
              "prompt": "The subject turns to face the camera and smiles warmly.",
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/veo3-i2v-input.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/veo3.1/lite/image-to-video", {
        input: {
            prompt: "The subject turns to face the camera and smiles warmly.",
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/veo3-i2v-input.png"
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
        --url https://fal.run/fal-ai/veo3.1/lite/image-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "The subject turns to face the camera and smiles warmly.",
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/veo3-i2v-input.png"
      }'
      ```
    </CodeGroup>

    ## Examples

    > Time-lapse of the city transitioning through the day. Shadows shift across buildings, traffic flows in streaks of light, clouds race across the sky. The scene shifts from bright midday to warm golden hour. Smooth hyperlapse feel.

    <video src="https://v3b.fal.media/files/b/0a94686f/UtJVZJIY6D9NwIaB3TVwu_738e51572750421fbb5fc3b78029988a.mp4" controls width="100%" />

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt describing how the image should be animated
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
      The aspect ratio of the generated video. Default value: `"auto"`

      Possible values: `auto`, `16:9`, `9:16`
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="8s">
      The duration of the generated video. Default value: `"8s"`

      Possible values: `4s`, `6s`, `8s`
    </ParamField>

    <ParamField body="negative_prompt" type="string">
      A negative prompt to guide the video generation.
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="720p">
      The resolution of the generated video. Default value: `"720p"`

      Possible values: `720p`, `1080p`
    </ParamField>

    <ParamField body="generate_audio" type="boolean" default="true">
      Whether to generate audio for the video. Default value: `true`
    </ParamField>

    <ParamField body="seed" type="integer">
      The seed for the random number generator.
    </ParamField>

    <ParamField body="auto_fix" type="boolean" default="false">
      Whether to automatically attempt to fix prompts that fail content policy or other validation checks by rewriting them.
    </ParamField>

    <ParamField body="safety_tolerance" type="SafetyToleranceEnum" default="4">
      The safety tolerance level for content moderation. 1 is the most strict (blocks most content), 6 is the least strict. Default value: `"4"`

      Possible values: `1`, `2`, `3`, `4`, `5`, `6`
    </ParamField>

    <ParamField body="image_url" type="string" required>
      URL of the input image to animate. Should be 720p or higher resolution in 16:9 or 9:16 aspect ratio.
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "The subject turns to face the camera and smiles warmly.",
      "aspect_ratio": "auto",
      "duration": "8s",
      "resolution": "720p",
      "generate_audio": true,
      "auto_fix": false,
      "safety_tolerance": "4",
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/veo3-i2v-input.png"
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

  <Tab title="First Last Frame To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/veo3.1/lite/first-last-frame-to-video`
    **Endpoint ID:** `fal-ai/veo3.1/lite/first-last-frame-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/veo3.1/lite/first-last-frame-to-video/playground">
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
          "fal-ai/veo3.1/lite/first-last-frame-to-video",
          arguments={
              "prompt": "A smooth transition between the two frames with natural motion.",
              "first_frame_url": "https://storage.googleapis.com/falserverless/example_inputs/veo31-flf2v-input-1.jpeg",
              "last_frame_url": "https://storage.googleapis.com/falserverless/example_inputs/veo31-flf2v-input-2.jpeg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/veo3.1/lite/first-last-frame-to-video", {
        input: {
            prompt: "A smooth transition between the two frames with natural motion.",
            first_frame_url: "https://storage.googleapis.com/falserverless/example_inputs/veo31-flf2v-input-1.jpeg",
            last_frame_url: "https://storage.googleapis.com/falserverless/example_inputs/veo31-flf2v-input-2.jpeg"
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
        --url https://fal.run/fal-ai/veo3.1/lite/first-last-frame-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A smooth transition between the two frames with natural motion.",
        "first_frame_url": "https://storage.googleapis.com/falserverless/example_inputs/veo31-flf2v-input-1.jpeg",
        "last_frame_url": "https://storage.googleapis.com/falserverless/example_inputs/veo31-flf2v-input-2.jpeg"
      }'
      ```
    </CodeGroup>

    ## Examples

    > The sun arcs across the sky from sunrise to sunset. Light transitions from cool dawn blue through warm golden midday to deep amber sunset. Shadows rotate and lengthen. Clouds drift and change shape. Smooth time-lapse feel.

    <video src="https://v3b.fal.media/files/b/0a946880/sfDxO-znDhQthS00Pa2Ns_d99979ba04614c3d963ebaa342627b3c.mp4" controls width="100%" />

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt describing the video you want to generate
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
      The aspect ratio of the generated video. Default value: `"auto"`

      Possible values: `auto`, `16:9`, `9:16`
    </ParamField>

    <ParamField body="duration" type="string" default="8s">
      The duration of the generated video. Default value: `"8s"`
    </ParamField>

    <ParamField body="negative_prompt" type="string">
      A negative prompt to guide the video generation.
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="720p">
      The resolution of the generated video. Default value: `"720p"`

      Possible values: `720p`, `1080p`
    </ParamField>

    <ParamField body="generate_audio" type="boolean" default="true">
      Whether to generate audio for the video. Default value: `true`
    </ParamField>

    <ParamField body="seed" type="integer">
      The seed for the random number generator.
    </ParamField>

    <ParamField body="auto_fix" type="boolean" default="false">
      Whether to automatically attempt to fix prompts that fail content policy or other validation checks by rewriting them.
    </ParamField>

    <ParamField body="safety_tolerance" type="SafetyToleranceEnum" default="4">
      The safety tolerance level for content moderation. 1 is the most strict (blocks most content), 6 is the least strict. Default value: `"4"`

      Possible values: `1`, `2`, `3`, `4`, `5`, `6`
    </ParamField>

    <ParamField body="first_frame_url" type="string" required>
      URL of the first frame of the video
    </ParamField>

    <ParamField body="last_frame_url" type="string" required>
      URL of the last frame of the video
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A smooth transition between the two frames with natural motion.",
      "aspect_ratio": "auto",
      "duration": "8s",
      "resolution": "720p",
      "generate_audio": true,
      "auto_fix": false,
      "safety_tolerance": "4",
      "first_frame_url": "https://storage.googleapis.com/falserverless/example_inputs/veo31-flf2v-input-1.jpeg",
      "last_frame_url": "https://storage.googleapis.com/falserverless/example_inputs/veo31-flf2v-input-2.jpeg"
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

* [Veo 3.1](/model-api-reference/video-generation-api/veo-3.1) — Video Generation
* [Veo 3.1 Fast](/model-api-reference/video-generation-api/veo-3.1-fast) — Video Generation
* [Veo3.1 Lite Image to Video](/model-api-reference/video-generation-api/veo3.1-lite-image-to-video) — Video Generation
* [Veo3.1 Lite FLF](/model-api-reference/video-generation-api/veo3.1-lite-flf) — Video Generation
* [Veo3.1 Lite Text to Video](/model-api-reference/video-generation-api/veo3.1-lite-text-to-video) — Video Generation

## Limitations

* `aspect_ratio` restricted to: `16:9`, `9:16`
* `duration` restricted to: `4s`, `6s`, `8s`
* `resolution` restricted to: `720p`, `1080p`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`, `6`
* `aspect_ratio` restricted to: `auto`, `16:9`, `9:16`
