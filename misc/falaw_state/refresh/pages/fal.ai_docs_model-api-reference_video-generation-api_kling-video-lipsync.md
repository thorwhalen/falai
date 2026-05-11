> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Video Lipsync API

> API reference for Kling Video Lipsync. Kling LipSync is an audio-to-video model that generates realistic lip movements from audio input.

<Tabs>
  <Tab title="Audio To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/lipsync/audio-to-video`
    **Endpoint ID:** `fal-ai/kling-video/lipsync/audio-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/lipsync/audio-to-video/playground">
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
          "fal-ai/kling-video/lipsync/audio-to-video",
          arguments={
              "video_url": "https://fal.media/files/koala/8teUPbRRMtAUTORDvqy0l.mp4",
              "audio_url": "https://storage.googleapis.com/falserverless/kling/kling-audio.mp3"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/lipsync/audio-to-video", {
        input: {
            video_url: "https://fal.media/files/koala/8teUPbRRMtAUTORDvqy0l.mp4",
            audio_url: "https://storage.googleapis.com/falserverless/kling/kling-audio.mp3"
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
        --url https://fal.run/fal-ai/kling-video/lipsync/audio-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "video_url": "https://fal.media/files/koala/8teUPbRRMtAUTORDvqy0l.mp4",
        "audio_url": "https://storage.googleapis.com/falserverless/kling/kling-audio.mp3"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="video_url" type="string" required>
      The URL of the video to generate the lip sync for. Supports .mp4/.mov, ≤100MB, 2–10s, 720p/1080p only, width/height 720–1920px.
    </ParamField>

    <ParamField body="audio_url" type="string" required>
      The URL of the audio to generate the lip sync for. Minimum duration is 2s and maximum duration is 60s. Maximum file size is 5MB.
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "video_url": "https://fal.media/files/koala/8teUPbRRMtAUTORDvqy0l.mp4",
      "audio_url": "https://storage.googleapis.com/falserverless/kling/kling-audio.mp3"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://storage.googleapis.com/falserverless/kling/kling_output.mp4"
      }
    }
    ```
  </Tab>

  <Tab title="Text To Video">
    **Endpoint:** `POST https://fal.run/fal-ai/kling-video/lipsync/text-to-video`
    **Endpoint ID:** `fal-ai/kling-video/lipsync/text-to-video`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/kling-video/lipsync/text-to-video/playground">
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
          "fal-ai/kling-video/lipsync/text-to-video",
          arguments={
              "video_url": "https://fal.media/files/koala/8teUPbRRMtAUTORDvqy0l.mp4",
              "text": "Mental health is as important as physical health, shaping our emotions, thoughts, and daily interactions.",
              "voice_id": "genshin_klee2"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/kling-video/lipsync/text-to-video", {
        input: {
            video_url: "https://fal.media/files/koala/8teUPbRRMtAUTORDvqy0l.mp4",
            text: "Mental health is as important as physical health, shaping our emotions, thoughts, and daily interactions.",
            voice_id: "genshin_klee2"
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
        --url https://fal.run/fal-ai/kling-video/lipsync/text-to-video \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "video_url": "https://fal.media/files/koala/8teUPbRRMtAUTORDvqy0l.mp4",
        "text": "Mental health is as important as physical health, shaping our emotions, thoughts, and daily interactions.",
        "voice_id": "genshin_klee2"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="video_url" type="string" required>
      The URL of the video to generate the lip sync for. Supports .mp4/.mov, ≤100MB, 2-60s, 720p/1080p only, width/height 720–1920px. If validation fails, an error is returned.
    </ParamField>

    <ParamField body="text" type="string" required>
      Text content for lip-sync video generation. Max 120 characters.
    </ParamField>

    <ParamField body="voice_id" type="VoiceIdEnum" required>
      Voice ID to use for speech synthesis

      Possible values: `genshin_vindi2`, `zhinen_xuesheng`, `AOT`, `ai_shatang`, `genshin_klee2`, `genshin_kirara`, `ai_kaiya`, `oversea_male1`, `ai_chenjiahao_712`, `girlfriend_4_speech02`, `chat1_female_new-3`, `chat_0407_5-1`, `cartoon-boy-07`, `uk_boy1`, `cartoon-girl-01`, `PeppaPig_platform`, `ai_huangzhong_712`, `ai_huangyaoshi_712`, `ai_laoguowang_712`, `chengshu_jiejie`, `you_pingjing`, `calm_story1`, `uk_man2`, `laopopo_speech02`, `heainainai_speech02`, `reader_en_m-v1`, `commercial_lady_en_f-v1`, `tiyuxi_xuedi`, `tiexin_nanyou`, `girlfriend_1_speech02`, `girlfriend_2_speech02`, `zhuxi_speech02`, `uk_oldman3`, `dongbeilaotie_speech02`, `chongqingxiaohuo_speech02`, `chuanmeizi_speech02`, `chaoshandashu_speech02`, `ai_taiwan_man2_speech02`, `xianzhanggui_speech02`, `tianjinjiejie_speech02`, `diyinnansang_DB_CN_M_04-v2`, `yizhipiannan-v1`, `guanxiaofang-v2`, `tianmeixuemei-v1`, `daopianyansang-v1`, `mengwa-v1`
    </ParamField>

    <ParamField body="voice_language" type="VoiceLanguageEnum" default="en">
      The voice language corresponding to the Voice ID Default value: `"en"`

      Possible values: `zh`, `en`
    </ParamField>

    <ParamField body="voice_speed" type="float" default="1">
      Speech rate for Text to Video generation Default value: `1`

      Range: `0.8` to `2`
    </ParamField>

    ### Output Schema

    <ParamField body="video" type="File" required>
      The generated video
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "video_url": "https://fal.media/files/koala/8teUPbRRMtAUTORDvqy0l.mp4",
      "text": "Mental health is as important as physical health, shaping our emotions, thoughts, and daily interactions.",
      "voice_id": "genshin_klee2",
      "voice_language": "en",
      "voice_speed": 1
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "video": {
        "url": "https://storage.googleapis.com/falserverless/kling/kling_text_lipsync.mp4"
      }
    }
    ```
  </Tab>
</Tabs>

Kuaishou's Kling LipSync generates realistic lip-synchronized video from audio input in approximately 12 minutes at \$0.014 per 5-second increment. Trading speed for precision lip-sync accuracy, the model handles 2-10 second source videos with audio up to 60 seconds. Purpose-built for dubbing, content localization, and audio-driven character animation where **mouth movement realism** matters more than generation time.

**Use Cases:** Video Dubbing & Translation | Audio-Driven Character Animation | Content Localization for Global Markets

***

## Performance

At \$0.014 per 5-second video increment (rounded up), Kling LipSync positions as a specialized audio-to-video tool trading inference speed for **lip-sync precision**. Processing takes approximately 12 minutes regardless of video duration within the 2-10 second input range.

| Metric                   | Result                   | Context                                              |
| :----------------------- | :----------------------- | :--------------------------------------------------- |
| **Inference Speed**      | \~12 minutes             | Fixed processing time for 2-10s input videos         |
| **Cost per Video**       | \$0.014 per 5s increment | Billed in 5-second increments (3s video = 5s charge) |
| **Input Video Duration** | 2-10 seconds             | 720p/1080p, ≤100MB, .mp4/.mov only                   |
| **Audio Duration**       | 2-60 seconds             | ≤5MB file size, .mp3/.wav/.ogg/.m4a/.aac formats     |
| **Resolution Support**   | 720p-1080p               | Width/height constrained to 720-1920px               |

***

## Precision Lip-Sync Without Training Data

Kling LipSync uses audio-driven facial animation architecture that generates mouth movements directly from audio waveforms without requiring speaker-specific training data, contrasting with traditional lip-sync approaches that need extensive footage of the target speaker.

**What this means for you:**

* **Zero-shot speaker adaptation:** Sync any audio to any face without pre-training on that specific person, enabling rapid dubbing workflows across multiple speakers and languages

* **Extended audio support:** Process up to 60 seconds of audio against 2-10 second video clips, useful for looping background characters or extending dialogue beyond source footage length

* **Format flexibility:** Accepts 5 audio formats (.mp3, .wav, .ogg, .m4a, .aac) and standard video containers (.mp4, .mov), integrating into existing [video generation workflows](https://fal.ai/models) without format conversion overhead

* **Increment-based pricing transparency:** 5-second billing increments mean predictable costs (a 3-second video costs the same as 5 seconds at $0.014, a 7-second video bills as 10 seconds at $0.028)

***

## Technical Specifications

| Spec                        | Details                                                                               |
| :-------------------------- | :------------------------------------------------------------------------------------ |
| **Architecture**            | Kling LipSync                                                                         |
| **Input Formats**           | Video: .mp4, .mov (2-10s, ≤100MB) / Audio: .mp3, .wav, .ogg, .m4a, .aac (2-60s, ≤5MB) |
| **Output Formats**          | .mp4 video with synchronized lip movements                                            |
| **Resolution Requirements** | 720p or 1080p input, width/height 720-1920px                                          |
| **License**                 | Commercial use via fal partnership                                                    |

[API Documentation](https://fal.ai/models/fal-ai/kling-video/lipsync/audio-to-video/api) | [Quickstart Guide](https://docs.fal.ai/model-apis/quickstart) | [Enterprise Pricing](https://fal.ai/pricing)

## Related

* [Kling LipSync Text-to-Video](/model-api-reference/video-generation-api/kling-lipsync-text-to-video) — Video Generation
* [Kling LipSync Audio-to-Video](/model-api-reference/video-generation-api/kling-lipsync-audio-to-video) — Video Generation

## Limitations

* `voice_language` restricted to: `zh`, `en`
* `voice_speed` range: 0.8 to 2
