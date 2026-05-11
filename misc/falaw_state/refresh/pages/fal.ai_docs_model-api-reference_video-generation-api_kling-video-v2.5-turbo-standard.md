> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video V2.5 Turbo Standard API

> API reference for Kling Video V2.5 Turbo Standard. Kling 2.5 Turbo Standard: Top-tier image-to-video generation with unparalleled motion fluidity, cinematic visuals, and exceptional prompt precision.

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/v2.5-turbo/standard/image-to-video`
**Endpoint ID:** `fal-ai/kling-video/v2.5-turbo/standard/image-to-video`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v2.5-turbo/standard/image-to-video/playground">
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
      "fal-ai/kling-video/v2.5-turbo/standard/image-to-video",
      arguments={
          "prompt": "In a dimly lit room, a playful cat's eyes light up, fixated on a dancing red dot. With boundless energy, it pounces and leaps, chasing the elusive beam across the floor and up the walls. The simple joy of the hunt unfolds in clear, uncomplicated visuals.",
          "image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling_v25_std_i2v_input.png"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/kling-video/v2.5-turbo/standard/image-to-video", {
    input: {
        prompt: "In a dimly lit room, a playful cat's eyes light up, fixated on a dancing red dot. With boundless energy, it pounces and leaps, chasing the elusive beam across the floor and up the walls. The simple joy of the hunt unfolds in clear, uncomplicated visuals.",
        image_url: "https://storage.googleapis.com/falserverless/example_inputs/kling_v25_std_i2v_input.png"
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
    --url https://fal.run/fal-ai/kling-video/v2.5-turbo/standard/image-to-video \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "In a dimly lit room, a playful cat'\''s eyes light up, fixated on a dancing red dot. With boundless energy, it pounces and leaps, chasing the elusive beam across the floor and up the walls. The simple joy of the hunt unfolds in clear, uncomplicated visuals.",
    "image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling_v25_std_i2v_input.png"
  }'
  ```
</CodeGroup>

### Input Schema

<ParamField body="prompt" type="string" required />

<ParamField body="image_url" type="string" required>
  URL of the image to be used for the video
</ParamField>

<ParamField body="duration" type="DurationEnum" default="5">
  The duration of the generated video in seconds Default value: `"5"`

  Possible values: `5`, `10`
</ParamField>

<ParamField body="negative_prompt" type="string" default="blur, distort, and low quality">
  Default value: `"blur, distort, and low quality"`
</ParamField>

<ParamField body="cfg_scale" type="float" default="0.5">
  The CFG (Classifier Free Guidance) scale is a measure of how close you want
  the model to stick to your prompt. Default value: `0.5`

  Range: `0` to `1`
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The generated video
</ParamField>

### Input Example

```json theme={null}
{
  "prompt": "In a dimly lit room, a playful cat's eyes light up, fixated on a dancing red dot. With boundless energy, it pounces and leaps, chasing the elusive beam across the floor and up the walls. The simple joy of the hunt unfolds in clear, uncomplicated visuals.",
  "image_url": "https://storage.googleapis.com/falserverless/example_inputs/kling_v25_std_i2v_input.png",
  "duration": "5",
  "negative_prompt": "blur, distort, and low quality",
  "cfg_scale": 0.5
}
```

### Output Example

```json theme={null}
{
  "video": {
    "url": "https://storage.googleapis.com/falserverless/example_outputs/kling_v25_std_i2v_output.mp4"
  }
}
```

## Related

* [Kling Video](/model-api-reference/video-generation-api/kling-video) — Video Generation
* [Kling v2.5 Text to Video](/model-api-reference/video-generation-api/kling-v2.5-text-to-video) — Video Generation

## Limitations

* `duration` restricted to: `5`, `10`
* `cfg_scale` range: 0 to 1
