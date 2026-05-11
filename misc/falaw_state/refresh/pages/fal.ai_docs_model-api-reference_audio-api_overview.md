> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Audio API

> Audio API reference. Models for audio processing including text-to-speech, speech-to-text, voice cloning, and music generation..

## Overview

Models for audio processing including text-to-speech, speech-to-text, voice cloning, and music generation.

## Top Models

<CardGroup cols={2}>
  <Card title="Whisper API" href="/model-api-reference/audio-api/whisper">
    Whisper is a model for speech transcription and translation.

    <Frame>
      <img src="https://storage.googleapis.com/falserverless/gallery/whisper.jpg" alt="Example output from Whisper" noZoom />
    </Frame>
  </Card>

  <Card title="Kling Video Create Voice API" href="/model-api-reference/audio-api/kling-video-create-voice">
    Create Voices to be used with Kling Models Voice Control

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a868c52/jCucNmpNTg7UQ2WYGJHAr_36ad5b9439824f5e9f8fd7f1ed297d27.jpg" alt="Example output from Kling Video Create Voice" noZoom />
    </Frame>
  </Card>

  <Card title="xAI Text to Speech API" href="/model-api-reference/audio-api/xai-tts">
    Generate speech with expressive and realistic voices from xAI

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a92763c/4toOv_gM9xUL_Zwmt4Gc8_67e9f077fc4c48e78dfa428f7d50b190.jpg" alt="Example output from xAI Text to Speech" noZoom />
    </Frame>
  </Card>
</CardGroup>

Explore all audio models on [fal.ai/models](https://fal.ai/models).

## Quick Start

Get started with **Whisper**:

<CodeGroup>
  ```python title="Python" theme={null}
  import fal_client

  def on_queue_update(update):
      if isinstance(update, fal_client.InProgress):
          for log in update.logs:
             print(log["message"])

  result = fal_client.subscribe(
      "fal-ai/whisper",
      arguments={
          "audio_url": "https://storage.googleapis.com/falserverless/model_tests/whisper/dinner_conversation.mp3"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/whisper", {
    input: {
        audio_url: "https://storage.googleapis.com/falserverless/model_tests/whisper/dinner_conversation.mp3"
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
