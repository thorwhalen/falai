> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Whisper API

> API reference for Whisper. Whisper is a model for speech transcription and translation.

**Endpoint:** `POST https://fal.run/fal-ai/whisper`
**Endpoint ID:** `fal-ai/whisper`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/whisper/playground">
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
      "fal-ai/whisper",
      arguments={
          "audio_url": "https://storage.googleapis.com/falserverless/model_tests/whisper/dinner_conversation.mp3"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/whisper", {
    input: {
        audio_url: "https://storage.googleapis.com/falserverless/model_tests/whisper/dinner_conversation.mp3"
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
    --url https://fal.run/fal-ai/whisper \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "audio_url": "https://storage.googleapis.com/falserverless/model_tests/whisper/dinner_conversation.mp3"
  }'
  ```
</CodeGroup>

## Capabilities

* Audio input
* Text prompt input

## API Reference

### Input Schema

<ParamField body="audio_url" type="string" required>
  URL of the audio file to transcribe. Supported formats: mp3, mp4, mpeg, mpga, m4a, wav or webm.
</ParamField>

<ParamField body="task" type="TaskEnum" default="transcribe">
  Task to perform on the audio file. Either transcribe or translate. Default value: `"transcribe"`

  Possible values: `transcribe`, `translate`
</ParamField>

<ParamField body="language" type="Enum">
  Language of the audio file. If set to null, the language will be
  automatically detected. Defaults to null.

  If translate is selected as the task, the audio will be translated to
  English, regardless of the language selected.

  Possible values: `af`, `am`, `ar`, `as`, `az`, `ba`, `be`, `bg`, `bn`, `bo`, `br`, `bs`, `ca`, `cs`, `cy`, `da`, `de`, `el`, `en`, `es`, `et`, `eu`, `fa`, `fi`, `fo`, `fr`, `gl`, `gu`, `ha`, `haw`, `he`, `hi`, `hr`, `ht`, `hu`, `hy`, `id`, `is`, `it`, `ja`, `jw`, `ka`, `kk`, `km`, `kn`, `ko`, `la`, `lb`, `ln`, `lo`, `lt`, `lv`, `mg`, `mi`, `mk`, `ml`, `mn`, `mr`, `ms`, `mt`, `my`, `ne`, `nl`, `nn`, `no`, `oc`, `pa`, `pl`, `ps`, `pt`, `ro`, `ru`, `sa`, `sd`, `si`, `sk`, `sl`, `sn`, `so`, `sq`, `sr`, `su`, `sv`, `sw`, `ta`, `te`, `tg`, `th`, `tk`, `tl`, `tr`, `tt`, `uk`, `ur`, `uz`, `vi`, `yi`, `yo`, `zh`
</ParamField>

<ParamField body="diarize" type="boolean" default="false">
  Whether to diarize the audio file. Defaults to false. Setting to true will add costs proportional to diarization inference time.
</ParamField>

<ParamField body="chunk_level" type="ChunkLevelEnum" default="segment">
  Level of the chunks to return. Either none, segment or word. `none` would imply that all of the audio will be transcribed without the timestamp tokens, we suggest to switch to `none` if you are not satisfied with the transcription quality, since it will usually improve the quality of the results. Switching to `none` will also provide minor speed ups in the transcription due to less amount of generated tokens. Notice that setting to none will produce **a single chunk with the whole transcription**. Default value: `"segment"`

  Possible values: `none`, `segment`, `word`
</ParamField>

<ParamField body="batch_size" type="integer" default="64">
  Default value: `64`

  Range: `1` to `64`
</ParamField>

<ParamField body="prompt" type="string" default="">
  Prompt to use for generation. Defaults to an empty string. Default value: `""`
</ParamField>

<ParamField body="num_speakers" type="integer">
  Number of speakers in the audio file. Defaults to null.
  If not provided, the number of speakers will be automatically
  detected.
</ParamField>

### Output Schema

<ParamField body="text" type="string" required>
  Transcription of the audio file
</ParamField>

<ParamField body="chunks" type="list<WhisperChunk>">
  Timestamp chunks of the audio file
</ParamField>

<ParamField body="inferred_languages" type="list<Enum>" required>
  List of languages that the audio file is inferred to be. Defaults to null.
</ParamField>

<ParamField body="diarization_segments" type="list<DiarizationSegment>" required>
  Speaker diarization segments of the audio file. Only present if diarization is enabled.
</ParamField>

## Input Example

```json theme={null}
{
  "audio_url": "https://storage.googleapis.com/falserverless/model_tests/whisper/dinner_conversation.mp3",
  "task": "transcribe",
  "diarize": false,
  "chunk_level": "segment",
  "batch_size": 64,
  "prompt": "",
  "num_speakers": null
}
```

## Output Example

```json theme={null}
{
  "text": "María, ¿qué cenamos hoy? No sé, ¿qué cenamos? ¿Cenamos pollo frito o pollo asado o algo? Mejor a la plancha, quiero una salada. A la plancha, vale. Y hacemos una ensalada con tomate y esas cosas. Vale. Pues eso lo hacemos, ¿vale? Venga, vale.",
  "chunks": [
    {
      "text": ""
    }
  ],
  "diarization_segments": [
    {
      "speaker": ""
    }
  ]
}
```

## Limitations

* `task` restricted to: `transcribe`, `translate`
* `chunk_level` restricted to: `none`, `segment`, `word`
* `batch_size` range: 1 to 64
