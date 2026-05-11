> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Xai Tts API

> API reference for Xai Tts. Generate speech with expressive and realistic voices from xAI

**Endpoint:** `POST https://fal.run/xai/tts/v1`
**Endpoint ID:** `xai/tts/v1`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/xai/tts/v1/playground">
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
      "xai/tts/v1",
      arguments={
          "text": "Hello! This is xAI text to speech, brought to you by Fal AI."
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("xai/tts/v1", {
    input: {
        text: "Hello! This is xAI text to speech, brought to you by Fal AI."
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
    --url https://fal.run/xai/tts/v1 \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "text": "Hello! This is xAI text to speech, brought to you by Fal AI."
  }'
  ```
</CodeGroup>

### Input Schema

<ParamField body="text" type="string" required>
  The text to convert to speech. Maximum 15,000 characters. Supports speech tags for expressive delivery: inline tags like \[laugh], \[pause], \[sigh] and wrapping tags like \<whisper>text\</whisper>, \<slow>text\</slow>.
</ParamField>

<ParamField body="voice" type="VoiceEnum" default="eve">
  Voice to use for synthesis. eve: energetic, upbeat. ara: warm, friendly. rex: confident, clear. sal: smooth, balanced. leo: authoritative, strong. Default value: `"eve"`

  Possible values: `eve`, `ara`, `rex`, `sal`, `leo`
</ParamField>

<ParamField body="language" type="LanguageEnum" default="auto">
  BCP-47 language code or 'auto' for automatic detection. Supported: en, zh, fr, de, hi, id, it, ja, ko, pt-BR, pt-PT, ru, es-MX, es-ES, tr, vi, bn, ar-EG, ar-SA, ar-AE. Default value: `"auto"`

  Possible values: `auto`, `en`, `ar-EG`, `ar-SA`, `ar-AE`, `bn`, `zh`, `fr`, `de`, `hi`, `id`, `it`, `ja`, `ko`, `pt-BR`, `pt-PT`, `ru`, `es-MX`, `es-ES`, `tr`, `vi`
</ParamField>

<ParamField body="output_format" type="OutputFormat">
  Output format configuration. Defaults to MP3 at 24 kHz / 128 kbps.
</ParamField>

### Output Schema

<ParamField body="audio" type="File" required>
  The generated audio file.
</ParamField>

### Input Example

```json theme={null}
{
  "text": "Hello! This is xAI text to speech, brought to you by Fal AI.",
  "voice": "eve",
  "language": "auto"
}
```

### Output Example

```json theme={null}
{
  "audio": {
    "url": "https://v3b.fal.media/files/b/0a92750b/exZJCm6TDejS5xIulJs2r_xai_tts_output.mp3"
  }
}
```

## Limitations

* `voice` restricted to: `eve`, `ara`, `rex`, `sal`, `leo`
