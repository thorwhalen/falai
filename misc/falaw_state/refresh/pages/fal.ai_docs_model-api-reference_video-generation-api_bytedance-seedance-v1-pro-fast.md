> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Seedance V1 Pro Fast API

> API reference for Bytedance Seedance V1 Pro Fast. Image to Video endpoint for Seedance 1.0 Pro Fast, a next-generation video model designed to deliver maximum performance at minimal cost

<Tabs>
  <Tab title="Image To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedance/v1/pro/fast/image-to-video`
    **Endpoint ID:** `fal-ai/bytedance/seedance/v1/pro/fast/image-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedance/v1/pro/fast/image-to-video/playground">
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
          "fal-ai/bytedance/seedance/v1/pro/fast/image-to-video",
          arguments={
              "prompt": "Bathed in a stark spotlight, a lone ballet dancer takes center stage. Her movements, precise and graceful, tell a story of passion and dedication against the velvet darkness. The scene evokes a sense of intimacy, highlighting the raw emotion and artistry of her performance.",
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/seedance_fast_i2v_input.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/seedance/v1/pro/fast/image-to-video", {
        input: {
            prompt: "Bathed in a stark spotlight, a lone ballet dancer takes center stage. Her movements, precise and graceful, tell a story of passion and dedication against the velvet darkness. The scene evokes a sense of intimacy, highlighting the raw emotion and artistry of her performance.",
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/seedance_fast_i2v_input.png"
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
        --url https://fal.run/fal-ai/bytedance/seedance/v1/pro/fast/image-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Bathed in a stark spotlight, a lone ballet dancer takes center stage. Her movements, precise and graceful, tell a story of passion and dedication against the velvet darkness. The scene evokes a sense of intimacy, highlighting the raw emotion and artistry of her performance.",
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/seedance_fast_i2v_input.png"
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

    <ParamField body="resolution" type="ResolutionEnum" default="1080p">
      Video resolution - 480p for faster generation, 720p for balance, 1080p for higher quality Default value: `"1080p"`

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
      "prompt": "Bathed in a stark spotlight, a lone ballet dancer takes center stage. Her movements, precise and graceful, tell a story of passion and dedication against the velvet darkness. The scene evokes a sense of intimacy, highlighting the raw emotion and artistry of her performance.",
      "aspect_ratio": "auto",
      "resolution": "1080p",
      "duration": "5",
      "camera_fixed": false,
      "enable_safety_checker": true,
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/seedance_fast_i2v_input.png"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://storage.googleapis.com/falserverless/example_inputs/seedance_fast_i2v_output.mp4"
      },
      "seed": 42
    }
    ```
  </Tab>

  <Tab title="Text To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedance/v1/pro/fast/text-to-video`
    **Endpoint ID:** `fal-ai/bytedance/seedance/v1/pro/fast/text-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedance/v1/pro/fast/text-to-video/playground">
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
          "fal-ai/bytedance/seedance/v1/pro/fast/text-to-video",
          arguments={
              "prompt": "Inside a quiet dojo, a martial artist moves with precision and grace. The performance highlights the beauty and discipline inherent in the ancient practice. Each form unfolds clearly, a testament to dedication and skill."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/seedance/v1/pro/fast/text-to-video", {
        input: {
            prompt: "Inside a quiet dojo, a martial artist moves with precision and grace. The performance highlights the beauty and discipline inherent in the ancient practice. Each form unfolds clearly, a testament to dedication and skill."
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
        --url https://fal.run/fal-ai/bytedance/seedance/v1/pro/fast/text-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Inside a quiet dojo, a martial artist moves with precision and grace. The performance highlights the beauty and discipline inherent in the ancient practice. Each form unfolds clearly, a testament to dedication and skill."
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt used to generate the video
    </ParamField>

    <ParamField body="aspect_ratio" type="AspectRatioEnum" default="16:9">
      The aspect ratio of the generated video Default value: `"16:9"`

      Possible values: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
    </ParamField>

    <ParamField body="resolution" type="ResolutionEnum" default="1080p">
      Video resolution - 480p for faster generation, 720p for balance, 1080p for higher quality Default value: `"1080p"`

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
      "prompt": "Inside a quiet dojo, a martial artist moves with precision and grace. The performance highlights the beauty and discipline inherent in the ancient practice. Each form unfolds clearly, a testament to dedication and skill.",
      "aspect_ratio": "16:9",
      "resolution": "1080p",
      "duration": "5",
      "camera_fixed": false,
      "enable_safety_checker": true
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://storage.googleapis.com/falserverless/example_inputs/seedance_fast_t2v_output.mp4"
      },
      "seed": 42
    }
    ```
  </Tab>
</Tabs>

## Seedance 1.0 Pro Fast \[Text-to-Video]

Transform text prompts into professional-grade videos with ByteDance's next-generation video model engineered for maximum performance at minimal cost.

## Overview

Seedance 1.0 Pro Fast delivers high-quality video generation from text prompts with exceptional speed and efficiency. Built to support versatile production workflows, this model excels at creating videos with realistic motion and physical stability—making it ideal for everything from social media content to commercial productions. Generate compelling visual narratives without requiring complex video editing skills or production infrastructure.

## Key Capabilities

* **Text-to-video transformation**: Convert detailed text descriptions directly into coherent, high-quality video sequences
* **Fast inference times**: Deliver quick turnarounds for time-sensitive content creation workflows
* **Wide dynamic range**: Generate smooth large-scale movements from subtle expressions to active scenes with high stability
* **Production-ready output**: Create commercially viable videos suitable for marketing, social media, and professional applications

## Popular Use Cases

**Social Media Content Creation**\
Generate engaging video content for Instagram Reels, TikTok, and YouTube Shorts directly from text descriptions. Transform product descriptions, promotional copy, or creative concepts into thumb-stopping videos that capture attention across multiple platforms without hiring production crews or investing in expensive equipment.

**Marketing and Advertising**\
Create compelling commercial video content for campaigns, product launches, and brand storytelling. Generate multiple variations of marketing videos to test different messaging approaches, visual styles, and creative directions—enabling rapid iteration and A/B testing at a fraction of traditional production costs.

**Educational and Training Content**\
Develop instructional videos, demonstrations, and training materials by describing the scenes you need. Produce consistent, professional-quality educational content that illustrates complex concepts, procedures, or workflows without coordinating filming schedules or managing production logistics.

## Getting Started

Getting up and running with Seedance 1.0 Pro Fast takes just a few minutes. Here's how to begin:

**1. Get your API key**\
Sign up at [https://fal.ai/login](https://fal.ai/login) to obtain your credentials and access the platform.

**2. Install the client library**\
Add the fal.ai client to your project:

```bash theme={null}
npm install --save @fal-ai/client
```

**3. Make your first API call**\
Submit a video generation request with your text prompt:

```javascript theme={null}
import { fal } from "@fal-ai/client";

fal.config({
  credentials: "YOUR_FAL_KEY"
});

const result = await fal.subscribe("fal-ai/bytedance/seedance/v1/pro/fast/text-to-video", {
  input: {
    prompt: "Inside a quiet dojo, a martial artist moves with precision and grace. The performance highlights the beauty and discipline inherent in the ancient practice. Each form unfolds clearly, a testament to dedication and skill."
  },
  logs: true,
  onQueueUpdate: (update) => {
    if (update.status === "IN_PROGRESS") {
      update.logs.map((log) => log.message).forEach(console.log);
    }
  }
});

// Access the generated video
console.log(result.data.video.url);
console.log(result.requestId);
```

For Python developers:

```python theme={null}
from fal_client import FalClient

client = FalClient("YOUR_FAL_KEY")
result = client.subscribe("fal-ai/bytedance/seedance/v1/pro/fast/text-to-video", {
    "prompt": "Inside a quiet dojo, a martial artist moves with precision and grace. The performance highlights the beauty and discipline inherent in the ancient practice. Each form unfolds clearly, a testament to dedication and skill."
})

# Access the generated video
print(result["video"]["url"])
```

## Technical Specifications

**Model Architecture**

* Next-generation text-to-video model optimized for speed and quality balance
* Designed for commercial-scale deployment with reliable performance
* Features wide dynamic range enabling smooth generation of large-scale movements, from subtle expressions to active scenes with high stability and physical realism

**Input Capabilities**

* Text prompt-based video generation
* Default output: 1080p resolution at standard frame rates

**Performance**

* Fast inference optimized for production workflows
* Queue-based processing with status tracking and webhooks
* Scalable infrastructure for handling multiple concurrent requests
* No charges for cold starts or server errors (5xx)

## Best Practices

Achieve optimal results with these proven approaches:

**Craft Detailed, Specific Prompts**\
The quality of your generated video directly correlates with prompt specificity. Instead of generic descriptions like "a person walking," provide rich contextual details: "A young woman in a red coat walks confidently down a rain-slicked city street at dusk, her reflection shimmering in puddles as neon signs illuminate the background." Include information about movement, lighting, atmosphere, and visual style to guide the model toward your creative vision. ByteDance's Seedance technology excels at translating nuanced descriptions into visually coherent sequences.

**Leverage the Queue System for Production Workflows**\
For applications requiring multiple video generations or integration into larger content pipelines, utilize the queue system with webhooks rather than blocking operations. This approach enables you to submit requests asynchronously, track progress through status updates, and retrieve results when ready—essential for building responsive applications that maintain performance under load. Consider implementing webhook endpoints to automatically process completed videos without polling.

**Combine with Other AI Tools for Complete Workflows**\
Maximize creative potential by integrating Seedance into broader AI-powered production pipelines. Start with [AI image generators like Flux](https://fal.ai/models/fal-ai/flux-general/inpainting) to create reference frames, then extend them into video sequences. Add AI-generated music through [CassetteAI](https://fal.ai/models/cassetteai/music-generator) or create talking head videos with [lipsync capabilities](https://fal.ai/models/veed/lipsync) to build complete multimedia experiences that would traditionally require entire production teams.

## Advanced Features

**Webhook Integration for Asynchronous Processing**\
Configure webhook URLs to receive automatic notifications when video generation completes, enabling event-driven architectures and seamless integration with existing systems:

```javascript theme={null}
const { request_id } = await fal.queue.submit("fal-ai/bytedance/seedance/v1/pro/fast/text-to-video", {
  input: {
    prompt: "A serene mountain landscape at sunrise, with mist rolling through valleys"
  },
  webhookUrl: "https://your-domain.com/webhooks/video-complete"
});
```

**Queue Management and Status Tracking**\
Monitor generation progress in real-time and implement sophisticated retry logic for production applications:

```javascript theme={null}
const status = await fal.queue.status("fal-ai/bytedance/seedance/v1/pro/fast/text-to-video", {
  requestId: request_id,
  logs: true
});

// Retrieve result when ready
const result = await fal.queue.result("fal-ai/bytedance/seedance/v1/pro/fast/text-to-video", {
  requestId: request_id
});
```

## API Reference

```typescript theme={null}
interface SeedanceInput {
  prompt: string; // Detailed text description of the video to generate (required)
  webhookUrl?: string; // Optional webhook URL for completion notifications
}

interface SeedanceOutput {
  video: {
    url: string; // URL to the generated video file
    content_type: string; // MIME type of the video (e.g., "video/mp4")
    file_name: string; // Generated filename
    file_size: number; // Size of the video file in bytes
  };
  seed: number; // Random seed used for generation
}
```

## Pricing and Usage

Seedance 1.0 Pro Fast uses token-based pricing calculated by video dimensions and duration. Each 1080p 5-second video costs approximately **$0.245**. For other resolutions, pricing is **$1 per million video tokens**, where:

```
tokens(video) = (height × width × FPS × duration) / 1024
```

**Billing Notes:**

* Server errors (5xx) are not charged
* Client errors (422) are charged
* Cold starts incur no additional costs
* Purchased credits expire in 365 days; free credits expire in 90 days

For enterprise solutions requiring custom volume arrangements, private deployments, or dedicated infrastructure, contact sales for tailored pricing options. Volume discounts are available for high-usage customers.

## Support and Resources

We're here to help you succeed with Seedance 1.0 Pro Fast:

* **Documentation**: Explore comprehensive guides and API references at [https://docs.fal.ai/](https://docs.fal.ai/)
* **Interactive Playground**: Test the model and experiment with different prompts at the [Seedance playground](https://fal.ai/models/fal-ai/bytedance/seedance/v1/pro/fast/text-to-video)
* **Alternative Versions**: Explore the Seedance 1.0 Lite version for different performance characteristics
* **Developer Support**: Access technical assistance and integration guidance through our community channels

Ready to transform text into compelling video content? Sign up now at [https://fal.ai](https://fal.ai) and start creating with Seedance 1.0 Pro Fast.

[Get Started](https://fal.ai/login)

## Related

* [Seedance 1.0 Pro](/model-api-reference/video-generation-api/seedance-1.0-pro) — Video Generation
* [Seedance 1.0 Lite](/model-api-reference/video-generation-api/seedance-1.0-lite) — Video Generation
* [Bytedance](/model-api-reference/video-generation-api/bytedance) — Video Generation

## Limitations

* `aspect_ratio` restricted to: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `auto`
* `resolution` restricted to: `480p`, `720p`, `1080p`
* `num_frames` range: 29 to 289
* Content moderation via safety checker
* `aspect_ratio` restricted to: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
