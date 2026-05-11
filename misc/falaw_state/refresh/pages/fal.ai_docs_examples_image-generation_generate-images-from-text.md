> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate Images from Text Tutorial

## How to Generate Images using the fal API

To generate images using the fal API, you need to send a request to the appropriate endpoint with the desired input parameters. The API uses pre-trained models to generate images based on the provided text prompt. This allows you to create images by simply describing what you want in natural language.

Here’s an example of how to generate an image using the fal API from text:

```js theme={null}
import { fal } from "@fal-ai/client";

const result = await fal.subscribe("fal-ai/flux/dev", {
  input: {
    prompt: "a face of a cute puppy, in the style of pixar animation",
  },
});
```

## How to select the model to use

fal offers a variety of image generation models. You can select the model that best fits your needs based on the style and quality of the images you want to generate. Here are some of the available models:

* [fal-ai/flux/dev](https://fal.ai/models/fal-ai/flux/dev): FLUX.1 \[dev] is a 12 billion parameter flow transformer that generates high-quality images from text. It is suitable for personal and commercial use.
* [fal-ai/recraft-v3](https://fal.ai/models/fal-ai/recraft-v3): Recraft V3 is a text-to-image model with the ability to generate long texts, vector art, images in brand style, and much more. As of today, it is SOTA in image generation, proven by Hugging Face’s industry-leading Text-to-Image Benchmark by Artificial Analysis.
* [fal-ai/stable-diffusion-v35-large](https://fal.ai/models/fal-ai/stable-diffusion-v35-large): Stable Diffusion 3.5 Large is a Multimodal Diffusion Transformer (MMDiT) text-to-image model that features improved performance in image quality, typography, complex prompt understanding, and resource-efficiency.

To select a model, simply specify the model ID in the subscribe method as shown in the example above. You can find more models and their descriptions in the [Text to Image Models](https://fal.ai/models?categories=text-to-image) page.
