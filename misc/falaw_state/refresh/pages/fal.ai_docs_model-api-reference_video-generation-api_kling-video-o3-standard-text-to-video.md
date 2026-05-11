> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video O3 Standard Text To Video API

> API reference for Kling Video O3 Standard Text To Video. Generate realistic videos using Kling O3 from Kling Team!

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/o3/standard/text-to-video`
**Endpoint ID:** `fal-ai/kling-video/o3/standard/text-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/o3/standard/text-to-video/playground">
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
      "fal-ai/kling-video/o3/standard/text-to-video",
      arguments={},
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/kling-video/o3/standard/text-to-video", {
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
    --url https://fal.run/fal-ai/kling-video/o3/standard/text-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{}'
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
* Duration control
* Aspect ratio control

## API Reference

### Input Schema

<ParamField body="prompt" type="string">
  Text prompt for video generation. Required unless multi\_prompt is provided.
</ParamField>

<ParamField body="duration" type="DurationEnum" default="5">
  Video duration in seconds (3-15s). Default value: `"5"`

  Possible values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`
</ParamField>

<ParamField body="aspect_ratio" type="AspectRatioEnum" default="16:9">
  Aspect ratio of the generated video. Default value: `"16:9"`

  Possible values: `16:9`, `9:16`, `1:1`
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
  "prompt": "A mecha lands on the ground to save the city, and says \"I'm here\", in anime style",
  "duration": "5",
  "aspect_ratio": "16:9",
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
    "file_size": 13096952,
    "url": "https://v3b.fal.media/files/b/0a8d04e2/idOb9V-Q9ujlggPSKqsfS_output.mp4"
  }
}
```

## Limitations

* `aspect_ratio` restricted to: `16:9`, `9:16`, `1:1`
