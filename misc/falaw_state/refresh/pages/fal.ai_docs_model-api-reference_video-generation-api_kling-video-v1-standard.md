> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video V1 Standard API

> API reference for Kling Video V1 Standard. Generate video clips from your images using Kling 1.0

<Tabs>
  <Tab title="Image To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/v1/standard/image-to-video`
    **Endpoint ID:** `fal-ai/kling-video/v1/standard/image-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v1/standard/image-to-video/playground">
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
          "fal-ai/kling-video/v1/standard/image-to-video",
          arguments={
              "prompt": "Snowflakes fall as a car moves forward along the road.",
              "image_url": "https://storage.googleapis.com/falserverless/kling/kling_input.jpeg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/v1/standard/image-to-video", {
        input: {
            prompt: "Snowflakes fall as a car moves forward along the road.",
            image_url: "https://storage.googleapis.com/falserverless/kling/kling_input.jpeg"
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
        --url https://fal.run/fal-ai/kling-video/v1/standard/image-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Snowflakes fall as a car moves forward along the road.",
        "image_url": "https://storage.googleapis.com/falserverless/kling/kling_input.jpeg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt for the video
    </ParamField>

    <ParamField body="image_url" type="string" required>
      URL of the image to be used for the video
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="5">
      The duration of the generated video in seconds Default value: `"5"`

      Possible values: `5`, `10`
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="blur, distort, and low quality">
      Default value: `"blur, distort, and low quality"`
    </ParamField>

    <ParamField body="cfg_scale" type="float" default="0.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt. Default value: `0.5`

      Range: `0` to `1`
    </ParamField>

    <ParamField body="tail_image_url" type="string">
      URL of the image to be used for the end of the video
    </ParamField>

    <ParamField body="static_mask_url" type="string">
      URL of the image for Static Brush Application Area (Mask image created by users using the motion brush)
    </ParamField>

    <ParamField body="dynamic_masks" type="list<DynamicMask>">
      List of dynamic masks
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Snowflakes fall as a car moves forward along the road.",
      "image_url": "https://storage.googleapis.com/falserverless/kling/kling_input.jpeg",
      "duration": "5",
      "negative_prompt": "blur, distort, and low quality",
      "cfg_scale": 0.5,
      "static_mask_url": "https://storage.googleapis.com/falserverless/kling/new_static_mask.png",
      "dynamic_masks": [
        {
          "mask_url": "https://storage.googleapis.com/falserverless/kling/new_dynamic_mask.png",
          "trajectories": [
            {
              "x": 279,
              "y": 219
            },
            {
              "x": 417,
              "y": 65
            }
          ]
        }
      ]
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://storage.googleapis.com/falserverless/kling/kling_i2v_output.mp4"
      }
    }
    ```
  </Tab>

  <Tab title="Text To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/v1/standard/text-to-video`
    **Endpoint ID:** `fal-ai/kling-video/v1/standard/text-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v1/standard/text-to-video/playground">
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
          "fal-ai/kling-video/v1/standard/text-to-video",
          arguments={
              "prompt": "A stylish woman walks down a Tokyo street filled with warm glowing neon and animated city signage. She wears a black leather jacket, a long red dress, and black boots, and carries a black purse."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/v1/standard/text-to-video", {
        input: {
            prompt: "A stylish woman walks down a Tokyo street filled with warm glowing neon and animated city signage. She wears a black leather jacket, a long red dress, and black boots, and carries a black purse."
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
        --url https://fal.run/fal-ai/kling-video/v1/standard/text-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A stylish woman walks down a Tokyo street filled with warm glowing neon and animated city signage. She wears a black leather jacket, a long red dress, and black boots, and carries a black purse."
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required />

    <ParamField body="duration" type="DurationEnum" default="5">
      The duration of the generated video in seconds Default value: `"5"`

      Possible values: `5`, `10`
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="16:9">
      The aspect ratio of the generated video frame Default value: `"16:9"`

      Possible values: `16:9`, `9:16`, `1:1`
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="blur, distort, and low quality">
      Default value: `"blur, distort, and low quality"`
    </ParamField>

    <ParamField body="cfg_scale" type="float" default="0.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt. Default value: `0.5`

      Range: `0` to `1`
    </ParamField>

    <ParamField body="camera_control" type="Enum">
      Camera control parameters

      Possible values: `down_back`, `forward_up`, `right_turn_forward`, `left_turn_forward`
    </ParamField>

    <ParamField body="advanced_camera_control" type="CameraControl">
      Advanced Camera control parameters
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A stylish woman walks down a Tokyo street filled with warm glowing neon and animated city signage. She wears a black leather jacket, a long red dress, and black boots, and carries a black purse.",
      "duration": "5",
      "aspect_ratio": "16:9",
      "negative_prompt": "blur, distort, and low quality",
      "cfg_scale": 0.5
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://v2.fal.media/files/fb33a862b94d4d7195e610e4cbc5d392_output.mp4"
      }
    }
    ```
  </Tab>

  <Tab title="Ai Avatar">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/v1/standard/ai-avatar`
    **Endpoint ID:** `fal-ai/kling-video/v1/standard/ai-avatar`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v1/standard/ai-avatar/playground">
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
          "fal-ai/kling-video/v1/standard/ai-avatar",
          arguments={
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling_ai_avatar_input.jpg",
              "audio_url": "https://v3.fal.media/files/rabbit/9_0ZG_geiWjZOmn9yscO6_output.mp3"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/v1/standard/ai-avatar", {
        input: {
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/kling_ai_avatar_input.jpg",
            audio_url: "https://v3.fal.media/files/rabbit/9_0ZG_geiWjZOmn9yscO6_output.mp3"
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
        --url https://fal.run/fal-ai/kling-video/v1/standard/ai-avatar \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling_ai_avatar_input.jpg",
        "audio_url": "https://v3.fal.media/files/rabbit/9_0ZG_geiWjZOmn9yscO6_output.mp3"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The URL of the image to use as your avatar
    </ParamField>

    <ParamField body="audio_url" type="string" required>
      The URL of the audio file.
    </ParamField>

    <ParamField body="prompt" type="string" default=".">
      The prompt to use for the video generation. Default value: `"."`
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video
    </ParamField>

    <ParamField body="duration" type="float" required>
      Duration of the output video in seconds.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling_ai_avatar_input.jpg",
      "audio_url": "https://v3.fal.media/files/rabbit/9_0ZG_geiWjZOmn9yscO6_output.mp3",
      "prompt": "."
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://v3.fal.media/files/penguin/ln3x7H1p1jL0Pwo7675NI_output.mp4"
      }
    }
    ```
  </Tab>

  <Tab title="Effects">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/v1/standard/effects`
    **Endpoint ID:** `fal-ai/kling-video/v1/standard/effects`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v1/standard/effects/playground">
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
          "fal-ai/kling-video/v1/standard/effects",
          arguments={
              "effect_scene": "hug"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/v1/standard/effects", {
        input: {
            effect_scene: "hug"
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
        --url https://fal.run/fal-ai/kling-video/v1/standard/effects \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "effect_scene": "hug"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="input_image_urls" type="list<string>">
      URL of images to be used for hug, kiss or heart\_gesture video.
    </ParamField>

    <ParamField body="effect_scene" type="EffectSceneEnum" required>
      The effect scene to use for the video generation

      Possible values: `hug`, `kiss`, `heart_gesture`, `squish`, `expansion`, `fuzzyfuzzy`, `bloombloom`, `dizzydizzy`, `jelly_press`, `jelly_slice`, `jelly_squish`, `jelly_jiggle`, `pixelpixel`, `yearbook`, `instant_film`, `anime_figure`, `rocketrocket`, `fly_fly`, `disappear`, `lightning_power`, `bullet_time`, `bullet_time_360`, `media_interview`, `day_to_night`, `let's_ride`, `jumpdrop`, `swish_swish`, `running_man`, `jazz_jazz`, `swing_swing`, `skateskate`, `building_sweater`, `pure_white_wings`, `black_wings`, `golden_wing`, `pink_pink_wings`, `rampage_ape`, `a_list_look`, `countdown_teleport`, `firework_2026`, `instant_christmas`, `birthday_star`, `firework`, `celebration`, `tiger_hug_pro`, `pet_lion_pro`, `guardian_spirit`, `squeeze_scream`, `inner_voice`, `memory_alive`, `guess_what`, `eagle_snatch`, `hug_from_past`, `instant_kid`, `dollar_rain`, `cry_cry`, `building_collapse`, `mushroom`, `jesus_hug`, `shark_alert`, `lie_flat`, `polar_bear_hug`, `brown_bear_hug`, `office_escape_plow`, `watermelon_bomb`, `boss_coming`, `wig_out`, `car_explosion`, `tiger_hug`, `siblings`, `construction_worker`, `snatched`, `felt_felt`, `plushcut`, `drunk_dance`, `drunk_dance_pet`, `daoma_dance`, `bouncy_dance`, `smooth_sailing_dance`, `new_year_greeting`, `lion_dance`, `prosperity`, `great_success`, `golden_horse_fortune`, `red_packet_box`, `lucky_horse_year`, `lucky_red_packet`, `lucky_money_come`, `lion_dance_pet`, `dumpling_making_pet`, `fish_making_pet`, `pet_red_packet`, `lantern_glow`, `expression_challenge`, `overdrive`, `heart_gesture_dance`, `poping`, `martial_arts`, `running`, `nezha`, `motorcycle_dance`, `subject_3_dance`, `ghost_step_dance`, `phantom_jewel`, `zoom_out`, `cheers_2026`, `kiss_pro`, `fight_pro`, `hug_pro`, `heart_gesture_pro`, `dollar_rain_pro`, `pet_bee_pro`, `santa_random_surprise`, `magic_match_tree`, `happy_birthday`, `thumbs_up_pro`, `surprise_bouquet`, `bouquet_drop`, `3d_cartoon_1_pro`, `glamour_photo_shoot`, `box_of_joy`, `first_toast_of_the_year`, `my_santa_pic`, `santa_gift`, `steampunk_christmas`, `snowglobe`, `christmas_photo_shoot`, `ornament_crash`, `santa_express`, `particle_santa_surround`, `coronation_of_frost`, `spark_in_the_snow`, `scarlet_and_snow`, `cozy_toon_wrap`, `bullet_time_lite`, `magic_cloak`, `balloon_parade`, `jumping_ginger_joy`, `c4d_cartoon_pro`, `venomous_spider`, `throne_of_king`, `luminous_elf`, `woodland_elf`, `japanese_anime_1`, `american_comics`, `snowboarding`, `witch_transform`, `vampire_transform`, `pumpkin_head_transform`, `demon_transform`, `mummy_transform`, `zombie_transform`, `cute_pumpkin_transform`, `cute_ghost_transform`, `knock_knock_halloween`, `halloween_escape`, `baseball`, `trampoline`, `trampoline_night`, `pucker_up`, `feed_mooncake`, `flyer`, `dishwasher`, `pet_chinese_opera`, `magic_fireball`, `gallery_ring`, `pet_moto_rider`, `muscle_pet`, `pet_delivery`, `mythic_style`, `steampunk`, `3d_cartoon_2`, `pet_chef`, `santa_gifts`, `santa_hug`, `girlfriend`, `boyfriend`, `heart_gesture_1`, `pet_wizard`, `smoke_smoke`, `gun_shot`, `double_gun`, `pet_warrior`, `long_hair`, `pet_dance`, `wool_curly`, `pet_bee`, `marry_me`, `piggy_morph`, `ski_ski`, `magic_broom`, `splashsplash`, `surfsurf`, `fairy_wing`, `angel_wing`, `dark_wing`, `emoji`
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="5">
      The duration of the generated video in seconds Default value: `"5"`

      Possible values: `5`, `10`
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "input_image_urls": [
        "https://storage.googleapis.com/falserverless/juggernaut_examples/VHXMavzPyI27zi6JseyL4.png",
        "https://storage.googleapis.com/falserverless/juggernaut_examples/QEW5VrzccxGva7mPfEXjf.png"
      ],
      "effect_scene": "hug",
      "duration": "5"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "content_type": "video/mp4",
        "file_name": "output.mp4",
        "url": "https://storage.googleapis.com/falserverless/kling/kling_ex.mp4.mp4"
      }
    }
    ```
  </Tab>
</Tabs>

## Related

* [Kling 1.0](/model-api-reference/video-generation-api/kling-1.0) — Video Generation
* [Kling AI Avatar v2 Pro](/model-api-reference/video-generation-api/kling-ai-avatar-v2-pro) — Video Generation
* [Kling AI Avatar v2 Standard](/model-api-reference/video-generation-api/kling-ai-avatar-v2-standard) — Video Generation
* [Kling TTS](/model-api-reference/audio-api/kling-tts) — Audio
* [Kling AI Avatar Pro](/model-api-reference/video-generation-api/kling-ai-avatar-pro) — Video Generation
* [Kling 1.6](/model-api-reference/video-generation-api/kling-1.6) — Video Generation
* [Kling 1.5](/model-api-reference/video-generation-api/kling-1.5) — Video Generation

## Limitations

* `duration` restricted to: `5`, `10`
* `cfg_scale` range: 0 to 1
* `aspect_ratio` restricted to: `16:9`, `9:16`, `1:1`
* `camera_control` restricted to: `down_back`, `forward_up`, `right_turn_forward`, `left_turn_forward`
