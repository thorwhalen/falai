> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video O1 Reference To Video API

> API reference for Kling Video O1 Reference To Video. Transform images, elements, and text into consistent, high-quality video scenes, ensuring stable character identity, object details, and environmen

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/o1/reference-to-video`
**Endpoint ID:** `fal-ai/kling-video/o1/reference-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/o1/reference-to-video/playground">
  Run this model interactively with your own prompts.
</Card>

## Quick Start

<CodeGroup>
  ```python title="Python" theme={null}
  import fal_client

  def on_queue_update(update):
      if isinstance(update, fal_client.InProgress):
          for log in update.logs:
             print(log["message"])

  result = fal_client.subscribe(
      "fal-ai/kling-video/o1/reference-to-video",
      arguments={
          "prompt": "Take @Image1 as the start frame. Start with a high-angle satellite view of the ancient greenhouse ruin surrounded by nature. The camera swoops down and flies inside the building, revealing the character from @Element1 standing in the sun-drenched center. The camera then seamlessly transitions into a smooth 180-degree orbit around the character, moving to the back view. As the open backpack comes into focus, the camera continues to push forward, zooming deep inside the bag to reveal the glowing stone from @Element2 nestled inside. Cinematic lighting, hopeful atmosphere, 35mm lens. Make sure to keep it as the style of @Image2."
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/kling-video/o1/reference-to-video", {
    input: {
        prompt: "Take @Image1 as the start frame. Start with a high-angle satellite view of the ancient greenhouse ruin surrounded by nature. The camera swoops down and flies inside the building, revealing the character from @Element1 standing in the sun-drenched center. The camera then seamlessly transitions into a smooth 180-degree orbit around the character, moving to the back view. As the open backpack comes into focus, the camera continues to push forward, zooming deep inside the bag to reveal the glowing stone from @Element2 nestled inside. Cinematic lighting, hopeful atmosphere, 35mm lens. Make sure to keep it as the style of @Image2."
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
    --url https://fal.run/fal-ai/kling-video/o1/reference-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "Take @Image1 as the start frame. Start with a high-angle satellite view of the ancient greenhouse ruin surrounded by nature. The camera swoops down and flies inside the building, revealing the character from @Element1 standing in the sun-drenched center. The camera then seamlessly transitions into a smooth 180-degree orbit around the character, moving to the back view. As the open backpack comes into focus, the camera continues to push forward, zooming deep inside the bag to reveal the glowing stone from @Element2 nestled inside. Cinematic lighting, hopeful atmosphere, 35mm lens. Make sure to keep it as the style of @Image2."
  }'
  ```
</CodeGroup>

Kuaishou Technology's Kling O1 Reference transforms static images into consistent video sequences at \$0.112 per second, supporting up to 7 simultaneous reference inputs. Trading single-input simplicity for multi-element consistency, it maintains stable character and object identity across complex compositions through specialized reference conditioning. Built for narrative sequences requiring character continuity, product demonstrations with consistent styling, and complex scene transitions where object identity must persist frame-to-frame.

**Built for:** Multi-character storytelling | Brand-consistent product videos | Complex scene transitions with stable elements

***

## Multi-Reference Architecture for Consistent Generation

Kling O1 Reference uses a specialized reference-conditioning system that processes frontal images and multiple reference angles per element, then maintains their identity throughout generated video sequences. Unlike standard image-to-video models that treat input as a single keyframe, this architecture tracks multiple elements independently while preserving their visual characteristics across camera movements and scene changes.

**What this means for you:**

* **Up to 7 simultaneous inputs:** Combine tracked elements (characters/objects with frontal + reference angles), style reference images, and an optional start frame in a single generation. Reference them in prompts as @Element1, @Element2 for tracked objects or @Image1, @Image2 for style references and start frames.
* **Element-level consistency:** Each tracked element supports one frontal image plus multiple reference angles, ensuring characters and objects maintain identity through complex camera movements and transitions
* **Flexible duration control:** Generate 5-second ($0.56) or 10-second ($1.12) sequences at 16:9, 9:16, or 1:1 aspect ratios for platform-specific content optimization
* **Prompt-driven scene control:** Direct camera movements, lighting, and transitions through natural language while the model maintains element consistency. Specify "Take @Image1 as the start frame" to control the video's opening frame.

**Example input structure:** 2 tracked elements (character + object) + 2 style references + 1 start frame = 5 of 7 available inputs

***

## Performance Scaling

Kling O1 Reference prioritizes multi-element consistency over generation speed, with pricing scaled to video duration.

| Metric               | Result                    | Context                                                |
| :------------------- | :------------------------ | :----------------------------------------------------- |
| **Cost per Video**   | $0.56 (5s) or $1.12 (10s) | Based on \$0.112 per second rate                       |
| **Duration Options** | 5s or 10s                 | Fixed durations for consistent output quality          |
| **Maximum Inputs**   | 7 total                   | Combined: elements + reference images + start frame    |
| **Aspect Ratios**    | 16:9, 9:16, 1:1           | Platform-optimized formats for social, web, and mobile |

***

## Technical Specifications

| Spec               | Details                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| **Architecture**   | Kling O1 Reference Image to Video                                                                                              |
| **Input Formats**  | Image URLs (JPG, JPEG, PNG, WebP, GIF, AVIF) + text prompts                                                                    |
| **Output Formats** | MP4 video                                                                                                                      |
| **Video Duration** | 5 or 10 seconds                                                                                                                |
| **Aspect Ratios**  | 16:9, 9:16, 1:1                                                                                                                |
| **Input Types**    | Elements (frontal + reference angles, tracked), Reference Images (style/appearance guides), Start Frame (optional first frame) |
| **Prompt Syntax**  | @Element1, @Element2 for tracked objects; @Image1, @Image2 for references/start frame                                          |
| **License**        | Commercial use (Partner)                                                                                                       |

[API Documentation](https://fal.ai/models/fal-ai/kling-video/o1/reference-to-video/api)

***

## How It Stacks Up

**Kling Video Image to Video (v2.5-turbo)** - Kling O1 Reference trades single-input simplicity for multi-element consistency, making it ideal for narratives requiring multiple characters or objects with stable identity across camera movements. [Kling Video v2.5-turbo](https://fal.ai/models/fal-ai/kling-video/v2.5-turbo/pro/image-to-video) prioritizes single-image animation for straightforward transformations where element tracking isn't required.

**Kling 1.6 Image to Video** - Kling O1 Reference offers advanced element-level control through its reference system for complex multi-character scenes. [Kling 1.6](https://fal.ai/models/fal-ai/kling-video/v1.6/pro/image-to-video) provides established performance for standard image-to-video workflows without multi-reference capabilities.

## Related

* [Kling O1 First Frame Last Frame to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-first-frame-last-frame-to-video) — Video Generation
* [Kling O1 Edit Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-edit-video) — Video Generation
* [Kling O1 Reference Video to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-reference-video-to-video) — Video Generation
* [Kling O1 Reference Image to Video \[Standard\]](/model-api-reference/video-generation-api/kling-o1-reference-image-to-video) — Video Generation

## Capabilities

* Text prompt input
* Duration control
* Aspect ratio control

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required>
  Take @Element1, @Element2 to reference elements and @Image1, @Image2 to reference images in order.
</ParamField>

<ParamField body="image_urls" type="list<string>">
  Additional reference images for style/appearance. Reference in prompt as @Image1, @Image2, etc. Maximum 7 total (elements + reference images + start image).
</ParamField>

<ParamField body="elements" type="list<OmniVideoElementInput>">
  Elements (characters/objects) to include in the video. Reference in prompt as @Element1, @Element2, etc. Maximum 7 total (elements + reference images + start image).
</ParamField>

<ParamField body="duration" type="DurationEnum" default="5">
  Video duration in seconds. Default value: `"5"`

  Possible values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`
</ParamField>

<ParamField body="aspect_ratio" type="AspectRatioEnum" default="16:9">
  The aspect ratio of the generated video frame. Default value: `"16:9"`

  Possible values: `16:9`, `9:16`, `1:1`
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The generated video.
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "Take @Image1 as the start frame. Start with a high-angle satellite view of the ancient greenhouse ruin surrounded by nature. The camera swoops down and flies inside the building, revealing the character from @Element1 standing in the sun-drenched center. The camera then seamlessly transitions into a smooth 180-degree orbit around the character, moving to the back view. As the open backpack comes into focus, the camera continues to push forward, zooming deep inside the bag to reveal the glowing stone from @Element2 nestled inside. Cinematic lighting, hopeful atmosphere, 35mm lens. Make sure to keep it as the style of @Image2.",
  "image_urls": [
    "https://v3b.fal.media/files/b/koala/v9COzzH23FGBYdGLgbK3u.png",
    "https://v3b.fal.media/files/b/elephant/5Is2huKQFSE7A7c5uUeUF.png"
  ],
  "elements": [
    {
      "frontal_image_url": "https://v3b.fal.media/files/b/panda/MQp-ghIqshvMZROKh9lW3.png",
      "reference_image_urls": [
        "https://v3b.fal.media/files/b/kangaroo/YMpmQkYt9xugpOTQyZW0O.png",
        "https://v3b.fal.media/files/b/zebra/d6ywajNyJ6bnpa_xBue-K.png"
      ]
    },
    {
      "frontal_image_url": "https://v3b.fal.media/files/b/koala/gSnsA7HJlgcaTyR5Ujj2H.png",
      "reference_image_urls": [
        "https://v3b.fal.media/files/b/kangaroo/EBF4nWihspyv4pp6hgj7D.png"
      ]
    }
  ],
  "duration": "5",
  "aspect_ratio": "16:9"
}
```

## Output Example

```json theme={null}
{
  "video": {
    "content_type": "video/mp4",
    "file_name": "output.mp4",
    "file_size": 47359974,
    "url": "https://v3b.fal.media/files/b/panda/oVdiICFXY03Vbam-08Aj8_output.mp4"
  }
}
```

## Limitations

* `duration` restricted to: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`
* `aspect_ratio` restricted to: `16:9`, `9:16`, `1:1`
