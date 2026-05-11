> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bria Fibo Edit API

> API reference for Bria Fibo Edit. A high-quality editing model that achieves maximum controllability and transparency by combining JSON + Mask + Image.

<Tabs>
  <Tab title="Edit">
    **Endpoint:** `POST https://fal.run/bria/fibo-edit/edit`
    **Endpoint ID:** `bria/fibo-edit/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/fibo-edit/edit/playground">
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
          "bria/fibo-edit/edit",
          arguments={},
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bria/fibo-edit/edit", {
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
        --url https://fal.run/bria/fibo-edit/edit \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{}'
      ```
    </CodeGroup>

    ## Examples

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a8b696e/RDNU7DokXPnC6AasT4fVD_0943bf8f73d5424eb3cfb656abb4ce49.png" alt="Example output from Fibo Edit" />
    </Frame>

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a8b6984/5kSvXeLDU0_7iAqbeT9ht_0998cd4960b54a34b614b94411f339e3.png" alt="Example output from Fibo Edit" />
    </Frame>

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a8b6993/Bmgq09cV1iMd0hKYe-uXv_2d8cc1342c0a4a44ad26ed229f77fefb.png" alt="Example output from Fibo Edit" />
    </Frame>

    ### Input Schema

    <ParamField body="image_url" type="string">
      Reference image (file or URL).
    </ParamField>

    <ParamField body="mask_url" type="string">
      Mask image (file or URL). Optional
    </ParamField>

    <ParamField body="instruction" type="string">
      Instruction for image editing.
    </ParamField>

    <ParamField body="structured_instruction" type="StructuredInstruction">
      The structured prompt to generate an image from.
    </ParamField>

    <ParamField body="original_vgl" type="StructuredInstruction">
      The original vgl used to generate the image.
    </ParamField>

    <ParamField body="new_vgl" type="StructuredInstruction">
      The new vgl describing image after edit.
    </ParamField>

    <ParamField body="seed" type="integer" default="5555">
      Random seed for reproducibility. Default value: `5555`
    </ParamField>

    <ParamField body="steps_num" type="integer" default="30">
      Number of inference steps. Default value: `30`

      Range: `20` to `50`
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="">
      Negative prompt for image generation. Default value: `""`
    </ParamField>

    <ParamField body="guidance_scale" type="float | integer" default="5">
      Guidance scale for text. Default value: `5`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If true, returns the image directly in the response (increases latency).
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      Generated image.
    </ParamField>

    <ParamField body="images" type="list<Image>" default="">
      Generated images.
    </ParamField>

    <ParamField body="structured_instruction" type="Structured Instruction" required>
      Current instruction.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://v3b.fal.media/files/b/0a8b07e8/GYKVk2EVivg_MC3jRRZi3_png%20-%202026-01-13T094835.850%20(3).png",
      "instruction": "change lighting to starlight nighttime",
      "seed": 5555,
      "steps_num": 30,
      "negative_prompt": "",
      "guidance_scale": 5,
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      },
      "images": [
        {
          "url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/ewT7wv-jMgkqs7z7xQNNL_e8707c299d034feab7a64d903118098f.png"
        }
      ]
    }
    ```
  </Tab>

  <Tab title="Restore">
    **Endpoint:** `POST https://fal.run/bria/fibo-edit/restore`
    **Endpoint ID:** `bria/fibo-edit/restore`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/fibo-edit/restore/playground">
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
          "bria/fibo-edit/restore",
          arguments={
              "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/png+-+2026-01-13T134151.337.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bria/fibo-edit/restore", {
        input: {
            image_url: "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/png+-+2026-01-13T134151.337.png"
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
        --url https://fal.run/bria/fibo-edit/restore \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/png+-+2026-01-13T134151.337.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The source image.
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      Generated image.
    </ParamField>

    <ParamField body="images" type="list<Image>" default="">
      Generated images.
    </ParamField>

    <ParamField body="structured_instruction" type="Structured Instruction" required>
      Current instruction.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/png+-+2026-01-13T134151.337.png"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      },
      "images": []
    }
    ```
  </Tab>

  <Tab title="Relight">
    **Endpoint:** `POST https://fal.run/bria/fibo-edit/relight`
    **Endpoint ID:** `bria/fibo-edit/relight`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/fibo-edit/relight/playground">
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
          "bria/fibo-edit/relight",
          arguments={
              "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/bria_result+-+2026-01-13T095546.173.png",
              "light_direction": "front",
              "light_type": "soft overcast daylight lighting"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bria/fibo-edit/relight", {
        input: {
            image_url: "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/bria_result+-+2026-01-13T095546.173.png",
            light_direction: "front",
            light_type: "soft overcast daylight lighting"
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
        --url https://fal.run/bria/fibo-edit/relight \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/bria_result+-+2026-01-13T095546.173.png",
        "light_direction": "front",
        "light_type": "soft overcast daylight lighting"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The source image.
    </ParamField>

    <ParamField body="light_direction" type="Enum" required>
      Where the light comes from.

      Possible values: `front`, `side`, `bottom`, `top-down`
    </ParamField>

    <ParamField body="light_type" type="LightTypeEnum" required>
      The quality/style/time of day.

      Possible values: `midday`, `blue hour light`, `low-angle sunlight`, `sunrise light`, `spotlight on subject`, `overcast light`, `soft overcast daylight lighting`, `cloud-filtered lighting`, `fog-diffused lighting`, `moonlight lighting`, `starlight nighttime`, `soft bokeh lighting`, `harsh studio lighting`
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      Generated image.
    </ParamField>

    <ParamField body="images" type="list<Image>" default="">
      Generated images.
    </ParamField>

    <ParamField body="structured_instruction" type="Structured Instruction" required>
      Current instruction.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/bria_result+-+2026-01-13T095546.173.png",
      "light_direction": "front",
      "light_type": "soft overcast daylight lighting"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      },
      "images": []
    }
    ```
  </Tab>

  <Tab title="Sketch_to_colored_image">
    **Endpoint:** `POST https://fal.run/bria/fibo-edit/sketch_to_colored_image`
    **Endpoint ID:** `bria/fibo-edit/sketch_to_colored_image`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/fibo-edit/sketch_to_colored_image/playground">
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
          "bria/fibo-edit/sketch_to_colored_image",
          arguments={
              "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/create_a_b_w_sketch_of_a_cat.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bria/fibo-edit/sketch_to_colored_image", {
        input: {
            image_url: "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/create_a_b_w_sketch_of_a_cat.png"
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
        --url https://fal.run/bria/fibo-edit/sketch_to_colored_image \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/create_a_b_w_sketch_of_a_cat.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The source image.
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      Generated image.
    </ParamField>

    <ParamField body="images" type="list<Image>" default="">
      Generated images.
    </ParamField>

    <ParamField body="structured_instruction" type="Structured Instruction" required>
      Current instruction.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/create_a_b_w_sketch_of_a_cat.png"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      },
      "images": []
    }
    ```
  </Tab>

  <Tab title="Erase_by_text">
    **Endpoint:** `POST https://fal.run/bria/fibo-edit/erase_by_text`
    **Endpoint ID:** `bria/fibo-edit/erase_by_text`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/fibo-edit/erase_by_text/playground">
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
          "bria/fibo-edit/erase_by_text",
          arguments={
              "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/an_empty_table_in_living_room.png",
              "object_name": "Table"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bria/fibo-edit/erase_by_text", {
        input: {
            image_url: "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/an_empty_table_in_living_room.png",
            object_name: "Table"
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
        --url https://fal.run/bria/fibo-edit/erase_by_text \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/an_empty_table_in_living_room.png",
        "object_name": "Table"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The source image.
    </ParamField>

    <ParamField body="object_name" type="string" required>
      The name of the object to remove.
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      Generated image.
    </ParamField>

    <ParamField body="images" type="list<Image>" default="">
      Generated images.
    </ParamField>

    <ParamField body="structured_instruction" type="Structured Instruction" required>
      Current instruction.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/an_empty_table_in_living_room.png",
      "object_name": "Table"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      },
      "images": []
    }
    ```
  </Tab>

  <Tab title="Colorize">
    **Endpoint:** `POST https://fal.run/bria/fibo-edit/colorize`
    **Endpoint ID:** `bria/fibo-edit/colorize`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/fibo-edit/colorize/playground">
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
          "bria/fibo-edit/colorize",
          arguments={
              "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/png+-+2026-01-13T083840.113.png",
              "color": "contemporary color"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bria/fibo-edit/colorize", {
        input: {
            image_url: "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/png+-+2026-01-13T083840.113.png",
            color: "contemporary color"
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
        --url https://fal.run/bria/fibo-edit/colorize \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/png+-+2026-01-13T083840.113.png",
        "color": "contemporary color"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The source image.
    </ParamField>

    <ParamField body="color" type="ColorEnum" required>
      Select the color palette or aesthetic for the output image

      Possible values: `contemporary color`, `vivid color`, `black and white colors`, `sepia vintage`
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      Generated image.
    </ParamField>

    <ParamField body="images" type="list<Image>" default="">
      Generated images.
    </ParamField>

    <ParamField body="structured_instruction" type="Structured Instruction" required>
      Current instruction.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/png+-+2026-01-13T083840.113.png",
      "color": "contemporary color"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      },
      "images": []
    }
    ```
  </Tab>

  <Tab title="Restyle">
    **Endpoint:** `POST https://fal.run/bria/fibo-edit/restyle`
    **Endpoint ID:** `bria/fibo-edit/restyle`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/fibo-edit/restyle/playground">
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
          "bria/fibo-edit/restyle",
          arguments={
              "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/high_camera_angle_warm_filter.png",
              "style": "3D Render"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bria/fibo-edit/restyle", {
        input: {
            image_url: "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/high_camera_angle_warm_filter.png",
            style: "3D Render"
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
        --url https://fal.run/bria/fibo-edit/restyle \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/high_camera_angle_warm_filter.png",
        "style": "3D Render"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The source image.
    </ParamField>

    <ParamField body="style" type="StyleEnum" required>
      Select the desired artistic style for the output image.

      Possible values: `3D Render`, `Cubism`, `Oil Painting`, `Anime`, `Cartoon`, `Coloring Book`, `Retro Ad`, `Pop Art Halftone`, `Vector Art`, `Story Board`, `Art Nouveau`, `Cross Etching`, `Wood Cut`
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      Generated image.
    </ParamField>

    <ParamField body="images" type="list<Image>" default="">
      Generated images.
    </ParamField>

    <ParamField body="structured_instruction" type="Structured Instruction" required>
      Current instruction.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/high_camera_angle_warm_filter.png",
      "style": "3D Render"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      },
      "images": []
    }
    ```
  </Tab>

  <Tab title="Rewrite_text">
    **Endpoint:** `POST https://fal.run/bria/fibo-edit/rewrite_text`
    **Endpoint ID:** `bria/fibo-edit/rewrite_text`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/fibo-edit/rewrite_text/playground">
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
          "bria/fibo-edit/rewrite_text",
          arguments={
              "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/create_an_image_of_cake__with_text_on_it_saying___Hi_there__.png",
              "new_text": "FIBO Edit!"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bria/fibo-edit/rewrite_text", {
        input: {
            image_url: "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/create_an_image_of_cake__with_text_on_it_saying___Hi_there__.png",
            new_text: "FIBO Edit!"
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
        --url https://fal.run/bria/fibo-edit/rewrite_text \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/create_an_image_of_cake__with_text_on_it_saying___Hi_there__.png",
        "new_text": "FIBO Edit!"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The source image.
    </ParamField>

    <ParamField body="new_text" type="string" required>
      The new text string to appear in the image.
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      Generated image.
    </ParamField>

    <ParamField body="images" type="list<Image>" default="">
      Generated images.
    </ParamField>

    <ParamField body="structured_instruction" type="Structured Instruction" required>
      Current instruction.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/create_an_image_of_cake__with_text_on_it_saying___Hi_there__.png",
      "new_text": "FIBO Edit!"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      },
      "images": []
    }
    ```
  </Tab>

  <Tab title="Add_object_by_text">
    **Endpoint:** `POST https://fal.run/bria/fibo-edit/add_object_by_text`
    **Endpoint ID:** `bria/fibo-edit/add_object_by_text`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/fibo-edit/add_object_by_text/playground">
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
          "bria/fibo-edit/add_object_by_text",
          arguments={
              "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/an_empty_table_in_living_room.png",
              "instruction": "Place a red vase with flowers on the table."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bria/fibo-edit/add_object_by_text", {
        input: {
            image_url: "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/an_empty_table_in_living_room.png",
            instruction: "Place a red vase with flowers on the table."
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
        --url https://fal.run/bria/fibo-edit/add_object_by_text \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/an_empty_table_in_living_room.png",
        "instruction": "Place a red vase with flowers on the table."
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The source image.
    </ParamField>

    <ParamField body="instruction" type="string" required>
      The full natural language command describing what to add and where.
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      Generated image.
    </ParamField>

    <ParamField body="images" type="list<Image>" default="">
      Generated images.
    </ParamField>

    <ParamField body="structured_instruction" type="Structured Instruction" required>
      Current instruction.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/an_empty_table_in_living_room.png",
      "instruction": "Place a red vase with flowers on the table."
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      },
      "images": []
    }
    ```
  </Tab>

  <Tab title="Blend">
    **Endpoint:** `POST https://fal.run/bria/fibo-edit/blend`
    **Endpoint ID:** `bria/fibo-edit/blend`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/fibo-edit/blend/playground">
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
          "bria/fibo-edit/blend",
          arguments={
              "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/shirt.png",
              "instruction": "Place the art on the shirt, keep the art exactly the same"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bria/fibo-edit/blend", {
        input: {
            image_url: "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/shirt.png",
            instruction: "Place the art on the shirt, keep the art exactly the same"
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
        --url https://fal.run/bria/fibo-edit/blend \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/shirt.png",
        "instruction": "Place the art on the shirt, keep the art exactly the same"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The source image.
    </ParamField>

    <ParamField body="instruction" type="string" required>
      Instruct what elements you would like to blend in your image.
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      Generated image.
    </ParamField>

    <ParamField body="images" type="list<Image>" default="">
      Generated images.
    </ParamField>

    <ParamField body="structured_instruction" type="Structured Instruction" required>
      Current instruction.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/shirt.png",
      "instruction": "Place the art on the shirt, keep the art exactly the same"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      },
      "images": []
    }
    ```
  </Tab>

  <Tab title="Replace_object_by_text">
    **Endpoint:** `POST https://fal.run/bria/fibo-edit/replace_object_by_text`
    **Endpoint ID:** `bria/fibo-edit/replace_object_by_text`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/fibo-edit/replace_object_by_text/playground">
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
          "bria/fibo-edit/replace_object_by_text",
          arguments={
              "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/a_bowl_of_fruits__should_have_a_red_apple.png",
              "instruction": "Replace the red apple with a green pear"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bria/fibo-edit/replace_object_by_text", {
        input: {
            image_url: "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/a_bowl_of_fruits__should_have_a_red_apple.png",
            instruction: "Replace the red apple with a green pear"
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
        --url https://fal.run/bria/fibo-edit/replace_object_by_text \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/a_bowl_of_fruits__should_have_a_red_apple.png",
        "instruction": "Replace the red apple with a green pear"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The source image.
    </ParamField>

    <ParamField body="instruction" type="string" required>
      The full natural language command describing what to replace.
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      Generated image.
    </ParamField>

    <ParamField body="images" type="list<Image>" default="">
      Generated images.
    </ParamField>

    <ParamField body="structured_instruction" type="Structured Instruction" required>
      Current instruction.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/a_bowl_of_fruits__should_have_a_red_apple.png",
      "instruction": "Replace the red apple with a green pear"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      },
      "images": []
    }
    ```
  </Tab>

  <Tab title="Reseason">
    **Endpoint:** `POST https://fal.run/bria/fibo-edit/reseason`
    **Endpoint ID:** `bria/fibo-edit/reseason`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/fibo-edit/reseason/playground">
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
          "bria/fibo-edit/reseason",
          arguments={
              "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/create_a_realistic_image_of_a_green_field_in_the_spring__also_add_trees.png",
              "season": "winter"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bria/fibo-edit/reseason", {
        input: {
            image_url: "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/create_a_realistic_image_of_a_green_field_in_the_spring__also_add_trees.png",
            season: "winter"
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
        --url https://fal.run/bria/fibo-edit/reseason \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/create_a_realistic_image_of_a_green_field_in_the_spring__also_add_trees.png",
        "season": "winter"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The source image.
    </ParamField>

    <ParamField body="season" type="SeasonEnum" required>
      The desired season.

      Possible values: `spring`, `summer`, `autumn`, `winter`
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      Generated image.
    </ParamField>

    <ParamField body="images" type="list<Image>" default="">
      Generated images.
    </ParamField>

    <ParamField body="structured_instruction" type="Structured Instruction" required>
      Current instruction.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://bria-datasets.s3.us-east-1.amazonaws.com/Liza/create_a_realistic_image_of_a_green_field_in_the_spring__also_add_trees.png",
      "season": "winter"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019,
        "width": 1024,
        "height": 1024
      },
      "images": []
    }
    ```
  </Tab>
</Tabs>

## Related

* [Fibo Edit \[Restore\]](/model-api-reference/image-generation-api/fibo-edit) — Image Generation

## Limitations

* `steps_num` range: 20 to 50
* `light_direction` restricted to: `front`, `side`, `bottom`, `top-down`
* `color` restricted to: `contemporary color`, `vivid color`, `black and white colors`, `sepia vintage`
* `season` restricted to: `spring`, `summer`, `autumn`, `winter`
