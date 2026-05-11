> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video V2.6 Standard API

> API reference for Kling Video V2.6 Standard. Transfer movements from a reference video to any character image. Cost-effective mode for motion transfer, perfect for portraits and simple animations.

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/v2.6/standard/motion-control`
**Endpoint ID:** `fal-ai/kling-video/v2.6/standard/motion-control`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v2.6/standard/motion-control/playground">
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
      "fal-ai/kling-video/v2.6/standard/motion-control",
      arguments={
          "image_url": "https://v3b.fal.media/files/b/0a875302/8NaxQrQxDNHppHtqcchMm.png",
          "video_url": "https://v3b.fal.media/files/b/0a8752bc/2xrNS217ngQ3wzXqA7LXr_output.mp4",
          "character_orientation": "video"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/kling-video/v2.6/standard/motion-control", {
    input: {
        image_url: "https://v3b.fal.media/files/b/0a875302/8NaxQrQxDNHppHtqcchMm.png",
        video_url: "https://v3b.fal.media/files/b/0a8752bc/2xrNS217ngQ3wzXqA7LXr_output.mp4",
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
    --url https://fal.run/fal-ai/kling-video/v2.6/standard/motion-control \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "image_url": "https://v3b.fal.media/files/b/0a875302/8NaxQrQxDNHppHtqcchMm.png",
    "video_url": "https://v3b.fal.media/files/b/0a8752bc/2xrNS217ngQ3wzXqA7LXr_output.mp4",
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

### Output Schema

<ParamField body="video" type="File" required>
  The generated video
</ParamField>

### Input Example

```json theme={null}
{
  "prompt": "An african american woman dancing",
  "image_url": "https://v3b.fal.media/files/b/0a875302/8NaxQrQxDNHppHtqcchMm.png",
  "video_url": "https://v3b.fal.media/files/b/0a8752bc/2xrNS217ngQ3wzXqA7LXr_output.mp4",
  "keep_original_sound": true,
  "character_orientation": "video"
}
```

### Output Example

```json theme={null}
{
  "video": {
    "content_type": "video/mp4",
    "file_name": "output.mp4",
    "file_size": 35299865,
    "url": "https://v3b.fal.media/files/b/0a875336/8p3rFiXtx3fE2TLoh59KP_output.mp4"
  }
}
```

## Related

* [Kling Video v2.6 Image to Video](/model-api-reference/video-generation-api/kling-video-v2.6-image-to-video) — Video Generation
* [Kling Video v2.6 Text to Video](/model-api-reference/video-generation-api/kling-video-v2.6-text-to-video) — Video Generation
* [Kling Video v2.6 Motion Control \[Pro\]](/model-api-reference/video-generation-api/kling-video-v2.6-motion-control) — Video Generation

## Limitations

* `character_orientation` restricted to: `image`, `video`
