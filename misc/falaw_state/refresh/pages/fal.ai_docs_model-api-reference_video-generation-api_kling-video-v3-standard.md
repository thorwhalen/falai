> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video V3 Standard API

> API reference for Kling Video V3 Standard. Kling 3.0 Standard: Top-tier image-to-video with cinematic visuals, fluid motion, and native audio generation, with custom element support.

<Tabs>
  <Tab title="Image To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/v3/standard/image-to-video`
    **Endpoint ID:** `fal-ai/kling-video/v3/standard/image-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v3/standard/image-to-video/playground">
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
          "fal-ai/kling-video/v3/standard/image-to-video",
          arguments={
              "start_image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling-v3/standard-i2v/start_image.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/v3/standard/image-to-video", {
        input: {
            start_image_url: "https://storage.googleapis.com/falserverless/example_inputs/kling-v3/standard-i2v/start_image.png"
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
        --url https://fal.run/fal-ai/kling-video/v3/standard/image-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "start_image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling-v3/standard-i2v/start_image.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string">
      Text prompt for video generation. Either prompt or multi\_prompt must be provided, but not both.
    </ParamField>

    <ParamField body="multi_prompt" type="list<KlingV3MultiPromptElement>">
      List of prompts for multi-shot video generation. If provided, divides the video into multiple shots.
    </ParamField>

    <ParamField body="start_image_url" type="string" required>
      URL of the image to be used for the video
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="5">
      The duration of the generated video in seconds Default value: `"5"`

      Possible values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`
    </ParamField>

    <ParamField body="generate_audio" type="boolean" default="true">
      Whether to generate native audio for the video. Supports Chinese and English voice output. Other languages are automatically translated to English. For English speech, use lowercase letters; for acronyms or proper nouns, use uppercase. Default value: `true`
    </ParamField>

    <ParamField body="end_image_url" type="string">
      URL of the image to be used for the end of the video
    </ParamField>

    <ParamField body="elements" type="list<KlingV3ComboElementInput>">
      Elements (characters/objects) to include in the video. Each example can either be an image set (frontal + reference images) or a video. Reference in prompt as @Element1, @Element2, etc.
    </ParamField>

    <ParamField body="shot_type" type="string" default="customize">
      The type of multi-shot video generation. Required when multi\_prompt is provided. Default value: `"customize"`
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
      "prompt": "Camera slowly orbits around the vase. Soft light shifts across the ceramic surface. The pampas grass sways gently. Shadows move elegantly. Smooth continuous motion, premium feel.",
      "multi_prompt": null,
      "start_image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling-v3/standard-i2v/start_image.png",
      "duration": "12",
      "generate_audio": true,
      "elements": [
        {
          "frontal_image_url": "https://v3b.fal.media/files/b/0a8cfd5f/-kZL-ha3Iuelku5IHXC-A_glasses.png",
          "reference_image_urls": [
            "https://v3b.fal.media/files/b/0a8cfd62/psPCmzrD1y9vDgdyNfKAL_glasses_back.png"
          ]
        },
        {
          "video_url": "https://v3b.fal.media/files/b/0a8cfd66/b03SOiQvKLlFx_jqdNZ9z_child_video.mp4"
        }
      ],
      "shot_type": "customize",
      "negative_prompt": "blur, distort, and low quality",
      "cfg_scale": 0.5
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "content_type": "video/mp4",
        "file_name": "out.mp4",
        "file_size": 3149129,
        "url": "https://storage.googleapis.com/falserverless/example_outputs/kling-v3/standard-i2v/out.mp4"
      }
    }
    ```
  </Tab>

  <Tab title="Text To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/v3/standard/text-to-video`
    **Endpoint ID:** `fal-ai/kling-video/v3/standard/text-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v3/standard/text-to-video/playground">
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
          "fal-ai/kling-video/v3/standard/text-to-video",
          arguments={},
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/v3/standard/text-to-video", {
        input: {},
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
        --url https://fal.run/fal-ai/kling-video/v3/standard/text-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{}'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string">
      Text prompt for video generation. Either prompt or multi\_prompt must be provided, but not both.
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="5">
      The duration of the generated video in seconds Default value: `"5"`

      Possible values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`
    </ParamField>

    <ParamField body="multi_prompt" type="list<KlingV3MultiPromptElement>">
      List of prompts for multi-shot video generation. If provided, overrides the single prompt and divides the video into multiple shots with specified prompts and durations.
    </ParamField>

    <ParamField body="generate_audio" type="boolean" default="true">
      Whether to generate native audio for the video. Supports Chinese and English voice output. Other languages are automatically translated to English. For English speech, use lowercase letters; for acronyms or proper nouns, use uppercase. Default value: `true`
    </ParamField>

    <ParamField body="shot_type" type="ShotTypeEnum" default="customize">
      The type of multi-shot video generation Default value: `"customize"`

      Possible values: `customize`, `intelligent`
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
      "prompt": "Cinematic drone shot flying through ancient stone ruins covered in moss and vines at golden hour. Camera starts low, rises through crumbling archways, revealing a vast misty valley beyond. Volumetric light rays pierce through gaps in the stone. Epic scale, photorealistic, 8K quality.",
      "duration": "5",
      "multi_prompt": null,
      "generate_audio": true,
      "shot_type": "customize",
      "aspect_ratio": "16:9",
      "negative_prompt": "blur, distort, and low quality",
      "cfg_scale": 0.5
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "content_type": "video/mp4",
        "file_name": "output.mp4",
        "file_size": 6797486,
        "url": "https://storage.googleapis.com/falserverless/example_outputs/kling-v3/standard-t2v/out.mp4"
      }
    }
    ```
  </Tab>

  <Tab title="Motion Control">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/v3/standard/motion-control`
    **Endpoint ID:** `fal-ai/kling-video/v3/standard/motion-control`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v3/standard/motion-control/playground">
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
          "fal-ai/kling-video/v3/standard/motion-control",
          arguments={
              "image_url": "https://v3b.fal.media/files/b/0a90ee31/VHtWK5BZMa-XoT6gahJKS_077.png",
              "video_url": "https://v3b.fal.media/files/b/0a90edae/3nvl30ic9g2otKRcOV5nO_output.mp4",
              "character_orientation": "video"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/v3/standard/motion-control", {
        input: {
            image_url: "https://v3b.fal.media/files/b/0a90ee31/VHtWK5BZMa-XoT6gahJKS_077.png",
            video_url: "https://v3b.fal.media/files/b/0a90edae/3nvl30ic9g2otKRcOV5nO_output.mp4",
            character_orientation: "video"
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
        --url https://fal.run/fal-ai/kling-video/v3/standard/motion-control \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://v3b.fal.media/files/b/0a90ee31/VHtWK5BZMa-XoT6gahJKS_077.png",
        "video_url": "https://v3b.fal.media/files/b/0a90edae/3nvl30ic9g2otKRcOV5nO_output.mp4",
        "character_orientation": "video"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" />

    <ParamField body="image_url" type="string" required>
      Reference image URL. The characters, backgrounds, and other elements in the generated video are based on this reference image. Characters should have clear body proportions, avoid occlusion, and occupy more than 5% of the image area.
    </ParamField>

    <ParamField body="video_url" type="string" required>
      Reference video URL. The character actions in the generated video will be consistent with this reference video. Should contain a realistic style character with entire body or upper body visible, including head, without obstruction. Duration limit depends on character\_orientation: 10s max for 'image', 30s max for 'video'.
    </ParamField>

    <ParamField body="keep_original_sound" type="boolean" default="true">
      Whether to keep the original sound from the reference video. Default value: `true`
    </ParamField>

    <ParamField body="character_orientation" type="CharacterOrientationEnum" required>
      Controls whether the output character's orientation matches the reference image or video. 'video': orientation matches reference video - better for complex motions (max 30s). 'image': orientation matches reference image - better for following camera movements (max 10s).

      Possible values: `image`, `video`
    </ParamField>

    <ParamField body="elements" type="list<KlingV3ImageElementInput>">
      Optional element for facial consistency binding. Upload a facial element to enhance identity preservation in the generated video. Only 1 element is supported. Reference in prompt as @Element1. Element binding is only supported when character\_orientation is 'video'.
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "An man dancing",
      "image_url": "https://v3b.fal.media/files/b/0a90ee31/VHtWK5BZMa-XoT6gahJKS_077.png",
      "video_url": "https://v3b.fal.media/files/b/0a90edae/3nvl30ic9g2otKRcOV5nO_output.mp4",
      "keep_original_sound": true,
      "character_orientation": "video",
      "elements": null
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://v3b.fal.media/files/b/0a90ee68/7-xpX-LTxX_nRHL776FrZ_output.mp4"
      }
    }
    ```
  </Tab>
</Tabs>

## Related

* [Kling Video v3 Text to Video \[Pro\]](/model-api-reference/video-generation-api/kling-video-v3-text-to-video) — Video Generation
* [Kling Video v3 Image to Video \[Pro\]](/model-api-reference/video-generation-api/kling-video-v3-image-to-video) — Video Generation
* [Kling Video](/model-api-reference/video-generation-api/kling-video) — Video Generation

## Limitations

* `cfg_scale` range: 0 to 1
* `shot_type` restricted to: `customize`, `intelligent`
* `aspect_ratio` restricted to: `16:9`, `9:16`, `1:1`
* `character_orientation` restricted to: `image`, `video`
