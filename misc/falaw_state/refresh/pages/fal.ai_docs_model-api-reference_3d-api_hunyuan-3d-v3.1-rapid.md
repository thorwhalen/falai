> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hunyuan 3d V3.1 Rapid API

> API reference for Hunyuan 3d V3.1 Rapid. Rapidly generate 3D models from images using Hunyuan 3D.

<Tabs>
  <Tab title="Image To 3d">
    **Endpoint:** `POST https://fal.run/fal-ai/hunyuan-3d/v3.1/rapid/image-to-3d`
    **Endpoint ID:** `fal-ai/hunyuan-3d/v3.1/rapid/image-to-3d`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/hunyuan-3d/v3.1/rapid/image-to-3d/playground">
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
          "fal-ai/hunyuan-3d/v3.1/rapid/image-to-3d",
          arguments={
              "input_image_url": "https://v3b.fal.media/files/b/0a865ab1/omYcawLUo4RZbO8J6ZgZR.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/hunyuan-3d/v3.1/rapid/image-to-3d", {
        input: {
            input_image_url: "https://v3b.fal.media/files/b/0a865ab1/omYcawLUo4RZbO8J6ZgZR.png"
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
        --url https://fal.run/fal-ai/hunyuan-3d/v3.1/rapid/image-to-3d \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "input_image_url": "https://v3b.fal.media/files/b/0a865ab1/omYcawLUo4RZbO8J6ZgZR.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="input_image_url" type="string" required>
      Front view image URL. Resolution: 128-5000px, max 8MB (recommended ≤6MB for base64 encoding), formats: JPG/PNG/WEBP. Tips: simple background, single object, object >50% of frame.
    </ParamField>

    <ParamField body="enable_pbr" type="boolean" default="false">
      Enable PBR material generation (metallic, roughness, normal textures). Does not take effect when enable\_geometry is True.
    </ParamField>

    <ParamField body="enable_geometry" type="boolean" default="false">
      Generate geometry-only white model without textures. When enabled, enable\_pbr is ignored and OBJ is not supported (default output is GLB).
    </ParamField>

    ### Output Schema

    <ParamField body="model_glb" type="File">
      Generated 3D model file. Contains GLB if available, otherwise OBJ.
    </ParamField>

    <ParamField body="material_mtl" type="File">
      MTL material file for the OBJ model.
    </ParamField>

    <ParamField body="texture" type="File">
      Texture image for the 3D model.
    </ParamField>

    <ParamField body="thumbnail" type="File">
      Preview thumbnail of the generated model
    </ParamField>

    <ParamField body="model_urls" type="ModelUrls" required>
      URLs for different 3D model formats.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "input_image_url": "https://v3b.fal.media/files/b/0a865ab1/omYcawLUo4RZbO8J6ZgZR.png",
      "enable_pbr": false,
      "enable_geometry": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "model_glb": {
        "content_type": "model/obj",
        "file_name": "8b1dbea208d194b9089a950abc2df426.obj",
        "file_size": 3172659,
        "url": "https://v3b.fal.media/files/b/0a8c4439/vj933H8B4W3wbd3e2RNby_8b1dbea208d194b9089a950abc2df426.obj"
      },
      "material_mtl": {
        "content_type": "text/plain",
        "file_name": "material.mtl",
        "file_size": 88,
        "url": "https://v3b.fal.media/files/b/0a8c4439/_RhytNH4xZ5EFHr34YzJt_material.mtl"
      },
      "texture": {
        "content_type": "image/png",
        "file_name": "texture_20250901.png",
        "file_size": 11728567,
        "url": "https://v3b.fal.media/files/b/0a8c4439/_4NXiSoGcZ-GYwmgUTfHZ_texture_20250901.png"
      },
      "thumbnail": {
        "content_type": "image/png",
        "file_name": "preview.png",
        "file_size": 82521,
        "url": "https://v3b.fal.media/files/b/0a8c4439/70Sm1pZ16SQP-mEbaKICC_preview.png"
      },
      "model_urls": {
        "mtl": {
          "content_type": "text/plain",
          "file_name": "material.mtl",
          "file_size": 88,
          "url": "https://v3b.fal.media/files/b/0a8c4439/_RhytNH4xZ5EFHr34YzJt_material.mtl"
        },
        "obj": {
          "content_type": "model/obj",
          "file_name": "8b1dbea208d194b9089a950abc2df426.obj",
          "file_size": 3172659,
          "url": "https://v3b.fal.media/files/b/0a8c4439/vj933H8B4W3wbd3e2RNby_8b1dbea208d194b9089a950abc2df426.obj"
        },
        "texture": {
          "content_type": "image/png",
          "file_name": "texture_20250901.png",
          "file_size": 11728567,
          "url": "https://v3b.fal.media/files/b/0a8c4439/_4NXiSoGcZ-GYwmgUTfHZ_texture_20250901.png"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Text To 3d">
    **Endpoint:** `POST https://fal.run/fal-ai/hunyuan-3d/v3.1/rapid/text-to-3d`
    **Endpoint ID:** `fal-ai/hunyuan-3d/v3.1/rapid/text-to-3d`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/hunyuan-3d/v3.1/rapid/text-to-3d/playground">
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
          "fal-ai/hunyuan-3d/v3.1/rapid/text-to-3d",
          arguments={
              "prompt": "A rustic wooden treasure chest with metal bands and ornate lock"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/hunyuan-3d/v3.1/rapid/text-to-3d", {
        input: {
            prompt: "A rustic wooden treasure chest with metal bands and ornate lock"
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
        --url https://fal.run/fal-ai/hunyuan-3d/v3.1/rapid/text-to-3d \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A rustic wooden treasure chest with metal bands and ornate lock"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      Text description of the 3D content to generate. Max 200 UTF-8 characters.
    </ParamField>

    <ParamField body="enable_pbr" type="boolean" default="false">
      Enable PBR material generation (metallic, roughness, normal textures). Does not take effect when enable\_geometry is True.
    </ParamField>

    <ParamField body="enable_geometry" type="boolean" default="false">
      Generate geometry-only white model without textures. When enabled, enable\_pbr is ignored and OBJ is not supported (default output is GLB).
    </ParamField>

    ### Output Schema

    <ParamField body="model_obj" type="File">
      Generated 3D model in OBJ format.
    </ParamField>

    <ParamField body="material_mtl" type="File">
      MTL material file for the OBJ model.
    </ParamField>

    <ParamField body="texture" type="File">
      Texture image for the 3D model.
    </ParamField>

    <ParamField body="thumbnail" type="File">
      Preview thumbnail of the generated model
    </ParamField>

    <ParamField body="model_urls" type="ModelUrls" required>
      URLs for different 3D model formats.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A rustic wooden treasure chest with metal bands and ornate lock",
      "enable_pbr": false,
      "enable_geometry": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "model_obj": {
        "content_type": "model/obj",
        "file_name": "0f7f7a1ac578c80d4397a7f2b69b40ff.obj",
        "file_size": 5306476,
        "url": "https://v3b.fal.media/files/b/0a8c44d5/2W2KRP1DM_-4qI8F_n05b_0f7f7a1ac578c80d4397a7f2b69b40ff.obj"
      },
      "material_mtl": {
        "content_type": "text/plain",
        "file_name": "material.mtl",
        "file_size": 157,
        "url": "https://v3b.fal.media/files/b/0a8c44d5/EHzTxJtHpdIliaMNnEke-_material.mtl"
      },
      "texture": {
        "content_type": "image/png",
        "file_name": "material.png",
        "file_size": 5915609,
        "url": "https://v3b.fal.media/files/b/0a8c44d5/T0q-P0aqXVG_y7jff-XTa_material.png"
      },
      "thumbnail": {
        "content_type": "image/png",
        "file_name": "preview.png",
        "file_size": 281374,
        "url": "https://v3b.fal.media/files/b/0a8c44d6/D9_IYgpugP0deXvSwBC2J_preview.png"
      },
      "model_urls": {
        "mtl": {
          "content_type": "text/plain",
          "file_name": "material.mtl",
          "file_size": 157,
          "url": "https://v3b.fal.media/files/b/0a8c44d5/EHzTxJtHpdIliaMNnEke-_material.mtl"
        },
        "obj": {
          "content_type": "model/obj",
          "file_name": "0f7f7a1ac578c80d4397a7f2b69b40ff.obj",
          "file_size": 5306476,
          "url": "https://v3b.fal.media/files/b/0a8c44d5/2W2KRP1DM_-4qI8F_n05b_0f7f7a1ac578c80d4397a7f2b69b40ff.obj"
        },
        "texture": {
          "content_type": "image/png",
          "file_name": "material.png",
          "file_size": 5915609,
          "url": "https://v3b.fal.media/files/b/0a8c44d5/T0q-P0aqXVG_y7jff-XTa_material.png"
        }
      }
    }
    ```
  </Tab>
</Tabs>

## Related

* [Hunyuan 3D Pro Image to 3D](/model-api-reference/3d-api/hunyuan-3d-pro-image-to-3d) — 3D
* [Hunyuan 3D Pro Text to 3D](/model-api-reference/3d-api/hunyuan-3d-pro-text-to-3d) — 3D
* [Hunyuan 3d](/model-api-reference/3d-api/hunyuan-3d) — 3D
* [Hunyuan 3D Smart Topology](/model-api-reference/3d-api/hunyuan-3d-smart-topology) — 3D
* [Hunyuan 3D Part Splitter](/model-api-reference/3d-api/hunyuan-3d-part-splitter) — 3D
* [Hunyuan 3D Rapid Image to 3D](/model-api-reference/3d-api/hunyuan-3d-rapid-image-to-3d) — 3D
