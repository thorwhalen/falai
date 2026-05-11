> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ideogram Character API

> API reference for Ideogram Character. Generate consistent character appearances across multiple images. Maintain facial features, proportions, and distinctive traits for cohesive storytelling and bran

<Tabs>
  <Tab title="Character">
    **Endpoint:** `POST https://fal.run/fal-ai/ideogram/character`
    **Endpoint ID:** `fal-ai/ideogram/character`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/character/playground">
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
          "fal-ai/ideogram/character",
          arguments={
              "prompt": "Place the woman leisurely enjoying a cup of espresso while relaxing at a sunlit café table in Siena, Italy. The café setting showcases vintage wooden furniture with peeling white paint, aged brick flooring, and sun-bleached stone walls decorated with trailing ivy and vibrant potted geraniums that capture Siena's medieval character. Golden late-morning light streams through overhead, creating soft shadows that highlight the weathered architectural details. The composition appears slightly off-center, conveying the unguarded tranquility and personal intimacy of a peaceful moment savoring the Tuscan morning ambiance.",
              "reference_image_urls": [
                  "https://v3.fal.media/files/kangaroo/0rinwnj_Kn9Fsu2dK-aKm_image.png"
              ]
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/ideogram/character", {
        input: {
            prompt: "Place the woman leisurely enjoying a cup of espresso while relaxing at a sunlit café table in Siena, Italy. The café setting showcases vintage wooden furniture with peeling white paint, aged brick flooring, and sun-bleached stone walls decorated with trailing ivy and vibrant potted geraniums that capture Siena's medieval character. Golden late-morning light streams through overhead, creating soft shadows that highlight the weathered architectural details. The composition appears slightly off-center, conveying the unguarded tranquility and personal intimacy of a peaceful moment savoring the Tuscan morning ambiance.",
            reference_image_urls: [
              "https://v3.fal.media/files/kangaroo/0rinwnj_Kn9Fsu2dK-aKm_image.png"
            ]
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
        --url https://fal.run/fal-ai/ideogram/character \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Place the woman leisurely enjoying a cup of espresso while relaxing at a sunlit café table in Siena, Italy. The café setting showcases vintage wooden furniture with peeling white paint, aged brick flooring, and sun-bleached stone walls decorated with trailing ivy and vibrant potted geraniums that capture Siena'\''s medieval character. Golden late-morning light streams through overhead, creating soft shadows that highlight the weathered architectural details. The composition appears slightly off-center, conveying the unguarded tranquility and personal intimacy of a peaceful moment savoring the Tuscan morning ambiance.",
        "reference_image_urls": [
          "https://v3.fal.media/files/kangaroo/0rinwnj_Kn9Fsu2dK-aKm_image.png"
        ]
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_urls" type="list<string>">
      A set of images to use as style references (maximum total size 10MB across all style references). The images should be in JPEG, PNG or WebP format
    </ParamField>

    <ParamField body="rendering_speed" type="RenderingSpeedEnum" default="BALANCED">
      The rendering speed to use. Default value: `"BALANCED"`

      Possible values: `TURBO`, `BALANCED`, `QUALITY`
    </ParamField>

    <ParamField body="color_palette" type="ColorPalette">
      A color palette for generation, must EITHER be specified via one of the presets (name) or explicitly via hexadecimal representations of the color with optional weights (members)
    </ParamField>

    <ParamField body="style_codes" type="list<string>">
      A list of 8 character hexadecimal codes representing the style of the image. Cannot be used in conjunction with style\_reference\_images or style
    </ParamField>

    <ParamField body="style" type="StyleEnum" default="AUTO">
      The style type to generate with. Cannot be used with style\_codes. Default value: `"AUTO"`

      Possible values: `AUTO`, `REALISTIC`, `FICTION`
    </ParamField>

    <ParamField body="expand_prompt" type="boolean" default="true">
      Determine if MagicPrompt should be used in generating the request or not. Default value: `true`
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      Number of images to generate. Default value: `1`

      Range: `1` to `8`
    </ParamField>

    <ParamField body="seed" type="integer">
      Seed for the random number generator
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="prompt" type="string" required>
      The prompt to fill the masked part of the image.
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="square_hd">
      The resolution of the generated image Default value: `square_hd`

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="">
      Description of what to exclude from an image. Descriptions in the prompt take precedence to descriptions in the negative prompt. Default value: `""`
    </ParamField>

    <ParamField body="reference_image_urls" type="list<string>" required>
      A set of images to use as character references. Currently only 1 image is supported, rest will be ignored. (maximum total size 10MB across all character references). The images should be in JPEG, PNG or WebP format
    </ParamField>

    <ParamField body="reference_mask_urls" type="list<string>">
      A set of masks to apply to the character references. Currently only 1 mask is supported, rest will be ignored. (maximum total size 10MB across all character references). The masks should be in JPEG, PNG or WebP format
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<File>" required />

    <ParamField body="seed" type="integer" required>
      Seed used for the random number generator
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "rendering_speed": "BALANCED",
      "style": "AUTO",
      "expand_prompt": true,
      "num_images": 1,
      "sync_mode": false,
      "prompt": "Place the woman leisurely enjoying a cup of espresso while relaxing at a sunlit café table in Siena, Italy. The café setting showcases vintage wooden furniture with peeling white paint, aged brick flooring, and sun-bleached stone walls decorated with trailing ivy and vibrant potted geraniums that capture Siena's medieval character. Golden late-morning light streams through overhead, creating soft shadows that highlight the weathered architectural details. The composition appears slightly off-center, conveying the unguarded tranquility and personal intimacy of a peaceful moment savoring the Tuscan morning ambiance.",
      "image_size": "square_hd",
      "negative_prompt": "",
      "reference_image_urls": [
        "https://v3.fal.media/files/kangaroo/0rinwnj_Kn9Fsu2dK-aKm_image.png"
      ]
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://v3.fal.media/files/monkey/NC_1eo9ecE9fARcxviJ2R_image.png"
        }
      ],
      "seed": 123456
    }
    ```
  </Tab>

  <Tab title="Edit">
    **Endpoint:** `POST https://fal.run/fal-ai/ideogram/character/edit`
    **Endpoint ID:** `fal-ai/ideogram/character/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/character/edit/playground">
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
          "fal-ai/ideogram/character/edit",
          arguments={
              "prompt": "woman holding bag",
              "image_url": "https://v3.fal.media/files/panda/-LC_gNNV3wUHaGMQT3klE_output.png",
              "mask_url": "https://v3.fal.media/files/panda/jVDAgSkpsZFDP080ceSZJ_woman_face_mask.png",
              "reference_image_urls": [
                  "https://v3.fal.media/files/kangaroo/0rinwnj_Kn9Fsu2dK-aKm_image.png"
              ]
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/ideogram/character/edit", {
        input: {
            prompt: "woman holding bag",
            image_url: "https://v3.fal.media/files/panda/-LC_gNNV3wUHaGMQT3klE_output.png",
            mask_url: "https://v3.fal.media/files/panda/jVDAgSkpsZFDP080ceSZJ_woman_face_mask.png",
            reference_image_urls: [
              "https://v3.fal.media/files/kangaroo/0rinwnj_Kn9Fsu2dK-aKm_image.png"
            ]
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
        --url https://fal.run/fal-ai/ideogram/character/edit \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "woman holding bag",
        "image_url": "https://v3.fal.media/files/panda/-LC_gNNV3wUHaGMQT3klE_output.png",
        "mask_url": "https://v3.fal.media/files/panda/jVDAgSkpsZFDP080ceSZJ_woman_face_mask.png",
        "reference_image_urls": [
          "https://v3.fal.media/files/kangaroo/0rinwnj_Kn9Fsu2dK-aKm_image.png"
        ]
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_urls" type="list<string>">
      A set of images to use as style references (maximum total size 10MB across all style references). The images should be in JPEG, PNG or WebP format
    </ParamField>

    <ParamField body="rendering_speed" type="RenderingSpeedEnum" default="BALANCED">
      The rendering speed to use. Default value: `"BALANCED"`

      Possible values: `TURBO`, `BALANCED`, `QUALITY`
    </ParamField>

    <ParamField body="color_palette" type="ColorPalette">
      A color palette for generation, must EITHER be specified via one of the presets (name) or explicitly via hexadecimal representations of the color with optional weights (members)
    </ParamField>

    <ParamField body="style_codes" type="list<string>">
      A list of 8 character hexadecimal codes representing the style of the image. Cannot be used in conjunction with style\_reference\_images or style
    </ParamField>

    <ParamField body="expand_prompt" type="boolean" default="true">
      Determine if MagicPrompt should be used in generating the request or not. Default value: `true`
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      Number of images to generate. Default value: `1`

      Range: `1` to `8`
    </ParamField>

    <ParamField body="seed" type="integer">
      Seed for the random number generator
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="prompt" type="string" required>
      The prompt to fill the masked part of the image.
    </ParamField>

    <ParamField body="image_url" type="string" required>
      The image URL to generate an image from. MUST have the exact same dimensions (width and height) as the mask image.
    </ParamField>

    <ParamField body="mask_url" type="string" required>
      The mask URL to inpaint the image. MUST have the exact same dimensions (width and height) as the input image.
    </ParamField>

    <ParamField body="reference_image_urls" type="list<string>" required>
      A set of images to use as character references. Currently only 1 image is supported, rest will be ignored. (maximum total size 10MB across all character references). The images should be in JPEG, PNG or WebP format
    </ParamField>

    <ParamField body="reference_mask_urls" type="list<string>">
      A set of masks to apply to the character references. Currently only 1 mask is supported, rest will be ignored. (maximum total size 10MB across all character references). The masks should be in JPEG, PNG or WebP format
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<File>" required />

    <ParamField body="seed" type="integer" required>
      Seed used for the random number generator
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "rendering_speed": "BALANCED",
      "expand_prompt": true,
      "num_images": 1,
      "sync_mode": false,
      "prompt": "woman holding bag",
      "image_url": "https://v3.fal.media/files/panda/-LC_gNNV3wUHaGMQT3klE_output.png",
      "mask_url": "https://v3.fal.media/files/panda/jVDAgSkpsZFDP080ceSZJ_woman_face_mask.png",
      "reference_image_urls": [
        "https://v3.fal.media/files/kangaroo/0rinwnj_Kn9Fsu2dK-aKm_image.png"
      ]
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://v3.fal.media/files/zebra/JJR2zayRdL3Pg7kr9cFyk_image.png"
        }
      ],
      "seed": 123456
    }
    ```
  </Tab>

  <Tab title="Remix">
    **Endpoint:** `POST https://fal.run/fal-ai/ideogram/character/remix`
    **Endpoint ID:** `fal-ai/ideogram/character/remix`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/character/remix/playground">
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
          "fal-ai/ideogram/character/remix",
          arguments={
              "prompt": "A glamorous portrait photograph of a woman in an elegant ballroom setting. The subject wears a champagne-colored ball gown with a fitted bodice, long sleeves, and a full skirt adorned with delicate lace appliques. The dress features a crystal-embellished hair accessory and pearl drop earrings. The grand staircase has ornate gold railings and leads to an elaborate crystal chandelier hanging from an arched ceiling. The walls are decorated with classical paintings featuring floral motifs. The lighting is warm and dramatic, creating a soft glow throughout the space. The composition is shot in a formal portrait style with the subject positioned on the lower landing of the staircase, looking over her shoulder at the camera.",
              "image_url": "https://v3.fal.media/files/panda/mcxydS-_4ZjfBWFtgoo2z_XHLsl7khq6dC6Qp3cIdJl08rG0I.avif",
              "reference_image_urls": [
                  "https://v3.fal.media/files/kangaroo/0rinwnj_Kn9Fsu2dK-aKm_image.png"
              ]
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/ideogram/character/remix", {
        input: {
            prompt: "A glamorous portrait photograph of a woman in an elegant ballroom setting. The subject wears a champagne-colored ball gown with a fitted bodice, long sleeves, and a full skirt adorned with delicate lace appliques. The dress features a crystal-embellished hair accessory and pearl drop earrings. The grand staircase has ornate gold railings and leads to an elaborate crystal chandelier hanging from an arched ceiling. The walls are decorated with classical paintings featuring floral motifs. The lighting is warm and dramatic, creating a soft glow throughout the space. The composition is shot in a formal portrait style with the subject positioned on the lower landing of the staircase, looking over her shoulder at the camera.",
            image_url: "https://v3.fal.media/files/panda/mcxydS-_4ZjfBWFtgoo2z_XHLsl7khq6dC6Qp3cIdJl08rG0I.avif",
            reference_image_urls: [
              "https://v3.fal.media/files/kangaroo/0rinwnj_Kn9Fsu2dK-aKm_image.png"
            ]
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
        --url https://fal.run/fal-ai/ideogram/character/remix \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A glamorous portrait photograph of a woman in an elegant ballroom setting. The subject wears a champagne-colored ball gown with a fitted bodice, long sleeves, and a full skirt adorned with delicate lace appliques. The dress features a crystal-embellished hair accessory and pearl drop earrings. The grand staircase has ornate gold railings and leads to an elaborate crystal chandelier hanging from an arched ceiling. The walls are decorated with classical paintings featuring floral motifs. The lighting is warm and dramatic, creating a soft glow throughout the space. The composition is shot in a formal portrait style with the subject positioned on the lower landing of the staircase, looking over her shoulder at the camera.",
        "image_url": "https://v3.fal.media/files/panda/mcxydS-_4ZjfBWFtgoo2z_XHLsl7khq6dC6Qp3cIdJl08rG0I.avif",
        "reference_image_urls": [
          "https://v3.fal.media/files/kangaroo/0rinwnj_Kn9Fsu2dK-aKm_image.png"
        ]
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_urls" type="list<string>">
      A set of images to use as style references (maximum total size 10MB across all style references). The images should be in JPEG, PNG or WebP format
    </ParamField>

    <ParamField body="rendering_speed" type="RenderingSpeedEnum" default="BALANCED">
      The rendering speed to use. Default value: `"BALANCED"`

      Possible values: `TURBO`, `BALANCED`, `QUALITY`
    </ParamField>

    <ParamField body="color_palette" type="ColorPalette">
      A color palette for generation, must EITHER be specified via one of the presets (name) or explicitly via hexadecimal representations of the color with optional weights (members)
    </ParamField>

    <ParamField body="style_codes" type="list<string>">
      A list of 8 character hexadecimal codes representing the style of the image. Cannot be used in conjunction with style\_reference\_images or style
    </ParamField>

    <ParamField body="style" type="StyleEnum" default="AUTO">
      The style type to generate with. Cannot be used with style\_codes. Default value: `"AUTO"`

      Possible values: `AUTO`, `REALISTIC`, `FICTION`
    </ParamField>

    <ParamField body="expand_prompt" type="boolean" default="true">
      Determine if MagicPrompt should be used in generating the request or not. Default value: `true`
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      Number of images to generate. Default value: `1`

      Range: `1` to `8`
    </ParamField>

    <ParamField body="seed" type="integer">
      Seed for the random number generator
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="prompt" type="string" required>
      The prompt to remix the image with
    </ParamField>

    <ParamField body="image_url" type="string" required>
      The image URL to remix
    </ParamField>

    <ParamField body="strength" type="float" default="0.8">
      Strength of the input image in the remix Default value: `0.8`

      Range: `0.01` to `1`
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="square_hd">
      The resolution of the generated image Default value: `square_hd`

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="">
      Description of what to exclude from an image. Descriptions in the prompt take precedence to descriptions in the negative prompt. Default value: `""`
    </ParamField>

    <ParamField body="reference_image_urls" type="list<string>" required>
      A set of images to use as character references. Currently only 1 image is supported, rest will be ignored. (maximum total size 10MB across all character references). The images should be in JPEG, PNG or WebP format
    </ParamField>

    <ParamField body="reference_mask_urls" type="list<string>">
      A set of masks to apply to the character references. Currently only 1 mask is supported, rest will be ignored. (maximum total size 10MB across all character references). The masks should be in JPEG, PNG or WebP format
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<File>" required />

    <ParamField body="seed" type="integer" required>
      Seed used for the random number generator
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "rendering_speed": "BALANCED",
      "style": "AUTO",
      "expand_prompt": true,
      "num_images": 1,
      "sync_mode": false,
      "prompt": "A glamorous portrait photograph of a woman in an elegant ballroom setting. The subject wears a champagne-colored ball gown with a fitted bodice, long sleeves, and a full skirt adorned with delicate lace appliques. The dress features a crystal-embellished hair accessory and pearl drop earrings. The grand staircase has ornate gold railings and leads to an elaborate crystal chandelier hanging from an arched ceiling. The walls are decorated with classical paintings featuring floral motifs. The lighting is warm and dramatic, creating a soft glow throughout the space. The composition is shot in a formal portrait style with the subject positioned on the lower landing of the staircase, looking over her shoulder at the camera.",
      "image_url": "https://v3.fal.media/files/panda/mcxydS-_4ZjfBWFtgoo2z_XHLsl7khq6dC6Qp3cIdJl08rG0I.avif",
      "strength": 0.8,
      "image_size": "square_hd",
      "negative_prompt": "",
      "reference_image_urls": [
        "https://v3.fal.media/files/kangaroo/0rinwnj_Kn9Fsu2dK-aKm_image.png"
      ]
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://v3.fal.media/files/zebra/4F1SvlaPbkZt-Mle4CTH9_image.png"
        }
      ],
      "seed": 123456
    }
    ```
  </Tab>
</Tabs>

## Related

* [Ideogram V3 Character Edit](/model-api-reference/image-generation-api/ideogram-v3-character-edit) — Image Generation
* [Ideogram V3 Character Remix](/model-api-reference/image-generation-api/ideogram-v3-character-remix) — Image Generation
* [Ideogram V3 Character](/model-api-reference/image-generation-api/ideogram-v3-character) — Image Generation

## Limitations

* `rendering_speed` restricted to: `TURBO`, `BALANCED`, `QUALITY`
* `style` restricted to: `AUTO`, `REALISTIC`, `FICTION`
* `num_images` range: 1 to 8
* `image_size` restricted to: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
* `strength` range: 0.01 to 1
