> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Generation API

> Image Generation API reference. Generate and edit images using state-of-the-art diffusion and transformer models.

## Overview

Generate and edit images using state-of-the-art diffusion and transformer models. fal.ai offers a wide range of models for text-to-image generation, image-to-image editing, style transfer, and context-aware transformations — optimized for different use cases from fast prototyping to production-quality output.

## Top Models

<CardGroup cols={2}>
  <Card title="Nano Banana 2 API" href="/model-api-reference/image-generation-api/nano-banana-2">
    Nano Banana 2 is Google's new state-of-the-art fast image generation and editing model

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a900b9e/ptbZcVWIQ_fXGGHfv8Zez_0ea5ca41bdf143a29e21e30a53120672.jpg" alt="Example output from Nano Banana 2" noZoom />
    </Frame>
  </Card>

  <Card title="Nano Banana Pro API" href="/model-api-reference/image-generation-api/nano-banana-pro">
    Nano Banana Pro is Google's new state-of-the-art image generation and editing model

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a8691ce/SR0_u1zPJbx8jCIO6bJR0_8c83f0d66bbd48f3b55f825117941f84.jpg" alt="Example output from Nano Banana Pro" noZoom />
    </Frame>
  </Card>

  <Card title="Flux 2 Pro API" href="/model-api-reference/image-generation-api/flux-2-pro">
    Image editing with FLUX.2 \[pro] from Black Forest Labs. Ideal for high-quality image manipulation, style transfer, and sequential editing workflows

    <Frame>
      <img src="https://v3b.fal.media/files/b/penguin/UfryXXm9my6IM8HsoP9FL_054c2c2953dc491996904114c6e04836.jpg" alt="Example output from Flux 2 Pro" noZoom />
    </Frame>
  </Card>

  <Card title="FLUX1.1 [pro] ultra API" href="/model-api-reference/image-generation-api/flux-pro-v1.1-ultra">
    FLUX1.1 \[pro] ultra is the newest version of FLUX1.1 \[pro], maintaining professional-grade image quality while delivering up to 2K resolution with improved photo realism.

    <Frame>
      <img src="https://storage.googleapis.com/falserverless/gallery/flux-pro-v1-1-ultra.webp" alt="Example output from FLUX1.1 [pro] ultra" noZoom />
    </Frame>
  </Card>

  <Card title="FLUX.1 [dev] API" href="/model-api-reference/image-generation-api/flux-dev">
    FLUX.1 \[dev] is a 12 billion parameter flow transformer that generates high-quality images from text. It is suitable for personal and commercial use.

    <Frame>
      <img src="https://storage.googleapis.com/fal_cdn/fal/Upscale-1.jpeg" alt="Example output from FLUX.1 [dev]" noZoom />
    </Frame>
  </Card>

  <Card title="FLUX.1 [dev] with LoRAs API" href="/model-api-reference/image-generation-api/flux-lora">
    Super fast endpoint for the FLUX.1 \[dev] model with LoRA support, enabling rapid and high-quality image generation using pre-trained LoRA adaptations for personalization, specific styles, brand identi

    <Frame>
      <img src="https://fal.media/files/penguin/hHhmyazpcSq_W8c0TzXl4_14015fe83e3541848e6b2e2e1c7e4968.jpg" alt="Example output from FLUX.1 [dev] with LoRAs" noZoom />
    </Frame>
  </Card>

  <Card title="Nano Banana API" href="/model-api-reference/image-generation-api/nano-banana">
    Google's famous original image generation and editing model

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a95c085/S0ExtNZpsp_6xygCJ3MKG_Bj98CiYt.png" alt="Example output from Nano Banana" noZoom />
    </Frame>
  </Card>

  <Card title="Bytedance API" href="/model-api-reference/image-generation-api/bytedance-seedream-v4.5">
    A new-generation image creation model ByteDance, Seedream 4.5 integrates image generation and image editing capabilities into a single, unified architecture.

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a84910b/lDvWLqpxcFmzQHdadDA7t_4012f28b4f79444782d90d8927b42c29.jpg" alt="Example output from Bytedance" noZoom />
    </Frame>
  </Card>

  <Card title="Grok Imagine Image API" href="/model-api-reference/image-generation-api/xai-grok-imagine-image">
    Edit images precisely with xAI's Grok Imagine model

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a8a0dc7/kv2XmZ5em8Kb2-7oXZndp_b897f79cbc564e1d8f4e5d5c71710c2b.jpg" alt="Example output from Grok Imagine Image" noZoom />
    </Frame>
  </Card>

  <Card title="GPT-Image 1.5 API" href="/model-api-reference/image-generation-api/gpt-image-1.5">
    GPT Image 1.5 generates high-fidelity images with strong prompt adherence, preserving composition, lighting, and fine-grained detail.

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a875814/3KvlvWItvogHIOuPRWIVl_001c9e77742a4ff2a829a8ece127c0d1.jpg" alt="Example output from GPT-Image 1.5" noZoom />
    </Frame>
  </Card>

  <Card title="SeedVR2 API" href="/model-api-reference/image-generation-api/seedvr-upscale-image">
    Use SeedVR2 to upscale your images

    <Frame>
      <img src="https://v3.fal.media/files/panda/_-1rRy0_I6w-fbt3q0RDL_2f47fece6e2b433994dda482e8d20bb9.jpg" alt="Example output from SeedVR2" noZoom />
    </Frame>
  </Card>

  <Card title="Gemini 3 Pro Image Preview API" href="/model-api-reference/image-generation-api/gemini-3-pro-image-preview">
    Gemini 3 Pro Image (a.k.a Nano Banana Pro) is Google's state-of-the-art high-fidelity image generation and editing model

    <Frame>
      <img src="https://v3b.fal.media/files/b/penguin/Vp2KdBwHgd4Qp0ixnsOue_eb81afc63ac24064bc9d3e9ed48f9b74.jpg" alt="Example output from Gemini 3 Pro Image Preview" noZoom />
    </Frame>
  </Card>

  <Card title="Bria RMBG 2.0 API" href="/model-api-reference/image-generation-api/bria-background">
    Bria RMBG 2.0 enables seamless removal of backgrounds from images, ideal for professional editing tasks. Trained exclusively on licensed data for safe and risk-free commercial use. Model weights for c

    <Frame>
      <img src="https://v3.fal.media/files/lion/YBr6fXnaBoA_Hsy89qG6Q_44ab15cf50b0431fa4786c565c5b9032.png" alt="Example output from Bria RMBG 2.0" noZoom />
    </Frame>
  </Card>

  <Card title="Z-Image Turbo API" href="/model-api-reference/image-generation-api/z-image-turbo">
    Z-Image Turbo is a super fast text-to-image model of 6B parameters developed by Tongyi-MAI.

    <Frame>
      <img src="https://v3b.fal.media/files/b/koala/Pvji5sM6n6oNIo-p0Xsn__245f3d4eb5df4952aa80ec74f4afd7f2.jpg" alt="Example output from Z-Image Turbo" noZoom />
    </Frame>
  </Card>

  <Card title="Birefnet Background Removal API" href="/model-api-reference/image-generation-api/birefnet">
    bilateral reference framework (BiRefNet) for high-resolution dichotomous image segmentation (DIS)

    <Frame>
      <img src="https://storage.googleapis.com/falserverless/gallery/birefnet.webp" alt="Example output from Birefnet Background Removal" noZoom />
    </Frame>
  </Card>

  <Card title="Topaz API" href="/model-api-reference/image-generation-api/topaz-upscale">
    Use the powerful and accurate topaz image enhancer to enhance your images.

    <Frame>
      <img src="https://storage.googleapis.com/fal_cdn/fal/Sound-3.jpg" alt="Example output from Topaz" noZoom />
    </Frame>
  </Card>

  <Card title="Ideogram Text to Image API" href="/model-api-reference/image-generation-api/ideogram-v3">
    Generate high-quality images, posters, and logos with Ideogram V3. Features exceptional typography handling and realistic outputs optimized for commercial and creative use.

    <Frame>
      <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/image-5.png?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=a5eb3affecfe0e642fd722ebf728f088" alt="Example output from Ideogram Text to Image" noZoom width="512" height="512" data-path="images/image-5.png" />
    </Frame>
  </Card>

  <Card title="Remove Background API" href="/model-api-reference/image-generation-api/imageutils">
    Remove the background from an image.

    <Frame>
      <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/image-5.png?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=a5eb3affecfe0e642fd722ebf728f088" alt="Example output from Remove Background" noZoom width="512" height="512" data-path="images/image-5.png" />
    </Frame>
  </Card>

  <Card title="Florence-2 Large API" href="/model-api-reference/image-generation-api/florence-2-large">
    Florence-2 is an advanced vision foundation model that uses a prompt-based approach to handle a wide range of vision and vision-language tasks

    <Frame>
      <img src="https://storage.googleapis.com/falserverless/gallery/florence-2-large.jpeg" alt="Example output from Florence-2 Large" noZoom />
    </Frame>
  </Card>
</CardGroup>

Explore all image generation models on [fal.ai/models](https://fal.ai/models).

## Quick Start

Get started with **Nano Banana 2**:

<CodeGroup>
  ```python title="Python" theme={null}
  import fal_client

  def on_queue_update(update):
      if isinstance(update, fal_client.InProgress):
          for log in update.logs:
             print(log["message"])

  result = fal_client.subscribe(
      "fal-ai/nano-banana-2",
      arguments={
          "prompt": "An action shot of a black lab swimming in an inground suburban swimming pool. The camera is placed meticulously on the water line, dividing the image in half, revealing both the dogs head above water holding a tennis ball in it's mouth, and it's paws paddling underwater."
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/nano-banana-2", {
    input: {
        prompt: "An action shot of a black lab swimming in an inground suburban swimming pool. The camera is placed meticulously on the water line, dividing the image in half, revealing both the dogs head above water holding a tennis ball in it's mouth, and it's paws paddling underwater."
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
</CodeGroup>

## Pricing

For detailed pricing information, see the [fal.ai pricing page](https://fal.ai/pricing) or individual model pages.
