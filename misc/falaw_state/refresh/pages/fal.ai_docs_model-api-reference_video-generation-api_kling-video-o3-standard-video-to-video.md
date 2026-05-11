> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video O3 Standard Video To Video API

> API reference for Kling Video O3 Standard Video To Video. Edit videos using Kling O3 from Kling Team!

<Tabs>
  <Tab title="Edit">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/o3/standard/video-to-video/edit`
    **Endpoint ID:** `fal-ai/kling-video/o3/standard/video-to-video/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/o3/standard/video-to-video/edit/playground">
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
          "fal-ai/kling-video/o3/standard/video-to-video/edit",
          arguments={
              "prompt": "change the main character to be Popeye from @Element1, dark lighting and rain, 3d character. make him sad, with rain dropping on him, dark light on the character.",
              "video_url": "https://storage.googleapis.com/falserverless/example_inputs/kling-o3/standard-v2v-edit/standard_video_reference.mp4"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/o3/standard/video-to-video/edit", {
        input: {
            prompt: "change the main character to be Popeye from @Element1, dark lighting and rain, 3d character. make him sad, with rain dropping on him, dark light on the character.",
            video_url: "https://storage.googleapis.com/falserverless/example_inputs/kling-o3/standard-v2v-edit/standard_video_reference.mp4"
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
        --url https://fal.run/fal-ai/kling-video/o3/standard/video-to-video/edit \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "change the main character to be Popeye from @Element1, dark lighting and rain, 3d character. make him sad, with rain dropping on him, dark light on the character.",
        "video_url": "https://storage.googleapis.com/falserverless/example_inputs/kling-o3/standard-v2v-edit/standard_video_reference.mp4"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      Text prompt for video generation. Reference video as @Video1.
    </ParamField>

    <ParamField body="video_url" type="string" required>
      Reference video URL. Only .mp4/.mov formats, 3-10s duration, 720-2160px resolution, max 200MB.
    </ParamField>

    <ParamField body="image_urls" type="list<string>">
      Reference images for style/appearance. Reference in prompt as @Image1, @Image2, etc. Maximum 4 total (elements + reference images) when using video.
    </ParamField>

    <ParamField body="keep_audio" type="boolean" default="true">
      Whether to keep the original audio from the reference video. Default value: `true`
    </ParamField>

    <ParamField body="elements" type="list<KlingV3ImageElementInput>">
      Elements (characters/objects) to include. Reference in prompt as @Element1, @Element2.
    </ParamField>

    <ParamField body="shot_type" type="string" default="customize">
      The type of multi-shot video generation. Default value: `"customize"`
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "change the main character to be Popeye from @Element1, dark lighting and rain, 3d character. make him sad, with rain dropping on him, dark light on the character.",
      "video_url": "https://storage.googleapis.com/falserverless/example_inputs/kling-o3/standard-v2v-edit/standard_video_reference.mp4",
      "image_urls": null,
      "keep_audio": true,
      "elements": [
        {
          "frontal_image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling-o3/standard-v2v-edit/element1_front.jpg",
          "reference_image_urls": [
            "https://storage.googleapis.com/falserverless/example_inputs/kling-o3/standard-v2v-edit/standard_element1_reference1.jpg"
          ]
        }
      ],
      "shot_type": "customize"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "content_type": "video/mp4",
        "file_name": "output.mp4",
        "file_size": 4322769,
        "url": "https://storage.googleapis.com/falserverless/example_outputs/kling-o3/standard-v2v-edit/output.mp4"
      }
    }
    ```
  </Tab>

  <Tab title="Reference">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/o3/standard/video-to-video/reference`
    **Endpoint ID:** `fal-ai/kling-video/o3/standard/video-to-video/reference`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/o3/standard/video-to-video/reference/playground">
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
          "fal-ai/kling-video/o3/standard/video-to-video/reference",
          arguments={
              "prompt": "Replace both character with @Element1 and @Element2",
              "video_url": "https://storage.googleapis.com/falserverless/example_inputs/kling-o3/standard-v2v-reference/video_reference.mp4"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/o3/standard/video-to-video/reference", {
        input: {
            prompt: "Replace both character with @Element1 and @Element2",
            video_url: "https://storage.googleapis.com/falserverless/example_inputs/kling-o3/standard-v2v-reference/video_reference.mp4"
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
        --url https://fal.run/fal-ai/kling-video/o3/standard/video-to-video/reference \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Replace both character with @Element1 and @Element2",
        "video_url": "https://storage.googleapis.com/falserverless/example_inputs/kling-o3/standard-v2v-reference/video_reference.mp4"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      Text prompt for video generation. Reference video as @Video1.
    </ParamField>

    <ParamField body="video_url" type="string" required>
      Reference video URL. Only .mp4/.mov formats, 3-10s duration, 720-2160px resolution, max 200MB.
    </ParamField>

    <ParamField body="image_urls" type="list<string>">
      Reference images for style/appearance. Reference in prompt as @Image1, @Image2, etc. Maximum 4 total (elements + reference images) when using video.
    </ParamField>

    <ParamField body="keep_audio" type="boolean" default="true">
      Whether to keep the original audio from the reference video. Default value: `true`
    </ParamField>

    <ParamField body="elements" type="list<KlingV3ImageElementInput>">
      Elements (characters/objects) to include. Reference in prompt as @Element1, @Element2.
    </ParamField>

    <ParamField body="shot_type" type="string" default="customize">
      The type of multi-shot video generation. Default value: `"customize"`
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
      Aspect ratio. Default value: `"auto"`

      Possible values: `auto`, `16:9`, `9:16`, `1:1`
    </ParamField>

    <ParamField body="duration" type="Enum">
      Video duration in seconds (3-15s for reference video).

      Possible values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Replace both character with @Element1 and @Element2",
      "video_url": "https://storage.googleapis.com/falserverless/example_inputs/kling-o3/standard-v2v-reference/video_reference.mp4",
      "image_urls": null,
      "keep_audio": false,
      "elements": [
        {
          "frontal_image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling-o3/standard-v2v-reference/element1_front.png",
          "reference_image_urls": [
            "https://storage.googleapis.com/falserverless/example_inputs/kling-o3/standard-v2v-reference/element1_reference1.png"
          ]
        },
        {
          "frontal_image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling-o3/standard-v2v-reference/element2_front.png",
          "reference_image_urls": [
            "https://storage.googleapis.com/falserverless/example_inputs/kling-o3/standard-v2v-reference/element2_reference1.png"
          ]
        }
      ],
      "shot_type": "customize",
      "aspect_ratio": "auto",
      "duration": "5"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "content_type": "video/mp4",
        "file_name": "output.mp4",
        "file_size": 7992288,
        "url": "https://storage.googleapis.com/falserverless/example_outputs/kling-o3/standard-v2v-reference/output.mp4"
      }
    }
    ```
  </Tab>
</Tabs>

## Related

* [Kling O3 Image to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o3-image-to-video) — Video Generation
* [Kling O3 Reference to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o3-reference-to-video) — Video Generation
* [Kling O3 Edit Video \[Pro\]](/model-api-reference/video-generation-api/kling-o3-edit-video) — Video Generation
* [Kling O3 Text to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o3-text-to-video) — Video Generation
* [Kling O3 Reference Video to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o3-reference-video-to-video) — Video Generation

## Limitations

* `aspect_ratio` restricted to: `auto`, `16:9`, `9:16`, `1:1`
