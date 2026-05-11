> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux Pro V1.1 API

> API reference for Flux Pro V1.1. FLUX1.1 [pro] is an enhanced version of FLUX.1 [pro], improved image generation capabilities, delivering superior composition, detail, and artistic fidelity compared t

<Tabs>
  <Tab title="V1.1">
    **Endpoint:** `POST https://fal.run/fal-ai/flux-pro/v1.1`
    **Endpoint ID:** `fal-ai/flux-pro/v1.1`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-pro/v1.1/playground">
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
          "fal-ai/flux-pro/v1.1",
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

      const result = await fal.subscribe("fal-ai/flux-pro/v1.1", {
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
        --url https://fal.run/fal-ai/flux-pro/v1.1 \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"FLUX\" is painted over it in big, white brush strokes with visible texture."
      }'
      ```
    </CodeGroup>

    ## Examples

    > A close-up artistic photograph of fresh blueberries on a white surface. The surface has a marbled, fluid texture with swirls of white and various shades of blue, creating an abstract, paint-like effect. The blueberries are scattered across the image, some sitting on the white areas and others nestle...

    <Frame>
      <img src="https://fal.media/files/monkey/uc-qNBVx7VwfdOgxRWOTk_f9dccef1336846ebb6e5e9fb54d39102.jpg" alt="Generated image: A close-up artistic photograph of fresh blueberries on a white surface. The surf" />
    </Frame>

    > A visually stunning image of the Turritopsis dohrnii jellyfish floating gracefully in clear water. Include a close-up of its unique, translucent body, showcasing the regeneration process. The background should have a serene underwater environment with soft lighting.

    <Frame>
      <img src="https://fal.media/files/zebra/OSziSU95wFPfP342slckQ_ecbd433f9d034cfeaa9c064f7d207d2f.jpg" alt="Generated image: A visually stunning image of the Turritopsis dohrnii jellyfish floating graceful" />
    </Frame>

    > A cartoon character walking in autumn nature holding a phone and working on his phone
    > In autumn graphic style

    <Frame>
      <img src="https://fal.media/files/monkey/8-SB6BBmYYgYHAMZEj8Ra_6ee9375c0b58433095425d528a2b9f7c.jpg" alt="Generated image: A cartoon character walking in autumn nature holding a phone and working on his " />
    </Frame>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to generate an image from.
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="landscape_4_3">
      The size of the generated image. Default value: `landscape_4_3`

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
    </ParamField>

    <ParamField body="seed" type="integer">
      The same seed and the same prompt given to the same version of the model
      will output the same image every time.
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      The number of images to generate. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`
    </ParamField>

    <ParamField body="safety_tolerance" type="SafetyToleranceEnum" default="2">
      The safety tolerance level for the generated image. 1 being the most strict and 5 being the most permissive. Default value: `"2"`

      Possible values: `1`, `2`, `3`, `4`, `5`, `6`
    </ParamField>

    <ParamField body="enhance_prompt" type="boolean" default="false">
      Whether to enhance the prompt for better results.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<registry__image__fast_sdxl__models__Image>" required>
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
      "sync_mode": false,
      "num_images": 1,
      "output_format": "jpeg",
      "safety_tolerance": "2",
      "enhance_prompt": false
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
    **Endpoint:** `POST https://fal.run/fal-ai/flux-pro/v1.1/redux`
    **Endpoint ID:** `fal-ai/flux-pro/v1.1/redux`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/flux-pro/v1.1/redux/playground">
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
          "fal-ai/flux-pro/v1.1/redux",
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

      const result = await fal.subscribe("fal-ai/flux-pro/v1.1/redux", {
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
        --url https://fal.run/fal-ai/flux-pro/v1.1/redux \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://fal.media/files/kangaroo/acQvq-Kmo2lajkgvcEHdv.png"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" default="">
      The prompt to generate an image from. Default value: `""`
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

    <ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
      The format of the generated image. Default value: `"jpeg"`

      Possible values: `jpeg`, `png`
    </ParamField>

    <ParamField body="safety_tolerance" type="SafetyToleranceEnum" default="2">
      The safety tolerance level for the generated image. 1 being the most strict and 5 being the most permissive. Default value: `"2"`

      Possible values: `1`, `2`, `3`, `4`, `5`, `6`
    </ParamField>

    <ParamField body="enhance_prompt" type="boolean" default="false">
      Whether to enhance the prompt for better results.
    </ParamField>

    <ParamField body="image_url" type="string" required>
      The image URL to generate an image from. Needs to match the dimensions of the mask.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<registry__image__fast_sdxl__models__Image>" required>
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
      "prompt": "",
      "image_size": "landscape_4_3",
      "num_inference_steps": 28,
      "guidance_scale": 3.5,
      "sync_mode": false,
      "num_images": 1,
      "output_format": "jpeg",
      "safety_tolerance": "2",
      "enhance_prompt": false,
      "image_url": "https://fal.media/files/kangaroo/acQvq-Kmo2lajkgvcEHdv.png"
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

## FLUX1.1 \[pro] - Professional Text-to-Image Generation

Transform your text descriptions into stunning, high-quality images with FLUX1.1 \[pro], an enhanced version of FLUX.1 \[pro] with improved image generation capabilities, delivering superior composition, detail, and artistic fidelity compared to its predecessor.

### Overview

FLUX1.1 \[pro] generates professional-grade images from text descriptions with enhanced performance and speed. Built on a 12 billion parameter flow transformer architecture, it delivers exceptional quality while maintaining rapid generation speeds and superior prompt adherence.

#### Key Capabilities

* **Enhanced image generation** with superior composition and detail
* **Improved prompt adherence** and output diversity
* **Six times faster** than the original FLUX.1 \[pro]
* **Highest Elo score** on Artificial Analysis image arena
* **Commercial-ready image quality** with artistic fidelity
* **Professional-grade performance** optimized for production use

### Getting Started

Getting up and running with FLUX1.1 \[pro] takes just a few minutes. Here's how to begin:

1. Get your API key at [https://fal.ai/login](https://fal.ai/login)
2. Install the client library for your preferred language
3. Make your first API call

#### JavaScript/TypeScript Installation:

```bash theme={null}
npm install --save @fal-ai/client
```

#### Python Installation:

```bash theme={null}
pip install fal-client
```

### Simple Integration Example

Here's a basic example of generating an image using TypeScript:

```typescript theme={null}
import { fal } from "@fal-ai/client";

fal.config({
  credentials: "YOUR_FAL_KEY"
});

const result = await fal.subscribe("fal-ai/flux-pro/v1.1", {
  input: {
    prompt: "A serene mountain landscape at sunset, photorealistic style"
  }
});
```

### Advanced Features

FLUX1.1 \[pro] offers sophisticated controls for professional use cases:

#### Enhanced Performance

Six times faster generation than its predecessor while maintaining superior image quality and better prompt adherence.

#### Superior Composition

Delivers improved artistic fidelity with enhanced detail rendering and composition quality compared to previous versions.

#### Prompt Adherence

Excels at accurately interpreting and generating images based on complex prompts and specific requirements, making it highly versatile for various creative needs.

#### Output Diversity

Increased variety and creativity in generated outputs while maintaining consistency and quality.

### Best Practices

Maximize your results with these proven approaches:

#### Image Quality

Use detailed, specific prompts that describe both content and style. The enhanced prompt adherence means more precise descriptions yield better results.

#### Performance Optimization

Take advantage of the improved speed while maintaining high quality output. The model balances efficiency with superior visual fidelity.

#### Production Implementation

Implement proper error handling and retry logic for robust production deployments. The model's enhanced reliability makes it ideal for enterprise use.

### Technical Specifications

#### Model Architecture

* 12 billion parameter flow transformer
* Enhanced version of FLUX.1 \[pro]
* Hybrid architecture with multimodal and parallel diffusion transformer blocks
* Flow matching methodology with rotary positional embeddings

#### Performance Metrics

* **Speed**: 6x faster than original FLUX.1 \[pro]
* **Quality**: Superior composition, detail, and artistic fidelity
* **Benchmark**: Highest overall Elo score on Artificial Analysis arena
* **Commercial usage**: Approved for professional and commercial use

#### Codename "Blueberry"

FLUX1.1 \[pro] was tested under the codename "blueberry" and achieved the highest overall Elo score among all image models on the Artificial Analysis image arena, surpassing competing models in visual quality and prompt accuracy.

### API Reference

The FLUX1.1 \[pro] API accepts standard text-to-image parameters:

```typescript theme={null}
interface FluxProParameters {
  prompt: string;              // Your detailed text description
  width?: number;             // Output image width
  height?: number;            // Output image height
  num_inference_steps?: number; // Generation steps
  guidance_scale?: number;     // Prompt adherence strength
  seed?: number;              // For reproducible results
}
```

### Pricing and Usage

Your request will cost \$0.04 per megapixel. Images are billed by rounding up to the nearest megapixel. Our transparent, usage-based pricing offers excellent value:

* **Competitive pricing**: \$0.04 per megapixel
* **Commercial usage rights** included
* **No hidden fees** or minimum commitments
* **Enterprise-grade reliability** with cost-effective scaling

[View detailed pricing](https://fal.ai/pricing) or [contact sales](mailto:support@fal.ai) for enterprise solutions.

### Support and Resources

Additional resources to help you succeed:

#### Documentation

Complete API documentation available at [https://docs.fal.ai/](https://docs.fal.ai/)

#### Community

Join our active developer community for support and inspiration

#### Enterprise Support

Dedicated support channels for enterprise customers

Ready to transform your text into stunning images with the most advanced FLUX model available? Sign up now at [https://fal.ai](https://fal.ai) and start creating with FLUX1.1 \[pro].

[Get Started with FLUX1.1 Pro](https://fal.ai/login)

## Related

* [FLUX1.1 \[pro\] ultra](/model-api-reference/image-generation-api/flux1.1-ultra) — Image Generation
* [FLUX.1 \[pro\] Fill](/model-api-reference/image-generation-api/flux.1-fill) — Image Generation
* [FLUX1.1 \[pro\] Redux](/model-api-reference/image-generation-api/flux1.1-redux) — Image Generation
* [FLUX1.1 \[pro\] ultra Redux](/model-api-reference/image-generation-api/flux1.1-ultra-redux) — Image Generation
* [FLUX1.1 \[pro\] ultra Fine-tuned](/model-api-reference/image-generation-api/flux1.1-ultra-fine-tuned) — Image Generation
* [FLUX.1 \[pro\] Fill Fine-tuned](/model-api-reference/image-generation-api/flux.1-fill-fine-tuned) — Image Generation
* [FLUX1.1 \[pro\]](/model-api-reference/image-generation-api/flux1.1) — Image Generation

## Limitations

* `image_size` restricted to: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`
* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`, `6`
* `num_inference_steps` range: 1 to 50
* `guidance_scale` range: 1 to 20
