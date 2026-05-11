> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video O3 Standard Image To Video API

> API reference for Kling Video O3 Standard Image To Video. Generate a video by taking a start frame and an end frame, animating the transition between them while following text-driven style and scene g

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/o3/standard/image-to-video`
**Endpoint ID:** `fal-ai/kling-video/o3/standard/image-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/o3/standard/image-to-video/playground">
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
      "fal-ai/kling-video/o3/standard/image-to-video",
      arguments={
          "image_url": "https://v3b.fal.media/files/b/0a8cfd5a/8ABMp4n9rh3kfD2Rq8fHd_start_frame.png"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/kling-video/o3/standard/image-to-video", {
    input: {
        image_url: "https://v3b.fal.media/files/b/0a8cfd5a/8ABMp4n9rh3kfD2Rq8fHd_start_frame.png"
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
    --url https://fal.run/fal-ai/kling-video/o3/standard/image-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "image_url": "https://v3b.fal.media/files/b/0a8cfd5a/8ABMp4n9rh3kfD2Rq8fHd_start_frame.png"
  }'
  ```
</CodeGroup>

## Related

* [Kling O3 Image to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o3-image-to-video) — Video Generation
* [Kling O3 Reference to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o3-reference-to-video) — Video Generation
* [Kling O3 Edit Video \[Pro\]](/model-api-reference/video-generation-api/kling-o3-edit-video) — Video Generation
* [Kling O3 Text to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o3-text-to-video) — Video Generation
* [Kling O3 Reference Video to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o3-reference-video-to-video) — Video Generation

## Capabilities

* Text prompt input
* Image input
* Duration control

## API Reference

### Input Schema

<ParamField body="prompt" type="string">
  Text prompt for video generation. Either prompt or multi\_prompt must be provided, but not both.
</ParamField>

<ParamField body="image_url" type="string" required>
  URL of the start frame image.
</ParamField>

<ParamField body="end_image_url" type="string">
  URL of the end frame image (optional).
</ParamField>

<ParamField body="duration" type="DurationEnum" default="5">
  Video duration in seconds (3-15s). Default value: `"5"`

  Possible values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`
</ParamField>

<ParamField body="generate_audio" type="boolean" default="false">
  Whether to generate native audio for the video.
</ParamField>

<ParamField body="multi_prompt" type="list<KlingV3MultiPromptElement>">
  List of prompts for multi-shot video generation.
</ParamField>

<ParamField body="shot_type" type="string" default="customize">
  The type of multi-shot video generation. Default value: `"customize"`
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The generated video.
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "The character walks forward slowly, with the camera following from behind.",
  "image_url": "https://v3b.fal.media/files/b/0a8cfd5a/8ABMp4n9rh3kfD2Rq8fHd_start_frame.png",
  "end_image_url": "https://v3b.fal.media/files/b/0a8d0248/S415GcxackjjLKom6f3jq_VTImWrNO.png",
  "duration": "10",
  "generate_audio": false,
  "multi_prompt": null,
  "shot_type": "customize"
}
```

## Output Example

```json theme={null}
{
  "video": {
    "content_type": "video/mp4",
    "file_name": "output.mp4",
    "file_size": 12037975,
    "url": "https://v3b.fal.media/files/b/0a8d0278/pgIO9yOXTFCTetKBsqDwX_output.mp4"
  }
}
```
