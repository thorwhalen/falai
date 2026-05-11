> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal api

Call any model on fal directly from the command line. Useful for quick testing without writing code.

## Usage

```bash theme={null}
fal api <model_id> [key=value ...]
```

**Arguments:**

| Argument   | Description                                                      |
| ---------- | ---------------------------------------------------------------- |
| `model_id` | The model endpoint to call (e.g., `fal-ai/flux/schnell`)         |
| `params`   | Key-value pairs for the request body (e.g., `prompt="a sunset"`) |

## Examples

**Generate an image:**

```bash theme={null}
fal api fal-ai/flux/schnell prompt="a cat wearing sunglasses"
```

The CLI shows real-time status updates (queued, in progress) and logs while the request is processing, then prints the result.

**Nested parameters:**

Use bracket notation for nested values:

```bash theme={null}
fal api fal-ai/flux/schnell prompt="a sunset" image_size[width]:=1280 image_size[height]:=720
```

Use `:=` for non-string values (numbers, booleans):

```bash theme={null}
fal api fal-ai/flux/schnell prompt="a sunset" num_images:=4 seed:=42
```

**Streaming endpoints:**

If the model ID ends with `/stream`, the CLI streams output as it's generated:

```bash theme={null}
fal api fal-ai/any-llm/stream prompt="What is the meaning of life?" model=google/gemini-flash-1.5
```

## How It Works

* For regular endpoints: submits via the queue, polls for status with live log display, then prints the result
* For `/stream` endpoints: connects via streaming and prints output as it arrives
* Uses your configured `FAL_KEY` for authentication
