> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bria Fibo Lite API

> API reference for Bria Fibo Lite. Fibo Lite, the new addition to the Fibo model family, allows generating high-quality images with the same controllability of the JSON structured prompt with significa

**Endpoint:** `POST https://fal.run/bria/fibo-lite/generate`
**Endpoint ID:** `bria/fibo-lite/generate`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/bria/fibo-lite/generate/playground">
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
      "bria/fibo-lite/generate",
      arguments={},
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("bria/fibo-lite/generate", {
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
    --url https://fal.run/bria/fibo-lite/generate \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{}'
  ```
</CodeGroup>

## Examples

> several coffee beans floating independently in mid air, the subject is red, in a red photo, red and black duotone image, red wash, red light, red lens, extreme close up, a dark black empty background, closeup, dramatic lighting with a strong red hue that gives the image a moody and intense atmospher...

<Frame>
  <img src="https://v3b.fal.media/files/b/0a8739b1/5PkOKEpdQu16ZkS3ovA92_e0d9e8ab6833478aa854cba5ca1c88ad.png" alt="Generated image: several coffee beans floating independently in mid air, the subject is red, in a" />
</Frame>

<Frame>
  <img src="https://v3b.fal.media/files/b/0a873af8/6YpzosRTtGfE40Iw28xvo_99cc31c90a474a42a3b64be2b1e6aacd.png" alt="Example output from Fibo Lite" />
</Frame>

<Frame>
  <img src="https://v3b.fal.media/files/b/0a873aed/b_8ygdKfq7HQnL5s8PD3J_5c4a1f3dca65408ba7bbc9cb45b1688a.png" alt="Example output from Fibo Lite" />
</Frame>

### Input Schema

<ParamField body="prompt" type="string">
  The prompt to generate.
</ParamField>

<ParamField body="structured_prompt" type="StructuredPrompt">
  The structured prompt to generate.
</ParamField>

<ParamField body="image_url" type="string">
  Input image URL
</ParamField>

<ParamField body="seed" type="integer" default="7">
  Seed for the random number generator. Default value: `7`
</ParamField>

<ParamField body="aspect_ratio" type="AspectRatioEnum" default="1:1">
  Aspect ratio. Options: 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9 Default value: `"1:1"`

  Possible values: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`
</ParamField>

<ParamField body="negative_prompt" type="string" default="">
  Negative prompt for image generation. Default value: `""`
</ParamField>

<ParamField body="steps_num" type="integer" default="8">
  Number of inference steps. Default value: `8`

  Range: `4` to `30`
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

<ParamField body="structured_prompt" type="StructuredPrompt" required>
  Current prompt.
</ParamField>

### Input Example

```json theme={null}
{
  "prompt": "Oil painting of a fluffy, wide-eyed cat sitting upright, holding a small wooden sign reading \"Feed Me.\" Rich textures, dramatic brushstrokes, warm tones, and vintage charm.",
  "seed": 7,
  "aspect_ratio": "1:1",
  "negative_prompt": "",
  "steps_num": 8,
  "sync_mode": false
}
```

### Output Example

```json theme={null}
{
  "image": {
    "url": "",
    "content_type": "image/png",
    "file_name": "z9RV14K95DvU.png",
    "file_size": 4404019,
    "width": 1024,
    "height": 1024
  },
  "structured_prompt": {
    "short_description": "",
    "objects": [
      {
        "description": "",
        "location": "",
        "relationship": ""
      }
    ],
    "background_setting": "",
    "lighting": {
      "conditions": "",
      "direction": ""
    },
    "aesthetics": {
      "composition": "",
      "color_scheme": "",
      "mood_atmosphere": "",
      "aesthetic_score": "",
      "preference_score": ""
    },
    "text_render": [
      {
        "text": "",
        "location": "",
        "size": "",
        "color": "",
        "font": ""
      }
    ],
    "context": "",
    "artistic_style": ""
  }
}
```

**Overview**

Fibo Lite, the new addition to the Fibo model family, allows generating **high-quality** images with the same **controllability** of the JSON structured prompt, while using significantly fewer inference steps, resulting in significantly **improved latency.**

This is a two-stage distilled model for the [FIBO](https://huggingface.co/briaai/FIBO) text-to-image model, combining:

1. CFG Distillation: First, we distill classifier-free guidance into the model, enabling inference with Guidance Scale = 1.0 (skipping the negative prompt pass).
2. SCFM (Shortcutting Flow Matching): On top of the CFG-distilled merged model, we apply velocity field self-distillation to enable efficient few-step sampling.

### **🔑 Key Benefits**

* Two-Stage Distillation: Combines CFG distillation with SCFM for maximum efficiency—the SCFM was trained on top of the already CFG-distilled merged model.
* Few-Step Generation: SCFM enables efficient sampling in significantly fewer inference steps.
* No CFG Overhead: Running at guidance\_scale=1 means calculating the noise prediction only once per step instead of twice.
* Quality Tradeoff: As a distillation approach, there is a slight quality degradation compared to the full model at CFG=5, but the speed gains make it ideal for rapid iteration and production workflows.
* Drop-in Replacement: Works seamlessly with existing FIBO workflows—just set guidance\_scale=1.0.
* Memory Efficient: Minimal additional GPU memory overhead.

## Limitations

* `steps_num` range: 4 to 30
