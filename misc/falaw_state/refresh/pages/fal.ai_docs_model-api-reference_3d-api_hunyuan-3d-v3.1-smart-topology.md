> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hunyuan 3d V3.1 Smart Topology API

> API reference for Hunyuan 3d V3.1 Smart Topology. Optimize 3D mesh topology with Hunyuan 3D Smart Topology.

**Endpoint:** `POST https://fal.run/fal-ai/hunyuan-3d/v3.1/smart-topology`
**Endpoint ID:** `fal-ai/hunyuan-3d/v3.1/smart-topology`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/hunyuan-3d/v3.1/smart-topology/playground">
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
      "fal-ai/hunyuan-3d/v3.1/smart-topology",
      arguments={},
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/hunyuan-3d/v3.1/smart-topology", {
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
    --url https://fal.run/fal-ai/hunyuan-3d/v3.1/smart-topology \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{}'
  ```
</CodeGroup>

## Related

* [Hunyuan 3D Pro Image to 3D](/model-api-reference/3d-api/hunyuan-3d-pro-image-to-3d) — 3D
* [Hunyuan 3D Pro Text to 3D](/model-api-reference/3d-api/hunyuan-3d-pro-text-to-3d) — 3D
* [Hunyuan 3D Rapid Image to 3D](/model-api-reference/3d-api/hunyuan-3d-rapid-image-to-3d) — 3D
* [Hunyuan 3d](/model-api-reference/3d-api/hunyuan-3d) — 3D
* [Hunyuan 3D Part Splitter](/model-api-reference/3d-api/hunyuan-3d-part-splitter) — 3D

## API Reference

### Input Schema

<ParamField body="input_file_url" type="string" default="https://v3b.fal.media/files/b/0a8c09c0/VYDiCTcDGK55qY2-idGbX_model.glb">
  URL of GLB or OBJ file to optimize topology. Max size: 200MB. Default value: `"https://v3b.fal.media/files/b/0a8c09c0/VYDiCTcDGK55qY2-idGbX_model.glb"`
</ParamField>

<ParamField body="input_file_type" type="InputFileTypeEnum" default="glb">
  Input 3D file format. Default value: `"glb"`

  Possible values: `glb`, `obj`
</ParamField>

<ParamField body="polygon_type" type="PolygonTypeEnum" default="triangle">
  Output polygon type. triangle: triangular faces only. quadrilateral: mixed quad and triangle faces. Default value: `"triangle"`

  Possible values: `triangle`, `quadrilateral`
</ParamField>

<ParamField body="face_level" type="FaceLevelEnum" default="medium">
  Target polygon density. high: more detail/polygons, medium: balanced, low: fewer polygons. Default value: `"medium"`

  Possible values: `high`, `medium`, `low`
</ParamField>

### Output Schema

<ParamField body="model_glb" type="File" required>
  Processed 3D model with optimized topology (primary file).
</ParamField>

<ParamField body="model_urls" type="ModelUrls" required>
  URLs for different 3D model formats
</ParamField>

## Input Example

```json theme={null}
{
  "input_file_url": "https://v3b.fal.media/files/b/0a8c09c0/VYDiCTcDGK55qY2-idGbX_model.glb",
  "input_file_type": "glb",
  "polygon_type": "triangle",
  "face_level": "medium"
}
```

## Output Example

```json theme={null}
{
  "model_glb": {
    "content_type": "model/obj",
    "file_name": "model.obj",
    "file_size": 394409,
    "url": "https://v3b.fal.media/files/b/0a8c0ab4/tqMY5NJLnHjpwN8rQ15dj_model.obj"
  },
  "model_urls": {
    "glb": {
      "content_type": "model/gltf-binary",
      "file_name": "model.glb",
      "file_size": 206004,
      "url": "https://v3b.fal.media/files/b/0a8c0ab4/eX-_x0Wv8fZL05l9CGp6Y_model.glb"
    },
    "obj": {
      "content_type": "model/obj",
      "file_name": "model.obj",
      "file_size": 394409,
      "url": "https://v3b.fal.media/files/b/0a8c0ab4/tqMY5NJLnHjpwN8rQ15dj_model.obj"
    }
  }
}
```

## Limitations

* `input_file_type` restricted to: `glb`, `obj`
* `polygon_type` restricted to: `triangle`, `quadrilateral`
* `face_level` restricted to: `high`, `medium`, `low`
