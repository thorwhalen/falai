> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux Dev API

> API reference for Flux Dev. FLUX.1 [dev] is a 12 billion parameter flow transformer that generates high-quality images from text. It is suitable for personal and commercial use.

<Tabs>
  <Tab title="Dev">
    **Endpoint:** `POST https://fal.run/fal-ai/flux/dev`
    **Endpoint ID:** `fal-ai/flux/dev`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux/dev/playground">
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
          "fal-ai/flux/dev",
          arguments={
              "prompt": "Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"FLUX\" is painted over it in big, white brush strokes with visible texture."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/flux/dev", {
        input: {
            prompt: "Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"FLUX\" is painted over it in big, white brush strokes with visible texture."
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
        --url https://fal.run/fal-ai/flux/dev \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"FLUX\" is painted over it in big, white brush strokes with visible texture."
      }'
      ```
    </CodeGroup>

    ## Examples

    > portrait | wide angle shot of eyes off to one side of frame, lucid dream-like woman, looking off in distance ::8 style | daydreampunk with glowing skin and eyes, styled in headdress, beautiful, she is dripping in neon lights, very colorful blue, green, purple, bioluminescent, glowing ::8 background ...

    <Frame>
      <img src="https://v3.fal.media/files/koala/WF1Q_8cKxy7yC252zR59b.png" alt="Generated image: portrait | wide angle shot of eyes off to one side of frame, lucid dream-like wo" />
    </Frame>

    > a girl walking through a field, in the style of ethereal trees, dark yellow and azure, majestic, sweeping seascapes, photorealistic representation, graceful balance, wimmelbilder, orange

    <Frame>
      <img src="https://v3.fal.media/files/tiger/s99noBJtji7y3u1V60Dj6.png" alt="Generated image: a girl walking through a field, in the style of ethereal trees, dark yellow and " />
    </Frame>

    > Microscopic photograph of mites caught in a drop of water, green colored sparks raining from above across a gradient background, brightly shining sparks, emitting green light, shallow depth of field volumetric lighting, cinematic, intricate detail, ultra-realistic

    <Frame>
      <img src="https://v3.fal.media/files/kangaroo/0VRJN1EFfcyen5Bjf_gCs.png" alt="Generated image: Microscopic photograph of mites caught in a drop of water, green colored sparks " />
    </Frame>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to generate an image from.
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="landscape_4_3">
      The size of the generated image. Default value: `landscape_4_3`

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
    </ParamField>

    <ParamField body="num_inference_steps" type="integer" default="28">
      The number of inference steps to perform. Default value: `28`

      Range: `1` to `50`
    </ParamField>

    <ParamField body="seed" type="integer">
      The same seed and the same prompt given to the same version of the model
      will output the same image every time.
    </ParamField>

    <ParamField body="guidance_scale" type="float" default="3.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `3.5`

      Range: `1` to `20`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      The number of images to generate. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`
    </ParamField>

    <ParamField body="acceleration" type="AccelerationEnum" default="none">
      The speed of the generation. The higher the speed, the faster the generation. Default value: `"none"`

      Possible values: `none`, `regular`, `high`
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
      The generated image files info.
    </ParamField>

    <ParamField body="timings" type="Timings" required />

    <ParamField body="seed" type="integer" required>
      Seed of the generated Image. It will be the same value of the one passed in the
      input or the randomly generated that was used in case none was passed.
    </ParamField>

    <ParamField body="has_nsfw_concepts" type="list<boolean>" required>
      Whether the generated images contain NSFW concepts.
    </ParamField>

    <ParamField body="prompt" type="string" required>
      The prompt used for generating the image.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"FLUX\" is painted over it in big, white brush strokes with visible texture.",
      "image_size": "landscape_4_3",
      "num_inference_steps": 28,
      "guidance_scale": 3.5,
      "sync_mode": false,
      "num_images": 1,
      "enable_safety_checker": true,
      "output_format": "jpeg",
      "acceleration": "none"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "",
          "content_type": "image/jpeg"
        }
      ],
      "prompt": ""
    }
    ```
  </Tab>

  <Tab title="Image To Image">
    **Endpoint:** `POST https://fal.run/fal-ai/flux/dev/image-to-image`
    **Endpoint ID:** `fal-ai/flux/dev/image-to-image`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux/dev/image-to-image/playground">
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
          "fal-ai/flux/dev/image-to-image",
          arguments={
              "image_url": "https://fal.media/files/koala/Chls9L2ZnvuipUTEwlnJC.png",
              "prompt": "A cat dressed as a wizard with a background of a mystic forest."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/flux/dev/image-to-image", {
        input: {
            image_url: "https://fal.media/files/koala/Chls9L2ZnvuipUTEwlnJC.png",
            prompt: "A cat dressed as a wizard with a background of a mystic forest."
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
        --url https://fal.run/fal-ai/flux/dev/image-to-image \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://fal.media/files/koala/Chls9L2ZnvuipUTEwlnJC.png",
        "prompt": "A cat dressed as a wizard with a background of a mystic forest."
      }'
      ```
    </CodeGroup>

    ## Examples

    > a cat dressed as a wizard with a background of a mystic forest.

    <Frame>
      <img src="https://fal.media/files/tiger/n97jyGIpam7ZY5x8dpfZt.png" alt="Generated image: a cat dressed as a wizard with a background of a mystic forest." />
    </Frame>

    > woman, in cyberpunk city, purple, green, neon

    <Frame>
      <img src="https://fal.media/files/zebra/4ylIRCvHJDiD_hPLsoRIc.png" alt="Generated image: woman, in cyberpunk city, purple, green, neon" />
    </Frame>

    > cartoon tiger, anime style

    <Frame>
      <img src="https://fal.media/files/monkey/qxTAEasn1R3kJyEKlzqzi.png" alt="Generated image: cartoon tiger, anime style" />
    </Frame>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The URL of the image to generate an image from.
    </ParamField>

    <ParamField body="strength" type="float" default="0.95">
      The strength of the initial image. Higher strength values are better for this model. Default value: `0.95`

      Range: `0.01` to `1`
    </ParamField>

    <ParamField body="num_inference_steps" type="integer" default="40">
      The number of inference steps to perform. Default value: `40`

      Range: `10` to `50`
    </ParamField>

    <ParamField body="prompt" type="string" required>
      The prompt to generate an image from.
    </ParamField>

    <ParamField body="seed" type="integer">
      The same seed and the same prompt given to the same version of the model
      will output the same image every time.
    </ParamField>

    <ParamField body="guidance_scale" type="float" default="3.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `3.5`

      Range: `1` to `20`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      The number of images to generate. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`
    </ParamField>

    <ParamField body="acceleration" type="AccelerationEnum" default="none">
      The speed of the generation. The higher the speed, the faster the generation. Default value: `"none"`

      Possible values: `none`, `regular`, `high`
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
      The generated image files info.
    </ParamField>

    <ParamField body="timings" type="Timings" required />

    <ParamField body="seed" type="integer" required>
      Seed of the generated Image. It will be the same value of the one passed in the
      input or the randomly generated that was used in case none was passed.
    </ParamField>

    <ParamField body="has_nsfw_concepts" type="list<boolean>" required>
      Whether the generated images contain NSFW concepts.
    </ParamField>

    <ParamField body="prompt" type="string" required>
      The prompt used for generating the image.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://fal.media/files/koala/Chls9L2ZnvuipUTEwlnJC.png",
      "strength": 0.95,
      "num_inference_steps": 40,
      "prompt": "A cat dressed as a wizard with a background of a mystic forest.",
      "guidance_scale": 3.5,
      "sync_mode": false,
      "num_images": 1,
      "enable_safety_checker": true,
      "output_format": "jpeg",
      "acceleration": "none"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "",
          "content_type": "image/jpeg"
        }
      ],
      "prompt": ""
    }
    ```
  </Tab>

  <Tab title="Redux">
    **Endpoint:** `POST https://fal.run/fal-ai/flux/dev/redux`
    **Endpoint ID:** `fal-ai/flux/dev/redux`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux/dev/redux/playground">
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
          "fal-ai/flux/dev/redux",
          arguments={
              "image_url": "https://fal.media/files/kangaroo/acQvq-Kmo2lajkgvcEHdv.png"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/flux/dev/redux", {
        input: {
            image_url: "https://fal.media/files/kangaroo/acQvq-Kmo2lajkgvcEHdv.png"
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
        --url https://fal.run/fal-ai/flux/dev/redux \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://fal.media/files/kangaroo/acQvq-Kmo2lajkgvcEHdv.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The URL of the image to generate an image from.
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="landscape_4_3">
      The size of the generated image. Default value: `landscape_4_3`

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
    </ParamField>

    <ParamField body="num_inference_steps" type="integer" default="28">
      The number of inference steps to perform. Default value: `28`

      Range: `1` to `50`
    </ParamField>

    <ParamField body="seed" type="integer">
      The same seed and the same prompt given to the same version of the model
      will output the same image every time.
    </ParamField>

    <ParamField body="guidance_scale" type="float" default="3.5">
      The CFG (Classifier Free Guidance) scale is a measure of how close you want
      the model to stick to your prompt when looking for a related image to show you. Default value: `3.5`

      Range: `1` to `20`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      The number of images to generate. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`
    </ParamField>

    <ParamField body="acceleration" type="AccelerationEnum" default="none">
      The speed of the generation. The higher the speed, the faster the generation. Default value: `"none"`

      Possible values: `none`, `regular`, `high`
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
      The generated image files info.
    </ParamField>

    <ParamField body="timings" type="Timings" required />

    <ParamField body="seed" type="integer" required>
      Seed of the generated Image. It will be the same value of the one passed in the
      input or the randomly generated that was used in case none was passed.
    </ParamField>

    <ParamField body="has_nsfw_concepts" type="list<boolean>" required>
      Whether the generated images contain NSFW concepts.
    </ParamField>

    <ParamField body="prompt" type="string" required>
      The prompt used for generating the image.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://fal.media/files/kangaroo/acQvq-Kmo2lajkgvcEHdv.png",
      "image_size": "landscape_4_3",
      "num_inference_steps": 28,
      "guidance_scale": 3.5,
      "sync_mode": false,
      "num_images": 1,
      "enable_safety_checker": true,
      "output_format": "jpeg",
      "acceleration": "none"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "",
          "content_type": "image/jpeg"
        }
      ],
      "prompt": ""
    }
    ```
  </Tab>
</Tabs>

## FLUX.1 \[dev] - High-Performance Image Generation API

Transform your creative vision into stunning images with FLUX.1 \[dev], a state-of-the-art text-to-image generation model powered by a 12 billion parameter flow transformer. Built for both speed and quality, FLUX.1 \[dev] delivers professional-grade results suitable for personal and commercial use.

### Key Benefits

Create production-ready images faster and with greater control. FLUX.1 \[dev] enables you to:

* Generate high-fidelity images from natural language descriptions
* Achieve consistent results across multiple generations
* Scale from prototype to production with enterprise-grade reliability
* Access both personal and commercial licensing options
* Deploy anywhere with flexible API integration
* Use streaming capabilities for real-time generation

### Popular Use Cases

**Content Creation**
Generate marketing visuals, social media assets, and blog illustrations at scale. Perfect for agencies and content teams who need consistent, high-quality imagery.

**Product Development**\
Create concept art, UI mockups, and design variations for rapid prototyping. Ideal for designers exploring visual directions.

**E-commerce**
Generate product lifestyle images, seasonal campaigns, and A/B testing visuals to boost conversion rates.

**Entertainment**
Produce game assets, storyboard illustrations, and creative concept art for media projects.

### Technical Overview

FLUX.1 \[dev] is built on advanced flow transformer architecture that enables:

* **Performance**: 12B parameters optimized for rapid inference
* **Flexibility**: Support for multiple generation approaches including streaming
* **Quality**: Enhanced image coherence and composition
* **Licensing**: Suitable for both personal and commercial use

### Getting Started

Getting up and running with FLUX.1 \[dev] is straightforward. Here's how to begin:

1. Get your API key at [https://fal.ai/login](https://fal.ai/login)
2. Install the client library:

```bash theme={null}
# For JavaScript/TypeScript
npm install --save @fal-ai/client

# For Python
pip install fal-client
```

3. Make your first API call:

```javascript theme={null}
import { fal } from "@fal-ai/client";

const result = await fal.subscribe("fal-ai/flux/dev", {
  input: {
    prompt: "A serene mountain landscape at sunset, photorealistic style"
  }
});
```

### Streaming Support

FLUX.1 \[dev] supports streaming requests for real-time generation:

```javascript theme={null}
import { fal } from "@fal-ai/client";

const stream = await fal.stream("fal-ai/flux/dev", {
  input: {
    prompt: "Your detailed prompt here"
  }
});

for await (const event of stream) {
  console.log(event);
}

const result = await stream.done();
```

### Best Practices

For optimal results when using FLUX.1 \[dev]:

* Keep prompts clear and specific while maintaining natural language
* Start with default parameters and adjust based on results
* Consider using negative prompts to refine unwanted elements
* Monitor usage for cost-effective scaling
* Take advantage of streaming for interactive applications

### Advanced Features

#### Image Style Control

Fine-tune the artistic direction of your generations through comprehensive style parameters. Adjust attributes like composition, lighting, and artistic influence while maintaining consistent quality.

#### API Parameters

The model supports various configuration options:

* **CFG Scale**: Control prompt adherence (default: 3.5)
* **Safety Checker**: Enable content safety filtering
* **Output Format**: Choose between PNG and other formats
* **Number of Images**: Generate multiple variations
* **Speed Settings**: Optimize for generation speed

#### Batch Processing

Generate multiple variations efficiently with built-in batching support. Perfect for creating asset collections or exploring creative variations.

### Integration Support

Our comprehensive SDK support makes integration seamless across your technology stack:

* REST API for platform-agnostic integration
* Native SDKs for Python and JavaScript/TypeScript
* Streaming capabilities for real-time applications
* Detailed documentation and code examples
* Enterprise support options available

### Pricing and Usage

Your request will cost \$0.025 per megapixel. Images are billed by rounding up to the nearest megapixel. Our transparent, usage-based pricing scales with your needs:

* **Cost-effective**: \$0.025 per megapixel
* **Commercial usage rights** included
* **No subscription fees** or minimum commitments
* **Transparent billing** with clear pricing structure

[View detailed pricing](https://fal.ai/pricing) or [contact sales](mailto:support@fal.ai) for enterprise solutions.

### Licensing

FLUX.1 \[dev] is suitable for both personal and commercial use through fal.ai's platform. The model provides flexible licensing options that support various use cases from individual projects to enterprise deployments.

### Migration Guide

Moving from other platforms? Our migration tools and documentation help ensure a smooth transition to FLUX.1 \[dev]. Contact our support team for personalized migration assistance and best practices.

### Getting Help

We're here to support your success with FLUX.1 \[dev]:

* **Documentation**: Comprehensive guides at [https://docs.fal.ai](https://docs.fal.ai)
* **Support**: Technical assistance via [support@fal.ai](mailto:support@fal.ai)
* **Community**: Join our Discord for tips and discussions
* **Updates**: Regular model improvements and feature additions

Ready to transform your creative vision into reality? Get started at [https://fal.ai/models/fal-ai/flux/dev](https://fal.ai/models/fal-ai/flux/dev).

## Related

* [FLUX.1 \[schnell\]](/model-api-reference/image-generation-api/flux.1) — Image Generation
* [FLUX.1 \[dev\] Redux](/model-api-reference/image-generation-api/flux.1-redux) — Image Generation

## Limitations

* `image_size` restricted to: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
* `num_inference_steps` range: 1 to 50
* `guidance_scale` range: 1 to 20
* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`
* `acceleration` restricted to: `none`, `regular`, `high`
* Content moderation via safety checker
* `strength` range: 0.01 to 1
* `num_inference_steps` range: 10 to 50
