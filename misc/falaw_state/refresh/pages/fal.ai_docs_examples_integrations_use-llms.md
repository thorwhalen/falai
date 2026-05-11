> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use LLMs Tutorial

> fal provides an easy-to-use API for generating text using Language Models (LLMs). You can use the `fal-ai/any-llm` endpoint to generate text based on a given prompt and model.

Here’s an example of how to use the `fal-ai/any-llm` endpoint to generate text using the `anthropic/claude-3.5-sonnet` model:

```js theme={null}
import { fal } from "@fal-ai/client";

const result = await fal.subscribe("fal-ai/any-llm", {
  input: {
    model: "anthropic/claude-3.5-sonnet",
    prompt: "What is the meaning of life?"
  },
});
```

## How to select LLM model to use

fal offers a variety of LLM models. You can select the model that best fits your needs based on the style and quality of the text you want to generate. Here are some of the available models:

* `anthropic/claude-3.5-sonnet`: Claude 3.5 Sonnet
* `google/gemini-pro-1.5`: Gemini Pro 1.5
* `meta-llama/llama-3.2-3b-instruct`: Llama 3.2 3B Instruct
* `openai/gpt-4o`: GPT-4o

To select a model, simply specify the model ID in the `model` field as shown in the example above. You can find more LLMs in the [Any LLM](https://fal.ai/models/fal-ai/any-llm) page.
