> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video V2.1 Pro API

> API reference for Kling Video V2.1 Pro. Kling 2.1 Pro is an advanced endpoint for the Kling 2.1 model, offering professional-grade videos with enhanced visual fidelity, precise camera movements, and d

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/v2.1/pro/image-to-video`
**Endpoint ID:** `fal-ai/kling-video/v2.1/pro/image-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v2.1/pro/image-to-video/playground">
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
      "fal-ai/kling-video/v2.1/pro/image-to-video",
      arguments={
          "prompt": "Warm, incandescent streetlights paint the rain-slicked cobblestones in pools of amber light as a couple walks hand-in-hand, their silhouettes stark against the blurry backdrop of a city shrouded in a gentle downpour; the camera lingers on the subtle textures of their rain-soaked coats and the glistening reflections dancing on the wet pavement, creating a sense of intimate vulnerability and shared quietude.",
          "image_url": "https://v3.fal.media/files/lion/_I_io6Gtk83c72d-afXf8_image.webp"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/kling-video/v2.1/pro/image-to-video", {
    input: {
        prompt: "Warm, incandescent streetlights paint the rain-slicked cobblestones in pools of amber light as a couple walks hand-in-hand, their silhouettes stark against the blurry backdrop of a city shrouded in a gentle downpour; the camera lingers on the subtle textures of their rain-soaked coats and the glistening reflections dancing on the wet pavement, creating a sense of intimate vulnerability and shared quietude.",
        image_url: "https://v3.fal.media/files/lion/_I_io6Gtk83c72d-afXf8_image.webp"
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
    --url https://fal.run/fal-ai/kling-video/v2.1/pro/image-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "Warm, incandescent streetlights paint the rain-slicked cobblestones in pools of amber light as a couple walks hand-in-hand, their silhouettes stark against the blurry backdrop of a city shrouded in a gentle downpour; the camera lingers on the subtle textures of their rain-soaked coats and the glistening reflections dancing on the wet pavement, creating a sense of intimate vulnerability and shared quietude.",
    "image_url": "https://v3.fal.media/files/lion/_I_io6Gtk83c72d-afXf8_image.webp"
  }'
  ```
</CodeGroup>

## Examples

> Golden sunlight bathes a weathered old man, his hands, gnarled like ancient olive branches, scattering seeds onto the cobblestones where a flock of iridescent pigeons descends,

<video src="https://v3.fal.media/files/lion/PqeSJnszNGpIM4QN8nGGs_output.mp4" controls width="100%" />

> Golden sunlight bathes the rugged mountain peak as a lone yogi finds stillness amidst the windswept, rocky terrain, their movements a fluid dance between earth and sky;  breath becoming one with the vastness of the alpine landscape, a testament to the quiet power found in moments of mindful connecti...

<video src="https://v3.fal.media/files/panda/pxDM7XwZGaKpkKPzDoUMN_output.mp4" controls width="100%" />

> Warm, incandescent streetlights paint the rain-slicked cobblestones in pools of amber light as a couple walks hand-in-hand, their silhouettes stark against the blurry backdrop of a city shrouded in a gentle downpour; the camera lingers on the subtle textures of their rain-soaked coats and the gliste...

<video src="https://v3.fal.media/files/rabbit/Y5I8-7u3e7ogVSvPin1TS_output.mp4" controls width="100%" />

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

<ParamField body="tail_image_url" type="string">
  URL of the image to be used for the end of the video
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The generated video
</ParamField>

### Input Example

```json theme={null}
{
  "prompt": "Warm, incandescent streetlights paint the rain-slicked cobblestones in pools of amber light as a couple walks hand-in-hand, their silhouettes stark against the blurry backdrop of a city shrouded in a gentle downpour; the camera lingers on the subtle textures of their rain-soaked coats and the glistening reflections dancing on the wet pavement, creating a sense of intimate vulnerability and shared quietude.",
  "image_url": "https://v3.fal.media/files/lion/_I_io6Gtk83c72d-afXf8_image.webp",
  "duration": "5",
  "negative_prompt": "blur, distort, and low quality",
  "cfg_scale": 0.5
}
```

### Output Example

```json theme={null}
{
  "video": {
    "url": "https://v3.fal.media/files/rabbit/Y5I8-7u3e7ogVSvPin1TS_output.mp4"
  }
}
```

## Kling AI v2.1 Pro - Professional Image-to-Video Generation

Transform static images into dynamic, fluid video content with Kling AI v2.1 Pro, the advanced image-to-video generation model from Kuaishou. Perfect for content creators, marketers, and developers who need high-quality video content at scale.

### Overview

Kling AI v2.1 Pro brings professional-grade video generation capabilities to your applications. Built on advanced machine learning architecture, it excels at creating natural motion patterns and seamless transitions from single images with enhanced visual fidelity, precise camera movements, and dynamic motion control.

Key Capabilities:

* Generate 5 or 10-second videos from any input image
* Advanced motion interpolation for smooth transitions
* Preserve fine details and textures throughout animation
* Support for diverse image types and subjects
* Professional-grade visual quality perfect for cinematic storytelling

### Getting Started

Getting up and running with Kling AI is straightforward. First, set up your development environment:

Using npm:

```bash theme={null}
npm install --save @fal-ai/client
```

Using pip:

```python theme={null}
pip install fal-client
```

Configure your authentication:

```typescript theme={null}
import { fal } from "@fal-ai/client";

fal.config({
  credentials: "YOUR_FAL_KEY_HERE"
});
```

### Making Your First API Call

Here's a simple example of generating a video from an image:

```typescript theme={null}
import { fal } from "@fal-ai/client";

const result = await fal.subscribe("fal-ai/kling-video/v2.1/pro/image-to-video", {
  input: {
    prompt: "Sunlight dapples through budding branches, illuminating a vibrant tapestry of greens",
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

### Advanced Features

The Pro version includes several advanced capabilities that set it apart:

#### Motion Control

Fine-tune the intensity and direction of motion with precise controls using motion brush masks and cfg\_scale parameters.

#### Quality Preservation

Advanced interpolation algorithms maintain image quality throughout the video sequence, ensuring crisp details and accurate color reproduction.

#### Special Effects

```typescript theme={null}
const result = await fal.subscribe("fal-ai/kling-video/v2.1/pro/image-to-video", {
  input: {
    prompt: "Romantic scene with special effects",
    image_url: "your-image-url",
    special_fx: "heart_gesture"
  }
});
```

### Model Variants

Kling 2.1 offers multiple quality tiers:

* **Pro**: Professional-grade quality (this model)
* **Standard**: `fal-ai/kling-video/v2.1/standard/image-to-video` - Cost-efficient option
* **Master**: `fal-ai/kling-video/v2.1/master/image-to-video` - Premium tier with unparalleled quality

### Best Practices

To achieve optimal results:

1. Provide high-quality input images (recommended: 1080p or higher)
2. Write detailed prompts describing motion, camera movement, and scene dynamics
3. Use negative prompts to avoid unwanted elements
4. Test different cfg\_scale values (0.3-0.7) for motion control
5. Consider aspect ratio based on your target platform

### Technical Specifications

Processing Capabilities:

* Input formats: JPG, JPEG, PNG, WEBP, GIF, AVIF
* Output format: MP4
* Resolution: Up to 1080p
* Frame rate: Standard video frame rates
* Processing time: Approximately 5 minutes

### Queue Management

For asynchronous processing:

```typescript theme={null}
// Submit request
const { request_id } = await fal.queue.submit("fal-ai/kling-video/v2.1/pro/image-to-video", {
  input: {
    prompt: "Your detailed video description",
    image_url: "your-image-url",
    duration: "10"
  }
});

// Check status
const status = await fal.queue.status("fal-ai/kling-video/v2.1/pro/image-to-video", {
  requestId: request_id,
  logs: true
});

// Get result
const result = await fal.queue.result("fal-ai/kling-video/v2.1/pro/image-to-video", {
  requestId: request_id
});
```

### Pricing and Usage

* **5-second video**: \$0.45
* **Additional seconds**: \$0.09 per second
* 10-second video: \$0.90
* Processing time: Approximately 5 minutes

[View detailed pricing](https://fal.ai/pricing) or [contact sales](mailto:support@fal.ai) for enterprise solutions.

### Support and Resources

Need help? Access comprehensive support through:

* Technical documentation at [docs.fal.ai](https://docs.fal.ai)
* API Reference: [fal.ai/models/fal-ai/kling-video/v2.1/pro/image-to-video/api](https://fal.ai/models/fal-ai/kling-video/v2.1/pro/image-to-video/api)
* Community forums for peer support
* Direct support channels for Pro users

### Ready to Create Professional Videos?

Get started with Kling AI v2.1 Pro today by signing up at [fal.ai](https://fal.ai) and generating your API key. Transform your static images into engaging, cinematic videos with professional-grade quality.

## Related

* [Kling 2.1 (standard)](/model-api-reference/video-generation-api/kling-2.1-standard) — Video Generation
* [Kling 2.1 Master](/model-api-reference/video-generation-api/kling-2.1-master) — Video Generation

## Limitations

* `duration` restricted to: `5`, `10`
* `cfg_scale` range: 0 to 1
