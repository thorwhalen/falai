> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video V2.1 Standard API

> API reference for Kling Video V2.1 Standard. Kling 2.1 Standard is a cost-efficient endpoint for the Kling 2.1 model, delivering high-quality image-to-video generation

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/v2.1/standard/image-to-video`
**Endpoint ID:** `fal-ai/kling-video/v2.1/standard/image-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v2.1/standard/image-to-video/playground">
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
      "fal-ai/kling-video/v2.1/standard/image-to-video",
      arguments={
          "prompt": "As the sun dips below the horizon, painting the sky in fiery hues of orange and purple, powerful waves relentlessly crash against jagged, dark rocks, their white foam a stark contrast to the deepening twilight; the textured surface of the rocks, wet and glistening, reflects the vibrant colors, creating a mesmerizing spectacle of nature's raw power and breathtaking beauty",
          "image_url": "https://storage.googleapis.com/falserverless/model_tests/kling/kling-image-to-video.jpg"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/kling-video/v2.1/standard/image-to-video", {
    input: {
        prompt: "As the sun dips below the horizon, painting the sky in fiery hues of orange and purple, powerful waves relentlessly crash against jagged, dark rocks, their white foam a stark contrast to the deepening twilight; the textured surface of the rocks, wet and glistening, reflects the vibrant colors, creating a mesmerizing spectacle of nature's raw power and breathtaking beauty",
        image_url: "https://storage.googleapis.com/falserverless/model_tests/kling/kling-image-to-video.jpg"
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
    --url https://fal.run/fal-ai/kling-video/v2.1/standard/image-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "As the sun dips below the horizon, painting the sky in fiery hues of orange and purple, powerful waves relentlessly crash against jagged, dark rocks, their white foam a stark contrast to the deepening twilight; the textured surface of the rocks, wet and glistening, reflects the vibrant colors, creating a mesmerizing spectacle of nature'\''s raw power and breathtaking beauty",
    "image_url": "https://storage.googleapis.com/falserverless/model_tests/kling/kling-image-to-video.jpg"
  }'
  ```
</CodeGroup>

## Examples

> A soft, ethereal light bathes the windowpane as countless raindrops dance and collide, their translucent forms creating shimmering, ephemeral patterns against the glass; the gentle rhythm of the falling water creates a mesmerizing, almost hypnotic effect, complemented by a subtle, melancholic piano ...

<video src="https://v3.fal.media/files/panda/CSekH2UBpK0byk9wU7hug_output.mp4" controls width="100%" />

> As the sun dips below the horizon, painting the sky in fiery hues of orange and purple, powerful waves relentlessly crash against jagged, dark rocks, their white foam a stark contrast to the deepening twilight; the textured surface of the rocks, wet and glistening, reflects the vibrant colors, creat...

<video src="https://v3.fal.media/files/panda/aIxNQwcs5syCT5sYT5_HB_output.mp4" controls width="100%" />

> A tapestry of deep indigo and velvety black slowly yields to the first blush of dawn,  as pinpricks of amber light bloom into fiery streaks across the cityscape, revealing a textured landscape of concrete canyons and glowing windows; the city's awakening unfolds like a dream, a symphony of vibrant h...

<video src="https://v3.fal.media/files/rabbit/_Y-5S3Y3d5onS7ZgjVh1B_output.mp4" controls width="100%" />

### Input Schema

<ParamField body="prompt" type="string" required />

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

### Output Schema

<ParamField body="video" type="File" required>
  The generated video
</ParamField>

### Input Example

```json theme={null}
{
  "prompt": "As the sun dips below the horizon, painting the sky in fiery hues of orange and purple, powerful waves relentlessly crash against jagged, dark rocks, their white foam a stark contrast to the deepening twilight; the textured surface of the rocks, wet and glistening, reflects the vibrant colors, creating a mesmerizing spectacle of nature's raw power and breathtaking beauty",
  "image_url": "https://storage.googleapis.com/falserverless/model_tests/kling/kling-image-to-video.jpg",
  "duration": "5",
  "negative_prompt": "blur, distort, and low quality",
  "cfg_scale": 0.5
}
```

### Output Example

```json theme={null}
{
  "video": {
    "url": "https://v3.fal.media/files/koala/17e3xh08J4_PkHS_0cbwF_output.mp4"
  }
}
```

## Kling AI v2.1 Standard - Cost-Efficient Image-to-Video Generation

Transform static images into fluid, natural-looking videos with Kling AI v2.1 Standard. This powerful image-to-video model delivers professional-quality motion synthesis ideal for content creators, marketers, and developers.

### Overview

Kling AI v2.1 Standard brings static images to life through advanced motion synthesis technology. Created by Kuaishou, this model excels at generating natural movement while preserving the original image's quality and details. As a cost-efficient endpoint for the Kling 2.1 model, it delivers high-quality image-to-video generation at an accessible price point.

#### Key Capabilities

Transform single images into dynamic videos with:

* Natural motion synthesis that respects physics and object relationships
* Consistent quality throughout the generated video sequence
* Preservation of fine details and textures from source images
* Support for diverse content types including people, animals, objects, and scenes
* Flexible duration options (5 or 10 seconds)

### Popular Use Cases

**Content Creation**
Generate marketing visuals, social media assets, and blog illustrations at scale. Perfect for agencies and content teams who need consistent, high-quality imagery.

**Product Development**\
Create concept art, UI mockups, and design variations for rapid prototyping. Ideal for designers exploring visual directions.

**E-commerce**
Generate product lifestyle images, seasonal campaigns, and A/B testing visuals to boost conversion rates.

**Entertainment**
Produce game assets, storyboard illustrations, and creative concept art for media projects.

### Getting Started

Getting up and running with Kling AI is straightforward. Here's how to begin:

1. Get your API key at [fal.ai/login](https://fal.ai/login)
2. Install the client library for your preferred language
3. Make your first API call

#### Installation

For JavaScript/TypeScript projects:

```bash theme={null}
npm install --save @fal-ai/client
```

For Python projects:

```bash theme={null}
pip install fal-client
```

#### Basic Usage

Here's a simple example of generating a video from an image:

```typescript theme={null}
import { fal } from "@fal-ai/client";

fal.config({
  credentials: "YOUR_FAL_KEY"
});

const result = await fal.subscribe("fal-ai/kling-video/v2.1/standard/image-to-video", {
  input: {
    prompt: "As the sun dips below the horizon, painting the sky in fiery hues",
    image_url: "https://example.com/your-image.jpg",
    duration: "5",
    aspect_ratio: "16:9",
    negative_prompt: "blur, distort, and low quality",
    cfg_scale: 0.5
  }
});

console.log(result.video.url);
```

### API Parameters

* `prompt` (required): Text description of the desired motion and scene
* `image_url` (required): URL of the input image
* `duration`: Video duration - "5" or "10" seconds
* `aspect_ratio`: Output aspect ratio (e.g., "16:9", "9:16", "1:1")
* `negative_prompt`: Elements to avoid in the generation
* `cfg_scale`: Classifier Free Guidance scale (default: 0.5)
* `static_mask_url`: URL for static motion brush mask
* `dynamic_mask_url`: URL for dynamic motion brush mask
* `special_fx`: Special effects like "hug", "kiss", "heart\_gesture", "squish", "expansion"
* `input_image_urls`: Array of up to 4 images for multi-image generation

### Technical Specifications

Performance characteristics:

* Input formats: JPG, JPEG, PNG, WEBP, GIF, AVIF
* Output format: MP4
* Duration options: 5 or 10 seconds
* Processing time: Variable based on load
* Video resolution: Maintains input quality

### Best Practices

To achieve optimal results:

Create videos that engage viewers by following these guidelines:

* Use high-quality source images with clear subjects
* Ensure proper lighting and contrast in your input images
* Consider the intended motion when framing your source image
* Test different cfg\_scale values (0.3-0.7) to find the right motion control
* Write detailed prompts describing the desired motion and scene dynamics

### Queue Management

For asynchronous processing:

```typescript theme={null}
// Submit request
const { request_id } = await fal.queue.submit("fal-ai/kling-video/v2.1/standard/image-to-video", {
  input: {
    prompt: "Your detailed video description",
    image_url: "your-image-url"
  }
});

// Check status
const status = await fal.queue.status("fal-ai/kling-video/v2.1/standard/image-to-video", {
  requestId: request_id,
  logs: true
});

// Get result
const result = await fal.queue.result("fal-ai/kling-video/v2.1/standard/image-to-video", {
  requestId: request_id
});
```

### Pricing and Usage

Cost-efficient pricing structure:

* **5-second video**: \$0.25
* **Additional seconds**: \$0.05 per second
* 10-second video: \$0.50

[View detailed pricing](https://fal.ai/pricing) or [contact sales](mailto:support@fal.ai) for enterprise solutions.

### Model Variants

Kling 2.1 offers multiple quality tiers:

* **Standard**: This model - Cost-efficient option
* **Pro**: `fal-ai/kling-video/v2.1/pro/image-to-video` - Professional grade
* **Master**: `fal-ai/kling-video/v2.1/master/image-to-video` - Premium quality

### Migration Guide

Coming from another platform? Our migration tools and guides make it simple to switch to Kling AI. The API structure follows industry standards with intuitive parameter naming.

### Support and Resources

* API Documentation: [fal.ai/models/fal-ai/kling-video/v2.1/standard/image-to-video/api](https://fal.ai/models/fal-ai/kling-video/v2.1/standard/image-to-video/api)
* Discord Community: [discord.com/invite/fal-ai](https://discord.com/invite/fal-ai)
* Support: [support@fal.ai](mailto:support@fal.ai)

Ready to get started? [Create your free account](https://fal.ai/login) and begin transforming your images into engaging videos with Kling AI v2.1 Standard.

## Related

* [Kling 2.1 (pro)](/model-api-reference/video-generation-api/kling-2.1-pro) — Video Generation
* [Kling 2.1 Master](/model-api-reference/video-generation-api/kling-2.1-master) — Video Generation

## Limitations

* `duration` restricted to: `5`, `10`
* `cfg_scale` range: 0 to 1
