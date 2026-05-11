> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hunyuan 3d V3.1 Part API

> API reference for Hunyuan 3d V3.1 Part. Split 3D models into parts with Hunyuan 3D

**Endpoint:** `POST https://fal.run/fal-ai/hunyuan-3d/v3.1/part`
**Endpoint ID:** `fal-ai/hunyuan-3d/v3.1/part`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/hunyuan-3d/v3.1/part/playground">
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
      "fal-ai/hunyuan-3d/v3.1/part",
      arguments={
          "input_file_url": "https://v3b.fal.media/files/b/0a8bf92a/XECcItG5QHt0LViFTRCON_converted.fbx"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/hunyuan-3d/v3.1/part", {
    input: {
        input_file_url: "https://v3b.fal.media/files/b/0a8bf92a/XECcItG5QHt0LViFTRCON_converted.fbx"
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
    --url https://fal.run/fal-ai/hunyuan-3d/v3.1/part \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "input_file_url": "https://v3b.fal.media/files/b/0a8bf92a/XECcItG5QHt0LViFTRCON_converted.fbx"
  }'
  ```
</CodeGroup>

## Related

* [Hunyuan 3D Pro Image to 3D](/model-api-reference/3d-api/hunyuan-3d-pro-image-to-3d) — 3D
* [Hunyuan 3D Pro Text to 3D](/model-api-reference/3d-api/hunyuan-3d-pro-text-to-3d) — 3D
* [Hunyuan 3D Rapid Image to 3D](/model-api-reference/3d-api/hunyuan-3d-rapid-image-to-3d) — 3D
* [Hunyuan 3d](/model-api-reference/3d-api/hunyuan-3d) — 3D
* [Hunyuan 3D Smart Topology](/model-api-reference/3d-api/hunyuan-3d-smart-topology) — 3D

## API Reference

### Input Schema

<ParamField body="input_file_url" type="string" required>
  URL of FBX file to split into parts. ONLY FBX format supported. Max size: 100MB, face count ≤30,000. Recommended: AIGC-generated models.
</ParamField>

### Output Schema

<ParamField body="result_files" type="list<File>" required>
  List of generated part files in FBX format
</ParamField>

## Input Example

```json theme={null}
{
  "input_file_url": "https://v3b.fal.media/files/b/0a8bf92a/XECcItG5QHt0LViFTRCON_converted.fbx"
}
```

## Output Example

```json theme={null}
{
  "result_files": [
    {
      "content_type": "application/octet-stream",
      "file_name": "part_0.fbx",
      "file_size": 2048000,
      "url": "https://v3b.fal.media/files/b/0a8bf94b/zOP--lT23slziGKp99dJm_part_0.fbx"
    }
  ]
}
```
