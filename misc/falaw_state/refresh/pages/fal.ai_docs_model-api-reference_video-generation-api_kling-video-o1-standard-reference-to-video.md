> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video O1 Standard Reference To Video API

> API reference for Kling Video O1 Standard Reference To Video. Transform images, elements, and text into consistent, high-quality video scenes, ensuring stable character identity, object details, and e

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/o1/standard/reference-to-video`
**Endpoint ID:** `fal-ai/kling-video/o1/standard/reference-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/o1/standard/reference-to-video/playground">
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
      "fal-ai/kling-video/o1/standard/reference-to-video",
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

  const result = await fal.subscribe("fal-ai/kling-video/o1/standard/reference-to-video", {
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
    --url https://fal.run/fal-ai/kling-video/o1/standard/reference-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "Take @Image1 as the start frame. Start with a high-angle satellite view of the ancient greenhouse ruin surrounded by nature. The camera swoops down and flies inside the building, revealing the character from @Element1 standing in the sun-drenched center. The camera then seamlessly transitions into a smooth 180-degree orbit around the character, moving to the back view. As the open backpack comes into focus, the camera continues to push forward, zooming deep inside the bag to reveal the glowing stone from @Element2 nestled inside. Cinematic lighting, hopeful atmosphere, 35mm lens. Make sure to keep it as the style of @Image2."
  }'
  ```
</CodeGroup>

## Related

* [Kling O1 First Frame Last Frame to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-first-frame-last-frame-to-video) — Video Generation
* [Kling O1 Edit Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-edit-video) — Video Generation
* [Kling O1 Reference Image to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-reference-image-to-video) — Video Generation
* [Kling O1 Reference Video to Video \[Pro\]](/model-api-reference/video-generation-api/kling-o1-reference-video-to-video) — Video Generation

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
