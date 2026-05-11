> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedvr Upscale API

> API reference for Seedvr Upscale. Upscale your videos using SeedVR2 with temporal consistency!

**Endpoint:** `POST https://fal.run/fal-ai/seedvr/upscale/video`
**Endpoint ID:** `fal-ai/seedvr/upscale/video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/seedvr/upscale/video/playground">
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
      "fal-ai/seedvr/upscale/video",
      arguments={
          "video_url": "https://storage.googleapis.com/falserverless/example_inputs/seedvr-input.mp4"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/seedvr/upscale/video", {
    input: {
        video_url: "https://storage.googleapis.com/falserverless/example_inputs/seedvr-input.mp4"
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
    --url https://fal.run/fal-ai/seedvr/upscale/video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "video_url": "https://storage.googleapis.com/falserverless/example_inputs/seedvr-input.mp4"
  }'
  ```
</CodeGroup>

### Input Schema

<ParamField body="video_url" type="string" required>
  The input video to be processed
</ParamField>

<ParamField body="upscale_mode" type="UpscaleModeEnum" default="factor">
  The mode to use for the upscale. If 'target', the upscale factor will be calculated based on the target resolution. If 'factor', the upscale factor will be used directly. Default value: `"factor"`

  Possible values: `target`, `factor`
</ParamField>

<ParamField body="upscale_factor" type="float" default="2">
  Upscaling factor to be used. Will multiply the dimensions with this factor when `upscale_mode` is `factor`. Default value: `2`

  Range: `1` to `10`
</ParamField>

<ParamField body="target_resolution" type="TargetResolutionEnum" default="1080p">
  The target resolution to upscale to when `upscale_mode` is `target`. Default value: `"1080p"`

  Possible values: `720p`, `1080p`, `1440p`, `2160p`
</ParamField>

<ParamField body="seed" type="integer">
  The random seed used for the generation process.
</ParamField>

<ParamField body="noise_scale" type="float" default="0.1">
  The noise scale to use for the generation process. Default value: `0.1`

  Range: `0` to `1`, step: `0.001`
</ParamField>

<ParamField body="output_format" type="OutputFormatEnum" default="X264 (.mp4)">
  The format of the output video. Default value: `"X264 (.mp4)"`

  Possible values: `X264 (.mp4)`, `VP9 (.webm)`, `PRORES4444 (.mov)`, `GIF (.gif)`
</ParamField>

<ParamField body="output_quality" type="OutputQualityEnum" default="high">
  The quality of the output video. Default value: `"high"`

  Possible values: `low`, `medium`, `high`, `maximum`
</ParamField>

<ParamField body="output_write_mode" type="OutputWriteModeEnum" default="balanced">
  The write mode of the output video. Default value: `"balanced"`

  Possible values: `fast`, `balanced`, `small`
</ParamField>

<ParamField body="sync_mode" type="boolean" default="false">
  If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  Upscaled video file after processing
</ParamField>

<ParamField body="seed" type="integer" required>
  The random seed used for the generation process.
</ParamField>

### Input Example

```json theme={null}
{
  "video_url": "https://storage.googleapis.com/falserverless/example_inputs/seedvr-input.mp4",
  "upscale_mode": "factor",
  "upscale_factor": 2,
  "target_resolution": "1080p",
  "noise_scale": 0.1,
  "output_format": "X264 (.mp4)",
  "output_quality": "high",
  "output_write_mode": "balanced",
  "sync_mode": false
}
```

### Output Example

```json theme={null}
{
  "video": {
    "content_type": "video/mp4",
    "url": "https://storage.googleapis.com/falserverless/example_outputs/seedvr-output.mp4"
  }
}
```

## Related

* [SeedVR2](/model-api-reference/image-generation-api/seedvr2) — Image Generation

## Limitations

* `upscale_mode` restricted to: `target`, `factor`
* `upscale_factor` range: 1 to 10
* `target_resolution` restricted to: `720p`, `1080p`, `1440p`, `2160p`
* `noise_scale` range: 0 to 1 (step 0.001)
* `output_format` restricted to: `X264 (.mp4)`, `VP9 (.webm)`, `PRORES4444 (.mov)`, `GIF (.gif)`
* `output_quality` restricted to: `low`, `medium`, `high`, `maximum`
* `output_write_mode` restricted to: `fast`, `balanced`, `small`
