> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Veo3.1 API

> API reference for Veo3.1. Veo 3.1 by Google, the most advanced AI video generation model in the world. With sound on!

**Endpoint:** `POST https://fal.run/fal-ai/veo3.1`
**Endpoint ID:** `fal-ai/veo3.1`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/veo3.1/playground">
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
      "fal-ai/veo3.1",
      arguments={
          "prompt": "Two person street interview in New York City.
  Sample Dialogue:
  Host: \"Did you hear the news?\"
  Person: \"Yes! Veo 3.1 is now available on fal. If you want to see it, go check their website.\""
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/veo3.1", {
    input: {
        prompt: "Two person street interview in New York City.
  Sample Dialogue:
  Host: \"Did you hear the news?\"
  Person: \"Yes! Veo 3.1 is now available on fal. If you want to see it, go check their website.\""
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
    --url https://fal.run/fal-ai/veo3.1 \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "Two person street interview in New York City.\nSample Dialogue:\nHost: \"Did you hear the news?\"\nPerson: \"Yes! Veo 3.1 is now available on fal. If you want to see it, go check their website.\""
  }'
  ```
</CodeGroup>

## Examples

> First-person view soaring low over a medieval battlefield at dawn, gliding past clashing knights in armor, fire-lit arrows whizzing overhead, splintered catapults burning near fallen soldiers, flying inches above torn flags and mud-soaked ground, ambient sounds of swords striking, war cries, gallopi...

<video src="https://v3.fal.media/files/penguin/D-wlVxx1E8BPr2AG9cxhb_output.mp4" controls width="100%" />

> A colossal, ancient library with impossibly high shelves, where books fly and pages turn on their own. Audio: the rustle of thousands of pages turning, the soft whoosh of flying books, distant, echoing whispers, a grand, magical orchestral piece with swirling harps and enchanted woodwinds.

<video src="https://v3.fal.media/files/zebra/bW6Jj6jeerM5Y4jwo49tN_output.mp4" controls width="100%" />

> A luxury yatch sets sail in the Bosphorus Strait. As it gracefully navigates through the current, the Maiden's Tower comes into view. While continuing its journey, seagulls greet it. The sounds of waves and seagulls can be heard.

<video src="https://v3.fal.media/files/penguin/ZOkKJXXKEDJ9fsNAeMNkE_output.mp4" controls width="100%" />

## Related

* [Veo 3.1 Fast](/model-api-reference/video-generation-api/veo-3.1-fast) — Video Generation
* [Veo 3.1](/model-api-reference/video-generation-api/veo-3.1) — Video Generation
* [Veo3.1 Lite Image to Video](/model-api-reference/video-generation-api/veo3.1-lite-image-to-video) — Video Generation
* [Veo3.1 Lite FLF](/model-api-reference/video-generation-api/veo3.1-lite-flf) — Video Generation
* [Veo3.1 Lite Text to Video](/model-api-reference/video-generation-api/veo3.1-lite-text-to-video) — Video Generation

## Capabilities

* Text prompt input
* Aspect ratio control
* Duration control
* Negative prompts
* Reproducible generation (seed)

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required>
  The text prompt describing the video you want to generate
</ParamField>

<ParamField body="aspect_ratio" type="AspectRatioEnum" default="16:9">
  Aspect ratio of the generated video Default value: `"16:9"`

  Possible values: `16:9`, `9:16`
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

<ParamField body="auto_fix" type="boolean" default="true">
  Whether to automatically attempt to fix prompts that fail content policy or other validation checks by rewriting them. Default value: `true`
</ParamField>

<ParamField body="safety_tolerance" type="SafetyToleranceEnum" default="4">
  The safety tolerance level for content moderation. 1 is the most strict (blocks most content), 6 is the least strict. Default value: `"4"`

  Possible values: `1`, `2`, `3`, `4`, `5`, `6`
</ParamField>

### Output Schema

<ParamField body="video" type="File" required>
  The generated video.
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "Two person street interview in New York City.\nSample Dialogue:\nHost: \"Did you hear the news?\"\nPerson: \"Yes! Veo 3.1 is now available on fal. If you want to see it, go check their website.\"",
  "aspect_ratio": "16:9",
  "duration": "8s",
  "resolution": "720p",
  "generate_audio": true,
  "auto_fix": true,
  "safety_tolerance": "4"
}
```

## Output Example

```json theme={null}
{
  "video": {
    "url": "https://v3b.fal.media/files/b/kangaroo/oUCiZjQwEy6bIQdPUSLDF_output.mp4"
  }
}
```

## Limitations

* `aspect_ratio` restricted to: `16:9`, `9:16`
* `duration` restricted to: `4s`, `6s`, `8s`
* `resolution` restricted to: `720p`, `1080p`, `4k`
* `safety_tolerance` restricted to: `1`, `2`, `3`, `4`, `5`, `6`
