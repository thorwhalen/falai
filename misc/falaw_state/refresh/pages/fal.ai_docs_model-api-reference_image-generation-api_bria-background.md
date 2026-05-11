> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bria Background API

> API reference for Bria Background. Bria RMBG 2.0 enables seamless removal of backgrounds from images, ideal for professional editing tasks. Trained exclusively on licensed data for safe and risk-free 

<Tabs>
  <Tab title="Remove">
    **Endpoint:** `POST https://fal.run/fal-ai/bria/background/remove`
    **Endpoint ID:** `fal-ai/bria/background/remove`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bria/background/remove/playground">
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
          "fal-ai/bria/background/remove",
          arguments={
              "image_url": "https://fal.media/files/panda/K5Rndvzmn1j-OI1VZXDVd.jpeg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bria/background/remove", {
        input: {
            image_url: "https://fal.media/files/panda/K5Rndvzmn1j-OI1VZXDVd.jpeg"
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
        --url https://fal.run/fal-ai/bria/background/remove \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://fal.media/files/panda/K5Rndvzmn1j-OI1VZXDVd.jpeg"
      }'
      ```
    </CodeGroup>

    ## Examples

    <Frame>
      <img src="https://v3.fal.media/files/lion/YBr6fXnaBoA_Hsy89qG6Q_44ab15cf50b0431fa4786c565c5b9032.png" alt="Example output from Bria RMBG 2.0" />
    </Frame>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      Input Image to erase from
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="Image" required>
      The generated image
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://fal.media/files/panda/K5Rndvzmn1j-OI1VZXDVd.jpeg",
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "content_type": "image/png",
        "file_name": "070c731993e949d993c10ef6283d335d.png",
        "file_size": 1076276,
        "height": 1024,
        "url": "https://v3.fal.media/files/tiger/GQEMNjRyxSoza7N8LPPqb_070c731993e949d993c10ef6283d335d.png",
        "width": 1024
      }
    }
    ```
  </Tab>

  <Tab title="Replace">
    **Endpoint:** `POST https://fal.run/fal-ai/bria/background/replace`
    **Endpoint ID:** `fal-ai/bria/background/replace`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/bria/background/replace/playground">
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
          "fal-ai/bria/background/replace",
          arguments={
              "image_url": "https://storage.googleapis.com/falserverless/bria/bria_bg_replace_fg.jpg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/bria/background/replace", {
        input: {
            image_url: "https://storage.googleapis.com/falserverless/bria/bria_bg_replace_fg.jpg"
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
        --url https://fal.run/fal-ai/bria/background/replace \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://storage.googleapis.com/falserverless/bria/bria_bg_replace_fg.jpg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      Input Image to erase from
    </ParamField>

    <ParamField body="ref_image_url" type="string" default="">
      The URL of the reference image to be used for generating the new background. Use "" to leave empty. Either ref\_image\_url or bg\_prompt has to be provided but not both. If both ref\_image\_url and ref\_image\_file are provided, ref\_image\_url will be used. Accepted formats are jpeg, jpg, png, webp. Default value: `""`
    </ParamField>

    <ParamField body="prompt" type="string">
      The prompt you would like to use to generate images.
    </ParamField>

    <ParamField body="negative_prompt" type="string" default="">
      The negative prompt you would like to use to generate images. Default value: `""`
    </ParamField>

    <ParamField body="refine_prompt" type="boolean" default="true">
      Whether to refine prompt Default value: `true`
    </ParamField>

    <ParamField body="seed" type="integer">
      The same seed and the same prompt given to the same version of the model
      will output the same image every time.

      Range: `0` to `2147483647`
    </ParamField>

    <ParamField body="fast" type="boolean" default="true">
      Whether to use the fast model Default value: `true`
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      Number of Images to generate. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<Image>" required>
      The generated images
    </ParamField>

    <ParamField body="seed" type="integer" required>
      Seed value used for generation.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://storage.googleapis.com/falserverless/bria/bria_bg_replace_fg.jpg",
      "ref_image_url": "https://storage.googleapis.com/falserverless/bria/bria_bg_replace_bg.jpg",
      "prompt": "Man leaning against a wall",
      "negative_prompt": "",
      "refine_prompt": true,
      "fast": true,
      "num_images": 1,
      "sync_mode": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "content_type": "image/png",
          "url": "https://storage.googleapis.com/falserverless/bria/bria_bg_replace_res.jpg"
        }
      ]
    }
    ```
  </Tab>
</Tabs>

Bria's RMBG 2.0 delivers production-grade background removal at \$0.018 per inference, trained exclusively on **licensed commercial data**. Trading breadth for legal certainty, this model solves the compliance headache that blocks most background removal tools from enterprise deployment. Built for teams that need defensible image segmentation without licensing risk.

**Use Cases:** E-commerce Product Photography | Marketing Asset Production | Professional Photo Editing

***

## Performance

At \$0.018 per generation, RMBG 2.0 is a **specialized utility model**, comparable to standard background removal pricing but with the critical differentiator of commercial licensing clarity.

| Metric                | Result                                                                                                                                                                                               | Context                                                |
| :-------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
| **Training Data**     | 100% licensed commercial imagery                                                                                                                                                                     | Legal defensibility for enterprise deployment          |
| **Cost per Image**    | \$0.018                                                                                                                                                                                              | 55 generations per \$1.00 on fal                       |
| **Input Format**      | Single image URL                                                                                                                                                                                     | Standard image-to-image pipeline                       |
| **Output Format**     | PNG with transparency                                                                                                                                                                                | 1024x1024 preserved dimensions                         |
| **Related Endpoints** | [Background Replace](https://fal.ai/models/fal-ai/bria/background/replace), [Product Shot](https://fal.ai/models/fal-ai/bria/product-shot), [Expand Image](https://fal.ai/models/fal-ai/bria/expand) | Same-family variants for product photography workflows |

***

## Built for Commercial Deployment

RMBG 2.0 uses a **segmentation architecture** trained exclusively on licensed data, contrasting sharply with open models trained on scraped web imagery.

**What this means for you:**

* **Enterprise-safe training data:** Every training image carries commercial licensing, eliminating copyright exposure in regulated industries

* **Transparent background removal:** Clean PNG output with alpha channel preservation for immediate compositing workflows

* **Single-purpose optimization:** Focused solely on background segmentation rather than multi-task compromise

* **Straightforward integration:** Standard image URL input via [fal's API](https://fal.ai/models/fal-ai/bria/background/remove/api) with synchronous or asynchronous processing modes

***

## Technical Specifications

| Spec               | Details                                      |
| :----------------- | :------------------------------------------- |
| **Architecture**   | Bria RMBG 2.0                                |
| **Input Formats**  | JPEG, PNG, WebP, GIF, AVIF via URL           |
| **Output Formats** | PNG with alpha channel transparency          |
| **Resolution**     | Up to 1024x1024 (preserves input dimensions) |
| **License**        | Commercial use with licensed training data   |

[API Documentation](https://fal.ai/models/fal-ai/bria/background/remove/api) | [Quickstart Guide](https://docs.fal.ai/model-apis/quickstart) | [Enterprise Pricing](https://fal.ai/pricing)

***

## How It Stacks Up

\*\*Bria Background Replace ($0.023)** – RMBG 2.0 ($0.018) strips backgrounds cleanly, 22% more cost-effective. [Background Replace](https://fal.ai/models/fal-ai/bria/background/replace) adds generative fill capabilities for product staging workflows where you need both removal and context reconstruction.

\*\*Bria Product Shot ($0.023)** – RMBG 2.0 ($0.018) handles pure segmentation, while [Product Shot](https://fal.ai/models/fal-ai/bria/product-shot) combines removal with studio-quality scene generation for e-commerce listings. Product Shot trades simplicity for complete product photography automation at 28% higher cost.

\*\*Bria Expand Image ($0.023)** – RMBG 2.0 focuses on isolation; [Expand Image](https://fal.ai/models/fal-ai/bria/expand) handles outpainting for aspect ratio adjustments post-removal. Teams typically chain RMBG 2.0 into Expand for complete product asset workflows, with Expand adding generative borders at $0.023 per operation.

## Related

* [Bria Expand Image](/model-api-reference/image-generation-api/bria-expand-image) — Image Generation
* [Bria Eraser](/model-api-reference/image-generation-api/bria-eraser) — Image Generation
* [Bria Product Shot](/model-api-reference/image-generation-api/bria-product-shot) — Image Generation
* [Bria Background Replace](/model-api-reference/image-generation-api/bria-background-replace) — Image Generation
* [Video](/model-api-reference/video-generation-api/video) — Video Generation
* [Bria GenFill](/model-api-reference/image-generation-api/bria-genfill) — Image Generation
* [Replace Background](/model-api-reference/image-generation-api/replace-background) — Image Generation
* [Bria Text-to-Image HD](/model-api-reference/image-generation-api/bria-text-to-image-hd) — Image Generation
* [Bria Text-to-Image Base](/model-api-reference/image-generation-api/bria-text-to-image-base) — Image Generation
* [Embed Product](/model-api-reference/image-generation-api/embed-product) — Image Generation
* [Bria Text-to-Image Fast](/model-api-reference/image-generation-api/bria-text-to-image-fast) — Image Generation
* [Bria RMBG 2.0](/model-api-reference/image-generation-api/bria-rmbg-2.0) — Image Generation

## Limitations

* `seed` range: 0 to 2147483647
* `num_images` range: 1 to 4
