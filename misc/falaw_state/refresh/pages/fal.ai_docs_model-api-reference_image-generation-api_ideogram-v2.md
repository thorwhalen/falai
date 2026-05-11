> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ideogram V2 API

> API reference for Ideogram V2. Generate high-quality images, posters, and logos with Ideogram V2. Features exceptional typography handling and realistic outputs optimized for commercial and creative u

**Endpoint:** `POST https://fal.run/fal-ai/ideogram/v2`
**Endpoint ID:** `fal-ai/ideogram/v2`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/v2/playground">
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
      "fal-ai/ideogram/v2",
      arguments={
          "prompt": "A comic style illustration of a skeleton sitting on a toilet in a bathroom. The bathroom has a Halloween decoration with a pumpkin jack-o-lantern and bats flying around. There is a text above the skeleton that says \"Just Waiting for Halloween with Ideogram 2.0 at fal.ai\""
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/ideogram/v2", {
    input: {
        prompt: "A comic style illustration of a skeleton sitting on a toilet in a bathroom. The bathroom has a Halloween decoration with a pumpkin jack-o-lantern and bats flying around. There is a text above the skeleton that says \"Just Waiting for Halloween with Ideogram 2.0 at fal.ai\""
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
    --url https://fal.run/fal-ai/ideogram/v2 \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "prompt": "A comic style illustration of a skeleton sitting on a toilet in a bathroom. The bathroom has a Halloween decoration with a pumpkin jack-o-lantern and bats flying around. There is a text above the skeleton that says \"Just Waiting for Halloween with Ideogram 2.0 at fal.ai\""
  }'
  ```
</CodeGroup>

## Examples

> A playful cat is sitting on the right side of a vibrant beach ball, situated on a sunny, sandy beach. The beach is dotted with sunbathers and colorful umbrellas. Waves gently lap at the shore, and a pristine blue sky is adorned with a few fluffy white clouds. Seagulls soar overhead, adding to the li...

<Frame>
  <img src="https://fal.media/files/kangaroo/pBa0_WFY5AEO6Q_mnbtNB_image.png" alt="Generated image: A playful cat is sitting on the right side of a vibrant beach ball, situated on " />
</Frame>

> A warm, hyper-detailed, low-saturation scene in the style of David Lynch, set against a soft-focus suburban American backdrop with muted colors and soothing tones, evoking a sense of nostalgia. Two characters, a young, ethnically ambiguous woman with sun-kissed, golden-brown skin and a bright, enigm...

<Frame>
  <img src="https://fal.media/files/koala/dSrkX-nFdB_nDA3NaKkMB_image.png" alt="Generated image: A warm, hyper-detailed, low-saturation scene in the style of David Lynch, set ag" />
</Frame>

> A marble-skinned figure with neoclassical features, matte skin, and wrinkles, majestically strides forward on a serene tropical beach with a palm tree and green foliage, amidst a blurred bustling galactic trade hub background.

<Frame>
  <img src="https://fal.media/files/penguin/xYDHqdCkh_azyfWaY8Lsp_image.png" alt="Generated image: A marble-skinned figure with neoclassical features, matte skin, and wrinkles, ma" />
</Frame>

## Related

* [Ideogram V2 Remix](/model-api-reference/image-generation-api/ideogram-v2-remix) — Image Generation
* [Ideogram V2 Edit](/model-api-reference/image-generation-api/ideogram-v2-edit) — Image Generation

## Capabilities

* Text prompt input
* Aspect ratio control
* Reproducible generation (seed)
* Synchronous mode
* Negative prompts

## API Reference

### Input Schema

<ParamField body="prompt" type="string" required />

<ParamField body="aspect_ratio" type="AspectRatioEnum" default="1:1">
  The aspect ratio of the generated image Default value: `"1:1"`

  Possible values: `10:16`, `16:10`, `9:16`, `16:9`, `4:3`, `3:4`, `1:1`, `1:3`, `3:1`, `3:2`, `2:3`
</ParamField>

<ParamField body="expand_prompt" type="boolean" default="true">
  Whether to expand the prompt with MagicPrompt functionality. Default value: `true`
</ParamField>

<ParamField body="seed" type="integer">
  Seed for the random number generator
</ParamField>

<ParamField body="style" type="StyleEnum" default="auto">
  The style of the generated image Default value: `"auto"`

  Possible values: `auto`, `general`, `realistic`, `design`, `render_3D`, `anime`
</ParamField>

<ParamField body="sync_mode" type="boolean" default="false">
  If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
</ParamField>

<ParamField body="negative_prompt" type="string" default="">
  A negative prompt to avoid in the generated image Default value: `""`
</ParamField>

### Output Schema

<ParamField body="images" type="list<File>" required />

<ParamField body="seed" type="integer" required>
  Seed used for the random number generator
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "A comic style illustration of a skeleton sitting on a toilet in a bathroom. The bathroom has a Halloween decoration with a pumpkin jack-o-lantern and bats flying around. There is a text above the skeleton that says \"Just Waiting for Halloween with Ideogram 2.0 at fal.ai\"",
  "aspect_ratio": "1:1",
  "expand_prompt": true,
  "style": "auto",
  "sync_mode": false,
  "negative_prompt": ""
}
```

## Output Example

```json theme={null}
{
  "images": [
    {
      "url": "https://fal.media/files/monkey/cNaoxPl0YAWYb-QVBvO9F_image.png"
    }
  ],
  "seed": 123456
}
```

## Limitations

* `style` restricted to: `auto`, `general`, `realistic`, `design`, `render_3D`, `anime`
