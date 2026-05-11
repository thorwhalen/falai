> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Veo3.1 Image To Video API

> API reference for Veo3.1 Image To Video. Veo 3.1 is the latest state-of-the art video generation model from Google DeepMind

**Endpoint:** `POST https://fal.run/fal-ai/veo3.1/image-to-video`
**Endpoint ID:** `fal-ai/veo3.1/image-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/veo3.1/image-to-video/playground">
  Run this model interactively with your own prompts.
</Card>

## Quick Start

<CodeGroup>
  ```python title="Python" theme={null}
  import fal_client

  def on_queue_update(update):
      if isinstance(update, fal_client.InProgress):
          for log in update.logs:
             print(log["message"])

  result = fal_client.subscribe(
      "fal-ai/veo3.1/image-to-video",
      arguments={
          "prompt": "A monkey and polar bear host a casual podcast about AI inference, bringing their unique perspectives from different environments (tropical vs. arctic) to discuss how AI systems make decisions and process information.
  Sample Dialogue:
  Monkey (Banana): \"Welcome back to Bananas & Ice! I am Banana\"
  Polar Bear (Ice): \"And I'm Ice!\"",
          "image_url": "https://storage.googleapis.com/falserverless/example_inputs/veo31_i2v_input.jpg"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/veo3.1/image-to-video", {
    input: {
        prompt: "A monkey and polar bear host a casual podcast about AI inference, bringing their unique perspectives from different environments (tropical vs. arctic) to discuss how AI systems make decisions and process information.
  Sample Dialogue:
  Monkey (Banana): \"Welcome back to Bananas & Ice! I am Banana\"
  Polar Bear (Ice): \"And I'm Ice!\"",
        image_url: "https://storage.googleapis.com/falserverless/example_inputs/veo31_i2v_input.jpg"
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
    --url https://fal.run/fal-ai/veo3.1/image-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "A monkey and polar bear host a casual podcast about AI inference, bringing their unique perspectives from different environments (tropical vs. arctic) to discuss how AI systems make decisions and process information.\nSample Dialogue:\nMonkey (Banana): \"Welcome back to Bananas & Ice! I am Banana\"\nPolar Bear (Ice): \"And I'\''m Ice!\"",
    "image_url": "https://storage.googleapis.com/falserverless/example_inputs/veo31_i2v_input.jpg"
  }'
  ```
</CodeGroup>

## Related

* [Veo 3.1](/model-api-reference/video-generation-api/veo-3.1) — Video Generation
* [Veo 3.1 Fast](/model-api-reference/video-generation-api/veo-3.1-fast) — Video Generation
* [Veo3.1 Lite Image to Video](/model-api-reference/video-generation-api/veo3.1-lite-image-to-video) — Video Generation
* [Veo3.1 Lite FLF](/model-api-reference/video-generation-api/veo3.1-lite-flf) — Video Generation
* [Veo3.1 Lite Text to Video](/model-api-reference/video-generation-api/veo3.1-lite-text-to-video) — Video Generation

## Capabilities

* Text prompt input
* Aspect ratio control
* Duration control
* Negative prompts
* Reproducible generation (seed)
* Image input

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required>
  The text prompt describing the video you want to generate
</ParamField>

<ParamField body="aspect_ratio" type="AspectRatioEnum" default="auto">
  The aspect ratio of the generated video. Only 16:9 and 9:16 are supported. Default value: `"auto"`

  Possible values: `auto`, `16:9`, `9:16`
</ParamField>

<ParamField body="duration" type="DurationEnum" default="8s">
  The duration of the generated video. Default value: `"8s"`

  Possible values: `4s`, `6s`, `8s`
</ParamField>

<ParamField body="negative_prompt" type="string">
  A negative prompt to guide the video generation.
</ParamField>

<ParamField body="resolution" type="ResolutionEnum" default="720p">
  The resolution of the generated video. Default value: `"720p"`

  Possible values: `720p`, `1080p`, `4k`
</ParamField>

<ParamField body="generate_audio" type="boolean" default="true">
  Whether to generate audio for the video. Default value: `true`
</ParamField>

<ParamField body="seed" type="integer">
  The seed for the random number generator.
</ParamField>

<ParamField body="auto_fix" type="boolean" default="false">
  Whether to automatically attempt to fix prompts that fail content policy or other validation checks by rewriting them.
</ParamField>

<ParamField body="safety_tolerance" type="SafetyToleranceEnum" default="4">
  The safety tolerance level for content moderation. 1 is the most strict (blocks most content), 6 is the least strict. Default value: `"4"`

  Possible values: `1`, `2`, `3`, `4`, `5`, `6`
</ParamField>

<ParamField body="image_url" type="string" required>
  URL of the input image to animate. Should be 720p or higher resolution in 16:9 or 9:16 aspect ratio. If the image is not in 16:9 or 9:16 aspect ratio, it will be cropped to fit.
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The generated video.
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "A monkey and polar bear host a casual podcast about AI inference, bringing their unique perspectives from different environments (tropical vs. arctic) to discuss how AI systems make decisions and process information.\nSample Dialogue:\nMonkey (Banana): \"Welcome back to Bananas & Ice! I am Banana\"\nPolar Bear (Ice): \"And I'm Ice!\"",
  "aspect_ratio": "auto",
  "duration": "8s",
  "resolution": "720p",
  "generate_audio": true,
  "auto_fix": false,
  "safety_tolerance": "4",
  "image_url": "https://storage.googleapis.com/falserverless/example_inputs/veo31_i2v_input.jpg"
}
```

## Output Example

```json theme={null}
{
  "video": {
    "url": "https://storage.googleapis.com/falserverless/model_tests/gallery/veo3-1-i2v.mp4"
  }
}
```

## Limitations

* `aspect_ratio` restricted to: `auto`, `16:9`, `9:16`
* `duration` restricted to: `4s`, `6s`, `8s`
* `resolution` restricted to: `720p`, `1080p`, `4k`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`, `6`
