> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Dreamactor API

> API reference for Bytedance Dreamactor. Transfer motion from a video to characters in an image using Dreamactor v2. Great performance for non-human and multiple characters

**Endpoint:** `POST https://fal.run/fal-ai/bytedance/dreamactor/v2`
**Endpoint ID:** `fal-ai/bytedance/dreamactor/v2`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/dreamactor/v2/playground">
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
      "fal-ai/bytedance/dreamactor/v2",
      arguments={
          "image_url": "https://v3b.fal.media/files/b/0a8d6292/E9WNRJh8K8DF9lSV0bkXs_image.png",
          "video_url": "https://v3b.fal.media/files/b/0a8d633f/u5Ye7jXL0Cfo0ijz5M6YY_input_example_dreamactor.mp4"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/bytedance/dreamactor/v2", {
    input: {
        image_url: "https://v3b.fal.media/files/b/0a8d6292/E9WNRJh8K8DF9lSV0bkXs_image.png",
        video_url: "https://v3b.fal.media/files/b/0a8d633f/u5Ye7jXL0Cfo0ijz5M6YY_input_example_dreamactor.mp4"
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
    --url https://fal.run/fal-ai/bytedance/dreamactor/v2 \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "image_url": "https://v3b.fal.media/files/b/0a8d6292/E9WNRJh8K8DF9lSV0bkXs_image.png",
    "video_url": "https://v3b.fal.media/files/b/0a8d633f/u5Ye7jXL0Cfo0ijz5M6YY_input_example_dreamactor.mp4"
  }'
  ```
</CodeGroup>

### Input Schema

<ParamField body="image_url" type="string" required>
  The URL of the reference image to animate. Supports real people, animation, pets, etc. Format: jpeg, jpg or png. Max size: 4.7 MB. Resolution: between 480x480 and 1920x1080 (larger images will be proportionally reduced).
</ParamField>

<ParamField body="video_url" type="string" required>
  The URL of the driving template video providing motion, facial expressions, and lip movement reference. Max duration: 30 seconds. Format: mp4, mov or webm. Resolution: between 200x200 and 2048x1440. Supports full face and body driving.
</ParamField>

<ParamField body="trim_first_second" type="boolean" default="true">
  Whether to crop the first second of the output video. The output has a 1-second transition at the beginning; enable this to remove it. Default value: `true`
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  Generated video file.
</ParamField>

### Input Example

```json theme={null}
{
  "image_url": "https://v3b.fal.media/files/b/0a8d6292/E9WNRJh8K8DF9lSV0bkXs_image.png",
  "video_url": "https://v3b.fal.media/files/b/0a8d633f/u5Ye7jXL0Cfo0ijz5M6YY_input_example_dreamactor.mp4",
  "trim_first_second": true
}
```

### Output Example

```json theme={null}
{
  "video": {
    "url": "https://v3b.fal.media/files/b/0a8d6313/ONsZwYeJrFqi1W1jbnfYF_9HU7tPvX1hUlMMxXCepTz_video%20(1)%20(1).mp4"
  }
}
```
