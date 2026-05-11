> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hunyuan 3d V3.1 Pro API

> API reference for Hunyuan 3d V3.1 Pro. Generate 3D models from images with Hunyuan 3D Pro

<Tabs>
  <Tab title="Image To 3d">
    **Endpoint:** `POST https://fal.run/fal-ai/hunyuan-3d/v3.1/pro/image-to-3d`
    **Endpoint ID:** `fal-ai/hunyuan-3d/v3.1/pro/image-to-3d`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/hunyuan-3d/v3.1/pro/image-to-3d/playground">
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
          "fal-ai/hunyuan-3d/v3.1/pro/image-to-3d",
          arguments={
              "input_image_url": "https://v3b.fal.media/files/b/0a8c3155/BTXNRrzOFsO6OvdSxdXmv_6ZcaGmrY.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/hunyuan-3d/v3.1/pro/image-to-3d", {
        input: {
            input_image_url: "https://v3b.fal.media/files/b/0a8c3155/BTXNRrzOFsO6OvdSxdXmv_6ZcaGmrY.png"
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
        --url https://fal.run/fal-ai/hunyuan-3d/v3.1/pro/image-to-3d \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "input_image_url": "https://v3b.fal.media/files/b/0a8c3155/BTXNRrzOFsO6OvdSxdXmv_6ZcaGmrY.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="input_image_url" type="string" required>
      Front view image URL. Resolution: 128-5000px, max 8MB, formats: JPG/PNG/WEBP. Tips: simple background, single object, object >50% of frame.
    </ParamField>

    <ParamField body="back_image_url" type="string">
      Optional back/rear view image URL (JPG/PNG recommended).
    </ParamField>

    <ParamField body="left_image_url" type="string">
      Optional left side view image URL (JPG/PNG recommended).
    </ParamField>

    <ParamField body="right_image_url" type="string">
      Optional right side view image URL (JPG/PNG recommended).
    </ParamField>

    <ParamField body="top_image_url" type="string">
      Optional top view image URL (v3.1 exclusive, JPG/PNG recommended).
    </ParamField>

    <ParamField body="bottom_image_url" type="string">
      Optional bottom view image URL (v3.1 exclusive, JPG/PNG recommended).
    </ParamField>

    <ParamField body="left_front_image_url" type="string">
      Optional left-front 45 degree angle view image URL (v3.1 exclusive, JPG/PNG recommended).
    </ParamField>

    <ParamField body="right_front_image_url" type="string">
      Optional right-front 45 degree angle view image URL (v3.1 exclusive, JPG/PNG recommended).
    </ParamField>

    <ParamField body="generate_type" type="GenerateTypeEnum" default="Normal">
      Generation task type. Normal: textured model. Geometry: geometry-only white model (no textures). LowPoly/Sketch are not available in v3.1. Default value: `"Normal"`

      Possible values: `Normal`, `Geometry`
    </ParamField>

    <ParamField body="enable_pbr" type="boolean" default="false">
      Enable PBR material generation (metallic, roughness, normal textures). Ignored when generate\_type is Geometry.
    </ParamField>

    <ParamField body="face_count" type="integer" default="500000">
      Target polygon face count. Range: 40,000-1,500,000. Default: 500,000. Default value: `500000`

      Range: `40000` to `1500000`
    </ParamField>

    ### Output Schema

    <ParamField body="model_glb" type="File" required>
      Generated 3D object in GLB format.
    </ParamField>

    <ParamField body="thumbnail" type="File">
      Preview thumbnail of the generated model
    </ParamField>

    <ParamField body="model_urls" type="ModelUrls" required>
      URLs for different 3D model formats
    </ParamField>

    <ParamField body="seed" type="integer">
      The seed used for generation
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "input_image_url": "https://v3b.fal.media/files/b/0a8c3155/BTXNRrzOFsO6OvdSxdXmv_6ZcaGmrY.png",
      "generate_type": "Normal",
      "enable_pbr": false,
      "face_count": 500000
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "model_glb": {
        "content_type": "model/gltf-binary",
        "file_name": "model.glb",
        "file_size": 38554640,
        "url": "https://v3b.fal.media/files/b/0a8c3187/jOeZmtBuhdQMkDu65AkdT_model.glb"
      },
      "thumbnail": {
        "content_type": "image/png",
        "file_name": "preview.png",
        "file_size": 194908,
        "url": "https://v3b.fal.media/files/b/0a8c3187/gxidaODj4OvPXruCfrZ-__preview.png"
      },
      "model_urls": {
        "glb": {
          "content_type": "model/gltf-binary",
          "file_name": "model.glb",
          "file_size": 38554640,
          "url": "https://v3b.fal.media/files/b/0a8c3187/jOeZmtBuhdQMkDu65AkdT_model.glb"
        },
        "obj": {
          "content_type": "model/obj",
          "file_name": "model.obj",
          "file_size": 31447160,
          "url": "https://v3b.fal.media/files/b/0a8c3186/no-aBFEDnOuthILfv-wzs_model.obj"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Text To 3d">
    **Endpoint:** `POST https://fal.run/fal-ai/hunyuan-3d/v3.1/pro/text-to-3d`
    **Endpoint ID:** `fal-ai/hunyuan-3d/v3.1/pro/text-to-3d`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/hunyuan-3d/v3.1/pro/text-to-3d/playground">
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
          "fal-ai/hunyuan-3d/v3.1/pro/text-to-3d",
          arguments={
              "prompt": "A super cool space ship with details"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/hunyuan-3d/v3.1/pro/text-to-3d", {
        input: {
            prompt: "A super cool space ship with details"
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
        --url https://fal.run/fal-ai/hunyuan-3d/v3.1/pro/text-to-3d \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A super cool space ship with details"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      Text description of the 3D content to generate. Max 1024 UTF-8 characters.
    </ParamField>

    <ParamField body="generate_type" type="GenerateTypeEnum" default="Normal">
      Generation task type. Normal: textured model. Geometry: geometry-only white model (no textures). LowPoly/Sketch are not available in v3.1. Default value: `"Normal"`

      Possible values: `Normal`, `Geometry`
    </ParamField>

    <ParamField body="enable_pbr" type="boolean" default="false">
      Enable PBR material generation (metallic, roughness, normal textures). Ignored when generate\_type is Geometry.
    </ParamField>

    <ParamField body="face_count" type="integer" default="500000">
      Target polygon face count. Range: 40,000-1,500,000. Default: 500,000. Default value: `500000`

      Range: `40000` to `1500000`
    </ParamField>

    ### Output Schema

    <ParamField body="model_glb" type="File" required>
      Generated 3D object in GLB format.
    </ParamField>

    <ParamField body="thumbnail" type="File">
      Preview thumbnail of the generated model
    </ParamField>

    <ParamField body="model_urls" type="ModelUrls" required>
      URLs for different 3D model formats
    </ParamField>

    <ParamField body="seed" type="integer">
      The seed used for generation
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A super cool space ship with details",
      "generate_type": "Normal",
      "enable_pbr": false,
      "face_count": 500000
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "model_glb": {
        "content_type": "model/gltf-binary",
        "file_name": "model.glb",
        "file_size": 35833072,
        "url": "https://v3b.fal.media/files/b/0a8c5483/z6sbpr5wBRjqgnQlJM2Ot_model.glb"
      },
      "thumbnail": {
        "content_type": "image/png",
        "file_name": "preview.png",
        "file_size": 68927,
        "url": "https://v3b.fal.media/files/b/0a8c5483/EE97ZV7cM-3UVG4peyWTQ_preview.png"
      },
      "model_urls": {
        "glb": {
          "content_type": "model/gltf-binary",
          "file_name": "model.glb",
          "file_size": 35833072,
          "url": "https://v3b.fal.media/files/b/0a8c5483/z6sbpr5wBRjqgnQlJM2Ot_model.glb"
        },
        "mtl": {
          "content_type": "text/plain",
          "file_name": "material.mtl",
          "file_size": 88,
          "url": "https://v3b.fal.media/files/b/0a8c5482/ZxJepsEkhM67VSugmZ7QT_material.mtl"
        },
        "obj": {
          "content_type": "model/obj",
          "file_name": "6168030a8817075aaa55c94cc5145000.obj",
          "file_size": 34755929,
          "url": "https://v3b.fal.media/files/b/0a8c5482/ZzC1xlOftyGQxhDkbZzVW_6168030a8817075aaa55c94cc5145000.obj"
        },
        "texture": {
          "content_type": "image/png",
          "file_name": "texture_20250901.png",
          "file_size": 19996580,
          "url": "https://v3b.fal.media/files/b/0a8c5482/jOL2nBpcOGspwxQf0_U-z_texture_20250901.png"
        }
      }
    }
    ```
  </Tab>
</Tabs>

## Related

* [Hunyuan 3D Pro Text to 3D](/model-api-reference/3d-api/hunyuan-3d-pro-text-to-3d) — 3D
* [Hunyuan 3D Rapid Image to 3D](/model-api-reference/3d-api/hunyuan-3d-rapid-image-to-3d) — 3D
* [Hunyuan 3d](/model-api-reference/3d-api/hunyuan-3d) — 3D
* [Hunyuan 3D Smart Topology](/model-api-reference/3d-api/hunyuan-3d-smart-topology) — 3D
* [Hunyuan 3D Part Splitter](/model-api-reference/3d-api/hunyuan-3d-part-splitter) — 3D
* [Hunyuan 3D Pro Image to 3D](/model-api-reference/3d-api/hunyuan-3d-pro-image-to-3d) — 3D

## Limitations

* `generate_type` restricted to: `Normal`, `Geometry`
* `face_count` range: 40000 to 1500000
