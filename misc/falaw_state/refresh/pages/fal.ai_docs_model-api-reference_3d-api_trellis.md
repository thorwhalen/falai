> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Trellis API

> API reference for Trellis. Generate 3D models from your images using Trellis. A native 3D generative model enabling versatile and high-quality 3D asset creation.

<Tabs>
  <Tab title="Trellis">
    **Endpoint:** `POST https://fal.run/fal-ai/trellis`
    **Endpoint ID:** `fal-ai/trellis`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/trellis/playground">
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
          "fal-ai/trellis",
          arguments={
              "image_url": "https://storage.googleapis.com/falserverless/web-examples/rodin3d/warriorwoman.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/trellis", {
        input: {
            image_url: "https://storage.googleapis.com/falserverless/web-examples/rodin3d/warriorwoman.png"
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
        --url https://fal.run/fal-ai/trellis \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://storage.googleapis.com/falserverless/web-examples/rodin3d/warriorwoman.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      URL of the input image to convert to 3D
    </ParamField>

    <ParamField body="seed" type="integer">
      Random seed for reproducibility
    </ParamField>

    <ParamField body="ss_guidance_strength" type="float" default="7.5">
      Guidance strength for sparse structure generation Default value: `7.5`

      Range: `0` to `10`
    </ParamField>

    <ParamField body="ss_sampling_steps" type="integer" default="12">
      Sampling steps for sparse structure generation Default value: `12`

      Range: `1` to `50`
    </ParamField>

    <ParamField body="slat_guidance_strength" type="float" default="3">
      Guidance strength for structured latent generation Default value: `3`

      Range: `0` to `10`
    </ParamField>

    <ParamField body="slat_sampling_steps" type="integer" default="12">
      Sampling steps for structured latent generation Default value: `12`

      Range: `1` to `50`
    </ParamField>

    <ParamField body="mesh_simplify" type="float" default="0.95">
      Mesh simplification factor Default value: `0.95`

      Range: `0.9` to `0.98`
    </ParamField>

    <ParamField body="texture_size" type="TextureSizeEnum" default="1024">
      Texture resolution Default value: `"1024"`

      Possible values: `512`, `1024`, `2048`
    </ParamField>

    ### Output Schema

    <ParamField body="model_mesh" type="File" required>
      Generated 3D mesh file
    </ParamField>

    <ParamField body="timings" type="Timings" required>
      Processing timings
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://storage.googleapis.com/falserverless/web-examples/rodin3d/warriorwoman.png",
      "ss_guidance_strength": 7.5,
      "ss_sampling_steps": 12,
      "slat_guidance_strength": 3,
      "slat_sampling_steps": 12,
      "mesh_simplify": 0.95,
      "texture_size": 1024
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "model_mesh": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019
      }
    }
    ```
  </Tab>

  <Tab title="Multi">
    **Endpoint:** `POST https://fal.run/fal-ai/trellis/multi`
    **Endpoint ID:** `fal-ai/trellis/multi`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/trellis/multi/playground">
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
          "fal-ai/trellis/multi",
          arguments={
              "image_urls": [
                  "https://storage.googleapis.com/falserverless/model_tests/video_models/front.png",
                  "https://storage.googleapis.com/falserverless/model_tests/video_models/back.png",
                  "https://storage.googleapis.com/falserverless/model_tests/video_models/left.png"
              ]
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/trellis/multi", {
        input: {
            image_urls: [
              "https://storage.googleapis.com/falserverless/model_tests/video_models/front.png",
              "https://storage.googleapis.com/falserverless/model_tests/video_models/back.png",
              "https://storage.googleapis.com/falserverless/model_tests/video_models/left.png"
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
        --url https://fal.run/fal-ai/trellis/multi \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_urls": [
          "https://storage.googleapis.com/falserverless/model_tests/video_models/front.png",
          "https://storage.googleapis.com/falserverless/model_tests/video_models/back.png",
          "https://storage.googleapis.com/falserverless/model_tests/video_models/left.png"
        ]
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_urls" type="list<string>" required>
      List of URLs of input images to convert to 3D
    </ParamField>

    <ParamField body="seed" type="integer">
      Random seed for reproducibility
    </ParamField>

    <ParamField body="ss_guidance_strength" type="float" default="7.5">
      Guidance strength for sparse structure generation Default value: `7.5`

      Range: `0` to `10`
    </ParamField>

    <ParamField body="ss_sampling_steps" type="integer" default="12">
      Sampling steps for sparse structure generation Default value: `12`

      Range: `1` to `50`
    </ParamField>

    <ParamField body="slat_guidance_strength" type="float" default="3">
      Guidance strength for structured latent generation Default value: `3`

      Range: `0` to `10`
    </ParamField>

    <ParamField body="slat_sampling_steps" type="integer" default="12">
      Sampling steps for structured latent generation Default value: `12`

      Range: `1` to `50`
    </ParamField>

    <ParamField body="mesh_simplify" type="float" default="0.95">
      Mesh simplification factor Default value: `0.95`

      Range: `0.9` to `0.98`
    </ParamField>

    <ParamField body="texture_size" type="TextureSizeEnum" default="1024">
      Texture resolution Default value: `"1024"`

      Possible values: `512`, `1024`, `2048`
    </ParamField>

    <ParamField body="multiimage_algo" type="MultiimageAlgoEnum" default="stochastic">
      Algorithm for multi-image generation Default value: `"stochastic"`

      Possible values: `stochastic`, `multidiffusion`
    </ParamField>

    ### Output Schema

    <ParamField body="model_mesh" type="File" required>
      Generated 3D mesh file
    </ParamField>

    <ParamField body="timings" type="Timings" required>
      Processing timings
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_urls": [
        "https://storage.googleapis.com/falserverless/model_tests/video_models/front.png",
        "https://storage.googleapis.com/falserverless/model_tests/video_models/back.png",
        "https://storage.googleapis.com/falserverless/model_tests/video_models/left.png"
      ],
      "ss_guidance_strength": 7.5,
      "ss_sampling_steps": 12,
      "slat_guidance_strength": 3,
      "slat_sampling_steps": 12,
      "mesh_simplify": 0.95,
      "texture_size": 1024,
      "multiimage_algo": "stochastic"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "model_mesh": {
        "url": "",
        "content_type": "image/png",
        "file_name": "z9RV14K95DvU.png",
        "file_size": 4404019
      }
    }
    ```
  </Tab>
</Tabs>

## Trellis - Advanced AI Model for 3D Generation

Transform your creative workflows with Trellis, a powerful AI model designed for reliable, high-quality 3D asset generation from images. Built for developers who need production-ready 3D models with minimal complexity.

### Overview

Trellis provides a streamlined API for generating 3D models from images, utilizing a native 3D generative model based on Structured LATents (SLAT) representation. Whether you're building creative tools, content generation systems, or enhancing existing applications, Trellis delivers consistent, high-quality 3D assets with simple integration.

### Getting Started

Setting up Trellis takes just a few minutes. Choose your preferred SDK:

For JavaScript/TypeScript projects:

```bash theme={null}
npm install --save @fal-ai/client
```

For Python applications:

```bash theme={null}
pip install fal-client
```

Configure your authentication:

JavaScript:

```javascript theme={null}
import { fal } from "@fal-ai/client";

fal.config({
  credentials: "YOUR_FAL_KEY_HERE"
});
```

Python:

```python theme={null}
import fal_client
import os

os.environ["FAL_KEY"] = "YOUR_FAL_KEY_HERE"
```

### Basic Usage

Generate your first 3D model with just a few lines of code:

JavaScript:

```javascript theme={null}
const result = await fal.subscribe("fal-ai/trellis", {
  input: {
    image_url: "https://example.com/your-image.jpg"
  }
});
```

Python:

```python theme={null}
result = fal_client.subscribe("fal-ai/trellis", {
    "image_url": "https://example.com/your-image.jpg"
})
```

### Advanced Features

Trellis supports advanced configuration options to fine-tune your results:

**3D Output Formats**

* Generate multiple 3D representations (Radiance Fields, 3D Gaussians, meshes)
* Export to GLB format for universal compatibility
* Maintain high detail in both geometry and texture

**Quality Control**

* Intricate shape and texture detail preservation
* Flexible output format selection
* Support for local 3D editing capabilities

### API Parameters

**Input Parameters:**

* `image_url` (required): URL of the input image
* Additional configuration options available for advanced use cases

**Output:**

* 3D model in multiple formats
* GLB file export capability
* High-quality mesh and texture data

### Best Practices

Maximize your success with Trellis by following these guidelines:

**Error Handling**

```javascript theme={null}
try {
  const result = await fal.subscribe("fal-ai/trellis", {
    input: { image_url: "your-image-url" }
  });
} catch (error) {
  console.error("Generation failed:", error.message);
}
```

**Image Requirements**

* Use clear, well-lit images with distinct subjects
* Supported formats: JPG, JPEG, PNG, WebP, GIF, AVIF
* Best results with images showing full object visibility

### Technical Specifications

**Model Architecture:**

* Based on Structured LATents (SLAT) representation
* Powered by Rectified Flow Transformers
* Up to 2 billion parameters
* Trained on 500K diverse 3D objects

**Performance Metrics:**

* Fast 3D generation from single images
* High-quality output with intricate details
* Multiple output format support

### File Upload Support

Upload local images using the file storage API:

```javascript theme={null}
import { fal } from "@fal-ai/client";

const file = new File([imageData], "image.jpg", { type: "image/jpeg" });
const url = await fal.storage.upload(file);

const result = await fal.subscribe("fal-ai/trellis", {
  input: {
    image_url: url
  }
});
```

### Queue-Based Processing

For asynchronous workflows:

```javascript theme={null}
// Submit request
const { request_id } = await fal.queue.submit("fal-ai/trellis", {
  input: {
    image_url: "your-image-url"
  },
  webhookUrl: "https://optional.webhook.url/for/results"
});

// Check status
const status = await fal.queue.status("fal-ai/trellis", {
  requestId: request_id,
  logs: true
});

// Get result
const result = await fal.queue.result("fal-ai/trellis", {
  requestId: request_id
});
```

### Integration Support

Our documentation includes complete reference implementations for:

* React/Next.js applications
* Python backend services
* Node.js environments
* REST API clients

### Use Cases

**3D Asset Creation**

* Game development assets
* Product visualization
* Digital art and design
* AR/VR content creation

**Professional Applications**

* E-commerce product models
* Architecture visualization
* Educational content
* Creative prototyping

### Pricing and Usage

* **Cost**: \$0.02 per unit
* Transparent, usage-based pricing
* No subscription necessary
* No hidden fees or minimum commitments

[View detailed pricing](https://fal.ai/pricing) or [contact sales](mailto:support@fal.ai) for enterprise solutions.

### Support and Resources

Access comprehensive support through multiple channels:

**Documentation**

* [API Reference](https://fal.ai/models/fal-ai/trellis/api)
* [General fal.ai Documentation](https://docs.fal.ai/)
* Code examples and tutorials

**Community Support**

* Active developer community
* Regular updates and improvements
* Direct technical support

Get started with Trellis today and experience the next generation of AI-powered 3D asset generation. Sign up for an API key at [fal.ai](https://fal.ai/login).

## Related

* [Trellis](/model-api-reference/3d-api/trellis) — 3D

## Limitations

* `ss_guidance_strength` range: 0 to 10
* `ss_sampling_steps` range: 1 to 50
* `slat_guidance_strength` range: 0 to 10
* `slat_sampling_steps` range: 1 to 50
* `mesh_simplify` range: 0.9 to 0.98
* `texture_size` restricted to: `512`, `1024`, `2048`
* `multiimage_algo` restricted to: `stochastic`, `multidiffusion`
