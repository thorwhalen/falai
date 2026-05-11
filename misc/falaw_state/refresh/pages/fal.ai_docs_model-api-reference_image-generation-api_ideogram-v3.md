> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ideogram V3 API

> API reference for Ideogram V3. Generate high-quality images, posters, and logos with Ideogram V3. Features exceptional typography handling and realistic outputs optimized for commercial and creative u

<Tabs>
  <Tab title="V3">
    **Endpoint:** `POST https://fal.run/fal-ai/ideogram/v3`
    **Endpoint ID:** `fal-ai/ideogram/v3`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/v3/playground">
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
          "fal-ai/ideogram/v3",
          arguments={
              "prompt": "The Bone Forest stretched across the horizon, its trees fashioned from the ossified remains of ancient leviathans that once swam through the sky. Shamans with antlers growing from their shoulders and eyes that revealed the true nature of any being they beheld conducted rituals to commune with the spirits that still inhabited the calcified grove. In sky writes \"Ideogram V3 in fal.ai\""
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/ideogram/v3", {
        input: {
            prompt: "The Bone Forest stretched across the horizon, its trees fashioned from the ossified remains of ancient leviathans that once swam through the sky. Shamans with antlers growing from their shoulders and eyes that revealed the true nature of any being they beheld conducted rituals to commune with the spirits that still inhabited the calcified grove. In sky writes \"Ideogram V3 in fal.ai\""
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
        --url https://fal.run/fal-ai/ideogram/v3 \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "The Bone Forest stretched across the horizon, its trees fashioned from the ossified remains of ancient leviathans that once swam through the sky. Shamans with antlers growing from their shoulders and eyes that revealed the true nature of any being they beheld conducted rituals to commune with the spirits that still inhabited the calcified grove. In sky writes \"Ideogram V3 in fal.ai\""
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

    <ParamField body="style" type="Enum">
      The style type to generate with. Cannot be used with style\_codes.

      Possible values: `AUTO`, `GENERAL`, `REALISTIC`, `DESIGN`
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

    <ParamField body="style_preset" type="Enum">
      Style preset for generation. The chosen style preset will guide the generation.

      Possible values: `80S_ILLUSTRATION`, `90S_NOSTALGIA`, `ABSTRACT_ORGANIC`, `ANALOG_NOSTALGIA`, `ART_BRUT`, `ART_DECO`, `ART_POSTER`, `AURA`, `AVANT_GARDE`, `BAUHAUS`, `BLUEPRINT`, `BLURRY_MOTION`, `BRIGHT_ART`, `C4D_CARTOON`, `CHILDRENS_BOOK`, `COLLAGE`, `COLORING_BOOK_I`, `COLORING_BOOK_II`, `CUBISM`, `DARK_AURA`, `DOODLE`, `DOUBLE_EXPOSURE`, `DRAMATIC_CINEMA`, `EDITORIAL`, `EMOTIONAL_MINIMAL`, `ETHEREAL_PARTY`, `EXPIRED_FILM`, `FLAT_ART`, `FLAT_VECTOR`, `FOREST_REVERIE`, `GEO_MINIMALIST`, `GLASS_PRISM`, `GOLDEN_HOUR`, `GRAFFITI_I`, `GRAFFITI_II`, `HALFTONE_PRINT`, `HIGH_CONTRAST`, `HIPPIE_ERA`, `ICONIC`, `JAPANDI_FUSION`, `JAZZY`, `LONG_EXPOSURE`, `MAGAZINE_EDITORIAL`, `MINIMAL_ILLUSTRATION`, `MIXED_MEDIA`, `MONOCHROME`, `NIGHTLIFE`, `OIL_PAINTING`, `OLD_CARTOONS`, `PAINT_GESTURE`, `POP_ART`, `RETRO_ETCHING`, `RIVIERA_POP`, `SPOTLIGHT_80S`, `STYLIZED_RED`, `SURREAL_COLLAGE`, `TRAVEL_POSTER`, `VINTAGE_GEO`, `VINTAGE_POSTER`, `WATERCOLOR`, `WEIRD`, `WOODBLOCK_PRINT`
    </ParamField>

    <ParamField body="prompt" type="string" required />

    <ParamField body="image_size" type="ImageSize | Enum" default="square_hd">
      The resolution of the generated image Default value: `square_hd`

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="">
      Description of what to exclude from an image. Descriptions in the prompt take precedence to descriptions in the negative prompt. Default value: `""`
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
      "prompt": "The Bone Forest stretched across the horizon, its trees fashioned from the ossified remains of ancient leviathans that once swam through the sky. Shamans with antlers growing from their shoulders and eyes that revealed the true nature of any being they beheld conducted rituals to commune with the spirits that still inhabited the calcified grove. In sky writes \"Ideogram V3 in fal.ai\"",
      "image_size": "square_hd",
      "negative_prompt": ""
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://v3.fal.media/files/penguin/lHdRabS80guysb8Zw1kul_image.png"
        }
      ],
      "seed": 123456
    }
    ```
  </Tab>

  <Tab title="Reframe">
    **Endpoint:** `POST https://fal.run/fal-ai/ideogram/v3/reframe`
    **Endpoint ID:** `fal-ai/ideogram/v3/reframe`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/v3/reframe/playground">
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
          "fal-ai/ideogram/v3/reframe",
          arguments={
              "image_url": "https://v3.fal.media/files/lion/0qJs_qW8nz0wYsXhFa6Tk.png",
              "image_size": "square_hd"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/ideogram/v3/reframe", {
        input: {
            image_url: "https://v3.fal.media/files/lion/0qJs_qW8nz0wYsXhFa6Tk.png",
            image_size: "square_hd"
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
        --url https://fal.run/fal-ai/ideogram/v3/reframe \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://v3.fal.media/files/lion/0qJs_qW8nz0wYsXhFa6Tk.png",
        "image_size": "square_hd"
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

    <ParamField body="style" type="Enum">
      The style type to generate with. Cannot be used with style\_codes.

      Possible values: `AUTO`, `GENERAL`, `REALISTIC`, `DESIGN`
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

    <ParamField body="style_preset" type="Enum">
      Style preset for generation. The chosen style preset will guide the generation.

      Possible values: `80S_ILLUSTRATION`, `90S_NOSTALGIA`, `ABSTRACT_ORGANIC`, `ANALOG_NOSTALGIA`, `ART_BRUT`, `ART_DECO`, `ART_POSTER`, `AURA`, `AVANT_GARDE`, `BAUHAUS`, `BLUEPRINT`, `BLURRY_MOTION`, `BRIGHT_ART`, `C4D_CARTOON`, `CHILDRENS_BOOK`, `COLLAGE`, `COLORING_BOOK_I`, `COLORING_BOOK_II`, `CUBISM`, `DARK_AURA`, `DOODLE`, `DOUBLE_EXPOSURE`, `DRAMATIC_CINEMA`, `EDITORIAL`, `EMOTIONAL_MINIMAL`, `ETHEREAL_PARTY`, `EXPIRED_FILM`, `FLAT_ART`, `FLAT_VECTOR`, `FOREST_REVERIE`, `GEO_MINIMALIST`, `GLASS_PRISM`, `GOLDEN_HOUR`, `GRAFFITI_I`, `GRAFFITI_II`, `HALFTONE_PRINT`, `HIGH_CONTRAST`, `HIPPIE_ERA`, `ICONIC`, `JAPANDI_FUSION`, `JAZZY`, `LONG_EXPOSURE`, `MAGAZINE_EDITORIAL`, `MINIMAL_ILLUSTRATION`, `MIXED_MEDIA`, `MONOCHROME`, `NIGHTLIFE`, `OIL_PAINTING`, `OLD_CARTOONS`, `PAINT_GESTURE`, `POP_ART`, `RETRO_ETCHING`, `RIVIERA_POP`, `SPOTLIGHT_80S`, `STYLIZED_RED`, `SURREAL_COLLAGE`, `TRAVEL_POSTER`, `VINTAGE_GEO`, `VINTAGE_POSTER`, `WATERCOLOR`, `WEIRD`, `WOODBLOCK_PRINT`
    </ParamField>

    <ParamField body="image_url" type="string" required>
      The image URL to reframe
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" required>
      The resolution for the reframed output image

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
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
      "num_images": 1,
      "sync_mode": false,
      "image_url": "https://v3.fal.media/files/lion/0qJs_qW8nz0wYsXhFa6Tk.png",
      "image_size": "square_hd"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://v3.fal.media/files/zebra/LVW4AhVs3sCxsVKdg3EfT_image.png"
        }
      ],
      "seed": 123456
    }
    ```
  </Tab>

  <Tab title="Generate Transparent">
    **Endpoint:** `POST https://fal.run/fal-ai/ideogram/v3/generate-transparent`
    **Endpoint ID:** `fal-ai/ideogram/v3/generate-transparent`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/v3/generate-transparent/playground">
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
          "fal-ai/ideogram/v3/generate-transparent",
          arguments={
              "prompt": "A logo for Ideogram Coffee."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/ideogram/v3/generate-transparent", {
        input: {
            prompt: "A logo for Ideogram Coffee."
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
        --url https://fal.run/fal-ai/ideogram/v3/generate-transparent \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A logo for Ideogram Coffee."
      }'
      ```
    </CodeGroup>

    ## Examples

    > A low-poly 3D fox sitting upright, in warm orange and white geometric facets

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a954d91/792FF8-bFC7lEaJ5KQ1n8_image.png" alt="Generated image: A low-poly 3D fox sitting upright, in warm orange and white geometric facets" />
    </Frame>

    ### Input Schema

    <ParamField body="prompt" type="string" required />

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="1:1">
      The aspect ratio of the generated image. Default value: `"1:1"`

      Possible values: `1:3`, `3:1`, `1:2`, `2:1`, `9:16`, `16:9`, `10:16`, `16:10`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `1:1`
    </ParamField>

    <ParamField body="rendering_speed" type="RenderingSpeedEnum" default="BALANCED">
      The rendering speed to use. Default value: `"BALANCED"`

      Possible values: `FLASH`, `TURBO`, `BALANCED`, `QUALITY`
    </ParamField>

    <ParamField body="expand_prompt" type="boolean" default="true">
      Determine if MagicPrompt should be used in generating the request or not. Default value: `true`
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="">
      Description of what to exclude from an image. Descriptions in the prompt take precedence to descriptions in the negative prompt. Default value: `""`
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

    ### Output Schema

    <ParamField body="images" type="list<File>" required />

    <ParamField body="seed" type="integer" required>
      Seed used for the random number generator
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A logo for Ideogram Coffee.",
      "aspect_ratio": "1:1",
      "rendering_speed": "BALANCED",
      "expand_prompt": true,
      "negative_prompt": "",
      "num_images": 1,
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://v3.fal.media/files/lion/AUfCjtLkLOsdc9zEFrV-5_image.png"
        }
      ],
      "seed": 123456
    }
    ```
  </Tab>

  <Tab title="Edit">
    **Endpoint:** `POST https://fal.run/fal-ai/ideogram/v3/edit`
    **Endpoint ID:** `fal-ai/ideogram/v3/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/v3/edit/playground">
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
          "fal-ai/ideogram/v3/edit",
          arguments={
              "prompt": "black bag",
              "image_url": "https://v3.fal.media/files/panda/-LC_gNNV3wUHaGMQT3klE_output.png",
              "mask_url": "https://v3.fal.media/files/kangaroo/1dd3zEL5MXQ3Kb4-mRi9d_indir%20(20).png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/ideogram/v3/edit", {
        input: {
            prompt: "black bag",
            image_url: "https://v3.fal.media/files/panda/-LC_gNNV3wUHaGMQT3klE_output.png",
            mask_url: "https://v3.fal.media/files/kangaroo/1dd3zEL5MXQ3Kb4-mRi9d_indir%20(20).png"
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
        --url https://fal.run/fal-ai/ideogram/v3/edit \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "black bag",
        "image_url": "https://v3.fal.media/files/panda/-LC_gNNV3wUHaGMQT3klE_output.png",
        "mask_url": "https://v3.fal.media/files/kangaroo/1dd3zEL5MXQ3Kb4-mRi9d_indir%20(20).png"
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

    <ParamField body="style_preset" type="Enum">
      Style preset for generation. The chosen style preset will guide the generation.

      Possible values: `80S_ILLUSTRATION`, `90S_NOSTALGIA`, `ABSTRACT_ORGANIC`, `ANALOG_NOSTALGIA`, `ART_BRUT`, `ART_DECO`, `ART_POSTER`, `AURA`, `AVANT_GARDE`, `BAUHAUS`, `BLUEPRINT`, `BLURRY_MOTION`, `BRIGHT_ART`, `C4D_CARTOON`, `CHILDRENS_BOOK`, `COLLAGE`, `COLORING_BOOK_I`, `COLORING_BOOK_II`, `CUBISM`, `DARK_AURA`, `DOODLE`, `DOUBLE_EXPOSURE`, `DRAMATIC_CINEMA`, `EDITORIAL`, `EMOTIONAL_MINIMAL`, `ETHEREAL_PARTY`, `EXPIRED_FILM`, `FLAT_ART`, `FLAT_VECTOR`, `FOREST_REVERIE`, `GEO_MINIMALIST`, `GLASS_PRISM`, `GOLDEN_HOUR`, `GRAFFITI_I`, `GRAFFITI_II`, `HALFTONE_PRINT`, `HIGH_CONTRAST`, `HIPPIE_ERA`, `ICONIC`, `JAPANDI_FUSION`, `JAZZY`, `LONG_EXPOSURE`, `MAGAZINE_EDITORIAL`, `MINIMAL_ILLUSTRATION`, `MIXED_MEDIA`, `MONOCHROME`, `NIGHTLIFE`, `OIL_PAINTING`, `OLD_CARTOONS`, `PAINT_GESTURE`, `POP_ART`, `RETRO_ETCHING`, `RIVIERA_POP`, `SPOTLIGHT_80S`, `STYLIZED_RED`, `SURREAL_COLLAGE`, `TRAVEL_POSTER`, `VINTAGE_GEO`, `VINTAGE_POSTER`, `WATERCOLOR`, `WEIRD`, `WOODBLOCK_PRINT`
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
      "prompt": "black bag",
      "image_url": "https://v3.fal.media/files/panda/-LC_gNNV3wUHaGMQT3klE_output.png",
      "mask_url": "https://v3.fal.media/files/kangaroo/1dd3zEL5MXQ3Kb4-mRi9d_indir%20(20).png"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://v3.fal.media/files/panda/xr7EI_0X5kM8fDOjjcMei_image.png"
        }
      ],
      "seed": 123456
    }
    ```
  </Tab>

  <Tab title="Layerize Text">
    **Endpoint:** `POST https://fal.run/fal-ai/ideogram/v3/layerize-text`
    **Endpoint ID:** `fal-ai/ideogram/v3/layerize-text`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/v3/layerize-text/playground">
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
          "fal-ai/ideogram/v3/layerize-text",
          arguments={
              "image_url": "https://v3.fal.media/files/lion/0qJs_qW8nz0wYsXhFa6Tk.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/ideogram/v3/layerize-text", {
        input: {
            image_url: "https://v3.fal.media/files/lion/0qJs_qW8nz0wYsXhFa6Tk.png"
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
        --url https://fal.run/fal-ai/ideogram/v3/layerize-text \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://v3.fal.media/files/lion/0qJs_qW8nz0wYsXhFa6Tk.png"
      }'
      ```
    </CodeGroup>

    ## Examples

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a9552a2/Nw6eNYNT6_UzsiMsVI9f9_image.png" alt="Example output from Ideogram" />
    </Frame>

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a955269/sCOtM2vExnZl_Qk9bUBq5_image.png" alt="Example output from Ideogram" />
    </Frame>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      URL of the flat graphic image to layerize. Must be JPEG, PNG, or WebP (max 10MB).
    </ParamField>

    <ParamField body="prompt" type="string">
      Optional prompt to guide the layerization.
    </ParamField>

    <ParamField body="seed" type="integer">
      Seed for the random number generator.
    </ParamField>

    <ParamField body="font_file_h1_url" type="string">
      URL of the font file to use for h1 text. Cannot be used with font\_name\_h1.
    </ParamField>

    <ParamField body="font_name_h1" type="string">
      Name of the font to use for h1 text. Cannot be used with font\_file\_h1\_url.
    </ParamField>

    <ParamField body="font_file_h2_url" type="string">
      URL of the font file to use for h2 text. Cannot be used with font\_name\_h2.
    </ParamField>

    <ParamField body="font_name_h2" type="string">
      Name of the font to use for h2 text. Cannot be used with font\_file\_h2\_url.
    </ParamField>

    <ParamField body="font_file_body_url" type="string">
      URL of the font file to use for body text. Cannot be used with font\_name\_body.
    </ParamField>

    <ParamField body="font_name_body" type="string">
      Name of the font to use for body text. Cannot be used with font\_file\_body\_url.
    </ParamField>

    <ParamField body="font_file_small_url" type="string">
      URL of the font file to use for small text. Cannot be used with font\_name\_small.
    </ParamField>

    <ParamField body="font_name_small" type="string">
      Name of the font to use for small text. Cannot be used with font\_file\_small\_url.
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="File" required>
      The background image with text removed.
    </ParamField>

    <ParamField body="prompt" type="string" required>
      The prompt used for layerization. May differ from the input prompt if MagicPrompt expanded it.
    </ParamField>

    <ParamField body="text_containers" type="list<object>">
      Structured text containers with hierarchical text data (container -> items -> spans).
    </ParamField>

    <ParamField body="text_html" type="string">
      Rendered overlay HTML for compositing text over the background image.
    </ParamField>

    <ParamField body="image_layers" type="list<object>">
      Image layers extracted from the design.
    </ParamField>

    <ParamField body="seed" type="integer" required>
      Seed used for the random number generator.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://v3.fal.media/files/lion/0qJs_qW8nz0wYsXhFa6Tk.png",
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
        "file_size": 4404019
      },
      "prompt": "",
      "seed": 123456
    }
    ```
  </Tab>

  <Tab title="Remix">
    **Endpoint:** `POST https://fal.run/fal-ai/ideogram/v3/remix`
    **Endpoint ID:** `fal-ai/ideogram/v3/remix`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/v3/remix/playground">
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
          "fal-ai/ideogram/v3/remix",
          arguments={
              "prompt": "Old ancient city day light",
              "image_url": "https://v3.fal.media/files/lion/9-Yt8JfTw4OxrAjiUzwP9_output.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/ideogram/v3/remix", {
        input: {
            prompt: "Old ancient city day light",
            image_url: "https://v3.fal.media/files/lion/9-Yt8JfTw4OxrAjiUzwP9_output.png"
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
        --url https://fal.run/fal-ai/ideogram/v3/remix \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Old ancient city day light",
        "image_url": "https://v3.fal.media/files/lion/9-Yt8JfTw4OxrAjiUzwP9_output.png"
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

    <ParamField body="style" type="Enum">
      The style type to generate with. Cannot be used with style\_codes.

      Possible values: `AUTO`, `GENERAL`, `REALISTIC`, `DESIGN`
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
      "prompt": "Old ancient city day light",
      "image_url": "https://v3.fal.media/files/lion/9-Yt8JfTw4OxrAjiUzwP9_output.png",
      "strength": 0.8,
      "image_size": "square_hd",
      "negative_prompt": ""
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://v3.fal.media/files/koala/eYZG26O54NTdWzdpDWBL-_image.png"
        }
      ],
      "seed": 123456
    }
    ```
  </Tab>

  <Tab title="Replace Background">
    **Endpoint:** `POST https://fal.run/fal-ai/ideogram/v3/replace-background`
    **Endpoint ID:** `fal-ai/ideogram/v3/replace-background`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/v3/replace-background/playground">
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
          "fal-ai/ideogram/v3/replace-background",
          arguments={
              "prompt": "A beautiful sunset over mountains that writes Ideogram v3 in fal.ai",
              "image_url": "https://v3.fal.media/files/rabbit/F6dvKPFL9VzKiM8asJOgm_MJj6yUB6rGjTsv_1YHIcA_image.webp"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/ideogram/v3/replace-background", {
        input: {
            prompt: "A beautiful sunset over mountains that writes Ideogram v3 in fal.ai",
            image_url: "https://v3.fal.media/files/rabbit/F6dvKPFL9VzKiM8asJOgm_MJj6yUB6rGjTsv_1YHIcA_image.webp"
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
        --url https://fal.run/fal-ai/ideogram/v3/replace-background \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A beautiful sunset over mountains that writes Ideogram v3 in fal.ai",
        "image_url": "https://v3.fal.media/files/rabbit/F6dvKPFL9VzKiM8asJOgm_MJj6yUB6rGjTsv_1YHIcA_image.webp"
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

    <ParamField body="style" type="Enum">
      The style type to generate with. Cannot be used with style\_codes.

      Possible values: `AUTO`, `GENERAL`, `REALISTIC`, `DESIGN`
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

    <ParamField body="style_preset" type="Enum">
      Style preset for generation. The chosen style preset will guide the generation.

      Possible values: `80S_ILLUSTRATION`, `90S_NOSTALGIA`, `ABSTRACT_ORGANIC`, `ANALOG_NOSTALGIA`, `ART_BRUT`, `ART_DECO`, `ART_POSTER`, `AURA`, `AVANT_GARDE`, `BAUHAUS`, `BLUEPRINT`, `BLURRY_MOTION`, `BRIGHT_ART`, `C4D_CARTOON`, `CHILDRENS_BOOK`, `COLLAGE`, `COLORING_BOOK_I`, `COLORING_BOOK_II`, `CUBISM`, `DARK_AURA`, `DOODLE`, `DOUBLE_EXPOSURE`, `DRAMATIC_CINEMA`, `EDITORIAL`, `EMOTIONAL_MINIMAL`, `ETHEREAL_PARTY`, `EXPIRED_FILM`, `FLAT_ART`, `FLAT_VECTOR`, `FOREST_REVERIE`, `GEO_MINIMALIST`, `GLASS_PRISM`, `GOLDEN_HOUR`, `GRAFFITI_I`, `GRAFFITI_II`, `HALFTONE_PRINT`, `HIGH_CONTRAST`, `HIPPIE_ERA`, `ICONIC`, `JAPANDI_FUSION`, `JAZZY`, `LONG_EXPOSURE`, `MAGAZINE_EDITORIAL`, `MINIMAL_ILLUSTRATION`, `MIXED_MEDIA`, `MONOCHROME`, `NIGHTLIFE`, `OIL_PAINTING`, `OLD_CARTOONS`, `PAINT_GESTURE`, `POP_ART`, `RETRO_ETCHING`, `RIVIERA_POP`, `SPOTLIGHT_80S`, `STYLIZED_RED`, `SURREAL_COLLAGE`, `TRAVEL_POSTER`, `VINTAGE_GEO`, `VINTAGE_POSTER`, `WATERCOLOR`, `WEIRD`, `WOODBLOCK_PRINT`
    </ParamField>

    <ParamField body="prompt" type="string" required>
      Cyber punk city with neon lights and skyscrappers
    </ParamField>

    <ParamField body="image_url" type="string" required>
      The image URL whose background needs to be replaced
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
      "prompt": "A beautiful sunset over mountains that writes Ideogram v3 in fal.ai",
      "image_url": "https://v3.fal.media/files/rabbit/F6dvKPFL9VzKiM8asJOgm_MJj6yUB6rGjTsv_1YHIcA_image.webp"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://v3.fal.media/files/lion/AUfCjtLkLOsdc9zEFrV-5_image.png"
        }
      ],
      "seed": 123456
    }
    ```
  </Tab>
</Tabs>

## Related

* [Ideogram](/model-api-reference/image-generation-api/ideogram) — Image Generation
* [Ideogram V3 Edit](/model-api-reference/image-generation-api/ideogram-v3-edit) — Image Generation
* [Ideogram Replace Background](/model-api-reference/image-generation-api/ideogram-replace-background) — Image Generation
* [Ideogram Text to Image](/model-api-reference/image-generation-api/ideogram-text-to-image) — Image Generation

## Limitations

* `rendering_speed` restricted to: `TURBO`, `BALANCED`, `QUALITY`
* `style` restricted to: `AUTO`, `GENERAL`, `REALISTIC`, `DESIGN`
* `num_images` range: 1 to 8
* `image_size` restricted to: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
* `rendering_speed` restricted to: `FLASH`, `TURBO`, `BALANCED`, `QUALITY`
* `strength` range: 0.01 to 1
