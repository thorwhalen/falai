> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Video Generation API

> Video Generation API reference. Generate videos from text prompts or images using cutting-edge video generation models.

## Overview

Generate videos from text prompts or images using cutting-edge video generation models. These models support text-to-video, image-to-video, and video-to-video workflows.

## Top Models

<CardGroup cols={2}>
  <Card title="Seedance 2.0 Text to Video API API" href="/model-api-reference/video-generation-api/bytedance-seedance-2.0-text-to-video">
    ByteDance's most advanced text-to-video model. Cinematic output with native audio, multi-shot editing, real-world physics, and director-level camera control.

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a9460e7/626QXDcTbiOI5I3LPidrR_1ae86d7b0fbb47b3b6d1a41e7fc00956.jpg" alt="Example output from Seedance 2.0 Text to Video API" noZoom />
    </Frame>
  </Card>

  <Card title="Kling Video v3 Text to Video [Pro] API" href="/model-api-reference/video-generation-api/kling-video-v3-pro">
    Kling 3.0 Pro: Top-tier text-to-video with cinematic visuals, fluid motion, and native audio generation, with multi-shot support.

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a8cfd13/t6TSkWzl6cFAzvO1PCdDu_f38263f637d245929f03881454951540.jpg" alt="Example output from Kling Video v3 Text to Video [Pro]" noZoom />
    </Frame>
  </Card>

  <Card title="Sora 2 API" href="/model-api-reference/video-generation-api/sora-2-text-to-video">
    Text-to-video endpoint for Sora 2, OpenAI's state-of-the-art video model capable of creating richly detailed, dynamic clips with audio from natural language or images.

    <Frame>
      <img src="https://v3.fal.media/files/penguin/eOGowiQKXIKwyDfwgeWQO_b80784431c524553a564ebdd7550d7e6.jpg" alt="Example output from Sora 2" noZoom />
    </Frame>
  </Card>

  <Card title="Veo 3.1 API" href="/model-api-reference/video-generation-api/veo3.1">
    Veo 3.1 by Google, the most advanced AI video generation model in the world. With sound on!

    <Frame>
      <img src="https://v3b.fal.media/files/b/tiger/TGTZBJyLk9HdwjB6SB90e.png" alt="Example output from Veo 3.1" noZoom />
    </Frame>
  </Card>

  <Card title="Grok Imagine Video API" href="/model-api-reference/video-generation-api/xai-grok-imagine-video">
    Generate videos from images with audio using xAI's Grok Imagine Video model.

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a8a0dd0/3wXg362MQ0pczC2ZQFBfW_c153dd469fd14b75bbd9fa6d27f1b63e.jpg" alt="Example output from Grok Imagine Video" noZoom />
    </Frame>
  </Card>

  <Card title="Topaz Video Upscale API" href="/model-api-reference/video-generation-api/topaz-upscale">
    Professional-grade video upscaling using Topaz technology. Enhance your videos with high-quality upscaling.

    <Frame>
      <img src="https://storage.googleapis.com/falserverless/gallery/topaz-video-upscale.png" alt="Example output from Topaz Video Upscale" noZoom />
    </Frame>
  </Card>

  <Card title="SeedVR2 API" href="/model-api-reference/video-generation-api/seedvr-upscale">
    Upscale your videos using SeedVR2 with temporal consistency!

    <Frame>
      <img src="https://v3.fal.media/files/koala/cAs3xUC9Lx-jlQh-27-60_4dddbb5a9bac42da86ddf20a5b9d30b3.jpg" alt="Example output from SeedVR2" noZoom />
    </Frame>
  </Card>

  <Card title="Video API" href="/model-api-reference/video-generation-api/bria-video">
    Automatically remove backgrounds from videos -perfect for creating clean, professional content without a green screen.

    <Frame>
      <img src="https://storage.googleapis.com/fal_cdn/fal/Sound-2.jpg" alt="Example output from Video" noZoom />
    </Frame>
  </Card>

  <Card title="Birefnet API" href="/model-api-reference/video-generation-api/birefnet-v2">
    Video background removal version of bilateral reference framework (BiRefNet) for high-resolution dichotomous image segmentation (DIS)

    <Frame>
      <img src="https://v3b.fal.media/files/b/monkey/SKrLsOM3RMOk-QuNj8-io_6356be1b301e454394d2e0a853b98c76.jpg" alt="Example output from Birefnet" noZoom />
    </Frame>
  </Card>
</CardGroup>

Explore all video generation models on [fal.ai/models](https://fal.ai/models).

## Quick Start

Get started with **Bytedance Seedance 2.0 Text To Video**:

<CodeGroup>
  ```python title="Python" theme={null}
  import fal_client

  def on_queue_update(update):
      if isinstance(update, fal_client.InProgress):
          for log in update.logs:
             print(log["message"])

  result = fal_client.subscribe(
      "bytedance/seedance-2.0/text-to-video",
      arguments={
          "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("bytedance/seedance-2.0/text-to-video", {
    input: {
        prompt: "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."
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
