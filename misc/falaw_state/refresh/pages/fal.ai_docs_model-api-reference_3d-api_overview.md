> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 3D API

> 3D API reference. Generate 3D assets from text or images using AI models.

## Overview

Generate 3D assets from text or images using AI models. Create 3D meshes, textures, and scenes for games, design, and visualization.

## Top Models

<CardGroup cols={2}>
  <Card title="Trellis 2 API" href="/model-api-reference/3d-api/trellis-2">
    Generate 3D models from your images using Trellis 2. A native 3D generative model enabling versatile and high-quality 3D asset creation.

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a87573c/DwQCx7YBl36dnFSHaU8OT_bfc26b64d210462489530b5d5d5d98e1.jpg" alt="Example output from Trellis 2" noZoom />
    </Frame>
  </Card>

  <Card title="Hunyuan 3D Pro Image to 3D API" href="/model-api-reference/3d-api/hunyuan-3d-v3.1-pro">
    Generate 3D models from images with Hunyuan 3D Pro

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a8c1eed/a9u-FinZ2o0AGqcGFlRoD_5c16e7c0e1ae412cacc53893cae95698.jpg" alt="Example output from Hunyuan 3D Pro Image to 3D" noZoom />
    </Frame>
  </Card>

  <Card title="Trellis API" href="/model-api-reference/3d-api/trellis">
    Generate 3D models from your images using Trellis. A native 3D generative model enabling versatile and high-quality 3D asset creation.

    <Frame>
      <img src="https://storage.googleapis.com/falserverless/web-examples/trellis/trellis-photo.jpg" alt="Example output from Trellis" noZoom />
    </Frame>
  </Card>
</CardGroup>

Explore all 3d models on [fal.ai/models](https://fal.ai/models).

## Quick Start

Get started with **Trellis 2**:

<CodeGroup>
  ```python title="Python" theme={null}
  import fal_client

  def on_queue_update(update):
      if isinstance(update, fal_client.InProgress):
          for log in update.logs:
             print(log["message"])

  result = fal_client.subscribe(
      "fal-ai/trellis-2",
      arguments={
          "image_url": "https://v3b.fal.media/files/b/0a86b60d/xkpao5B0uxmH0tmJm0HVL_2fe35ce1-fe44-475b-b582-6846a149537c.png"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/trellis-2", {
    input: {
        image_url: "https://v3b.fal.media/files/b/0a86b60d/xkpao5B0uxmH0tmJm0HVL_2fe35ce1-fe44-475b-b582-6846a149537c.png"
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
