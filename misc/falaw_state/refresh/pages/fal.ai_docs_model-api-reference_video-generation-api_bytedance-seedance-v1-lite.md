> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Seedance V1 Lite API

> API reference for Bytedance Seedance V1 Lite. Seedance 1.0 Lite

<Tabs>
  <Tab title="Image To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedance/v1/lite/image-to-video`
    **Endpoint ID:** `fal-ai/bytedance/seedance/v1/lite/image-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedance/v1/lite/image-to-video/playground">
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
          "fal-ai/bytedance/seedance/v1/lite/image-to-video",
          arguments={
              "prompt": "A little dog is running in the sunshine. The camera follows the dog as it plays in a garden.",
              "image_url": "https://fal.media/files/koala/f_xmiodPjhiKjdBkFmTu1.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/seedance/v1/lite/image-to-video", {
        input: {
            prompt: "A little dog is running in the sunshine. The camera follows the dog as it plays in a garden.",
            image_url: "https://fal.media/files/koala/f_xmiodPjhiKjdBkFmTu1.png"
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
        --url https://fal.run/fal-ai/bytedance/seedance/v1/lite/image-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A little dog is running in the sunshine. The camera follows the dog as it plays in a garden.",
        "image_url": "https://fal.media/files/koala/f_xmiodPjhiKjdBkFmTu1.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt used to generate the video
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
      The aspect ratio of the generated video Default value: `"auto"`

      Possible values: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `auto`
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="720p">
      Video resolution - 480p for faster generation, 720p for higher quality Default value: `"720p"`

      Possible values: `480p`, `720p`, `1080p`
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="5">
      Duration of the video in seconds Default value: `"5"`

      Possible values: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`
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

    <ParamField body="num_frames" type="integer">
      The number of frames to generate. If provided, will override duration.

      Range: `29` to `289`
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
      "prompt": "A little dog is running in the sunshine. The camera follows the dog as it plays in a garden.",
      "aspect_ratio": "auto",
      "resolution": "720p",
      "duration": "5",
      "camera_fixed": false,
      "enable_safety_checker": true,
      "image_url": "https://fal.media/files/koala/f_xmiodPjhiKjdBkFmTu1.png"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://v3.fal.media/files/penguin/qmLZSvOIzTKs6bDFXiEtH_video.mp4"
      },
      "seed": 42
    }
    ```
  </Tab>

  <Tab title="Text To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedance/v1/lite/text-to-video`
    **Endpoint ID:** `fal-ai/bytedance/seedance/v1/lite/text-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedance/v1/lite/text-to-video/playground">
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
          "fal-ai/bytedance/seedance/v1/lite/text-to-video",
          arguments={
              "prompt": "A little dog is running in the sunshine. The camera follows the dog as it plays in a garden."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/seedance/v1/lite/text-to-video", {
        input: {
            prompt: "A little dog is running in the sunshine. The camera follows the dog as it plays in a garden."
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
        --url https://fal.run/fal-ai/bytedance/seedance/v1/lite/text-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A little dog is running in the sunshine. The camera follows the dog as it plays in a garden."
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt used to generate the video
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="16:9">
      The aspect ratio of the generated video Default value: `"16:9"`

      Possible values: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `9:21`
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="720p">
      Video resolution - 480p for faster generation, 720p for higher quality Default value: `"720p"`

      Possible values: `480p`, `720p`, `1080p`
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="5">
      Duration of the video in seconds Default value: `"5"`

      Possible values: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`
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

    <ParamField body="num_frames" type="integer">
      The number of frames to generate. If provided, will override duration.

      Range: `29` to `289`
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
      "prompt": "A little dog is running in the sunshine. The camera follows the dog as it plays in a garden.",
      "aspect_ratio": "16:9",
      "resolution": "720p",
      "duration": "5",
      "camera_fixed": false,
      "enable_safety_checker": true
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://v3.fal.media/files/penguin/qmLZSvOIzTKs6bDFXiEtH_video.mp4"
      },
      "seed": 42
    }
    ```
  </Tab>

  <Tab title="Reference To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedance/v1/lite/reference-to-video`
    **Endpoint ID:** `fal-ai/bytedance/seedance/v1/lite/reference-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedance/v1/lite/reference-to-video/playground">
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
          "fal-ai/bytedance/seedance/v1/lite/reference-to-video",
          arguments={
              "prompt": "The girl catches the puppy and hugs it.",
              "reference_image_urls": [
                  "https://storage.googleapis.com/falserverless/example_inputs/seedance_reference.jpeg",
                  "https://storage.googleapis.com/falserverless/example_inputs/seedance_reference_2.jpeg"
              ]
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/seedance/v1/lite/reference-to-video", {
        input: {
            prompt: "The girl catches the puppy and hugs it.",
            reference_image_urls: [
              "https://storage.googleapis.com/falserverless/example_inputs/seedance_reference.jpeg",
              "https://storage.googleapis.com/falserverless/example_inputs/seedance_reference_2.jpeg"
            ]
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
        --url https://fal.run/fal-ai/bytedance/seedance/v1/lite/reference-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "The girl catches the puppy and hugs it.",
        "reference_image_urls": [
          "https://storage.googleapis.com/falserverless/example_inputs/seedance_reference.jpeg",
          "https://storage.googleapis.com/falserverless/example_inputs/seedance_reference_2.jpeg"
        ]
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt used to generate the video
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
      The aspect ratio of the generated video Default value: `"auto"`

      Possible values: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `auto`
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="720p">
      Video resolution - 480p for faster generation, 720p for higher quality Default value: `"720p"`

      Possible values: `480p`, `720p`
    </ParamField>

    <ParamField body="duration" type="DurationEnum" default="5">
      Duration of the video in seconds Default value: `"5"`

      Possible values: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`
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

    <ParamField body="num_frames" type="integer">
      The number of frames to generate. If provided, will override duration.

      Range: `29` to `289`
    </ParamField>

    <ParamField body="reference_image_urls" type="list<string>" required>
      Reference images to generate the video with.
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
      "prompt": "The girl catches the puppy and hugs it.",
      "aspect_ratio": "auto",
      "resolution": "720p",
      "duration": "5",
      "camera_fixed": false,
      "enable_safety_checker": true,
      "reference_image_urls": [
        "https://storage.googleapis.com/falserverless/example_inputs/seedance_reference.jpeg",
        "https://storage.googleapis.com/falserverless/example_inputs/seedance_reference_2.jpeg"
      ]
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://storage.googleapis.com/falserverless/example_outputs/seedance_reference_output.mp4"
      },
      "seed": 42
    }
    ```
  </Tab>
</Tabs>

## Seedance 1.0 - High-Quality AI Video Generation by ByteDance

Transform your creative vision into professional videos with Seedance, ByteDance's advanced video generation model. Available in both Pro and Lite versions, Seedance delivers exceptional text-to-video and image-to-video generation capabilities for content creators, marketers, and developers.

### Overview

Seedance 1.0 is a fast and efficient video generation model that creates high-quality videos from text prompts or images. The model supports multiple aspect ratios, resolutions, and durations for versatile video generation.

#### Available Endpoints

**Seedance Lite (Fast & Cost-Effective)**

* Text-to-Video: `fal-ai/bytedance/seedance/v1/lite/text-to-video`
* Image-to-Video: `fal-ai/bytedance/seedance/v1/lite/image-to-video`
* Resolution: Up to 720p
* Duration: 5 or 10 seconds

**Seedance Pro (Premium Quality)**

* Text-to-Video: `fal-ai/bytedance/seedance/v1/pro/text-to-video`
* Image-to-Video: `fal-ai/bytedance/seedance/v1/pro/image-to-video`
* Resolution: Up to 1080p
* Duration: 5 or 10 seconds

### Getting Started

Setting up Seedance is straightforward. First, install your preferred client:

For JavaScript/TypeScript:

```bash theme={null}
npm install --save @fal-ai/client
```

For Python:

```bash theme={null}
pip install fal-client
```

Configure your authentication:

```typescript theme={null}
import { fal } from "@fal-ai/client";

fal.config({
  credentials: "YOUR_FAL_KEY_HERE"
});
```

### Creating Your First Video

#### Text-to-Video Generation

Generate videos directly from text descriptions:

```typescript theme={null}
const result = await fal.subscribe("fal-ai/bytedance/seedance/v1/lite/text-to-video", {
  input: {
    prompt: "A little dog is running in the sunshine. The camera follows the dog as it plays in a garden.",
    aspect_ratio: "16:9",
    resolution: "720p",
    duration: "5"
  }
});

console.log(result.video.url);
```

#### Image-to-Video Generation

Animate still images with descriptive prompts:

```typescript theme={null}
const result = await fal.subscribe("fal-ai/bytedance/seedance/v1/lite/image-to-video", {
  input: {
    image_url: "https://example.com/your-image.jpg",
    prompt: "A skier glides over fresh snow, joyously smiling while kicking up large clouds of snow",
    resolution: "720p",
    duration: "5"
  }
});
```

### API Parameters

#### Common Parameters

* `prompt` (required): Descriptive text for video generation
* `aspect_ratio`: "16:9", "9:16", or "1:1"
* `resolution`: "480p", "720p", or "1080p" (Pro only)
* `duration`: "5" or "10" (seconds)
* `seed`: Random seed for reproducible results (use -1 for random)

#### Image-to-Video Specific

* `image_url` (required): URL of the input image
* Supported formats: jpg, jpeg, png, webp, gif, avif

### Advanced Features

#### Camera Movement Instructions (Pro)

Seedance Pro supports camera movement instructions using square brackets:

```typescript theme={null}
const result = await fal.subscribe("fal-ai/bytedance/seedance/v1/pro/text-to-video", {
  input: {
    prompt: "A bright blue race car speeds along a snowy racetrack. [Low-angle shot] Captures several cars speeding along the racetrack through a harsh snowstorm. [Overhead shot] The camera gradually pulls upward, revealing the full race scene",
    resolution: "1080p",
    duration: "10"
  }
});
```

Supported movements include:

* Truck left/right, Pan left/right
* Push in/Pull out, Pedestal up/down
* Tilt up/down, Zoom in/out
* Shake, Tracking shot, Static shot

#### File Upload Support

Upload local files for image-to-video generation:

```typescript theme={null}
import { fal } from "@fal-ai/client";

const file = new File([imageData], "image.jpg", { type: "image/jpeg" });
const url = await fal.storage.upload(file);

const result = await fal.subscribe("fal-ai/bytedance/seedance/v1/lite/image-to-video", {
  input: {
    image_url: url,
    prompt: "Animate this scene with gentle movement",
    resolution: "720p",
    duration: "5"
  }
});
```

### Pricing

**Seedance Lite**

* \$0.18 per 720p 5-second video
* \$1.80 per million video tokens
* Formula: `tokens = (height × width × FPS × duration) / 1024`

**Seedance Pro**

* \~\$0.62 per 1080p 5-second video
* \$2.50 per million video tokens
* Premium quality with advanced features

### Best Practices

#### For Optimal Results

1. **Write Clear, Detailed Prompts**
   * Begin with the main subject
   * Include important visual details
   * Specify desired movement or camera actions
   * Use camera movement instructions in Pro for cinematic effects

2. **Optimize Performance**
   * Start with shorter durations (5 seconds) during testing
   * Use Lite for rapid prototyping and social media content
   * Choose Pro for professional productions requiring highest quality

3. **Image-to-Video Tips**
   * Use high-quality input images
   * Ensure images have clear subjects
   * Match prompt descriptions to image content
   * Consider aspect ratio compatibility

### Use Cases

**Seedance Lite - Perfect for:**

* Social media content (TikTok, Instagram Reels)
* Quick creative concepts and prototypes
* Educational content and demonstrations
* Marketing previews and teasers

**Seedance Pro - Ideal for:**

* Professional marketing campaigns
* High-quality brand content
* Cinematic storytelling with multi-shot sequences
* Premium product demonstrations

### Error Handling

Implement robust error handling for production use:

```typescript theme={null}
try {
  const result = await fal.subscribe("fal-ai/bytedance/seedance/v1/lite/text-to-video", {
    input: {
      prompt: "Your creative prompt",
      resolution: "720p",
      duration: "5"
    }
  });
  console.log(result.video.url);
} catch (error) {
  console.error("Video generation failed:", error.message);
  // Implement fallback logic
}
```

### Queue Management

For long-running requests, use the queue API:

```typescript theme={null}
// Submit request
const { request_id } = await fal.queue.submit("fal-ai/bytedance/seedance/v1/pro/text-to-video", {
  input: {
    prompt: "Complex multi-shot video prompt",
    resolution: "1080p",
    duration: "10"
  },
  webhookUrl: "https://your-webhook.url/results"
});

// Check status
const status = await fal.queue.status("fal-ai/bytedance/seedance/v1/pro/text-to-video", {
  requestId: request_id
});

// Get result
const result = await fal.queue.result("fal-ai/bytedance/seedance/v1/pro/text-to-video", {
  requestId: request_id
});
```

### Technical Details

* **Inference Speed**: \~41 seconds for 5-second 1080p video on L20 GPU
* **Concurrency**: Up to 10 simultaneous renders
* **API Authentication**: Key-based authentication via FAL\_KEY
* **Output Format**: MP4 video files
* **Partner Model**: Available through fal.ai's inference infrastructure

### Support

For implementation assistance and additional resources:

* **Documentation**: [fal.ai Documentation](https://docs.fal.ai/)
* **API Reference**: View model-specific endpoints and parameters
* **Model Gallery**: Explore all Seedance variants at [fal.ai/models](https://fal.ai/models)
* **Dashboard**: Manage API keys at [fal.ai/dashboard](https://fal.ai/dashboard)

### Getting Started Today

Ready to transform your ideas into compelling videos? Sign up at [fal.ai](https://fal.ai/) to get your API key and start creating with Seedance. Both Pro and Lite versions offer unique advantages for different use cases, ensuring you have the right tool for your creative needs.

## Related

* [Seedance 1.0 Pro](/model-api-reference/video-generation-api/seedance-1.0-pro) — Video Generation
* [Bytedance](/model-api-reference/video-generation-api/bytedance) — Video Generation
* [Seedance 1.0 Lite](/model-api-reference/video-generation-api/seedance-1.0-lite) — Video Generation

## Limitations

* `aspect_ratio` restricted to: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `auto`
* `resolution` restricted to: `480p`, `720p`, `1080p`
* `num_frames` range: 29 to 289
* Content moderation via safety checker
* `aspect_ratio` restricted to: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `9:21`
* `resolution` restricted to: `480p`, `720p`
