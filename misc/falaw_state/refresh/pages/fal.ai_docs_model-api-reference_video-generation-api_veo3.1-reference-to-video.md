> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Veo3.1 Reference To Video API

> API reference for Veo3.1 Reference To Video. Generate Videos from images using Google's Veo 3.1

**Endpoint:** `POST https://fal.run/fal-ai/veo3.1/reference-to-video`
**Endpoint ID:** `fal-ai/veo3.1/reference-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/veo3.1/reference-to-video/playground">
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
      "fal-ai/veo3.1/reference-to-video",
      arguments={
          "prompt": "A chimpanzee wearing overalls frolics in the grassy field, gently playing with the butterflies. In the background, a circus tent and carousel beckon.",
          "image_urls": [
              "https://storage.googleapis.com/falserverless/example_inputs/veo31-r2v-input-1.png",
              "https://storage.googleapis.com/falserverless/example_inputs/veo31-r2v-input-2.png",
              "https://storage.googleapis.com/falserverless/example_inputs/veo31-r2v-input-3.png"
          ]
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/veo3.1/reference-to-video", {
    input: {
        prompt: "A chimpanzee wearing overalls frolics in the grassy field, gently playing with the butterflies. In the background, a circus tent and carousel beckon.",
        image_urls: [
          "https://storage.googleapis.com/falserverless/example_inputs/veo31-r2v-input-1.png",
          "https://storage.googleapis.com/falserverless/example_inputs/veo31-r2v-input-2.png",
          "https://storage.googleapis.com/falserverless/example_inputs/veo31-r2v-input-3.png"
        ]
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
    --url https://fal.run/fal-ai/veo3.1/reference-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "A chimpanzee wearing overalls frolics in the grassy field, gently playing with the butterflies. In the background, a circus tent and carousel beckon.",
    "image_urls": [
      "https://storage.googleapis.com/falserverless/example_inputs/veo31-r2v-input-1.png",
      "https://storage.googleapis.com/falserverless/example_inputs/veo31-r2v-input-2.png",
      "https://storage.googleapis.com/falserverless/example_inputs/veo31-r2v-input-3.png"
    ]
  }'
  ```
</CodeGroup>

## Related

* [Veo 3.1](/model-api-reference/video-generation-api/veo-3.1) — Video Generation
* [Veo 3.1 Fast](/model-api-reference/video-generation-api/veo-3.1-fast) — Video Generation
* [Veo3.1 Lite Image to Video](/model-api-reference/video-generation-api/veo3.1-lite-image-to-video) — Video Generation
* [Veo3.1 Lite FLF](/model-api-reference/video-generation-api/veo3.1-lite-flf) — Video Generation
* [Veo3.1 Lite Text to Video](/model-api-reference/video-generation-api/veo3.1-lite-text-to-video) — Video Generation

## Capabilities

* Text prompt input
* Aspect ratio control
* Duration control

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required>
  The text prompt describing the video you want to generate
</ParamField>

<ParamField body="aspect_ratio" type="AspectRatioEnum" default="16:9">
  The aspect ratio of the generated video. Default value: `"16:9"`

  Possible values: `16:9`, `9:16`
</ParamField>

<ParamField body="duration" type="string" default="8s">
  The duration of the generated video. Default value: `"8s"`
</ParamField>

<ParamField body="resolution" type="ResolutionEnum" default="720p">
  The resolution of the generated video. Default value: `"720p"`

  Possible values: `720p`, `1080p`, `4k`
</ParamField>

<ParamField body="generate_audio" type="boolean" default="true">
  Whether to generate audio for the video. Default value: `true`
</ParamField>

<ParamField body="auto_fix" type="boolean" default="false">
  Whether to automatically attempt to fix prompts that fail content policy or other validation checks by rewriting them.
</ParamField>

<ParamField body="safety_tolerance" type="SafetyToleranceEnum" default="4">
  The safety tolerance level for content moderation. 1 is the most strict (blocks most content), 6 is the least strict. Default value: `"4"`

  Possible values: `1`, `2`, `3`, `4`, `5`, `6`
</ParamField>

<ParamField body="image_urls" type="list<string>" required>
  URLs of the reference images to use for consistent subject appearance
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The generated video.
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "A chimpanzee wearing overalls frolics in the grassy field, gently playing with the butterflies. In the background, a circus tent and carousel beckon.",
  "aspect_ratio": "16:9",
  "duration": "8s",
  "resolution": "720p",
  "generate_audio": true,
  "auto_fix": false,
  "safety_tolerance": "4",
  "image_urls": [
    "https://storage.googleapis.com/falserverless/example_inputs/veo31-r2v-input-1.png",
    "https://storage.googleapis.com/falserverless/example_inputs/veo31-r2v-input-2.png",
    "https://storage.googleapis.com/falserverless/example_inputs/veo31-r2v-input-3.png"
  ]
}
```

## Output Example

```json theme={null}
{
  "video": {
    "url": "https://storage.googleapis.com/falserverless/example_outputs/veo31-r2v-output.mp4"
  }
}
```

## Limitations

* `aspect_ratio` restricted to: `16:9`, `9:16`
* `resolution` restricted to: `720p`, `1080p`, `4k`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`, `6`
