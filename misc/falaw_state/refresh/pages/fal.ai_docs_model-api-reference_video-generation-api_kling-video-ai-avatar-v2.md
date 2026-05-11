> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video Ai Avatar V2 API

> API reference for Kling Video Ai Avatar V2. Kling AI Avatar v2 Pro: The premium endpoint for creating avatar videos with realistic humans, animals, cartoons, or stylized characters

<Tabs>
  <Tab title="Pro">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/ai-avatar/v2/pro`
    **Endpoint ID:** `fal-ai/kling-video/ai-avatar/v2/pro`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/ai-avatar/v2/pro/playground">
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
          "fal-ai/kling-video/ai-avatar/v2/pro",
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

      const result = await fal.subscribe("fal-ai/kling-video/ai-avatar/v2/pro", {
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
        --url https://fal.run/fal-ai/kling-video/ai-avatar/v2/pro \
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

  <Tab title="Standard">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/ai-avatar/v2/standard`
    **Endpoint ID:** `fal-ai/kling-video/ai-avatar/v2/standard`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/ai-avatar/v2/standard/playground">
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
          "fal-ai/kling-video/ai-avatar/v2/standard",
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

      const result = await fal.subscribe("fal-ai/kling-video/ai-avatar/v2/standard", {
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
        --url https://fal.run/fal-ai/kling-video/ai-avatar/v2/standard \
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
</Tabs>

Kuaishou's Kling AI Avatar v2 Pro transforms static images into synchronized talking avatar videos at \$0.115 per second of output. Trading simplicity for production-grade lip sync and motion quality, this premium endpoint handles realistic humans, animals, cartoons, and stylized characters without manual rigging. Built for content creators who need broadcast-quality avatar videos without the technical overhead of traditional animation pipelines.

**Built for:** Marketing video production | Social media content | Character animation | Educational content | Podcast visualization

***

## Audio-Driven Animation Without the Complexity

Kling AI Avatar v2 Pro uses audio-synchronized motion generation to animate any portrait or character image. Unlike traditional animation workflows that require rigging, keyframing, and manual lip sync adjustment, this model maps audio waveforms directly to facial movements and expressions.

**What this means for you:**

* **Simple dual-input API:** Upload one portrait photo (JPG, PNG, WebP, GIF, AVIF) plus one audio file (MP3, OGG, WAV, M4A, AAC) to generate synchronized avatar videos
* **Natural lip synchronization:** Audio-driven facial animation matches speech patterns without manual keyframe adjustment
* **Multi-character support:** Works across realistic humans, animals, cartoon styles, and stylized characters from the same endpoint
* **Production-ready output:** Generate avatar videos suitable for commercial use at broadcast quality standards
* **Optional prompt refinement:** Include text prompts to guide subtle aspects of the animation beyond audio synchronization

***

## Performance That Scales

Pricing scales linearly with output duration, making cost predictable for batch production workflows.

| Metric                 | Result               | Context                                                                                                        |
| :--------------------- | :------------------- | :------------------------------------------------------------------------------------------------------------- |
| **Cost per Second**    | \$0.115              | Approximately 8.7 seconds of video per \$1.00 on fal                                                           |
| **Cost per Minute**    | \$6.90               | Predictable scaling for longer content                                                                         |
| **Standard Tier Cost** | \$0.0562/second      | [Kling AI Avatar v2 Standard](https://fal.ai/models/fal-ai/kling-video/ai-avatar/v2/standard) at \~49% savings |
| **Output Duration**    | Matches audio length | Video automatically scaled to audio file duration                                                              |

***

## Technical Specifications

| Spec                | Details                                   |
| :------------------ | :---------------------------------------- |
| **Architecture**    | Kling AI Avatar v2 Pro                    |
| **Image Formats**   | JPG, JPEG, PNG, WebP, GIF, AVIF           |
| **Audio Formats**   | MP3, OGG, WAV, M4A, AAC                   |
| **Output Format**   | MP4 video with synchronized audio         |
| **Generation Type** | Image-to-video with audio synchronization |
| **License**         | Commercial use permitted (Partner)        |

[API Documentation](https://fal.ai/models/fal-ai/kling-video/ai-avatar/v2/pro/api) | [Quickstart Guide](https://docs.fal.ai/model-apis/quickstart)

***

## How It Stacks Up

**[Kling AI Avatar v2 Standard](https://fal.ai/models/fal-ai/kling-video/ai-avatar/v2/standard)** – Kling AI Avatar v2 Pro delivers enhanced facial detail and smoother lip-sync precision at $0.115/second versus Standard's $0.0562/second. Choose Pro for professional productions where output quality justifies the 2x cost premium, Standard for high-volume workflows where cost efficiency matters more.

**[Kling 2.5 Turbo Pro Image-to-Video](https://fal.ai/models/fal-ai/kling-video/v2.5-turbo/pro/image-to-video)** – Kling AI Avatar v2 Pro specializes in audio-synchronized avatar animation with automatic lip sync and facial motion for talking head content. Kling 2.5 Turbo Pro handles general image-to-video animation at $0.35 for 5 seconds ($0.07/additional second) without audio synchronization, for broader motion graphics and scene animation workflows.

**[Kling 2.1 Master Image-to-Video](https://fal.ai/models/fal-ai/kling-video/v2.1/master/image-to-video)** – Kling AI Avatar v2 Pro constrains generation around audio input for consistent character performance at $0.115/second. Kling 2.1 Master emphasizes maximum quality and cinematic motion at $1.40 for 5 seconds (\$0.28/additional second) for high-fidelity general video generation without audio synchronization.

**[Argil Avatars Audio-to-Video](https://fal.ai/models/argil/avatars/audio-to-video)** – Kling AI Avatar v2 Pro supports custom image input for any character style at $0.115/second with premium lip-sync quality. Argil Avatars uses pre-trained avatar templates at $0.02/second for 5.75x cost savings when custom character appearance isn't required.

## Related

* [Kling AI Avatar v2 Standard](/model-api-reference/video-generation-api/kling-ai-avatar-v2-standard) — Video Generation
* [Kling AI Avatar](/model-api-reference/video-generation-api/kling-ai-avatar) — Video Generation
* [Kling TTS](/model-api-reference/audio-api/kling-tts) — Audio
* [Kling AI Avatar Pro](/model-api-reference/video-generation-api/kling-ai-avatar-pro) — Video Generation
* [Kling AI Avatar v2 Pro](/model-api-reference/video-generation-api/kling-ai-avatar-v2-pro) — Video Generation
