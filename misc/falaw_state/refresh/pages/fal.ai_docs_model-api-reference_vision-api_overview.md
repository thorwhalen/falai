> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vision API

> Vision API reference. Models for understanding and analyzing images, including captioning, visual question answering, and object detection..

## Overview

Models for understanding and analyzing images, including captioning, visual question answering, and object detection.

## Top Models

<CardGroup cols={2}>
  <Card title="OpenRouter [Vision] API" href="/model-api-reference/vision-api/openrouter-router">
    Run any Vision Language Model with fal. Analyze and understand images using Claude (Anthropic), GPT-5 / GPT-4o (OpenAI), Gemini (Google), Grok (xAI), Llama (Meta), Qwen, Pixtral (Mistral), and more. S

    <Frame>
      <img src="https://v3b.fal.media/files/b/penguin/v-wl5CGbHxNVatcGXntIY_e14c7922d88348769a90469d1c206501.jpg" alt="Example output from OpenRouter [Vision]" noZoom />
    </Frame>
  </Card>

  <Card title="NSFW Filter API" href="/model-api-reference/vision-api/imageutils">
    Predict the probability of an image being NSFW.

    <Frame>
      <img src="https://storage.googleapis.com/falserverless/gallery/nsfw-filter.webp" alt="Example output from NSFW Filter" noZoom />
    </Frame>
  </Card>

  <Card title="Florence-2 Large API" href="/model-api-reference/vision-api/florence-2-large">
    Florence-2 is an advanced vision foundation model that uses a prompt-based approach to handle a wide range of vision and vision-language tasks

    <Frame>
      <img src="https://storage.googleapis.com/falserverless/gallery/florence-2-large.jpeg" alt="Example output from Florence-2 Large" noZoom />
    </Frame>
  </Card>
</CardGroup>

Explore all vision models on [fal.ai/models](https://fal.ai/models).

## Quick Start

Get started with **OpenRouter \[Vision]**:

<CodeGroup>
  ```python title="Python" theme={null}
  import fal_client

  def on_queue_update(update):
      if isinstance(update, fal_client.InProgress):
          for log in update.logs:
             print(log["message"])

  result = fal_client.subscribe(
      "openrouter/router/vision",
      arguments={
          "image_urls": [
              "https://fal.media/files/tiger/4Ew1xYW6oZCs6STQVC7V8_86440216d0fe42e4b826d03a2121468e.jpg"
          ],
          "prompt": "Caption this image for a text-to-image model with as much detail as possible.",
          "model": "google/gemini-2.5-flash"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("openrouter/router/vision", {
    input: {
        image_urls: [
          "https://fal.media/files/tiger/4Ew1xYW6oZCs6STQVC7V8_86440216d0fe42e4b826d03a2121468e.jpg"
        ],
        prompt: "Caption this image for a text-to-image model with as much detail as possible.",
        model: "google/gemini-2.5-flash"
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
