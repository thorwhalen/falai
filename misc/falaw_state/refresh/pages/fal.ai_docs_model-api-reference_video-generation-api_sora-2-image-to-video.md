> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sora 2 Image To Video API

> API reference for Sora 2 Image To Video. Image-to-video endpoint for Sora 2, OpenAI's state-of-the-art video model capable of creating richly detailed, dynamic clips with audio from natural language o

<Tabs>
  <Tab title="Image To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/sora-2/image-to-video`
    **Endpoint ID:** `fal-ai/sora-2/image-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/sora-2/image-to-video/playground">
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
          "fal-ai/sora-2/image-to-video",
          arguments={
              "prompt": "Front-facing 'invisible' action-cam on a skydiver in freefall above bright clouds; camera locked on his face. He speaks over the wind with clear lipsync: 'This is insanely fun! You've got to try it—book a tandem and go!' Natural wind roar, voice close-mic'd and slightly compressed so it's intelligible. Midday sun, goggles and jumpsuit flutter, altimeter visible, parachute rig on shoulders. Energetic but stable framing with subtle shake; brief horizon roll. End on first tug of canopy and wind noise dropping.",
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/sora-2-i2v-input.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/sora-2/image-to-video", {
        input: {
            prompt: "Front-facing 'invisible' action-cam on a skydiver in freefall above bright clouds; camera locked on his face. He speaks over the wind with clear lipsync: 'This is insanely fun! You've got to try it—book a tandem and go!' Natural wind roar, voice close-mic'd and slightly compressed so it's intelligible. Midday sun, goggles and jumpsuit flutter, altimeter visible, parachute rig on shoulders. Energetic but stable framing with subtle shake; brief horizon roll. End on first tug of canopy and wind noise dropping.",
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/sora-2-i2v-input.png"
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
        --url https://fal.run/fal-ai/sora-2/image-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Front-facing '\''invisible'\'' action-cam on a skydiver in freefall above bright clouds; camera locked on his face. He speaks over the wind with clear lipsync: '\''This is insanely fun! You'\''ve got to try it—book a tandem and go!'\'' Natural wind roar, voice close-mic'\''d and slightly compressed so it'\''s intelligible. Midday sun, goggles and jumpsuit flutter, altimeter visible, parachute rig on shoulders. Energetic but stable framing with subtle shake; brief horizon roll. End on first tug of canopy and wind noise dropping.",
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/sora-2-i2v-input.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt describing the video you want to generate
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="auto">
      The resolution of the generated video Default value: `"auto"`

      Possible values: `auto`, `720p`
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
      The aspect ratio of the generated video Default value: `"auto"`

      Possible values: `auto`, `9:16`, `16:9`
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="4">
      Duration of the generated video in seconds Default value: `"4"`

      Possible values: `4`, `8`, `12`, `16`, `20`
    </ParamField>

    <ParamField body="delete_video" type="boolean" default="true">
      Whether to delete the video after generation for privacy reasons. If True, the video cannot be used for remixing and will be permanently deleted. Default value: `true`
    </ParamField>

    <ParamField body="model" type="ModelEnum" default="sora-2">
      The model to use for the generation. When the default model is selected, the latest snapshot of the model will be used - otherwise, select a specific snapshot of the model. Default value: `"sora-2"`

      Possible values: `sora-2`, `sora-2-2025-12-08`, `sora-2-2025-10-06`
    </ParamField>

    <ParamField body="detect_and_block_ip" type="boolean" default="false">
      If enabled, the prompt (and image for image-to-video) will be checked for known intellectual property references and the request will be blocked if any are detected.
    </ParamField>

    <ParamField body="character_ids" type="list<string>">
      Up to two character IDs (from create-character) to use in the video. Refer to characters by name in the prompt. When set, only the OpenAI provider is used.
    </ParamField>

    <ParamField body="image_url" type="string" required>
      The URL of the image to use as the first frame
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="VideoFile" required>
      The generated video
    </ParamField>

    <ParamField body="video_id" type="string" required>
      The ID of the generated video
    </ParamField>

    <ParamField body="thumbnail" type="ImageFile">
      Thumbnail image for the video
    </ParamField>

    <ParamField body="spritesheet" type="ImageFile">
      Spritesheet image for the video
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Front-facing 'invisible' action-cam on a skydiver in freefall above bright clouds; camera locked on his face. He speaks over the wind with clear lipsync: 'This is insanely fun! You've got to try it—book a tandem and go!' Natural wind roar, voice close-mic'd and slightly compressed so it's intelligible. Midday sun, goggles and jumpsuit flutter, altimeter visible, parachute rig on shoulders. Energetic but stable framing with subtle shake; brief horizon roll. End on first tug of canopy and wind noise dropping.",
      "resolution": "auto",
      "aspect_ratio": "auto",
      "duration": 4,
      "delete_video": true,
      "model": "sora-2",
      "detect_and_block_ip": false,
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/sora-2-i2v-input.png"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "content_type": "video/mp4",
        "url": "https://storage.googleapis.com/falserverless/example_outputs/sora_2_i2v_output.mp4"
      },
      "video_id": "video_123"
    }
    ```
  </Tab>

  <Tab title="Pro">
    **Endpoint:** `POST https://fal.run/fal-ai/sora-2/image-to-video/pro`
    **Endpoint ID:** `fal-ai/sora-2/image-to-video/pro`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/sora-2/image-to-video/pro/playground">
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
          "fal-ai/sora-2/image-to-video/pro",
          arguments={
              "prompt": "Front-facing 'invisible' action-cam on a skydiver in freefall above bright clouds; camera locked on his face. He speaks over the wind with clear lipsync: 'This is insanely fun! You've got to try it—book a tandem and go!' Natural wind roar, voice close-mic'd and slightly compressed so it's intelligible. Midday sun, goggles and jumpsuit flutter, altimeter visible, parachute rig on shoulders. Energetic but stable framing with subtle shake; brief horizon roll. End on first tug of canopy and wind noise dropping.",
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/sora-2-i2v-input.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/sora-2/image-to-video/pro", {
        input: {
            prompt: "Front-facing 'invisible' action-cam on a skydiver in freefall above bright clouds; camera locked on his face. He speaks over the wind with clear lipsync: 'This is insanely fun! You've got to try it—book a tandem and go!' Natural wind roar, voice close-mic'd and slightly compressed so it's intelligible. Midday sun, goggles and jumpsuit flutter, altimeter visible, parachute rig on shoulders. Energetic but stable framing with subtle shake; brief horizon roll. End on first tug of canopy and wind noise dropping.",
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/sora-2-i2v-input.png"
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
        --url https://fal.run/fal-ai/sora-2/image-to-video/pro \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Front-facing '\''invisible'\'' action-cam on a skydiver in freefall above bright clouds; camera locked on his face. He speaks over the wind with clear lipsync: '\''This is insanely fun! You'\''ve got to try it—book a tandem and go!'\'' Natural wind roar, voice close-mic'\''d and slightly compressed so it'\''s intelligible. Midday sun, goggles and jumpsuit flutter, altimeter visible, parachute rig on shoulders. Energetic but stable framing with subtle shake; brief horizon roll. End on first tug of canopy and wind noise dropping.",
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/sora-2-i2v-input.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt describing the video you want to generate
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="auto">
      The resolution of the generated video Default value: `"auto"`

      Possible values: `auto`, `720p`, `1080p`, `true_1080p`
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
      The aspect ratio of the generated video Default value: `"auto"`

      Possible values: `auto`, `9:16`, `16:9`
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="4">
      Duration of the generated video in seconds Default value: `"4"`

      Possible values: `4`, `8`, `12`, `16`, `20`
    </ParamField>

    <ParamField body="delete_video" type="boolean" default="true">
      Whether to delete the video after generation for privacy reasons. If True, the video cannot be used for remixing and will be permanently deleted. Default value: `true`
    </ParamField>

    <ParamField body="detect_and_block_ip" type="boolean" default="false">
      If enabled, the prompt (and image for image-to-video) will be checked for known intellectual property references and the request will be blocked if any are detected.
    </ParamField>

    <ParamField body="character_ids" type="list<string>">
      Up to two character IDs (from create-character) to use in the video. Refer to characters by name in the prompt. When set, only the OpenAI provider is used.
    </ParamField>

    <ParamField body="image_url" type="string" required>
      The URL of the image to use as the first frame
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="VideoFile" required>
      The generated video
    </ParamField>

    <ParamField body="video_id" type="string" required>
      The ID of the generated video
    </ParamField>

    <ParamField body="thumbnail" type="ImageFile">
      Thumbnail image for the video
    </ParamField>

    <ParamField body="spritesheet" type="ImageFile">
      Spritesheet image for the video
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Front-facing 'invisible' action-cam on a skydiver in freefall above bright clouds; camera locked on his face. He speaks over the wind with clear lipsync: 'This is insanely fun! You've got to try it—book a tandem and go!' Natural wind roar, voice close-mic'd and slightly compressed so it's intelligible. Midday sun, goggles and jumpsuit flutter, altimeter visible, parachute rig on shoulders. Energetic but stable framing with subtle shake; brief horizon roll. End on first tug of canopy and wind noise dropping.",
      "resolution": "auto",
      "aspect_ratio": "auto",
      "duration": 4,
      "delete_video": true,
      "detect_and_block_ip": false,
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/sora-2-i2v-input.png"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "content_type": "video/mp4",
        "url": "https://storage.googleapis.com/falserverless/example_outputs/sora-2-pro-i2v-output.mp4"
      },
      "video_id": "video_123"
    }
    ```
  </Tab>
</Tabs>

## Related

* [Sora 2](/model-api-reference/video-generation-api/sora-2) — Video Generation

## Limitations

* `resolution` restricted to: `auto`, `720p`
* `aspect_ratio` restricted to: `auto`, `9:16`, `16:9`
* `duration` restricted to: `4`, `8`, `12`, `16`, `20`
* `model` restricted to: `sora-2`, `sora-2-2025-12-08`, `sora-2-2025-10-06`
* `resolution` restricted to: `auto`, `720p`, `1080p`, `true_1080p`
