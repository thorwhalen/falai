> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Veo3.1 Fast API

> API reference for Veo3.1 Fast. Faster and more cost effective version of Google's Veo 3.1!

<Tabs>
  <Tab title="Fast">
    **Endpoint:** `POST https://fal.run/fal-ai/veo3.1/fast`
    **Endpoint ID:** `fal-ai/veo3.1/fast`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/veo3.1/fast/playground">
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
          "fal-ai/veo3.1/fast",
          arguments={
              "prompt": "Two person street interview in New York City.
      Sample Dialogue:
      Host: \"Did you hear the news?\"
      Person: \"Yes! Veo 3.1 is now available on fal. If you want to see it, go check their website.\""
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/veo3.1/fast", {
        input: {
            prompt: "Two person street interview in New York City.
      Sample Dialogue:
      Host: \"Did you hear the news?\"
      Person: \"Yes! Veo 3.1 is now available on fal. If you want to see it, go check their website.\""
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
        --url https://fal.run/fal-ai/veo3.1/fast \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Two person street interview in New York City.\nSample Dialogue:\nHost: \"Did you hear the news?\"\nPerson: \"Yes! Veo 3.1 is now available on fal. If you want to see it, go check their website.\""
      }'
      ```
    </CodeGroup>

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

      Possible values: `720p`, `1080p`, `4k`
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
      "prompt": "Two person street interview in New York City.\nSample Dialogue:\nHost: \"Did you hear the news?\"\nPerson: \"Yes! Veo 3.1 is now available on fal. If you want to see it, go check their website.\"",
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
        "url": "https://v3b.fal.media/files/b/kangaroo/oUCiZjQwEy6bIQdPUSLDF_output.mp4"
      }
    }
    ```
  </Tab>

  <Tab title="Image To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/veo3.1/fast/image-to-video`
    **Endpoint ID:** `fal-ai/veo3.1/fast/image-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/veo3.1/fast/image-to-video/playground">
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
          "fal-ai/veo3.1/fast/image-to-video",
          arguments={
              "prompt": "A monkey and polar bear host a casual podcast about AI inference, bringing their unique perspectives from different environments (tropical vs. arctic) to discuss how AI systems make decisions and process information.
      Sample Dialogue:
      Monkey (Banana): \"Welcome back to Bananas & Ice! I am Banana\"
      Polar Bear (Ice): \"And I'm Ice!\"",
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/veo31_i2v_input.jpg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/veo3.1/fast/image-to-video", {
        input: {
            prompt: "A monkey and polar bear host a casual podcast about AI inference, bringing their unique perspectives from different environments (tropical vs. arctic) to discuss how AI systems make decisions and process information.
      Sample Dialogue:
      Monkey (Banana): \"Welcome back to Bananas & Ice! I am Banana\"
      Polar Bear (Ice): \"And I'm Ice!\"",
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/veo31_i2v_input.jpg"
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
        --url https://fal.run/fal-ai/veo3.1/fast/image-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A monkey and polar bear host a casual podcast about AI inference, bringing their unique perspectives from different environments (tropical vs. arctic) to discuss how AI systems make decisions and process information.\nSample Dialogue:\nMonkey (Banana): \"Welcome back to Bananas & Ice! I am Banana\"\nPolar Bear (Ice): \"And I'\''m Ice!\"",
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/veo31_i2v_input.jpg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt describing the video you want to generate
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
      The aspect ratio of the generated video. Only 16:9 and 9:16 are supported. Default value: `"auto"`

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

      Possible values: `720p`, `1080p`, `4k`
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
      URL of the input image to animate. Should be 720p or higher resolution in 16:9 or 9:16 aspect ratio. If the image is not in 16:9 or 9:16 aspect ratio, it will be cropped to fit.
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A monkey and polar bear host a casual podcast about AI inference, bringing their unique perspectives from different environments (tropical vs. arctic) to discuss how AI systems make decisions and process information.\nSample Dialogue:\nMonkey (Banana): \"Welcome back to Bananas & Ice! I am Banana\"\nPolar Bear (Ice): \"And I'm Ice!\"",
      "aspect_ratio": "auto",
      "duration": "8s",
      "resolution": "720p",
      "generate_audio": true,
      "auto_fix": false,
      "safety_tolerance": "4",
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/veo31_i2v_input.jpg"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://storage.googleapis.com/falserverless/model_tests/gallery/veo3-1-i2v.mp4"
      }
    }
    ```
  </Tab>

  <Tab title="First Last Frame To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/veo3.1/fast/first-last-frame-to-video`
    **Endpoint ID:** `fal-ai/veo3.1/fast/first-last-frame-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/veo3.1/fast/first-last-frame-to-video/playground">
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
          "fal-ai/veo3.1/fast/first-last-frame-to-video",
          arguments={
              "prompt": "A woman looks into the camera, breathes in, then exclaims energetically, \"have you guys checked out Veo3.1 First-Last-Frame-to-Video on Fal? It's incredible!\"",
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

      const result = await fal.subscribe("fal-ai/veo3.1/fast/first-last-frame-to-video", {
        input: {
            prompt: "A woman looks into the camera, breathes in, then exclaims energetically, \"have you guys checked out Veo3.1 First-Last-Frame-to-Video on Fal? It's incredible!\"",
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
        --url https://fal.run/fal-ai/veo3.1/fast/first-last-frame-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A woman looks into the camera, breathes in, then exclaims energetically, \"have you guys checked out Veo3.1 First-Last-Frame-to-Video on Fal? It'\''s incredible!\"",
        "first_frame_url": "https://storage.googleapis.com/falserverless/example_inputs/veo31-flf2v-input-1.jpeg",
        "last_frame_url": "https://storage.googleapis.com/falserverless/example_inputs/veo31-flf2v-input-2.jpeg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt describing the video you want to generate
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

      Possible values: `720p`, `1080p`, `4k`
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
      "prompt": "A woman looks into the camera, breathes in, then exclaims energetically, \"have you guys checked out Veo3.1 First-Last-Frame-to-Video on Fal? It's incredible!\"",
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
        "url": "https://storage.googleapis.com/falserverless/example_outputs/veo31-flf2v-output.mp4"
      }
    }
    ```
  </Tab>

  <Tab title="Extend Video">
    **Endpoint:** `POST https://fal.run/fal-ai/veo3.1/fast/extend-video`
    **Endpoint ID:** `fal-ai/veo3.1/fast/extend-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/veo3.1/fast/extend-video/playground">
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
          "fal-ai/veo3.1/fast/extend-video",
          arguments={
              "prompt": "Continue the scene naturally, maintaining the same style and motion.",
              "video_url": "https://v3b.fal.media/files/b/0a8670fe/pY8UGl4_C452wOm9XUBYO_9ae04df8771c4f3f979fa5cabeca6ada.mp4"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/veo3.1/fast/extend-video", {
        input: {
            prompt: "Continue the scene naturally, maintaining the same style and motion.",
            video_url: "https://v3b.fal.media/files/b/0a8670fe/pY8UGl4_C452wOm9XUBYO_9ae04df8771c4f3f979fa5cabeca6ada.mp4"
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
        --url https://fal.run/fal-ai/veo3.1/fast/extend-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Continue the scene naturally, maintaining the same style and motion.",
        "video_url": "https://v3b.fal.media/files/b/0a8670fe/pY8UGl4_C452wOm9XUBYO_9ae04df8771c4f3f979fa5cabeca6ada.mp4"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt describing how the video should be extended
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
      The aspect ratio of the generated video. Default value: `"auto"`

      Possible values: `auto`, `16:9`, `9:16`
    </ParamField>

    <ParamField body="duration" type="string" default="7s">
      The duration of the generated video. Default value: `"7s"`
    </ParamField>

    <ParamField body="negative_prompt" type="string">
      A negative prompt to guide the video generation.
    </ParamField>

    <ParamField body="resolution" type="string" default="720p">
      The resolution of the generated video. Default value: `"720p"`
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

    <ParamField body="video_url" type="string" required>
      URL of the video to extend. The video should be 720p or 1080p resolution in 16:9 or 9:16 aspect ratio.
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The extended video.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Continue the scene naturally, maintaining the same style and motion.",
      "aspect_ratio": "auto",
      "duration": "7s",
      "resolution": "720p",
      "generate_audio": true,
      "auto_fix": false,
      "safety_tolerance": "4",
      "video_url": "https://v3b.fal.media/files/b/0a8670fe/pY8UGl4_C452wOm9XUBYO_9ae04df8771c4f3f979fa5cabeca6ada.mp4"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://v3b.fal.media/files/b/0a86711b/B_Z96VS4X9Dfd4M5ArB4H_c666e63f729f4a8fa1145c6727cef97d.mp4"
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
* `resolution` restricted to: `720p`, `1080p`, `4k`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`, `6`
* `aspect_ratio` restricted to: `auto`, `16:9`, `9:16`
