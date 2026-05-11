> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Seedance V1 Pro Text To Video API

> API reference for Bytedance Seedance V1 Pro Text To Video. Seedance 1.0 Pro, a high quality video generation model developed by Bytedance.

**Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedance/v1/pro/text-to-video`
**Endpoint ID:** `fal-ai/bytedance/seedance/v1/pro/text-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedance/v1/pro/text-to-video/playground">
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
      "fal-ai/bytedance/seedance/v1/pro/text-to-video",
      arguments={
          "prompt": "A bright blue race car speeds along a snowy racetrack. [Low-angle shot] Captures several cars speeding along the racetrack through a harsh snowstorm. [Overhead shot] The camera gradually pulls upward, revealing the full race scene illuminated by storm lights"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/bytedance/seedance/v1/pro/text-to-video", {
    input: {
        prompt: "A bright blue race car speeds along a snowy racetrack. [Low-angle shot] Captures several cars speeding along the racetrack through a harsh snowstorm. [Overhead shot] The camera gradually pulls upward, revealing the full race scene illuminated by storm lights"
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
    --url https://fal.run/fal-ai/bytedance/seedance/v1/pro/text-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "A bright blue race car speeds along a snowy racetrack. [Low-angle shot] Captures several cars speeding along the racetrack through a harsh snowstorm. [Overhead shot] The camera gradually pulls upward, revealing the full race scene illuminated by storm lights"
  }'
  ```
</CodeGroup>

## Related

* [Seedance 1.0 Pro](/model-api-reference/video-generation-api/seedance-1.0-pro) — Video Generation
* [Seedance 1.0 Lite](/model-api-reference/video-generation-api/seedance-1.0-lite) — Video Generation
* [Bytedance](/model-api-reference/video-generation-api/bytedance) — Video Generation

## Capabilities

* Text prompt input
* Aspect ratio control
* Duration control
* Reproducible generation (seed)
* Safety checker
* Frame count control

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required>
  The text prompt used to generate the video
</ParamField>

<ParamField body="aspect_ratio" type="AspectRatioEnum" default="16:9">
  The aspect ratio of the generated video Default value: `"16:9"`

  Possible values: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
</ParamField>

<ParamField body="resolution" type="ResolutionEnum" default="1080p">
  Video resolution - 480p for faster generation, 720p for balance, 1080p for higher quality Default value: `"1080p"`

  Possible values: `480p`, `720p`, `1080p`
</ParamField>

<ParamField body="duration" type="DurationEnum" default="5">
  Duration of the video in seconds Default value: `"5"`

  Possible values: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`
</ParamField>

<ParamField body="camera_fixed" type="boolean" default="false">
  Whether to fix the camera position
</ParamField>

<ParamField body="seed" type="integer">
  Random seed to control video generation. Use -1 for random.
</ParamField>

<ParamField body="enable_safety_checker" type="boolean" default="true">
  If set to true, the safety checker will be enabled. Default value: `true`
</ParamField>

<ParamField body="num_frames" type="integer">
  The number of frames to generate. If provided, will override duration.

  Range: `29` to `289`
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  Generated video file
</ParamField>

<ParamField body="seed" type="integer" required>
  Seed used for generation
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "A bright blue race car speeds along a snowy racetrack. [Low-angle shot] Captures several cars speeding along the racetrack through a harsh snowstorm. [Overhead shot] The camera gradually pulls upward, revealing the full race scene illuminated by storm lights",
  "aspect_ratio": "16:9",
  "resolution": "1080p",
  "duration": "5",
  "camera_fixed": false,
  "enable_safety_checker": true
}
```

## Output Example

```json theme={null}
{
  "video": {
    "url": "https://storage.googleapis.com/falserverless/example_inputs/seedance_pro_t2v.mp4"
  },
  "seed": 42
}
```

## Limitations

* `aspect_ratio` restricted to: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
* `resolution` restricted to: `480p`, `720p`, `1080p`
* `num_frames` range: 29 to 289
* Content moderation via safety checker
