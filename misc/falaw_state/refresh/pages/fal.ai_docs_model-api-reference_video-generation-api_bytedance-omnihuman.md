> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Omnihuman API

> API reference for Bytedance Omnihuman. OmniHuman generates video using an image of a human figure paired with an audio file. It produces vivid, high-quality videos where the character’s emotions and m

<Tabs>
  <Tab title="Omnihuman">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/omnihuman`
    **Endpoint ID:** `fal-ai/bytedance/omnihuman`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/omnihuman/playground">
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
          "fal-ai/bytedance/omnihuman",
          arguments={
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/omnihuman.png",
              "audio_url": "https://storage.googleapis.com/falserverless/example_inputs/omnihuman_audio.mp3"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/omnihuman", {
        input: {
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/omnihuman.png",
            audio_url: "https://storage.googleapis.com/falserverless/example_inputs/omnihuman_audio.mp3"
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
        --url https://fal.run/fal-ai/bytedance/omnihuman \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/omnihuman.png",
        "audio_url": "https://storage.googleapis.com/falserverless/example_inputs/omnihuman_audio.mp3"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The URL of the image used to generate the video
    </ParamField>

    <ParamField body="audio_url" type="string" required>
      The URL of the audio file to generate the video. Audio must be under 30s long.
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      Generated video file
    </ParamField>

    <ParamField body="duration" type="float" required>
      Duration of audio input/video output as used for billing.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/omnihuman.png",
      "audio_url": "https://storage.googleapis.com/falserverless/example_inputs/omnihuman_audio.mp3"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://storage.googleapis.com/falserverless/example_outputs/omnihuman_output.mp4"
      }
    }
    ```
  </Tab>

  <Tab title="V1.5">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/omnihuman/v1.5`
    **Endpoint ID:** `fal-ai/bytedance/omnihuman/v1.5`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/omnihuman/v1.5/playground">
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
          "fal-ai/bytedance/omnihuman/v1.5",
          arguments={
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/omnihuman_v15_input_image.png",
              "audio_url": "https://storage.googleapis.com/falserverless/example_inputs/omnihuman_v15_input_audio.mp3"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/omnihuman/v1.5", {
        input: {
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/omnihuman_v15_input_image.png",
            audio_url: "https://storage.googleapis.com/falserverless/example_inputs/omnihuman_v15_input_audio.mp3"
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
        --url https://fal.run/fal-ai/bytedance/omnihuman/v1.5 \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/omnihuman_v15_input_image.png",
        "audio_url": "https://storage.googleapis.com/falserverless/example_inputs/omnihuman_v15_input_audio.mp3"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string">
      The text prompt used to guide the video generation.
    </ParamField>

    <ParamField body="image_url" type="string" required>
      The URL of the image used to generate the video
    </ParamField>

    <ParamField body="audio_url" type="string" required>
      The URL of the audio file to generate the video. Audio must be under 30s long for 1080p generation and under 60s long for 720p generation.
    </ParamField>

    <ParamField body="turbo_mode" type="boolean" default="false">
      Generate a video at a faster rate with a slight quality trade-off.
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="1080p">
      The resolution of the generated video. Defaults to 1080p. 720p generation is faster and higher in quality. 1080p generation is limited to 30s audio and 720p generation is limited to 60s audio. Default value: `"1080p"`

      Possible values: `720p`, `1080p`
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      Generated video file
    </ParamField>

    <ParamField body="duration" type="float" required>
      Duration of audio input/video output as used for billing.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/omnihuman_v15_input_image.png",
      "audio_url": "https://storage.googleapis.com/falserverless/example_inputs/omnihuman_v15_input_audio.mp3",
      "turbo_mode": false,
      "resolution": "1080p"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://storage.googleapis.com/falserverless/example_outputs/omnihuman_v15_output.mp4"
      }
    }
    ```
  </Tab>
</Tabs>

ByteDance's OmniHuman model generates **audio-synchronized videos** from a single reference image at \$0.14 per second of output. With specialized lip-sync precision, the model trained on 18,700 hours of human motion data to maintain tight correlation between audio input and character movement. Built for content creators who need realistic talking head videos without motion capture equipment.

**Use Cases:** Social Media Content | Product Demos with Presenters | Educational Video Production

***

## Performance

At \$0.14 per second, OmniHuman sits in the mid-range for image-to-video generation on fal, trading cost for specialized **audio-sync capabilities** that generic models don't prioritize.

| Metric                 | Result                                                                                                                                                                                                                                                  | Context                                                        |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------- |
| **Audio Sync Quality** | Tight emotion/movement correlation                                                                                                                                                                                                                      | Trained on 18,700 hours of human motion data                   |
| **Max Audio Duration** | 30 seconds                                                                                                                                                                                                                                              | Hard limit enforced at API level                               |
| **Cost per Second**    | \$0.14                                                                                                                                                                                                                                                  | Billed on actual audio/video duration                          |
| **Output Quality**     | High-fidelity video                                                                                                                                                                                                                                     | Specialized for human figure animation                         |
| **Related Endpoints**  | [OmniHuman v1.5](https://fal.ai/models/fal-ai/bytedance/omnihuman/v1.5), [Seedance Pro](https://fal.ai/models/fal-ai/bytedance/seedance/v1/pro/image-to-video), [Seedance Lite](https://fal.ai/models/fal-ai/bytedance/seedance/v1/lite/image-to-video) | ByteDance family variants for different quality/cost tradeoffs |

***

## Audio-First Video Generation

OmniHuman flips the standard image-to-video workflow by making audio the **primary control signal** rather than text prompts or motion parameters. Where most models animate based on text descriptions or keyframes, this architecture analyzes audio waveforms to drive facial expressions, lip movements, and body language simultaneously.

**What this means for you:**

* **Natural speech synchronization:** Upload any audio file under 30 seconds and get matching lip movements without manual keyframe adjustment or phoneme mapping

* **Emotion-driven animation:** The model interprets audio tone and pacing to generate corresponding facial expressions and body gestures, not just mouth shapes

* **Single-image input:** Start with one reference photo rather than building character rigs or providing multiple angles

* **Production-ready output:** High-fidelity video maintains visual consistency across the full duration without drift or quality degradation

***

## Technical Specifications

| Spec                   | Details                                                                          |
| :--------------------- | :------------------------------------------------------------------------------- |
| **Architecture**       | OmniHuman                                                                        |
| **Input Formats**      | Single image (JPEG, PNG, WebP, GIF, AVIF) + audio file (MP3, OGG, WAV, M4A, AAC) |
| **Output Formats**     | MP4 video                                                                        |
| **Max Audio Duration** | 30 seconds                                                                       |
| **License**            | Commercial use allowed via fal partnership                                       |

[API Documentation](https://fal.ai/models/fal-ai/bytedance/omnihuman/api) | [Quickstart Guide](https://docs.fal.ai/model-apis/quickstart) | [Enterprise Pricing](https://fal.ai/pricing)

***

## How It Stacks Up

**Bytedance OmniHuman v1.5** ($0.14/sec) – [OmniHuman v1.5](https://fal.ai/models/fal-ai/bytedance/omnihuman/v1.5) offers enhanced audio processing and **improved motion quality** at the same $0.14 per second price point. The original OmniHuman remains viable for projects where the current quality threshold meets requirements without needing v1.5's refinements.

**Seedance 1.0 Pro** (\$0.14/sec) – OmniHuman prioritizes **audio-driven human animation** with specialized lip-sync capabilities. [Seedance Pro](https://fal.ai/models/fal-ai/bytedance/seedance/v1/pro/image-to-video) trades audio control for broader creative motion generation across any subject type, ideal for product animations or scene transitions where audio sync isn't critical.

**Seedance 1.0 Lite** ($0.08/sec) – [Seedance Lite](https://fal.ai/models/fal-ai/bytedance/seedance/v1/lite/image-to-video) delivers 43% cost savings ($0.08 vs \$0.14 per second) by simplifying motion generation **without audio processing**. Best for budget-conscious projects that can handle reduced quality or don't require speech synchronization.

## Limitations

* `resolution` restricted to: `720p`, `1080p`
