> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video O1 Video To Video API

> API reference for Kling Video O1 Video To Video. Edit an existing video using natural-language instructions, transforming subjects, settings, and style while retaining the original motion structure.

<Tabs>
  <Tab title="Edit">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/o1/video-to-video/edit`
    **Endpoint ID:** `fal-ai/kling-video/o1/video-to-video/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/o1/video-to-video/edit/playground">
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
          "fal-ai/kling-video/o1/video-to-video/edit",
          arguments={
              "prompt": "Replace the character in the video with @Element1, maintaining the same movements and camera angles. Transform the landscape into @Image1",
              "video_url": "https://v3b.fal.media/files/b/rabbit/ku8_Wdpf-oTbGRq4lB5DU_output.mp4"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/o1/video-to-video/edit", {
        input: {
            prompt: "Replace the character in the video with @Element1, maintaining the same movements and camera angles. Transform the landscape into @Image1",
            video_url: "https://v3b.fal.media/files/b/rabbit/ku8_Wdpf-oTbGRq4lB5DU_output.mp4"
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
        --url https://fal.run/fal-ai/kling-video/o1/video-to-video/edit \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Replace the character in the video with @Element1, maintaining the same movements and camera angles. Transform the landscape into @Image1",
        "video_url": "https://v3b.fal.media/files/b/rabbit/ku8_Wdpf-oTbGRq4lB5DU_output.mp4"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      Use @Element1, @Element2 to reference elements and @Image1, @Image2 to reference images in order.
    </ParamField>

    <ParamField body="video_url" type="string" required>
      Reference video URL. Only .mp4/.mov formats supported, 3-10 seconds duration, 720-2160px resolution, max 200MB.

      Max file size: 200.0MB, Min width: 720px, Min height: 720px, Max width: 2160px, Max height: 2160px, Min duration: 3.0s, Max duration: 10.05s, Min FPS: 24.0, Max FPS: 60.0, Timeout: 30.0s
    </ParamField>

    <ParamField body="keep_audio" type="boolean" default="false">
      Whether to keep the original audio from the video.
    </ParamField>

    <ParamField body="image_urls" type="list<string>">
      Reference images for style/appearance. Reference in prompt as @Image1, @Image2, etc. Maximum 4 total (elements + reference images) when using video.
    </ParamField>

    <ParamField body="elements" type="list<OmniVideoElementInput>">
      Elements (characters/objects) to include. Reference in prompt as @Element1, @Element2, etc. Maximum 4 total (elements + reference images) when using video.
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Replace the character in the video with @Element1, maintaining the same movements and camera angles. Transform the landscape into @Image1",
      "video_url": "https://v3b.fal.media/files/b/rabbit/ku8_Wdpf-oTbGRq4lB5DU_output.mp4",
      "keep_audio": false,
      "image_urls": [
        "https://v3b.fal.media/files/b/lion/MKvhFko5_wYnfORYacNII_AgPt8v25Wt4oyKhjnhVK5.png"
      ],
      "elements": [
        {
          "frontal_image_url": "https://v3b.fal.media/files/b/panda/MQp-ghIqshvMZROKh9lW3.png",
          "reference_image_urls": [
            "https://v3b.fal.media/files/b/kangaroo/YMpmQkYt9xugpOTQyZW0O.png",
            "https://v3b.fal.media/files/b/zebra/d6ywajNyJ6bnpa_xBue-K.png"
          ]
        }
      ]
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "content_type": "video/mp4",
        "file_name": "output.mp4",
        "file_size": 7533071,
        "url": "https://v3b.fal.media/files/b/0a86603b/YAlbB2535l07BTy1wpDeI_output.mp4"
      }
    }
    ```
  </Tab>

  <Tab title="Reference">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/o1/video-to-video/reference`
    **Endpoint ID:** `fal-ai/kling-video/o1/video-to-video/reference`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/o1/video-to-video/reference/playground">
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
          "fal-ai/kling-video/o1/video-to-video/reference",
          arguments={
              "prompt": "Based on @Video1, generate the next shot. keep the style of the video",
              "video_url": "https://v3b.fal.media/files/b/panda/oVdiICFXY03Vbam-08Aj8_output.mp4"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/o1/video-to-video/reference", {
        input: {
            prompt: "Based on @Video1, generate the next shot. keep the style of the video",
            video_url: "https://v3b.fal.media/files/b/panda/oVdiICFXY03Vbam-08Aj8_output.mp4"
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
        --url https://fal.run/fal-ai/kling-video/o1/video-to-video/reference \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Based on @Video1, generate the next shot. keep the style of the video",
        "video_url": "https://v3b.fal.media/files/b/panda/oVdiICFXY03Vbam-08Aj8_output.mp4"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      Use @Element1, @Element2 to reference elements and @Image1, @Image2 to reference images in order.
    </ParamField>

    <ParamField body="video_url" type="string" required>
      Reference video URL. Only .mp4/.mov formats supported, 3-10 seconds duration, 720-2160px resolution, max 200MB.

      Max file size: 200.0MB, Min width: 720px, Min height: 720px, Max width: 2160px, Max height: 2160px, Min duration: 3.0s, Max duration: 10.05s, Min FPS: 24.0, Max FPS: 60.0, Timeout: 30.0s
    </ParamField>

    <ParamField body="keep_audio" type="boolean" default="false">
      Whether to keep the original audio from the video.
    </ParamField>

    <ParamField body="image_urls" type="list<string>">
      Reference images for style/appearance. Reference in prompt as @Image1, @Image2, etc. Maximum 4 total (elements + reference images) when using video.
    </ParamField>

    <ParamField body="elements" type="list<OmniVideoElementInput>">
      Elements (characters/objects) to include. Reference in prompt as @Element1, @Element2, etc. Maximum 4 total (elements + reference images) when using video.
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
      The aspect ratio of the generated video frame. If 'auto', the aspect ratio will be determined automatically based on the input video, and the closest aspect ratio to the input video will be used. Default value: `"auto"`

      Possible values: `auto`, `16:9`, `9:16`, `1:1`
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="5">
      Video duration in seconds. Default value: `"5"`

      Possible values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Based on @Video1, generate the next shot. keep the style of the video",
      "video_url": "https://v3b.fal.media/files/b/panda/oVdiICFXY03Vbam-08Aj8_output.mp4",
      "keep_audio": false,
      "image_urls": [],
      "elements": [
        {
          "frontal_image_url": "https://v3b.fal.media/files/b/panda/MQp-ghIqshvMZROKh9lW3.png",
          "reference_image_urls": [
            "https://v3b.fal.media/files/b/kangaroo/YMpmQkYt9xugpOTQyZW0O.png",
            "https://v3b.fal.media/files/b/zebra/d6ywajNyJ6bnpa_xBue-K.png"
          ]
        }
      ],
      "aspect_ratio": "auto",
      "duration": "5"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "content_type": "video/mp4",
        "file_name": "output.mp4",
        "file_size": 28472159,
        "url": "https://v3b.fal.media/files/b/kangaroo/3n_Lpxm_SjK5NYyBobRdS_output.mp4"
      }
    }
    ```
  </Tab>
</Tabs>

Kuaishou's Kling O1 Edit delivers natural language video transformation at \$0.168 per second, trading traditional masking workflows for prompt-based editing that preserves original motion structure. The model accepts up to 4 combined reference elements and images, enabling complex character swaps and environment transformations through simple text commands.

**Built for:** Character replacement in existing footage | Scene environment transformations | Style transfer while maintaining motion

***

## Context-Aware Video Transformation Without Masking

Kling O1 Edit operates on a fundamentally different approach than frame-by-frame editing tools: it understands the entire motion structure of your input video and applies transformations that respect camera angles, movement patterns, and spatial relationships. Where traditional video editing requires manual masking and frame-level adjustments, this model interprets natural language instructions and applies them across the full video duration.

**What this means for you:**

* **Multi-reference editing:** Combine up to 4 total elements and reference images in a single transformation, enabling complex character swaps with specific style references
* **Motion preservation:** Original camera movements and subject motion remain intact while subjects, settings, and visual style transform according to your prompt
* **Natural language control:** Direct the edit through conversational instructions rather than technical parameters. Example: "Replace the character with @Element1, maintaining the same movements and camera angles. Transform the landscape into @Image1"
* **Audio preservation:** Choose to keep original audio from your source video or generate silent output through the keep\_audio parameter
* **Element structure:** Each element accepts one frontal image plus multiple reference angles (frontal\_image\_url + reference\_image\_urls array), giving the model comprehensive visual context for accurate transformations

***

## Performance That Scales

Kling O1 Edit's per-second pricing model reflects the computational complexity of motion-preserving video transformation, with costs scaling directly to your input video duration.

| Metric                 | Result        | Context                                                |
| :--------------------- | :------------ | :----------------------------------------------------- |
| **Cost per Video**     | $0.50-$1.68   | Based on 3-10 second input duration at \$0.168/second  |
| **Input Duration**     | 3-10 seconds  | Supports .mp4, .mov, .webm, .m4v, .gif up to 200MB     |
| **Resolution Range**   | 720-2160px    | Accepts standard HD through 4K input resolutions       |
| **Reference Capacity** | Up to 4 total | Combined limit for elements and style reference images |

***

## Technical Specifications

| Spec               | Details                                                                                         |
| :----------------- | :---------------------------------------------------------------------------------------------- |
| **Architecture**   | Kling O1 Edit                                                                                   |
| **Input Formats**  | Video (.mp4, .mov, .webm, .m4v, .gif), reference images (.jpg, .jpeg, .png, .webp, .gif, .avif) |
| **Output Formats** | .mp4 video                                                                                      |
| **Video Duration** | 3-10 seconds (output matches input duration)                                                    |
| **Audio Handling** | Optional audio preservation via keep\_audio parameter (default: false)                          |
| **Prompt Syntax**  | @Element1, @Element2 for tracked elements; @Image1, @Image2 for style references                |
| **License**        | Commercial use via fal partnership                                                              |

[API Documentation](https://fal.ai/models/fal-ai/kling-video/o1/video-to-video/edit/api)

***

## How It Stacks Up

**Sora 2 Video to Video** - Kling O1 Edit prioritizes multi-reference element control with up to 4 combined inputs for complex character and environment transformations. [Sora 2's remix capabilities](https://fal.ai/models/fal-ai/sora-2/video-to-video/remix) emphasize broader creative reinterpretation and style transfer across longer video durations, ideal for narrative content that requires substantial visual reimagining.

**Wan Video to Video** - Kling O1 Edit's natural language interface eliminates technical parameter tuning, making it accessible for creators who want direct prompt-based control. [Wan's video-to-video endpoint](https://fal.ai/models/fal-ai/wan/v2.2-a14b/video-to-video) offers granular parameter control for users who need precise technical adjustments in their transformation workflows.

**AnimateDiff Video to Video** - Kling O1 Edit maintains original motion structure while transforming visual content, preserving the exact camera movements and subject actions from your source footage. [AnimateDiff](https://fal.ai/models/fal-ai/fast-animatediff/video-to-video) focuses on animation-style transformations and motion synthesis, serving creators building stylized or animated content from video references.

## Related

* [Kling O1 First Frame Last Frame to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-first-frame-last-frame-to-video) — Video Generation
* [Kling O1 Reference Image to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-reference-image-to-video) — Video Generation
* [Kling O1 Edit Video \[Standard\]](/model-api-reference/video-generation-api/kling-o1-edit-video) — Video Generation
* [Kling O1 Reference Video to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-reference-video-to-video) — Video Generation

## Limitations

* `aspect_ratio` restricted to: `auto`, `16:9`, `9:16`, `1:1`
* `duration` restricted to: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`
