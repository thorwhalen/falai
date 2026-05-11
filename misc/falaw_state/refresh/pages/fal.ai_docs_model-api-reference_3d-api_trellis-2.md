> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Trellis 2 API

> API reference for Trellis 2. Generate 3D models from your images using Trellis 2. A native 3D generative model enabling versatile and high-quality 3D asset creation.

**Endpoint:** `POST https://fal.run/fal-ai/trellis-2`
**Endpoint ID:** `fal-ai/trellis-2`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/trellis-2/playground">
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
      "fal-ai/trellis-2",
      arguments={
          "image_url": "https://v3b.fal.media/files/b/0a86b60d/xkpao5B0uxmH0tmJm0HVL_2fe35ce1-fe44-475b-b582-6846a149537c.png"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/trellis-2", {
    input: {
        image_url: "https://v3b.fal.media/files/b/0a86b60d/xkpao5B0uxmH0tmJm0HVL_2fe35ce1-fe44-475b-b582-6846a149537c.png"
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
    --url https://fal.run/fal-ai/trellis-2 \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "image_url": "https://v3b.fal.media/files/b/0a86b60d/xkpao5B0uxmH0tmJm0HVL_2fe35ce1-fe44-475b-b582-6846a149537c.png"
  }'
  ```
</CodeGroup>

## Capabilities

* Reproducible generation (seed)
* Image input

## API Reference

### Input Schema

<ParamField body="seed" type="integer">
  Random seed for reproducibility
</ParamField>

<ParamField body="resolution" type="ResolutionEnum" default="1024">
  Output resolution; higher is slower but more detailed Default value: `"1024"`

  Possible values: `512`, `1024`, `1536`
</ParamField>

<ParamField body="ss_guidance_strength" type="float" default="7.5">
  How closely the initial 3D structure follows the input image. Higher values produce more faithful but potentially noisier results. Default value: `7.5`

  Range: `0` to `10`
</ParamField>

<ParamField body="ss_guidance_rescale" type="float" default="0.7">
  Dampens artifacts from high guidance in stage 1. Lower values allow stronger guidance effects, higher values stabilize the output. Default value: `0.7`

  Range: `0` to `1`
</ParamField>

<ParamField body="ss_sampling_steps" type="integer" default="12">
  Number of denoising steps for the initial structure. More steps = slower but potentially higher quality. Default value: `12`

  Range: `1` to `50`
</ParamField>

<ParamField body="ss_rescale_t" type="float" default="5">
  Controls noise schedule sharpness for structure generation. Higher values produce sharper transitions. Default value: `5`

  Range: `1` to `6`
</ParamField>

<ParamField body="shape_slat_guidance_strength" type="float" default="7.5">
  How closely the detailed geometry follows the input image. Higher values add more detail but may introduce noise. Default value: `7.5`

  Range: `0` to `10`
</ParamField>

<ParamField body="shape_slat_guidance_rescale" type="float" default="0.5">
  Dampens artifacts from high guidance in the shape stage. Increase if you see noisy geometry. Default value: `0.5`

  Range: `0` to `1`
</ParamField>

<ParamField body="shape_slat_sampling_steps" type="integer" default="12">
  Number of denoising steps for shape refinement. More steps = slower but potentially smoother geometry. Default value: `12`

  Range: `1` to `50`
</ParamField>

<ParamField body="shape_slat_rescale_t" type="float" default="3">
  Controls noise schedule sharpness for shape refinement. Higher values produce sharper geometric details. Default value: `3`

  Range: `1` to `6`
</ParamField>

<ParamField body="tex_slat_guidance_strength" type="float" default="1">
  How closely the texture follows the input image colors. Higher values produce more vivid but potentially oversaturated textures. Default value: `1`

  Range: `0` to `10`
</ParamField>

<ParamField body="tex_slat_guidance_rescale" type="float" default="0">
  Dampens artifacts from high guidance in the texture stage. Increase if textures look noisy or have color banding.

  Range: `0` to `1`
</ParamField>

<ParamField body="tex_slat_sampling_steps" type="integer" default="12">
  Number of denoising steps for texture generation. More steps = slower but potentially cleaner textures. Default value: `12`

  Range: `1` to `50`
</ParamField>

<ParamField body="tex_slat_rescale_t" type="float" default="3">
  Controls noise schedule sharpness for texture generation. Higher values produce sharper texture details. Default value: `3`

  Range: `1` to `6`
</ParamField>

<ParamField body="decimation_target" type="integer" default="500000">
  Target number of vertices in the final mesh. Lower values produce smaller files but less detail. 500k is good for most uses, reduce to 20k-50k for web/mobile. Default value: `500000`

  Range: `5000` to `2000000`
</ParamField>

<ParamField body="texture_size" type="TextureSizeEnum" default="2048">
  Resolution of the texture image baked onto the mesh. Higher values capture finer surface details but produce larger files. Default value: `"2048"`

  Possible values: `1024`, `2048`, `4096`
</ParamField>

<ParamField body="remesh" type="boolean" default="true">
  Rebuild the mesh topology for cleaner triangles. Slower but usually produces better results for downstream use (animation, 3D printing, etc). Default value: `true`
</ParamField>

<ParamField body="remesh_band" type="float" default="1">
  Controls how far remeshing can move vertices from the original surface. Higher values allow more smoothing but may lose fine details. Default value: `1`

  Range: `0` to `4`
</ParamField>

<ParamField body="remesh_project" type="float" default="0">
  How much to project remeshed vertices back onto the original surface. 0 = no projection (smoother), 1 = full projection (preserves detail).

  Range: `0` to `1`
</ParamField>

<ParamField body="image_url" type="string" required>
  URL of the input image to convert to 3D
</ParamField>

### Output Schema

<ParamField body="model_glb" type="File" required>
  Generated 3D GLB file
</ParamField>

## Input Example

```json theme={null}
{
  "resolution": 1024,
  "ss_guidance_strength": 7.5,
  "ss_guidance_rescale": 0.7,
  "ss_sampling_steps": 12,
  "ss_rescale_t": 5,
  "shape_slat_guidance_strength": 7.5,
  "shape_slat_guidance_rescale": 0.5,
  "shape_slat_sampling_steps": 12,
  "shape_slat_rescale_t": 3,
  "tex_slat_guidance_strength": 1,
  "tex_slat_guidance_rescale": 0,
  "tex_slat_sampling_steps": 12,
  "tex_slat_rescale_t": 3,
  "decimation_target": 500000,
  "texture_size": 2048,
  "remesh": true,
  "remesh_band": 1,
  "remesh_project": 0,
  "image_url": "https://v3b.fal.media/files/b/0a86b60d/xkpao5B0uxmH0tmJm0HVL_2fe35ce1-fe44-475b-b582-6846a149537c.png"
}
```

## Output Example

```json theme={null}
{
  "model_glb": {
    "url": "https://v3b.fal.media/files/b/0a86b61d/DNmTkiWHUQ8k-rG6aussB_trellis2_68d6300f70f34d23b69a912b5fe60487.glb"
  }
}
```

## Limitations

* `resolution` restricted to: `512`, `1024`, `1536`
* `ss_guidance_strength` range: 0 to 10
* `ss_guidance_rescale` range: 0 to 1
* `ss_sampling_steps` range: 1 to 50
* `ss_rescale_t` range: 1 to 6
* `shape_slat_guidance_strength` range: 0 to 10
* `shape_slat_guidance_rescale` range: 0 to 1
* `shape_slat_sampling_steps` range: 1 to 50
* `shape_slat_rescale_t` range: 1 to 6
* `tex_slat_guidance_strength` range: 0 to 10
* `tex_slat_guidance_rescale` range: 0 to 1
* `tex_slat_sampling_steps` range: 1 to 50
* `tex_slat_rescale_t` range: 1 to 6
* `decimation_target` range: 5000 to 2000000
* `texture_size` restricted to: `1024`, `2048`, `4096`
* `remesh_band` range: 0 to 4
* `remesh_project` range: 0 to 1
