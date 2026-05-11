> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Topaz Upscale API

> API reference for Topaz Upscale. Professional-grade video upscaling using Topaz technology. Enhance your videos with high-quality upscaling.

**Endpoint:** `POST https://fal.run/fal-ai/topaz/upscale/video`
**Endpoint ID:** `fal-ai/topaz/upscale/video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/topaz/upscale/video/playground">
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
      "fal-ai/topaz/upscale/video",
      arguments={
          "video_url": "https://v3.fal.media/files/kangaroo/y5-1YTGpun17eSeggZMzX_video-1733468228.mp4"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/topaz/upscale/video", {
    input: {
        video_url: "https://v3.fal.media/files/kangaroo/y5-1YTGpun17eSeggZMzX_video-1733468228.mp4"
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
    --url https://fal.run/fal-ai/topaz/upscale/video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "video_url": "https://v3.fal.media/files/kangaroo/y5-1YTGpun17eSeggZMzX_video-1733468228.mp4"
  }'
  ```
</CodeGroup>

## Examples

<video src="https://v3b.fal.media/files/b/0a9599a1/0xGqHNlfD6WlZqtpEx4Mu_video.mp4" controls width="100%" />

### Input Schema

<ParamField body="video_url" type="string" required>
  URL of the video to upscale
</ParamField>

<ParamField body="model" type="ModelEnum" default="Proteus">
  Video enhancement model. Proteus is best for most videos, Artemis for denoise+sharpen, Nyx for dedicated denoising, Gaia HQ/CG for rendered content, Gaia 2 for animation and motion graphics at 2x, and Starlight for generative diffusion-based upscaling and enhancement. Default value: `"Proteus"`

  Possible values: `Proteus`, `Artemis HQ`, `Artemis MQ`, `Artemis LQ`, `Nyx`, `Nyx Fast`, `Nyx XL`, `Nyx HF`, `Gaia HQ`, `Gaia CG`, `Gaia 2`, `Starlight Precise 1`, `Starlight Precise 2`, `Starlight Precise 2.5`, `Starlight HQ`, `Starlight Mini`, `Starlight Sharp`, `Starlight Fast 1`, `Starlight Fast 2`
</ParamField>

<ParamField body="upscale_factor" type="float" default="2">
  Factor to upscale the video by (e.g. 2.0 doubles width and height) Default value: `2`

  Range: `1` to `4`
</ParamField>

<ParamField body="target_fps" type="integer">
  Target FPS for frame interpolation. If set, frame interpolation will be enabled.

  Range: `16` to `60`
</ParamField>

<ParamField body="compression" type="float">
  Compression artifact removal level (0.0-1.0). Default varies by model.

  Range: `0` to `1`
</ParamField>

<ParamField body="noise" type="float">
  Noise reduction level (0.0-1.0). Default varies by model.

  Range: `0` to `1`
</ParamField>

<ParamField body="halo" type="float">
  Halo reduction level (0.0-1.0). Default varies by model.

  Range: `0` to `1`
</ParamField>

<ParamField body="grain" type="float">
  Film grain amount (0.0-1.0). Default varies by model.

  Range: `0` to `1`
</ParamField>

<ParamField body="recover_detail" type="float">
  Recover original detail level (0.0-1.0). Higher values preserve more original detail.

  Range: `0` to `1`
</ParamField>

<ParamField body="H264_output" type="boolean" default="false">
  Whether to use H264 codec for output video. Default is H265.
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The upscaled video file
</ParamField>

### Input Example

```json theme={null}
{
  "video_url": "https://v3.fal.media/files/kangaroo/y5-1YTGpun17eSeggZMzX_video-1733468228.mp4",
  "model": "Proteus",
  "upscale_factor": 2,
  "H264_output": false
}
```

### Output Example

```json theme={null}
{
  "video": {
    "url": "https://v3.fal.media/files/penguin/ztj_LB4gQlW6HIfVs8zX4_upscaled.mp4"
  }
}
```

## Limitations

* `upscale_factor` range: 1 to 4
* `target_fps` range: 16 to 60
* `compression` range: 0 to 1
* `noise` range: 0 to 1
* `halo` range: 0 to 1
* `grain` range: 0 to 1
* `recover_detail` range: 0 to 1
