> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video O1 Standard Image To Video API

> API reference for Kling Video O1 Standard Image To Video. Generate a video by taking a start frame and an end frame, animating the transition between them while following text-driven style and scene g

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/o1/standard/image-to-video`
**Endpoint ID:** `fal-ai/kling-video/o1/standard/image-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/o1/standard/image-to-video/playground">
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
      "fal-ai/kling-video/o1/standard/image-to-video",
      arguments={
          "prompt": "Create a magical timelapse transition. The snow melts rapidly to reveal green grass, and the tree branches burst into bloom with pink flowers in real-time. The lighting shifts from cold winter light to warm spring sunshine. The camera pushes in slowly towards the tree. Disney-style magical transformation, cinematic, 8k.",
          "start_image_url": "https://v3b.fal.media/files/b/rabbit/NaslJIC7F2WodS6DFZRRJ.png"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/kling-video/o1/standard/image-to-video", {
    input: {
        prompt: "Create a magical timelapse transition. The snow melts rapidly to reveal green grass, and the tree branches burst into bloom with pink flowers in real-time. The lighting shifts from cold winter light to warm spring sunshine. The camera pushes in slowly towards the tree. Disney-style magical transformation, cinematic, 8k.",
        start_image_url: "https://v3b.fal.media/files/b/rabbit/NaslJIC7F2WodS6DFZRRJ.png"
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
    --url https://fal.run/fal-ai/kling-video/o1/standard/image-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "Create a magical timelapse transition. The snow melts rapidly to reveal green grass, and the tree branches burst into bloom with pink flowers in real-time. The lighting shifts from cold winter light to warm spring sunshine. The camera pushes in slowly towards the tree. Disney-style magical transformation, cinematic, 8k.",
    "start_image_url": "https://v3b.fal.media/files/b/rabbit/NaslJIC7F2WodS6DFZRRJ.png"
  }'
  ```
</CodeGroup>

## Related

* [Kling O1 First Frame Last Frame to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-first-frame-last-frame-to-video) — Video Generation
* [Kling O1 Edit Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-edit-video) — Video Generation
* [Kling O1 Reference Image to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-reference-image-to-video) — Video Generation
* [Kling O1 Reference Video to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-reference-video-to-video) — Video Generation

## Capabilities

* Text prompt input
* Duration control

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required>
  Use @Image1 to reference the start frame, @Image2 to reference the end frame.
</ParamField>

<ParamField body="start_image_url" type="string" required>
  Image to use as the first frame of the video.

  Max file size: 10.0MB, Min width: 300px, Min height: 300px, Min aspect ratio: 0.40, Max aspect ratio: 2.50, Timeout: 20.0s
</ParamField>

<ParamField body="end_image_url" type="string">
  Image to use as the last frame of the video.
</ParamField>

<ParamField body="duration" type="DurationEnum" default="5">
  Video duration in seconds. Default value: `"5"`

  Possible values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The generated video.
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "Create a magical timelapse transition. The snow melts rapidly to reveal green grass, and the tree branches burst into bloom with pink flowers in real-time. The lighting shifts from cold winter light to warm spring sunshine. The camera pushes in slowly towards the tree. Disney-style magical transformation, cinematic, 8k.",
  "start_image_url": "https://v3b.fal.media/files/b/rabbit/NaslJIC7F2WodS6DFZRRJ.png",
  "end_image_url": "https://v3b.fal.media/files/b/tiger/BwHi22qoQnqaTNMMhe533.png",
  "duration": "5"
}
```

## Output Example

```json theme={null}
{
  "video": {
    "content_type": "video/mp4",
    "file_name": "output.mp4",
    "file_size": 27588984,
    "url": "https://v3b.fal.media/files/b/koala/knryyyGF3ZVyMMrGr77CL_output.mp4"
  }
}
```

## Limitations

* `duration` restricted to: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`
