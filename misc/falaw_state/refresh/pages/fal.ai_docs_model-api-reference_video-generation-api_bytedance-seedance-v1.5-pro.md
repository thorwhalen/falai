> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Seedance V1.5 Pro API

> API reference for Bytedance Seedance V1.5 Pro. Generate videos with audio with Seedance 1.5 (supports start & end frame)

<Tabs>
  <Tab title="Image To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedance/v1.5/pro/image-to-video`
    **Endpoint ID:** `fal-ai/bytedance/seedance/v1.5/pro/image-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedance/v1.5/pro/image-to-video/playground">
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
          "fal-ai/bytedance/seedance/v1.5/pro/image-to-video",
          arguments={
              "prompt": "A man is crying and he says \"I shouldn't have done it. I regret everything\"",
              "image_url": "https://v3b.fal.media/files/b/0a8773cd/REzCWn1BKUVuMFTxR-R3W_image_317.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/seedance/v1.5/pro/image-to-video", {
        input: {
            prompt: "A man is crying and he says \"I shouldn't have done it. I regret everything\"",
            image_url: "https://v3b.fal.media/files/b/0a8773cd/REzCWn1BKUVuMFTxR-R3W_image_317.png"
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
        --url https://fal.run/fal-ai/bytedance/seedance/v1.5/pro/image-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A man is crying and he says \"I shouldn'\''t have done it. I regret everything\"",
        "image_url": "https://v3b.fal.media/files/b/0a8773cd/REzCWn1BKUVuMFTxR-R3W_image_317.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt used to generate the video
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="16:9">
      The aspect ratio of the generated video Default value: `"16:9"`

      Possible values: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `auto`
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="720p">
      Video resolution - 480p for faster generation, 720p for balance, 1080p for higher quality Default value: `"720p"`

      Possible values: `480p`, `720p`, `1080p`
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="5">
      Duration of the video in seconds Default value: `"5"`

      Possible values: `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`
    </ParamField>

    <ParamField body="camera_fixed" type="boolean" default="false">
      Whether to fix the camera position
    </ParamField>

    <ParamField body="seed" type="integer">
      Random seed to control video generation. Use -1 for random.
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    <ParamField body="generate_audio" type="boolean" default="true">
      Whether to generate audio for the video Default value: `true`
    </ParamField>

    <ParamField body="image_url" type="string" required>
      The URL of the image used to generate video
    </ParamField>

    <ParamField body="end_image_url" type="string">
      The URL of the image the video ends with. Defaults to None.
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      Generated video file
    </ParamField>

    <ParamField body="seed" type="integer" required>
      Seed used for generation
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A man is crying and he says \"I shouldn't have done it. I regret everything\"",
      "aspect_ratio": "16:9",
      "resolution": "720p",
      "duration": "5",
      "camera_fixed": false,
      "enable_safety_checker": true,
      "generate_audio": true,
      "image_url": "https://v3b.fal.media/files/b/0a8773cd/REzCWn1BKUVuMFTxR-R3W_image_317.png"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://v3b.fal.media/files/b/0a8773d3/l2fk-fIO_PQFPzbvHkQX1_video.mp4"
      },
      "seed": 42
    }
    ```
  </Tab>

  <Tab title="Text To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedance/v1.5/pro/text-to-video`
    **Endpoint ID:** `fal-ai/bytedance/seedance/v1.5/pro/text-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedance/v1.5/pro/text-to-video/playground">
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
          "fal-ai/bytedance/seedance/v1.5/pro/text-to-video",
          arguments={
              "prompt": "Defense attorney declaring \"Ladies and gentlemen, reasonable doubt isn't just a phrase, it's the foundation of justice itself\", footsteps on marble, jury shifting, courtroom drama, closing argument power."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/seedance/v1.5/pro/text-to-video", {
        input: {
            prompt: "Defense attorney declaring \"Ladies and gentlemen, reasonable doubt isn't just a phrase, it's the foundation of justice itself\", footsteps on marble, jury shifting, courtroom drama, closing argument power."
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
        --url https://fal.run/fal-ai/bytedance/seedance/v1.5/pro/text-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Defense attorney declaring \"Ladies and gentlemen, reasonable doubt isn'\''t just a phrase, it'\''s the foundation of justice itself\", footsteps on marble, jury shifting, courtroom drama, closing argument power."
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt used to generate the video
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="16:9">
      The aspect ratio of the generated video Default value: `"16:9"`

      Possible values: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `auto`
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="720p">
      Video resolution - 480p for faster generation, 720p for balance, 1080p for higher quality Default value: `"720p"`

      Possible values: `480p`, `720p`, `1080p`
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="5">
      Duration of the video in seconds Default value: `"5"`

      Possible values: `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`
    </ParamField>

    <ParamField body="camera_fixed" type="boolean" default="false">
      Whether to fix the camera position
    </ParamField>

    <ParamField body="seed" type="integer">
      Random seed to control video generation. Use -1 for random.
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    <ParamField body="generate_audio" type="boolean" default="true">
      Whether to generate audio for the video Default value: `true`
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      Generated video file
    </ParamField>

    <ParamField body="seed" type="integer" required>
      Seed used for generation
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Defense attorney declaring \"Ladies and gentlemen, reasonable doubt isn't just a phrase, it's the foundation of justice itself\", footsteps on marble, jury shifting, courtroom drama, closing argument power.",
      "aspect_ratio": "16:9",
      "resolution": "720p",
      "duration": "5",
      "camera_fixed": false,
      "enable_safety_checker": true,
      "generate_audio": true
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://v3b.fal.media/files/b/0a87743e/0K5lW0v-iC_BbKo64o0cA_video.mp4"
      },
      "seed": 42
    }
    ```
  </Tab>
</Tabs>

Animate any image into a cinematic video with synchronized audio. Upload a start frame and optionally an end frame and Seedance 1.5 Pro generates the motion, camera movement, dialogue, and sound design in between.

***

## Use Cases

| Use Case                | Why Seedance 1.5 Pro fits                                                                               |
| :---------------------- | :------------------------------------------------------------------------------------------------------ |
| **Photo animation**     | Breathe life into a still portrait or product shot with realistic motion and ambient sound.             |
| **Character animation** | Turn concept art or a single character frame into a speaking, emoting performance with lip-sync.        |
| **Product reveals**     | Start on a hero shot, end on packaging — the model animates the transition with cinematic flair.        |
| **Scene transitions**   | Define start and end compositions for precise A-to-B shots — useful for ads, trailers, or music videos. |
| **Storyboard-to-video** | Convert illustrated storyboard frames into rough-cut motion tests with matching audio.                  |
| **Social content**      | Animate memes, portraits, or fan art into shareable clips with sound.                                   |
| **Virtual avatars**     | Animate a single headshot into a talking-head video with natural speech and lip-sync.                   |

***

## Key Features

| Feature                      | Description                                                                                                         |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| **Start frame conditioning** | Upload an image to set the opening composition, lighting, subject, and style.                                       |
| **End frame conditioning**   | Optionally upload a second image to define where the shot lands — the model generates the motion path between them. |
| **Native audio generation**  | Dialogue, sound effects, and ambient audio rendered alongside the video. Lip movements stay locked to speech.       |
| **Cinematic camera work**    | Pan, tilt, zoom, dolly, orbit, tracking shots — describe the move in your prompt.                                   |
| **Character consistency**    | The subject from your start frame stays stable throughout — face, clothing, and expression.                         |
| **High resolution**          | Output up to 1080p with smooth temporal consistency.                                                                |

***

## Controls

| Parameter        | Options                                          | Notes                                                |
| :--------------- | :----------------------------------------------- | :--------------------------------------------------- |
| `prompt`         | Text (required)                                  | Describe action, dialogue, camera, and sound         |
| `image_url`      | URL (required)                                   | Start frame — sets the opening composition           |
| `end_image_url`  | URL (optional)                                   | End frame — defines the closing composition          |
| `aspect_ratio`   | `21:9` · `16:9` · `4:3` · `1:1` · `3:4` · `9:16` | Default: `16:9`                                      |
| `resolution`     | `480p` · `720p`                                  | `480p` for faster iteration; `720p` for final output |
| `duration`       | `4`–`12` seconds                                 | Default: `5`                                         |
| `generate_audio` | `true` / `false`                                 | Default: `true` — set `false` for silent video       |
| `camera_fixed`   | `true` / `false`                                 | Lock the camera in place (tripod shot)               |
| `seed`           | Integer                                          | Set a value for reproducibility; use `-1` for random |

***

## Start Frame / End Frame

This is the core differentiator from text-to-video. You control the opening and closing compositions directly.

| Frame                           | What it does                                                                                                            |
| :------------------------------ | :---------------------------------------------------------------------------------------------------------------------- |
| **Start frame** (`image_url`)   | Required. Sets the initial subject, pose, lighting, color grade, and environment. The model animates forward from here. |
| **End frame** (`end_image_url`) | Optional. Defines the final composition. The model generates a motion path that lands precisely on this frame.          |

**Tips:**

* Use the same subject in both frames for smooth transitions.
* Match aspect ratio and style between start and end frames.
* Motion is generated in latent space — not interpolated — so physics and camera movement feel natural.

***

## Prompting Tips

Your prompt guides what happens *between* the frames:

| Element         | Example                                             |
| :-------------- | :-------------------------------------------------- |
| **Action**      | "She turns to face the camera and smiles"           |
| **Dialogue**    | `"I've been waiting for this moment."` (use quotes) |
| **Camera**      | "Slow push-in ending on a close-up"                 |
| **Audio/Foley** | "Soft piano, room reverb, fabric rustling"          |

**More tips:**

* The start frame already defines the scene — focus your prompt on *motion* and *sound*.
* For talking heads, put the dialogue in quotes and describe the emotion: `"I can't believe it," voice breaking with emotion`.
* Use `camera_fixed: true` if you want the subject to move but the frame to stay locked.

***

## Specs

| Spec           | Value                                      |
| :------------- | :----------------------------------------- |
| Max duration   | 12 seconds                                 |
| Max resolution | 1080p                                      |
| Audio          | Mixed dialogue + foley + score, 48 kHz AAC |
| Output format  | MP4 (H.264)                                |

***

## API

[fal.ai → Seedance 1.5 Pro image-to-video](https://fal.ai/models/fal-ai/bytedance/seedance/v1.5/pro/image-to-video/api)

## Related

* [Bytedance](/model-api-reference/video-generation-api/bytedance) — Video Generation

## Limitations

* `aspect_ratio` restricted to: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `auto`
* `resolution` restricted to: `480p`, `720p`, `1080p`
* Content moderation via safety checker
