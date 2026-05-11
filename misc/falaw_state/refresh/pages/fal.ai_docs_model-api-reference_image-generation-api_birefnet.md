> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Birefnet API

> API reference for Birefnet. bilateral reference framework (BiRefNet) for high-resolution dichotomous image segmentation (DIS)

<Tabs>
  <Tab title="Birefnet">
    **Endpoint:** `POST https://fal.run/fal-ai/birefnet`
    **Endpoint ID:** `fal-ai/birefnet`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/birefnet/playground">
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
          "fal-ai/birefnet",
          arguments={
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/birefnet-input.jpeg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/birefnet", {
        input: {
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/birefnet-input.jpeg"
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
        --url https://fal.run/fal-ai/birefnet \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/birefnet-input.jpeg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="model" type="ModelEnum" default="General Use (Light)">
      Model to use for background removal.
      The 'General Use (Light)' model is the original model used in the BiRefNet repository.
      The 'General Use (Heavy)' model is a slower but more accurate model.
      The 'Portrait' model is a model trained specifically for portrait images.
      The 'General Use (Light)' model is recommended for most use cases.

      The corresponding models are as follows:

      * 'General Use (Light)': BiRefNet-DIS\_ep580.pth
      * 'General Use (Heavy)': BiRefNet-massive-epoch\_240.pth
      * 'Portrait': BiRefNet-portrait-TR\_P3M\_10k-epoch\_120.pth Default value: `"General Use (Light)"`

      Possible values: `General Use (Light)`, `General Use (Heavy)`, `Portrait`
    </ParamField>

    <ParamField body="operating_resolution" type="OperatingResolutionEnum" default="1024x1024">
      The resolution to operate on. The higher the resolution, the more accurate the output will be for high res input images. Default value: `"1024x1024"`

      Possible values: `1024x1024`, `2048x2048`
    </ParamField>

    <ParamField body="output_mask" type="boolean" default="false">
      Whether to output the mask used to remove the background
    </ParamField>

    <ParamField body="refine_foreground" type="boolean" default="true">
      Whether to refine the foreground using the estimated mask Default value: `true`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="image_url" type="string" required>
      URL of the image to remove background from
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="png">
      The format of the output image Default value: `"png"`

      Possible values: `webp`, `png`, `gif`
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="ImageFile" required>
      Image with background removed
    </ParamField>

    <ParamField body="mask_image" type="ImageFile">
      Mask used to remove the background
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "model": "General Use (Light)",
      "operating_resolution": "1024x1024",
      "output_mask": false,
      "refine_foreground": true,
      "sync_mode": false,
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/birefnet-input.jpeg",
      "output_format": "png"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "content_type": "image/png",
        "file_name": "birefnet-output.png",
        "height": 1024,
        "url": "https://storage.googleapis.com/falserverless/example_outputs/birefnet-output.png",
        "width": 1024
      }
    }
    ```
  </Tab>

  <Tab title="V2">
    **Endpoint:** `POST https://fal.run/fal-ai/birefnet/v2`
    **Endpoint ID:** `fal-ai/birefnet/v2`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/birefnet/v2/playground">
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
          "fal-ai/birefnet/v2",
          arguments={
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/birefnet-input.jpeg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/birefnet/v2", {
        input: {
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/birefnet-input.jpeg"
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
        --url https://fal.run/fal-ai/birefnet/v2 \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/birefnet-input.jpeg"
      }'
      ```
    </CodeGroup>

    ## Examples

    <Frame>
      <img src="https://fal.media/files/rabbit/LtkIjHOS-wgmPEghTIzkq_13ddac3a62f74e219b12cebef972ec18.png" alt="Example output from Birefnet Background Removal" />
    </Frame>

    ### Input Schema

    <ParamField body="model" type="ModelEnum" default="General Use (Light)">
      Model to use for background removal.
      The 'General Use (Light)' model is the original model used in the BiRefNet repository.
      The 'General Use (Light 2K)' model is the original model used in the BiRefNet repository but trained with 2K images.
      The 'General Use (Heavy)' model is a slower but more accurate model.
      The 'Matting' model is a model trained specifically for matting images.
      The 'Portrait' model is a model trained specifically for portrait images.
      The 'General Use (Dynamic)' model supports dynamic resolutions from 256x256 to 2304x2304.
      The 'General Use (Light)' model is recommended for most use cases.

      The corresponding models are as follows:

      * 'General Use (Light)': BiRefNet
      * 'General Use (Light 2K)': BiRefNet\_lite-2K
      * 'General Use (Heavy)': BiRefNet\_lite
      * 'Matting': BiRefNet-matting
      * 'Portrait': BiRefNet-portrait
      * 'General Use (Dynamic)': BiRefNet\_dynamic Default value: `"General Use (Light)"`

      Possible values: `General Use (Light)`, `General Use (Light 2K)`, `General Use (Heavy)`, `Matting`, `Portrait`, `General Use (Dynamic)`
    </ParamField>

    <ParamField body="operating_resolution" type="OperatingResolutionEnum" default="1024x1024">
      The resolution to operate on. The higher the resolution, the more accurate the output will be for high res input images. The '2304x2304' option is only available for the 'General Use (Dynamic)' model. Default value: `"1024x1024"`

      Possible values: `1024x1024`, `2048x2048`, `2304x2304`
    </ParamField>

    <ParamField body="output_mask" type="boolean" default="false">
      Whether to output the mask used to remove the background
    </ParamField>

    <ParamField body="refine_foreground" type="boolean" default="true">
      Whether to refine the foreground using the estimated mask Default value: `true`
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="image_url" type="string" required>
      URL of the image to remove background from
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="png">
      The format of the output image Default value: `"png"`

      Possible values: `webp`, `png`, `gif`
    </ParamField>

    <ParamField body="mask_only" type="boolean" default="false">
      Whether to return only the segmentation mask without applying it to the image. When set to `True`, only the mask will be returned and foreground refinement will be skipped. Useful for reducing computation and data transfer when only the mask is needed.
    </ParamField>

    ### Output Schema

    <ParamField body="image" type="ImageFile" required>
      Image with background removed. When `mask_only` is `True`, this contains the segmentation mask instead.
    </ParamField>

    <ParamField body="mask_image" type="ImageFile">
      Mask used to remove the background
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "model": "General Use (Light)",
      "operating_resolution": "1024x1024",
      "output_mask": false,
      "refine_foreground": true,
      "sync_mode": false,
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/birefnet-input.jpeg",
      "output_format": "png",
      "mask_only": false
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "image": {
        "content_type": "image/png",
        "file_name": "birefnet-output.png",
        "height": 1024,
        "url": "https://storage.googleapis.com/falserverless/example_outputs/birefnet-output.png",
        "width": 1024
      }
    }
    ```
  </Tab>
</Tabs>

BiRefNet's bilateral reference framework delivers high-resolution dichotomous image segmentation with precision mask generation. Trading traditional single-pass segmentation for a **dual-reference architecture**, it achieves cleaner edge detection and handles complex foreground-background separation. Purpose-built for production workflows requiring pixel-perfect transparency extraction from product photos, portraits, and complex scenes.

**Use Cases:** E-commerce Product Photography | Portrait Editing | Design Asset Preparation

***

## Performance

BiRefNet operates at **production-ready speeds** with three specialized model variants optimized for different accuracy-speed tradeoffs, processing images up to 2048x2048 resolution with optional mask output for downstream compositing workflows.

| Metric                   | Result                                                  | Context                                                    |
| :----------------------- | :------------------------------------------------------ | :--------------------------------------------------------- |
| **Operating Resolution** | Up to 2048x2048                                         | 4 megapixels max for high-fidelity edge detection          |
| **Model Variants**       | 3 specialized models                                    | Light (fast), Heavy (accurate), Portrait (optimized)       |
| **Cost per Inference**   | \$0 per compute second                                  | Pay only for actual processing time                        |
| **Output Formats**       | PNG, WebP, GIF                                          | Transparency-preserving formats with optional mask export  |
| **Related Endpoints**    | [BiRefNet v2](https://fal.ai/models/fal-ai/birefnet/v2) | Enhanced accuracy variant for demanding segmentation tasks |

***

## Precision Segmentation Architecture

BiRefNet's bilateral reference framework processes images through parallel pathways, one analyzing global context, the other focusing on local detail, then synthesizes both for edge-accurate mask generation. This contrasts with standard single-encoder approaches that struggle with fine details like hair strands or transparent objects.

**What this means for you:**

* **Three-tier model selection:** Choose Light (BiRefNet-DIS\_ep580) for speed, Heavy (BiRefNet-massive-epoch\_240) for complex scenes, or Portrait (BiRefNet-portrait-TR\_P3M\_10k-epoch\_120) for face-optimized segmentation based on your accuracy requirements

* **Scalable resolution processing:** Operate at 1024x1024 for standard workflows or 2048x2048 (4MP) for high-resolution source images requiring maximum edge fidelity

* **Optional foreground refinement:** Enable `refine_foreground` to apply mask-guided enhancement that preserves subject detail while ensuring clean transparency

* **Dual output capability:** Export both the background-removed image and the raw segmentation mask for manual compositing or downstream processing pipelines

***

## Technical Specifications

| Spec                      | Details                                     |
| :------------------------ | :------------------------------------------ |
| **Architecture**          | BiRefNet Bilateral Reference Framework      |
| **Input Formats**         | JPEG, PNG, WebP, GIF, AVIF via URL          |
| **Output Formats**        | PNG (default), WebP, GIF with alpha channel |
| **Operating Resolutions** | 1024x1024, 2048x2048                        |
| **License**               | Commercial use permitted                    |

[API Documentation](https://fal.ai/models/fal-ai/birefnet/api) | [Quickstart Guide](https://docs.fal.ai/model-apis/quickstart) | [Enterprise Pricing](https://fal.ai/pricing)

***

## How It Stacks Up

**BiRefNet v2** – BiRefNet v1 provides the core bilateral reference architecture with proven segmentation accuracy for general use cases. [BiRefNet v2](https://fal.ai/models/fal-ai/birefnet/v2) builds on this foundation with enhanced edge detection refinement for challenging scenarios like fine hair detail or semi-transparent objects where the original model may struggle.

## Limitations

* `model` restricted to: `General Use (Light)`, `General Use (Heavy)`, `Portrait`
* `operating_resolution` restricted to: `1024x1024`, `2048x2048`
* `output_format` restricted to: `webp`, `png`, `gif`
* `model` restricted to: `General Use (Light)`, `General Use (Light 2K)`, `General Use (Heavy)`, `Matting`, `Portrait`, `General Use (Dynamic)`
* `operating_resolution` restricted to: `1024x1024`, `2048x2048`, `2304x2304`
