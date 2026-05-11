> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Convert Speech to Text Tutorial

## How to Convert Speeches using the fal API

To convert speeches to text using the fal API, you need to send a request to the appropriate endpoint with the desired input parameters. The API uses pre-trained models to convert speeches to text based on the provided audio file. This allows you to convert speeches to text by simply providing the audio file.

Here is an example of how to convert speeches to text using the fal API:

```js theme={null}
import { fal } from "@fal-ai/client";

const result = await fal.subscribe("fal-ai/whisper", {
  input: {
    audio_url: "https://storage.googleapis.com/falserverless/model_tests/whisper/dinner_conversation.mp3"
  },
});
```

## How to select the model to use

fal offers a variety of speech-to-text models. You can select the model that best fits your needs based on the quality and accuracy of the speech-to-text conversion. Here are some of the available models:

* [fal-ai/whisper](https://fal.ai/models/fal-ai/whisper): Whisper is a model for speech transcription and translation.
* [fal-ai/wizper](https://fal.ai/models/fal-ai/wizper): Wizper is Whisper v3 Large — but optimized by our inference wizards. Same WER, double the performance!

To select a model, simply specify the model ID in the subscribe method as shown in the example above. You can find more models and their descriptions in the [Text to Image Models](https://fal.ai/models?categories=text-to-image) page.
