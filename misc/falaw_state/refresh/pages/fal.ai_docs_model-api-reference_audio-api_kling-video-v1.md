> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video V1 API

> API reference for Kling Video V1. Generate speech from text prompts and different voices using the Kling TTS model, which leverages advanced AI techniques to create high-quality text-to-speech.

**Endpoint:** `POST https://fal.run/fal-ai/kling-video/v1/tts`
**Endpoint ID:** `fal-ai/kling-video/v1/tts`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/v1/tts/playground">
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
      "fal-ai/kling-video/v1/tts",
      arguments={
          "text": "Hello world! Kling TTS is available on FAL!"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/kling-video/v1/tts", {
    input: {
        text: "Hello world! Kling TTS is available on FAL!"
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
    --url https://fal.run/fal-ai/kling-video/v1/tts \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "text": "Hello world! Kling TTS is available on FAL!"
  }'
  ```
</CodeGroup>

### Input Schema

<ParamField body="text" type="string" required>
  The text to be converted to speech
</ParamField>

<ParamField body="voice_id" type="VoiceIdEnum" default="genshin_vindi2">
  The voice ID to use for speech synthesis Default value: `"genshin_vindi2"`

  Possible values: `genshin_vindi2`, `zhinen_xuesheng`, `AOT`, `ai_shatang`, `genshin_klee2`, `genshin_kirara`, `ai_kaiya`, `oversea_male1`, `ai_chenjiahao_712`, `girlfriend_4_speech02`, `chat1_female_new-3`, `chat_0407_5-1`, `cartoon-boy-07`, `uk_boy1`, `cartoon-girl-01`, `PeppaPig_platform`, `ai_huangzhong_712`, `ai_huangyaoshi_712`, `ai_laoguowang_712`, `chengshu_jiejie`, `you_pingjing`, `calm_story1`, `uk_man2`, `laopopo_speech02`, `heainainai_speech02`, `reader_en_m-v1`, `commercial_lady_en_f-v1`, `tiyuxi_xuedi`, `tiexin_nanyou`, `girlfriend_1_speech02`, `girlfriend_2_speech02`, `zhuxi_speech02`, `uk_oldman3`, `dongbeilaotie_speech02`, `chongqingxiaohuo_speech02`, `chuanmeizi_speech02`, `chaoshandashu_speech02`, `ai_taiwan_man2_speech02`, `xianzhanggui_speech02`, `tianjinjiejie_speech02`, `diyinnansang_DB_CN_M_04-v2`, `yizhipiannan-v1`, `guanxiaofang-v2`, `tianmeixuemei-v1`, `daopianyansang-v1`, `mengwa-v1`
</ParamField>

<ParamField body="voice_speed" type="float" default="1">
  Rate of speech Default value: `1`

  Range: `0.8` to `2`
</ParamField>

### Output Schema

<ParamField body="audio" type="File" required>
  The generated audio
</ParamField>

### Input Example

```json theme={null}
{
  "text": "Hello world! Kling TTS is available on FAL!",
  "voice_id": "genshin_vindi2",
  "voice_speed": 1
}
```

### Output Example

```json theme={null}
{
  "audio": {
    "url": "https://v3.fal.media/files/monkey/O-ekVTtYqeDblD1oSf2uv_output.mp3"
  }
}
```

## Related

* [Kling AI Avatar v2 Pro](/model-api-reference/video-generation-api/kling-ai-avatar-v2-pro) — Video Generation
* [Kling AI Avatar v2 Standard](/model-api-reference/video-generation-api/kling-ai-avatar-v2-standard) — Video Generation
* [Kling AI Avatar](/model-api-reference/video-generation-api/kling-ai-avatar) — Video Generation
* [Kling AI Avatar Pro](/model-api-reference/video-generation-api/kling-ai-avatar-pro) — Video Generation

## Limitations

* `voice_speed` range: 0.8 to 2
