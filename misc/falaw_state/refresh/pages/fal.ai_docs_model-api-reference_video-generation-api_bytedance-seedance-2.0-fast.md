> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Seedance 2.0 Fast API

> API reference for Bytedance Seedance 2.0 Fast. ByteDance's most advanced text-to-video model, fast tier. Lower latency and cost with cinematic output, native audio, multi-shot editing, and director-le

<Tabs>
  <Tab title="Text To Video">
    **Endpoint:** `POST https://fal.run/bytedance/seedance-2.0/fast/text-to-video`
    **Endpoint ID:** `bytedance/seedance-2.0/fast/text-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bytedance/seedance-2.0/fast/text-to-video/playground">
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
          "bytedance/seedance-2.0/fast/text-to-video",
          arguments={
              "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bytedance/seedance-2.0/fast/text-to-video", {
        input: {
            prompt: "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."
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
        --url https://fal.run/bytedance/seedance-2.0/fast/text-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."
      }'
      ```
    </CodeGroup>

    ## Examples

    > A hyper-realistic medium shot of two women in their late 20s to early 30s sitting cross-legged on opposite ends of a deep charcoal sectional sofa in a cozy, lived-in apartment during a lazy Sunday afternoon, captured with a handheld camera feel as if a third friend is casually filming them; the firs...

    <video src="https://v3b.fal.media/files/b/0a959a2a/EaIW2xdGlq41Ab1codNXE_video.mp4" controls width="100%" />

    > Ultra high-end commercial product shot, photorealistic, 8K, cinematic lighting, macro detail, shallow depth of field, premium advertising aesthetic, dark chocolate bar snapping in half in slow motion, side macro, cocoa powder dust drifting, warm key light, deep brown backdrop, studio-grade color gra...

    <video src="https://v3b.fal.media/files/b/0a959996/WHdnS_NXRnLTPEOmjZ6ro_video.mp4" controls width="100%" />

    > A breathtaking cinematic aerial sequence following an original majestic parrot flying freely above an immense tropical jungle at golden hour. The camera stays locked in a fast, fluid, graceful follow shot behind and around the bird, gliding effortlessly through the air with a sense of wonder, speed,...

    <video src="https://v3b.fal.media/files/b/0a9499d5/xRH9GuSLwaWggKgkeSb_Q_video.mp4" controls width="100%" />

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt used to generate the video
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="720p">
      Video resolution - 480p for faster generation, 720p for balance. Default value: `"720p"`

      Possible values: `480p`, `720p`
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="auto">
      Duration of the video in seconds. Supports 4 to 15 seconds, or auto to let the model decide based on the prompt. Default value: `"auto"`

      Possible values: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
      The aspect ratio of the generated video. Use 16:9 for landscape, 9:16 for portrait/vertical, 1:1 for square, 21:9 for ultrawide cinematic, or auto to let the model decide. Default value: `"auto"`

      Possible values: `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
    </ParamField>

    <ParamField body="generate_audio" type="boolean" default="true">
      Whether to generate synchronized audio for the video, including sound effects, ambient sounds, and lip-synced speech. The cost of video generation is the same regardless of whether audio is generated or not. Default value: `true`
    </ParamField>

    <ParamField body="seed" type="integer">
      Random seed for reproducibility. Note that results may still vary slightly even with the same seed.
    </ParamField>

    <ParamField body="end_user_id" type="string">
      The unique user ID of the end user.
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video file.
    </ParamField>

    <ParamField body="seed" type="integer" required>
      The seed used for generation.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea.",
      "resolution": "720p",
      "duration": "auto",
      "aspect_ratio": "auto",
      "generate_audio": true
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://storage.googleapis.com/falserverless/example_outputs/bytedance/seedance_2/output.mp4"
      },
      "seed": 42
    }
    ```
  </Tab>

  <Tab title="Image To Video">
    **Endpoint:** `POST https://fal.run/bytedance/seedance-2.0/fast/image-to-video`
    **Endpoint ID:** `bytedance/seedance-2.0/fast/image-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bytedance/seedance-2.0/fast/image-to-video/playground">
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
          "bytedance/seedance-2.0/fast/image-to-video",
          arguments={
              "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea.",
              "image_url": "https://v3b.fal.media/files/b/0a8eba37/Cqg-4Uwzyz4DELfceT1CF_a17e588773ec45b1a9e6f100a787b80b.jpg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bytedance/seedance-2.0/fast/image-to-video", {
        input: {
            prompt: "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea.",
            image_url: "https://v3b.fal.media/files/b/0a8eba37/Cqg-4Uwzyz4DELfceT1CF_a17e588773ec45b1a9e6f100a787b80b.jpg"
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
        --url https://fal.run/bytedance/seedance-2.0/fast/image-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea.",
        "image_url": "https://v3b.fal.media/files/b/0a8eba37/Cqg-4Uwzyz4DELfceT1CF_a17e588773ec45b1a9e6f100a787b80b.jpg"
      }'
      ```
    </CodeGroup>

    ## Examples

    > Ultra high-end commercial product shot, photorealistic, 8K, cinematic lighting, macro detail, shallow depth of field, premium advertising aesthetic, crystal-cut perfume bottle catching prismatic light beams, slow orbit, hard sunlight through venetian blinds, warm sandstone wall background, studio-gr...

    <video src="https://v3b.fal.media/files/b/0a959949/4YjMSjuKAeIIOLFiGktEi_video.mp4" controls width="100%" />

    > A shimmering underwater stage is set as eight octopi glide into view, ready to perform graceful formations. Tentacles intertwine in perfect harmony, showcasing the elegance of synchronized movement. Delight and wonder fill the space as these intelligent sea creatures dance, revealing a captivating w\...

    <video src="https://v3b.fal.media/files/b/0a948ad6/F3LUFaihRZ3nClRH-DjM__video.mp4" controls width="100%" />

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt describing the desired motion and action for the video.
    </ParamField>

    <ParamField body="image_url" type="string" required>
      The URL of the starting frame image to animate. Supported formats: JPEG, PNG, WebP. Max 30 MB.
    </ParamField>

    <ParamField body="end_image_url" type="string">
      The URL of the image to use as the last frame of the video. When provided, the generated video will transition from the starting image to this ending image. Supported formats: JPEG, PNG, WebP. Max 30 MB.
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="720p">
      Video resolution - 480p for faster generation, 720p for balance. Default value: `"720p"`

      Possible values: `480p`, `720p`
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="auto">
      Duration of the video in seconds. Supports 4 to 15 seconds, or auto to let the model decide based on the prompt. Default value: `"auto"`

      Possible values: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
      The aspect ratio of the generated video. Use 16:9 for landscape, 9:16 for portrait/vertical, 1:1 for square, 21:9 for ultrawide cinematic, or auto to infer from the input image. Default value: `"auto"`

      Possible values: `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
    </ParamField>

    <ParamField body="generate_audio" type="boolean" default="true">
      Whether to generate synchronized audio for the video, including sound effects, ambient sounds, and lip-synced speech. The cost of video generation is the same regardless of whether audio is generated or not. Default value: `true`
    </ParamField>

    <ParamField body="seed" type="integer">
      Random seed for reproducibility. Note that results may still vary slightly even with the same seed.
    </ParamField>

    <ParamField body="end_user_id" type="string">
      The unique user ID of the end user.
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video file.
    </ParamField>

    <ParamField body="seed" type="integer" required>
      The seed used for generation.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea.",
      "image_url": "https://v3b.fal.media/files/b/0a8eba37/Cqg-4Uwzyz4DELfceT1CF_a17e588773ec45b1a9e6f100a787b80b.jpg",
      "resolution": "720p",
      "duration": "auto",
      "aspect_ratio": "auto",
      "generate_audio": true
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://storage.googleapis.com/falserverless/example_outputs/bytedance/seedance_2/output.mp4"
      },
      "seed": 42
    }
    ```
  </Tab>

  <Tab title="Reference To Video">
    **Endpoint:** `POST https://fal.run/bytedance/seedance-2.0/fast/reference-to-video`
    **Endpoint ID:** `bytedance/seedance-2.0/fast/reference-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bytedance/seedance-2.0/fast/reference-to-video/playground">
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
          "bytedance/seedance-2.0/fast/reference-to-video",
          arguments={
              "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("bytedance/seedance-2.0/fast/reference-to-video", {
        input: {
            prompt: "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."
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
        --url https://fal.run/bytedance/seedance-2.0/fast/reference-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."
      }'
      ```
    </CodeGroup>

    ## Examples

    > A hyper-realistic UGC-style medium close-up of a woman in her late 20s standing in her sunlit bedroom in front of a slightly messy bed with white linen sheets, filmed vertically as if she's holding her phone at arm's length for a TikTok or Instagram Reel; she has shoulder-length honey blonde waves, ...

    <video src="https://v3b.fal.media/files/b/0a959ac1/vVRE687-Tmi0f1mqmbpSz_video.mp4" controls width="100%" />

    > Beautiful fusion of these two scenes. Mills stand against a rugged coastline, their large wooden wheels turned by the relentless surge of tidal waves combined with a field of wildflowers bathed in soft sunlight transitions into where monarch butterflies take flight.

    <video src="https://v3b.fal.media/files/b/0a948b29/dWoaqkPO7UA6hlEQXjgyI_video.mp4" controls width="100%" />

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt used to generate the video.
    </ParamField>

    <ParamField body="image_urls" type="list<string>">
      Reference images to guide video generation. Refer to them in the prompt as @Image1, @Image2, etc. Supported formats: JPEG, PNG, WebP. Max 30 MB per image. Up to 9 images. Total files across all modalities must not exceed 12.
    </ParamField>

    <ParamField body="video_urls" type="list<string>">
      Reference videos to guide video generation. Refer to them in the prompt as @Video1, @Video2, etc. Supported formats: MP4, MOV. Up to 3 videos, combined duration must be between 2 and 15 seconds, total size under 50 MB. Each video must be between \~480p (640x640) and \~720p (834x1112) in resolution.
    </ParamField>

    <ParamField body="audio_urls" type="list<string>">
      Reference audio to guide video generation. Refer to them in the prompt as @Audio1, @Audio2, etc. Supported formats: MP3, WAV. Up to 3 files, combined duration must not exceed 15 seconds. Max 15 MB per file.If audio is provided, at least one reference image or video is required.
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="720p">
      Video resolution - 480p for faster generation, 720p for balance. Default value: `"720p"`

      Possible values: `480p`, `720p`
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="auto">
      Duration of the video in seconds. Supports 4 to 15 seconds, or auto to let the model decide based on the prompt. Default value: `"auto"`

      Possible values: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
      The aspect ratio of the generated video. Use 16:9 for landscape, 9:16 for portrait/vertical, 1:1 for square, 21:9 for ultrawide cinematic, or auto to let the model decide. Default value: `"auto"`

      Possible values: `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
    </ParamField>

    <ParamField body="generate_audio" type="boolean" default="true">
      Whether to generate synchronized audio for the video, including sound effects, ambient sounds, and lip-synced speech. The cost of video generation is the same regardless of whether audio is generated or not. Default value: `true`
    </ParamField>

    <ParamField body="seed" type="integer">
      Random seed for reproducibility. Note that results may still vary slightly even with the same seed.
    </ParamField>

    <ParamField body="end_user_id" type="string">
      The unique user ID of the end user.
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video file.
    </ParamField>

    <ParamField body="seed" type="integer" required>
      The seed used for generation.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea.",
      "image_urls": [
        "https://v3b.fal.media/files/b/0a8eba37/Cqg-4Uwzyz4DELfceT1CF_a17e588773ec45b1a9e6f100a787b80b.jpg"
      ],
      "resolution": "720p",
      "duration": "auto",
      "aspect_ratio": "auto",
      "generate_audio": true
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://storage.googleapis.com/falserverless/example_outputs/bytedance/seedance_2/output.mp4"
      },
      "seed": 42
    }
    ```
  </Tab>
</Tabs>

## Related

* [Seedance 2.0 Text to Video API](/model-api-reference/video-generation-api/seedance-2.0-text-to-video-api) — Video Generation
* [Seedance 2 Image to Video](/model-api-reference/video-generation-api/seedance-2-image-to-video) — Video Generation
* [Seedance 2 Reference to Video](/model-api-reference/video-generation-api/seedance-2-reference-to-video) — Video Generation
* [Seedance 2.0 Fast Image to Video](/model-api-reference/video-generation-api/seedance-2.0-fast-image-to-video) — Video Generation
* [Seedance 2.0 Fast Reference to Video](/model-api-reference/video-generation-api/seedance-2.0-fast-reference-to-video) — Video Generation
* [Seedance 2.0 Fast Text to Video](/model-api-reference/video-generation-api/seedance-2.0-fast-text-to-video) — Video Generation

## Limitations

* `resolution` restricted to: `480p`, `720p`
* `aspect_ratio` restricted to: `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
