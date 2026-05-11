> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bria Replace Background API

> API reference for Bria Replace Background. Creates enriched product shots by placing them in various environments using textual descriptions.

**Endpoint:** `POST https://fal.run/bria/replace-background`
**Endpoint ID:** `bria/replace-background`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/replace-background/playground">
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
      "bria/replace-background",
      arguments={},
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("bria/replace-background", {
    input: {},
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
    --url https://fal.run/bria/replace-background \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{}'
  ```
</CodeGroup>

## Related

* [Bria RMBG 2.0](/model-api-reference/image-generation-api/bria-rmbg-2.0) — Image Generation
* [Bria Expand Image](/model-api-reference/image-generation-api/bria-expand-image) — Image Generation
* [Bria Eraser](/model-api-reference/image-generation-api/bria-eraser) — Image Generation
* [Bria Product Shot](/model-api-reference/image-generation-api/bria-product-shot) — Image Generation
* [Bria Background Replace](/model-api-reference/image-generation-api/bria-background-replace) — Image Generation
* [Video](/model-api-reference/video-generation-api/video) — Video Generation
* [Bria GenFill](/model-api-reference/image-generation-api/bria-genfill) — Image Generation
* [Bria Text-to-Image HD](/model-api-reference/image-generation-api/bria-text-to-image-hd) — Image Generation
* [Bria Text-to-Image Base](/model-api-reference/image-generation-api/bria-text-to-image-base) — Image Generation
* [Embed Product](/model-api-reference/image-generation-api/embed-product) — Image Generation
* [Bria Text-to-Image Fast](/model-api-reference/image-generation-api/bria-text-to-image-fast) — Image Generation

## Capabilities

* Text prompt input
* Image input
* Reproducible generation (seed)
* Negative prompts
* Synchronous mode

## API Reference

### Input Schema

<ParamField body="prompt" type="string">
  Prompt for background replacement.
</ParamField>

<ParamField body="image_url" type="string" default="https://v3b.fal.media/files/b/0a8bea8c/Mztgx0NG3HPdby-4iPqwH_a_coffee_machine_standing_in_the_kitchen.png">
  Reference image (file or URL). Default value: `"https://v3b.fal.media/files/b/0a8bea8c/Mztgx0NG3HPdby-4iPqwH_a_coffee_machine_standing_in_the_kitchen.png"`
</ParamField>

<ParamField body="seed" type="integer" default="4925634">
  Random seed for reproducibility. Default value: `4925634`
</ParamField>

<ParamField body="steps_num" type="integer" default="30">
  Number of inference steps. Default value: `30`
</ParamField>

<ParamField body="negative_prompt" type="string" default="">
  Negative prompt for background replacement. Default value: `""`
</ParamField>

<ParamField body="sync_mode" type="boolean" default="false">
  If true, returns the image directly in the response (increases latency).
</ParamField>

### Output Schema

<ParamField body="image" type="Image" required>
  Generated image.
</ParamField>

<ParamField body="images" type="list<object>">
  Generated images.
</ParamField>

## Input Example

```json theme={null}
{
  "prompt": "On a smooth kitchen counter in front of a blue and white patterned ceramic tile wall. A yellow ceramic mug sits to the right. Shot from a straight-on front angle.",
  "image_url": "https://v3b.fal.media/files/b/0a8bea8c/Mztgx0NG3HPdby-4iPqwH_a_coffee_machine_standing_in_the_kitchen.png",
  "seed": 4925634,
  "steps_num": 30,
  "negative_prompt": "",
  "sync_mode": false
}
```

## Output Example

```json theme={null}
{
  "image": {
    "url": "",
    "content_type": "image/png",
    "file_name": "z9RV14K95DvU.png",
    "file_size": 4404019,
    "width": 1024,
    "height": 1024
  }
}
```
