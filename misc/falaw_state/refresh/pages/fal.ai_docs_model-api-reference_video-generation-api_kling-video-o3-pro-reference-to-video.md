> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video O3 Pro Reference To Video API

> API reference for Kling Video O3 Pro Reference To Video. Transform images, elements, and text into consistent, high-quality video scenes, ensuring stable character identity, object details, and enviro

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/o3/pro/reference-to-video`
**Endpoint ID:** `fal-ai/kling-video/o3/pro/reference-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/o3/pro/reference-to-video/playground">
  Run this model interactively with your own prompts.
</Card>

## Quick Start

<CodeGroup>
  ```python title="Python" theme={null}
  import fal_client

  def on_queue_update(update):
      if isinstance(update, fal_client.InProgress):
          for log in update.logs:
             print(log["message"])

  result = fal_client.subscribe(
      "fal-ai/kling-video/o3/pro/reference-to-video",
      arguments={},
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/kling-video/o3/pro/reference-to-video", {
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
    --url https://fal.run/fal-ai/kling-video/o3/pro/reference-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{}'
  ```
</CodeGroup>

## Related

* [Kling O3 Image to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o3-image-to-video) — Video Generation
* [Kling O3 Edit Video \[Pro\]](/model-api-reference/video-generation-api/kling-o3-edit-video) — Video Generation
* [Kling O3 Reference to Video \[Standard\]](/model-api-reference/video-generation-api/kling-o3-reference-to-video) — Video Generation
* [Kling O3 Text to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o3-text-to-video) — Video Generation
* [Kling O3 Reference Video to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o3-reference-video-to-video) — Video Generation

## Capabilities

* Text prompt input
* Duration control
* Aspect ratio control

## API Reference

### Input Schema

<ParamField body="prompt" type="string">
  Text prompt for video generation. Either prompt or multi\_prompt must be provided, but not both.
</ParamField>

<ParamField body="multi_prompt" type="list<KlingV3MultiPromptElement>">
  List of prompts for multi-shot video generation.
</ParamField>

<ParamField body="start_image_url" type="string">
  Image to use as the first frame of the video.
</ParamField>

<ParamField body="end_image_url" type="string">
  Image to use as the last frame of the video.
</ParamField>

<ParamField body="image_urls" type="list<string>">
  Reference images for style/appearance. Reference in prompt as @Image1, @Image2, etc. Maximum 4 total (elements + reference images) when using video.
</ParamField>

<ParamField body="elements" type="list<KlingV3ComboElementInput>">
  Elements (characters/objects) to include. Reference in prompt as @Element1, @Element2.
</ParamField>

<ParamField body="generate_audio" type="boolean" default="false">
  Whether to generate native audio for the video.
</ParamField>

<ParamField body="duration" type="DurationEnum" default="5">
  Video duration in seconds (3-15s). Default value: `"5"`

  Possible values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`
</ParamField>

<ParamField body="shot_type" type="string" default="customize">
  The type of multi-shot video generation. Default value: `"customize"`
</ParamField>

<ParamField body="aspect_ratio" type="AspectRatioEnum" default="16:9">
  The aspect ratio of the generated video frame. Default value: `"16:9"`

  Possible values: `16:9`, `9:16`, `1:1`
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The generated video.
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "@Element1 and @Element2 enters the scene from two sides. Elephant starts to play with the ball",
  "multi_prompt": null,
  "start_image_url": "https://v3b.fal.media/files/b/0a8d1b38/myilPNN_WYdJCmpTy4Sjr_6XNBi9Mm.png",
  "elements": [
    {
      "frontal_image_url": "https://v3b.fal.media/files/b/0a8d1b2e/yiHiZP1Now0V5JC5_OClE_PaKOtOGJ.png",
      "reference_image_urls": [
        "https://v3b.fal.media/files/b/0a8d1b1a/eZfSbcQ58EzD_l2SEbevg_F3U9GMLK.png"
      ]
    },
    {
      "frontal_image_url": "https://v3b.fal.media/files/b/0a8d1b19/_eIj7GjmI5zgQkMN936YJ_2f3hZ7Xb.png",
      "reference_image_urls": [
        "https://v3b.fal.media/files/b/0a8d1b3c/_ZE2iIjkb-Eun3WXXGP4x_TSG1ELBo.png"
      ]
    }
  ],
  "generate_audio": false,
  "duration": "8",
  "shot_type": "customize",
  "aspect_ratio": "16:9"
}
```

## Output Example

```json theme={null}
{
  "video": {
    "content_type": "video/mp4",
    "file_name": "output.mp4",
    "file_size": 18468404,
    "url": "https://v3b.fal.media/files/b/0a8d1c8a/ZxdKrvPb3CQEmeuS-u_kU_output.mp4"
  }
}
```

## Limitations

* `aspect_ratio` restricted to: `16:9`, `9:16`, `1:1`
