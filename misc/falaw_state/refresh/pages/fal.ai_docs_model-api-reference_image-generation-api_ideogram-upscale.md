> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ideogram Upscale API

> API reference for Ideogram Upscale. Ideogram Upscale enhances the resolution of the reference image by up to 2X and might enhance the reference image too. Optionally refine outputs with a prompt for g

**Endpoint:** `POST https://fal.run/fal-ai/ideogram/upscale`
**Endpoint ID:** `fal-ai/ideogram/upscale`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/ideogram/upscale/playground">
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
      "fal-ai/ideogram/upscale",
      arguments={
          "image_url": "https://fal.media/files/monkey/e6RtJf_ue0vyWzeiEmTby.png"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/ideogram/upscale", {
    input: {
        image_url: "https://fal.media/files/monkey/e6RtJf_ue0vyWzeiEmTby.png"
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
    --url https://fal.run/fal-ai/ideogram/upscale \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "image_url": "https://fal.media/files/monkey/e6RtJf_ue0vyWzeiEmTby.png"
  }'
  ```
</CodeGroup>

## Capabilities

* Image input
* Text prompt input
* Reproducible generation (seed)
* Synchronous mode

## API Reference

### Input Schema

<ParamField body="image_url" type="string" required>
  The image URL to upscale
</ParamField>

<ParamField body="prompt" type="string" default="">
  The prompt to upscale the image with Default value: `""`
</ParamField>

<ParamField body="resemblance" type="integer" default="50">
  The resemblance of the upscaled image to the original image Default value: `50`

  Range: `1` to `100`
</ParamField>

<ParamField body="detail" type="integer" default="50">
  The detail of the upscaled image Default value: `50`

  Range: `1` to `100`
</ParamField>

<ParamField body="expand_prompt" type="boolean" default="false">
  Whether to expand the prompt with MagicPrompt functionality.
</ParamField>

<ParamField body="seed" type="integer">
  Seed for the random number generator
</ParamField>

<ParamField body="sync_mode" type="boolean" default="false">
  If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
</ParamField>

### Output Schema

<ParamField body="images" type="list<File>" required />

<ParamField body="seed" type="integer" required>
  Seed used for the random number generator
</ParamField>

## Input Example

```json theme={null}
{
  "image_url": "https://fal.media/files/monkey/e6RtJf_ue0vyWzeiEmTby.png",
  "prompt": "",
  "resemblance": 50,
  "detail": 50,
  "expand_prompt": false,
  "sync_mode": false
}
```

## Output Example

```json theme={null}
{
  "images": [
    {
      "content_type": "image/png",
      "file_name": "image.png",
      "file_size": 6548418,
      "url": "https://fal.media/files/lion/DxTSV6683MLl4VPAVUHR3_image.png"
    }
  ],
  "seed": 123456
}
```

## Limitations

* `resemblance` range: 1 to 100
* `detail` range: 1 to 100
