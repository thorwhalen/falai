> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Openrouter Router API

> API reference for Openrouter Router. Run any Vision Language Model with fal. Analyze and understand images using Claude (Anthropic), GPT-5 / GPT-4o (OpenAI), Gemini (Google), Grok (xAI), Llama (Meta),

**Endpoint:** `POST https://fal.run/openrouter/router/vision`
**Endpoint ID:** `openrouter/router/vision`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/openrouter/router/vision/playground">
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
      "openrouter/router/vision",
      arguments={
          "image_urls": [
              "https://fal.media/files/tiger/4Ew1xYW6oZCs6STQVC7V8_86440216d0fe42e4b826d03a2121468e.jpg"
          ],
          "prompt": "Caption this image for a text-to-image model with as much detail as possible.",
          "model": "google/gemini-2.5-flash"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("openrouter/router/vision", {
    input: {
        image_urls: [
          "https://fal.media/files/tiger/4Ew1xYW6oZCs6STQVC7V8_86440216d0fe42e4b826d03a2121468e.jpg"
        ],
        prompt: "Caption this image for a text-to-image model with as much detail as possible.",
        model: "google/gemini-2.5-flash"
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
    --url https://fal.run/openrouter/router/vision \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "image_urls": [
      "https://fal.media/files/tiger/4Ew1xYW6oZCs6STQVC7V8_86440216d0fe42e4b826d03a2121468e.jpg"
    ],
    "prompt": "Caption this image for a text-to-image model with as much detail as possible.",
    "model": "google/gemini-2.5-flash"
  }'
  ```
</CodeGroup>

### Input Schema

<ParamField body="image_urls" type="list<string>" required>
  List of image URLs to be processed
</ParamField>

<ParamField body="prompt" type="string" required>
  Prompt to be used for the image
</ParamField>

<ParamField body="system_prompt" type="string">
  System prompt to provide context or instructions to the model
</ParamField>

<ParamField body="model" type="string" required>
  Name of the model to use. Charged based on actual token usage.
</ParamField>

<ParamField body="reasoning" type="boolean" default="false">
  Should reasoning be the part of the final answer.
</ParamField>

<ParamField body="temperature" type="float" default="1">
  This setting influences the variety in the model's responses. Lower values lead to more predictable and typical responses, while higher values encourage more diverse and less common responses. At 0, the model always gives the same response for a given input. Default value: `1`

  Range: `0` to `2`
</ParamField>

<ParamField body="max_tokens" type="integer">
  This sets the upper limit for the number of tokens the model can generate in response. It won't produce more than this limit. The maximum value is the context length minus the prompt length.
</ParamField>

### Output Schema

<ParamField body="output" type="string" required>
  Generated output
</ParamField>

<ParamField body="usage" type="UsageInfo" required>
  Token usage information
</ParamField>

### Input Example

```json theme={null}
{
  "image_urls": [
    "https://fal.media/files/tiger/4Ew1xYW6oZCs6STQVC7V8_86440216d0fe42e4b826d03a2121468e.jpg"
  ],
  "prompt": "Caption this image for a text-to-image model with as much detail as possible.",
  "system_prompt": "Only answer the question, do not provide any additional information or add any prefix/suffix other than the answer of the original question. Don't use markdown.",
  "model": "google/gemini-2.5-flash",
  "reasoning": false,
  "temperature": 1
}
```

### Output Example

```json theme={null}
{
  "output": "A close-up of a tiger's face focusing on its bright orange iris and the area around its eye, with white fur eyebrows and a contrasting black and rich orange striped fur pattern. The word \"FLUX\" is overlaid in bold, white, brush-stroke styled text across the tiger's face.",
  "usage": {
    "completion_tokens": 63,
    "cost": 0.0005595,
    "prompt_tokens": 1340,
    "total_tokens": 1403
  }
}
```

## 🚀 Usage with OpenAI Client

```python theme={null}
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://fal.run/openrouter/router/openai/v1",
    api_key="not-needed",
    default_headers={
        "Authorization": f"Key {os.environ['FAL_KEY']}",
    },
)

response = client.chat.completions.create(
    model="google/gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": "Only answer the question, do not provide any additional information or add any prefix/suffix other than the answer of the original question. Don't use markdown.",
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Caption this image for a text-to-image model with as much detail as possible."},
                {
                    "type": "image_url",
                    "image_url": "https://fal.media/files/tiger/4Ew1xYW6oZCs6STQVC7V8_86440216d0fe42e4b826d03a2121468e.jpg",
                },
            ],
        },
    ],
    temperature=1,
)

print(response.choices[0].message.content)
```

## 🚿 Streaming Example

```python theme={null}
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://fal.run/openrouter/router/openai/v1",
    api_key="not-needed",
    default_headers={
        "Authorization": f"Key {os.environ['FAL_KEY']}",
    },
)

stream = client.chat.completions.create(
    model="google/gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": "Only answer the question, do not provide any additional information or add any prefix/suffix other than the answer of the original question. Don't use markdown.",
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Caption this image for a text-to-image model with as much detail as possible."},
                {
                    "type": "image_url",
                    "image_url": "https://fal.media/files/tiger/4Ew1xYW6oZCs6STQVC7V8_86440216d0fe42e4b826d03a2121468e.jpg",
                },
            ],
        },
    ],
    temperature=1,
    stream=True,
)

for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## 📚 Documentation

For more details, visit the official docs:

* 🔗 [OpenRouter API Docs](https://openrouter.ai/docs/quickstart)
* ⚡ [fal.ai API Docs](https://docs.fal.ai/model-apis)

## Limitations

* `temperature` range: 0 to 2
