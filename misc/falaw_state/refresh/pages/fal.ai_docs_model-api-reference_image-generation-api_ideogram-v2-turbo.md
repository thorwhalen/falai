> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ideogram V2 Turbo API

> API reference for Ideogram V2 Turbo. Accelerated image generation with Ideogram V2 Turbo. Create high-quality visuals, posters, and logos with enhanced speed while maintaining Ideogram's signature qua

<Tabs>
  <Tab title="Turbo">
    **Endpoint:** `POST https://fal.run/fal-ai/ideogram/v2/turbo`
    **Endpoint ID:** `fal-ai/ideogram/v2/turbo`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/v2/turbo/playground">
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
          "fal-ai/ideogram/v2/turbo",
          arguments={
              "prompt": "A comic style illustration of a skeleton sitting on a toilet in a bathroom. The bathroom has a Halloween decoration with a pumpkin jack-o-lantern and bats flying around. There is a text above the skeleton that says \"Just Waiting for Halloween with Ideogram 2.0 at fal.ai\""
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/ideogram/v2/turbo", {
        input: {
            prompt: "A comic style illustration of a skeleton sitting on a toilet in a bathroom. The bathroom has a Halloween decoration with a pumpkin jack-o-lantern and bats flying around. There is a text above the skeleton that says \"Just Waiting for Halloween with Ideogram 2.0 at fal.ai\""
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
        --url https://fal.run/fal-ai/ideogram/v2/turbo \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A comic style illustration of a skeleton sitting on a toilet in a bathroom. The bathroom has a Halloween decoration with a pumpkin jack-o-lantern and bats flying around. There is a text above the skeleton that says \"Just Waiting for Halloween with Ideogram 2.0 at fal.ai\""
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required />

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="1:1">
      The aspect ratio of the generated image Default value: `"1:1"`

      Possible values: `10:16`, `16:10`, `9:16`, `16:9`, `4:3`, `3:4`, `1:1`, `1:3`, `3:1`, `3:2`, `2:3`
    </ParamField>

    <ParamField body="expand_prompt" type="boolean" default="true">
      Whether to expand the prompt with MagicPrompt functionality. Default value: `true`
    </ParamField>

    <ParamField body="seed" type="integer">
      Seed for the random number generator
    </ParamField>

    <ParamField body="style" type="StyleEnum" default="auto">
      The style of the generated image Default value: `"auto"`

      Possible values: `auto`, `general`, `realistic`, `design`, `render_3D`, `anime`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="">
      A negative prompt to avoid in the generated image Default value: `""`
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<File>" required />

    <ParamField body="seed" type="integer" required>
      Seed used for the random number generator
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A comic style illustration of a skeleton sitting on a toilet in a bathroom. The bathroom has a Halloween decoration with a pumpkin jack-o-lantern and bats flying around. There is a text above the skeleton that says \"Just Waiting for Halloween with Ideogram 2.0 at fal.ai\"",
      "aspect_ratio": "1:1",
      "expand_prompt": true,
      "style": "auto",
      "sync_mode": false,
      "negative_prompt": ""
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://fal.media/files/monkey/cNaoxPl0YAWYb-QVBvO9F_image.png"
        }
      ],
      "seed": 123456
    }
    ```
  </Tab>

  <Tab title="Remix">
    **Endpoint:** `POST https://fal.run/fal-ai/ideogram/v2/turbo/remix`
    **Endpoint ID:** `fal-ai/ideogram/v2/turbo/remix`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/v2/turbo/remix/playground">
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
          "fal-ai/ideogram/v2/turbo/remix",
          arguments={
              "prompt": "An ice field in north atlantic",
              "image_url": "https://fal.media/files/lion/FHOx4y4a0ef7Sgmo-sOUR_image.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/ideogram/v2/turbo/remix", {
        input: {
            prompt: "An ice field in north atlantic",
            image_url: "https://fal.media/files/lion/FHOx4y4a0ef7Sgmo-sOUR_image.png"
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
        --url https://fal.run/fal-ai/ideogram/v2/turbo/remix \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "An ice field in north atlantic",
        "image_url": "https://fal.media/files/lion/FHOx4y4a0ef7Sgmo-sOUR_image.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to remix the image with
    </ParamField>

    <ParamField body="image_url" type="string" required>
      The image URL to remix
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="1:1">
      The aspect ratio of the generated image Default value: `"1:1"`

      Possible values: `10:16`, `16:10`, `9:16`, `16:9`, `4:3`, `3:4`, `1:1`, `1:3`, `3:1`, `3:2`, `2:3`
    </ParamField>

    <ParamField body="strength" type="float" default="0.8">
      Strength of the input image in the remix Default value: `0.8`

      Range: `0.01` to `1`
    </ParamField>

    <ParamField body="expand_prompt" type="boolean" default="true">
      Whether to expand the prompt with MagicPrompt functionality. Default value: `true`
    </ParamField>

    <ParamField body="seed" type="integer">
      Seed for the random number generator
    </ParamField>

    <ParamField body="style" type="StyleEnum" default="auto">
      The style of the generated image Default value: `"auto"`

      Possible values: `auto`, `general`, `realistic`, `design`, `render_3D`, `anime`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<File>" required />

    <ParamField body="seed" type="integer" required>
      Seed used for the random number generator
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "An ice field in north atlantic",
      "image_url": "https://fal.media/files/lion/FHOx4y4a0ef7Sgmo-sOUR_image.png",
      "aspect_ratio": "1:1",
      "strength": 0.8,
      "expand_prompt": true,
      "style": "auto",
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://fal.media/files/monkey/cNaoxPl0YAWYb-QVBvO9F_image.png"
        }
      ],
      "seed": 123456
    }
    ```
  </Tab>

  <Tab title="Edit">
    **Endpoint:** `POST https://fal.run/fal-ai/ideogram/v2/turbo/edit`
    **Endpoint ID:** `fal-ai/ideogram/v2/turbo/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/v2/turbo/edit/playground">
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
          "fal-ai/ideogram/v2/turbo/edit",
          arguments={
              "prompt": "A knight in shining armour holding a greatshield with \"FAL\" on it",
              "image_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/knight.jpeg",
              "mask_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/mask_knight.jpeg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/ideogram/v2/turbo/edit", {
        input: {
            prompt: "A knight in shining armour holding a greatshield with \"FAL\" on it",
            image_url: "https://storage.googleapis.com/falserverless/flux-lora/example-images/knight.jpeg",
            mask_url: "https://storage.googleapis.com/falserverless/flux-lora/example-images/mask_knight.jpeg"
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
        --url https://fal.run/fal-ai/ideogram/v2/turbo/edit \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A knight in shining armour holding a greatshield with \"FAL\" on it",
        "image_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/knight.jpeg",
        "mask_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/mask_knight.jpeg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to fill the masked part of the image.
    </ParamField>

    <ParamField body="image_url" type="string" required>
      The image URL to generate an image from. Needs to match the dimensions of the mask.
    </ParamField>

    <ParamField body="mask_url" type="string" required>
      The mask URL to inpaint the image. Needs to match the dimensions of the input image.
    </ParamField>

    <ParamField body="seed" type="integer">
      Seed for the random number generator
    </ParamField>

    <ParamField body="style" type="StyleEnum" default="auto">
      The style of the generated image Default value: `"auto"`

      Possible values: `auto`, `general`, `realistic`, `design`, `render_3D`, `anime`
    </ParamField>

    <ParamField body="expand_prompt" type="boolean" default="true">
      Whether to expand the prompt with MagicPrompt functionality. Default value: `true`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<File>" required />

    <ParamField body="seed" type="integer" required>
      Seed used for the random number generator
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A knight in shining armour holding a greatshield with \"FAL\" on it",
      "image_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/knight.jpeg",
      "mask_url": "https://storage.googleapis.com/falserverless/flux-lora/example-images/mask_knight.jpeg",
      "style": "auto",
      "expand_prompt": true,
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://fal.media/files/monkey/cNaoxPl0YAWYb-QVBvO9F_image.png"
        }
      ],
      "seed": 123456
    }
    ```
  </Tab>
</Tabs>

## Related

* [Ideogram V2 Turbo Remix](/model-api-reference/image-generation-api/ideogram-v2-turbo-remix) — Image Generation
* [Ideogram V2 Turbo Edit](/model-api-reference/image-generation-api/ideogram-v2-turbo-edit) — Image Generation
* [Ideogram V2 Turbo](/model-api-reference/image-generation-api/ideogram-v2-turbo) — Image Generation

## Limitations

* `style` restricted to: `auto`, `general`, `realistic`, `design`, `render_3D`, `anime`
* `strength` range: 0.01 to 1
