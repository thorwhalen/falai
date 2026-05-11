> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bytedance Seedream V5 Lite API

> API reference for Bytedance Seedream V5 Lite. Image editing endpoint for the fast Lite version of Seedream 5.0, supporting high quality intelligent image editing with multiple inputs.

<Tabs>
  <Tab title="Edit">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedream/v5/lite/edit`
    **Endpoint ID:** `fal-ai/bytedance/seedream/v5/lite/edit`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedream/v5/lite/edit/playground">
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
          "fal-ai/bytedance/seedream/v5/lite/edit",
          arguments={
              "prompt": "Replace the product in Figure 1 with that in Figure 2. Seamlessly render logo in Figure 3 into the product design, in frosted glass texture. Remove any extra text in Figure 1, and design a catchy tagline for the perfume.",
              "image_urls": [
                  "https://v3b.fal.media/files/b/0a8f9936/KOsb_qPB_W0ZJ0Ee2OsnU_586e2892841d46f09049ee7199b303d3.png",
                  "https://v3b.fal.media/files/b/0a8f994e/JroWTogO6jOTFk9b6B3XM_591ca38cef2f44bbba2843cbf80fb1b2.png",
                  "https://v3b.fal.media/files/b/0a8f9960/Q6pzwXAiFaFPOpSScoE-D_0eca5db19e5242739f127efe49b38922.png"
              ]
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/seedream/v5/lite/edit", {
        input: {
            prompt: "Replace the product in Figure 1 with that in Figure 2. Seamlessly render logo in Figure 3 into the product design, in frosted glass texture. Remove any extra text in Figure 1, and design a catchy tagline for the perfume.",
            image_urls: [
              "https://v3b.fal.media/files/b/0a8f9936/KOsb_qPB_W0ZJ0Ee2OsnU_586e2892841d46f09049ee7199b303d3.png",
              "https://v3b.fal.media/files/b/0a8f994e/JroWTogO6jOTFk9b6B3XM_591ca38cef2f44bbba2843cbf80fb1b2.png",
              "https://v3b.fal.media/files/b/0a8f9960/Q6pzwXAiFaFPOpSScoE-D_0eca5db19e5242739f127efe49b38922.png"
            ]
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
        --url https://fal.run/fal-ai/bytedance/seedream/v5/lite/edit \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Replace the product in Figure 1 with that in Figure 2. Seamlessly render logo in Figure 3 into the product design, in frosted glass texture. Remove any extra text in Figure 1, and design a catchy tagline for the perfume.",
        "image_urls": [
          "https://v3b.fal.media/files/b/0a8f9936/KOsb_qPB_W0ZJ0Ee2OsnU_586e2892841d46f09049ee7199b303d3.png",
          "https://v3b.fal.media/files/b/0a8f994e/JroWTogO6jOTFk9b6B3XM_591ca38cef2f44bbba2843cbf80fb1b2.png",
          "https://v3b.fal.media/files/b/0a8f9960/Q6pzwXAiFaFPOpSScoE-D_0eca5db19e5242739f127efe49b38922.png"
        ]
      }'
      ```
    </CodeGroup>

    ## Examples

    > Change the season to winter. Cover everything in fresh white snow. The trees should be bare with snow on branches. The fallen leaves are replaced by snow. Overcast grey sky. The red car has a thin layer of snow on the hood and roof. Tire tracks in the fresh snow on the road.

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a8fc1a0/MX84wRTkjQh3JwBRTnvwj_5f3fd60da05144579bd30ada3997da10.png" alt="Generated image: Change the season to winter. Cover everything in fresh white snow. The trees sho" />
    </Frame>

    > Transform these into fluffy Japanese souffle pancakes. Make them much thicker and jigglier looking, tall and wobbly. Add a scoop of vanilla ice cream on top with a drizzle of honey. A small ceramic cup of matcha on the side. Change the setting to a cute Japanese cafe table with a checkered placemat....

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a8fc22e/yYBznQsdzYgLDcFlhVOMQ_152dac218a2549dda8c4b82c0b256718.png" alt="Generated image: Transform these into fluffy Japanese souffle pancakes. Make them much thicker an" />
    </Frame>

    > Change the weather to an approaching thunderstorm. Dark dramatic storm clouds rolling over the mountains. Lightning bolt striking one of the peaks in the distance. The lake surface is choppy with small waves. Wind bending the trees. The light is eerie and dramatic with a break in the clouds letting ...

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a8fc222/jcpgLgFk3hbrWS_3N32km_89ced5799c884b7c9ba80d19a4e89229.png" alt="Generated image: Change the weather to an approaching thunderstorm. Dark dramatic storm clouds ro" />
    </Frame>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt used to edit the image
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="auto_2K">
      The size of the generated image. Total pixels must be between 2560x1440 and 3072x3072. In case the image size does not fall within these parameters, the image size will be adjusted to by scaling. Default value: `auto_2K`

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`, `auto_2K`, `auto_3K`
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      Number of separate model generations to be run with the prompt. Default value: `1`

      Range: `1` to `6`
    </ParamField>

    <ParamField body="max_images" type="integer" default="1">
      If set to a number greater than one, enables multi-image generation. The model will potentially return up to `max_images` images every generation, and in total, `num_images` generations will be carried out. In total, the number of images generated will be between `num_images` and `max_images*num_images`. Default value: `1`

      Range: `1` to `6`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    <ParamField body="image_urls" type="list<string>" required>
      List of URLs of input images for editing. Presently, up to 10 image inputs are allowed. If over 10 images are sent, only the last 10 will be used.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
      Generated images
    </ParamField>

    <ParamField body="seed" type="integer" required>
      Seed used for generation.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Replace the product in Figure 1 with that in Figure 2. Seamlessly render logo in Figure 3 into the product design, in frosted glass texture. Remove any extra text in Figure 1, and design a catchy tagline for the perfume.",
      "image_size": "auto_2K",
      "num_images": 1,
      "max_images": 1,
      "sync_mode": false,
      "enable_safety_checker": true,
      "image_urls": [
        "https://v3b.fal.media/files/b/0a8f9936/KOsb_qPB_W0ZJ0Ee2OsnU_586e2892841d46f09049ee7199b303d3.png",
        "https://v3b.fal.media/files/b/0a8f994e/JroWTogO6jOTFk9b6B3XM_591ca38cef2f44bbba2843cbf80fb1b2.png",
        "https://v3b.fal.media/files/b/0a8f9960/Q6pzwXAiFaFPOpSScoE-D_0eca5db19e5242739f127efe49b38922.png"
      ]
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://v3b.fal.media/files/b/0a8fbf56/wu9vcxO3xO6lkHv5zdiIs_7aa8564f6e4f4cc795ecb8e923deb2fb.png"
        }
      ],
      "seed": 42
    }
    ```
  </Tab>

  <Tab title="Text To Image">
    **Endpoint:** `POST https://fal.run/fal-ai/bytedance/seedream/v5/lite/text-to-image`
    **Endpoint ID:** `fal-ai/bytedance/seedream/v5/lite/text-to-image`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bytedance/seedream/v5/lite/text-to-image/playground">
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
          "fal-ai/bytedance/seedream/v5/lite/text-to-image",
          arguments={
              "prompt": "Realistic DSLR photograph of anthropomorphic Penkingese dog enjoying a bowl of ramen on the Great Wall of China with the words \"Seedream 5.0 Lite available on fal\" visible at the top."
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bytedance/seedream/v5/lite/text-to-image", {
        input: {
            prompt: "Realistic DSLR photograph of anthropomorphic Penkingese dog enjoying a bowl of ramen on the Great Wall of China with the words \"Seedream 5.0 Lite available on fal\" visible at the top."
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
        --url https://fal.run/fal-ai/bytedance/seedream/v5/lite/text-to-image \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "Realistic DSLR photograph of anthropomorphic Penkingese dog enjoying a bowl of ramen on the Great Wall of China with the words \"Seedream 5.0 Lite available on fal\" visible at the top."
      }'
      ```
    </CodeGroup>

    ## Examples

    > A crumbling medieval stone castle floating on a massive chunk of earth above the clouds, thick roots dangling from the bottom, waterfalls cascading off the edges into the mist below, sunset sky painted in amber and violet, a flock of birds circling one tower, cinematic matte painting style, epic fan...

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a8fc193/EKCKuHaYvSdxTaaD4lC0R_b0d7ebf49f1549e69be167d6c84b2070.png" alt="Generated image: A crumbling medieval stone castle floating on a massive chunk of earth above the" />
    </Frame>

    > A cozy attic reading nook on a rainy afternoon, warm watercolor illustration style. An overstuffed armchair with a patchwork quilt draped over it, a steaming mug of tea on a stack of books, a cat curled up on the windowsill watching rain streak down the glass. Soft warm lamplight, muted earth tones ...

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a8fc193/Hisi7JfhJPercCx4ELfkd_f6878a536b4d4ad48421cdb4049851df.png" alt="Generated image: A cozy attic reading nook on a rainy afternoon, warm watercolor illustration sty" />
    </Frame>

    > On the left side of a small round marble cafe table, a man in a rust-colored linen shirt leaning forward with his chin on his hand. On the right side, a woman in an oversized cream knit sweater laughing with her head tilted back. Two steaming cappuccinos between them, a croissant on a plate. Warm Pa...

    <Frame>
      <img src="https://v3b.fal.media/files/b/0a8fc18e/8nwm9eNsIdO_pcJhyNc1P_40662ec4209a4dcf9601544a1e776465.png" alt="Generated image: On the left side of a small round marble cafe table, a man in a rust-colored lin" />
    </Frame>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The text prompt used to generate the image
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="auto_2K">
      The size of the generated image. Total pixels must be between 2560x1440 and 3072x3072. In case the image size does not fall within these parameters, the image size will be adjusted to by scaling. Default value: `auto_2K`

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`, `auto_2K`, `auto_3K`
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      Number of separate model generations to be run with the prompt. Default value: `1`

      Range: `1` to `6`
    </ParamField>

    <ParamField body="max_images" type="integer" default="1">
      If set to a number greater than one, enables multi-image generation. The model will potentially return up to `max_images` images every generation, and in total, `num_images` generations will be carried out. In total, the number of images generated will be between `num_images` and `max_images*num_images`. Default value: `1`

      Range: `1` to `6`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
      Generated images
    </ParamField>

    <ParamField body="seed" type="integer" required>
      Seed used for generation.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "Realistic DSLR photograph of anthropomorphic Penkingese dog enjoying a bowl of ramen on the Great Wall of China with the words \"Seedream 5.0 Lite available on fal\" visible at the top.",
      "image_size": "auto_2K",
      "num_images": 1,
      "max_images": 1,
      "sync_mode": false,
      "enable_safety_checker": true
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "url": "https://v3b.fal.media/files/b/0a8fbf48/fv693UaOADKqnujJRZN90_4518fc5e1fed4fb29963b22a8cc3d5a6.png"
        }
      ],
      "seed": 42
    }
    ```
  </Tab>
</Tabs>

ByteDance's Seedream 5.0 Lite delivers fast, intelligent and high quality image editing suitable for creative advertising and real-world usecases. It can process up to 10 reference images simultaneously for complex multi-source compositions.

**Built for:** Product mockup generation | Marketing asset creation | Creative iteration workflows

***

**What this means for you:**

* **High-resolution output:** Generate images up to 3072x3072 pixels with flexible aspect ratios.
* **Multi-image generation:** Request up to 6 separate generations per API call, with the option to generate multiple variations per generation using `max_images`
* **Safety integration:** Built-in content filtering enabled by default, with the option to disable for controlled environments

***

| Metric                   | Result          | Context                                                             |
| :----------------------- | :-------------- | :------------------------------------------------------------------ |
| **Cost per Image**       | \$0.035         | Cheaper than Nano Banana and Seedream 4.5                           |
| **Max Resolution**       | 9MP (3072x3072) | Total pixel count between 3.7MP and 9.43MP supported                |
| **Batch Capability**     | 1-6 images      | Per generation, with multi-generation support via `max_images`      |
| **Max Reference Images** | 10 images       | Multi-source composition capability (last 10 used if more provided) |
| **Output Format**        | PNG via URL     | Async by default, sync mode available for data URI returns          |

***

## Technical Specifications

| Spec                 | Details                                             |
| :------------------- | :-------------------------------------------------- |
| **Architecture**     | Seedream 5.0 Lite                                   |
| **Input Formats**    | Text prompts with detailed natural language support |
| **Output Formats**   | PNG images delivered via HTTPS URL or data URI      |
| **Resolution Range** | 2560x1440 to 3072x3072 total pixels                 |
| **License**          | Commercial use permitted under partner agreement    |

## Related

* [Bytedance](/model-api-reference/image-generation-api/bytedance) — Image Generation

## Limitations

* `image_size` restricted to: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`, `auto_2K`, `auto_3K`
* `num_images` range: 1 to 6
* `max_images` range: 1 to 6
* Content moderation via safety checker
