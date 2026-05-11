> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Z Image Turbo Controlnet API

> API reference for Z Image Turbo Controlnet. Generate images from text and edge, depth or pose images using Z-Image Turbo, Tongyi-MAI's super-fast 6B model.

<Tabs>
  <Tab title="Controlnet">
    **Endpoint:** `POST https://fal.run/fal-ai/z-image/turbo/controlnet`
    **Endpoint ID:** `fal-ai/z-image/turbo/controlnet`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/z-image/turbo/controlnet/playground">
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
          "fal-ai/z-image/turbo/controlnet",
          arguments={
              "prompt": "A single leopard, its spotted golden coat detailed with black rosettes, cautiously peeks its head through dense green foliage. The leopard’s eyes are alert and focused forward, ears perked, whiskers slightly visible. The bushes consist of thick, leafy shrubs with varying shades of green, some leaves partially obscuring the leopard’s muzzle and forehead. Soft natural daylight filters through the canopy above, casting dappled shadows across the animal’s fur and surrounding leaves. The composition is a medium close-up, centered on the leopard’s head emerging from the undergrowth, with shallow depth of field blurring the background vegetation.",
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/z-image-turbo-controlnet-input.jpg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/z-image/turbo/controlnet", {
        input: {
            prompt: "A single leopard, its spotted golden coat detailed with black rosettes, cautiously peeks its head through dense green foliage. The leopard’s eyes are alert and focused forward, ears perked, whiskers slightly visible. The bushes consist of thick, leafy shrubs with varying shades of green, some leaves partially obscuring the leopard’s muzzle and forehead. Soft natural daylight filters through the canopy above, casting dappled shadows across the animal’s fur and surrounding leaves. The composition is a medium close-up, centered on the leopard’s head emerging from the undergrowth, with shallow depth of field blurring the background vegetation.",
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/z-image-turbo-controlnet-input.jpg"
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
        --url https://fal.run/fal-ai/z-image/turbo/controlnet \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A single leopard, its spotted golden coat detailed with black rosettes, cautiously peeks its head through dense green foliage. The leopard’s eyes are alert and focused forward, ears perked, whiskers slightly visible. The bushes consist of thick, leafy shrubs with varying shades of green, some leaves partially obscuring the leopard’s muzzle and forehead. Soft natural daylight filters through the canopy above, casting dappled shadows across the animal’s fur and surrounding leaves. The composition is a medium close-up, centered on the leopard’s head emerging from the undergrowth, with shallow depth of field blurring the background vegetation.",
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/z-image-turbo-controlnet-input.jpg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to generate an image from.
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="auto">
      The size of the generated image. Default value: `auto`

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`, `auto`
    </ParamField>

    <ParamField body="num_inference_steps" type="integer" default="8">
      The number of inference steps to perform. Default value: `8`

      Range: `1` to `8`
    </ParamField>

    <ParamField body="seed" type="integer">
      The same seed and the same prompt given to the same version of the model
      will output the same image every time.
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      The number of images to generate. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="png">
      The format of the generated image. Default value: `"png"`

      Possible values: `jpeg`, `png`, `webp`
    </ParamField>

    <ParamField body="acceleration" type="AccelerationEnum" default="regular">
      The acceleration level to use. Default value: `"regular"`

      Possible values: `none`, `regular`, `high`
    </ParamField>

    <ParamField body="enable_prompt_expansion" type="boolean" default="false">
      Whether to enable prompt expansion. Note: this will increase the price by 0.0025 credits per request.
    </ParamField>

    <ParamField body="image_url" type="string" required>
      URL of Image for ControlNet generation.
    </ParamField>

    <ParamField body="control_scale" type="float" default="0.75">
      The scale of the controlnet conditioning. Default value: `0.75`

      Range: `0` to `1`
    </ParamField>

    <ParamField body="control_start" type="float" default="0">
      The start of the controlnet conditioning.

      Range: `0` to `1`
    </ParamField>

    <ParamField body="control_end" type="float" default="0.8">
      The end of the controlnet conditioning. Default value: `0.8`

      Range: `0` to `1`
    </ParamField>

    <ParamField body="preprocess" type="Enum" default="none">
      What kind of preprocessing to apply to the image, if any. Default value: `none`

      Possible values: `none`, `canny`, `depth`, `pose`
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<ImageFile>" required>
      The generated image files info.
    </ParamField>

    <ParamField body="timings" type="Timings" required>
      The timings of the generation process.
    </ParamField>

    <ParamField body="seed" type="integer" required>
      Seed of the generated Image. It will be the same value of the one passed in the input or the randomly generated that was used in case none was passed.
    </ParamField>

    <ParamField body="has_nsfw_concepts" type="list<boolean>" required>
      Whether the generated images contain NSFW concepts.
    </ParamField>

    <ParamField body="prompt" type="string" required>
      The prompt used for generating the image.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A single leopard, its spotted golden coat detailed with black rosettes, cautiously peeks its head through dense green foliage. The leopard’s eyes are alert and focused forward, ears perked, whiskers slightly visible. The bushes consist of thick, leafy shrubs with varying shades of green, some leaves partially obscuring the leopard’s muzzle and forehead. Soft natural daylight filters through the canopy above, casting dappled shadows across the animal’s fur and surrounding leaves. The composition is a medium close-up, centered on the leopard’s head emerging from the undergrowth, with shallow depth of field blurring the background vegetation.",
      "image_size": "auto",
      "num_inference_steps": 8,
      "sync_mode": false,
      "num_images": 1,
      "enable_safety_checker": true,
      "output_format": "png",
      "acceleration": "regular",
      "enable_prompt_expansion": false,
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/z-image-turbo-controlnet-input.jpg",
      "control_scale": 0.75,
      "control_start": 0,
      "control_end": 0.8,
      "preprocess": "none"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "content_type": "image/png",
          "height": 1024,
          "url": "https://storage.googleapis.com/falserverless/example_outputs/z-image-turbo-controlnet-output.jpg",
          "width": 1536
        }
      ],
      "prompt": ""
    }
    ```
  </Tab>

  <Tab title="Lora">
    **Endpoint:** `POST https://fal.run/fal-ai/z-image/turbo/controlnet/lora`
    **Endpoint ID:** `fal-ai/z-image/turbo/controlnet/lora`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/z-image/turbo/controlnet/lora/playground">
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
          "fal-ai/z-image/turbo/controlnet/lora",
          arguments={
              "prompt": "A single leopard, its spotted golden coat detailed with black rosettes, cautiously peeks its head through dense green foliage. The leopard’s eyes are alert and focused forward, ears perked, whiskers slightly visible. The bushes consist of thick, leafy shrubs with varying shades of green, some leaves partially obscuring the leopard’s muzzle and forehead. Soft natural daylight filters through the canopy above, casting dappled shadows across the animal’s fur and surrounding leaves. The composition is a medium close-up, centered on the leopard’s head emerging from the undergrowth, with shallow depth of field blurring the background vegetation.",
              "image_url": "https://storage.googleapis.com/falserverless/example_inputs/z-image-turbo-controlnet-input.jpg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/z-image/turbo/controlnet/lora", {
        input: {
            prompt: "A single leopard, its spotted golden coat detailed with black rosettes, cautiously peeks its head through dense green foliage. The leopard’s eyes are alert and focused forward, ears perked, whiskers slightly visible. The bushes consist of thick, leafy shrubs with varying shades of green, some leaves partially obscuring the leopard’s muzzle and forehead. Soft natural daylight filters through the canopy above, casting dappled shadows across the animal’s fur and surrounding leaves. The composition is a medium close-up, centered on the leopard’s head emerging from the undergrowth, with shallow depth of field blurring the background vegetation.",
            image_url: "https://storage.googleapis.com/falserverless/example_inputs/z-image-turbo-controlnet-input.jpg"
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
        --url https://fal.run/fal-ai/z-image/turbo/controlnet/lora \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "prompt": "A single leopard, its spotted golden coat detailed with black rosettes, cautiously peeks its head through dense green foliage. The leopard’s eyes are alert and focused forward, ears perked, whiskers slightly visible. The bushes consist of thick, leafy shrubs with varying shades of green, some leaves partially obscuring the leopard’s muzzle and forehead. Soft natural daylight filters through the canopy above, casting dappled shadows across the animal’s fur and surrounding leaves. The composition is a medium close-up, centered on the leopard’s head emerging from the undergrowth, with shallow depth of field blurring the background vegetation.",
        "image_url": "https://storage.googleapis.com/falserverless/example_inputs/z-image-turbo-controlnet-input.jpg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="prompt" type="string" required>
      The prompt to generate an image from.
    </ParamField>

    <ParamField body="image_size" type="ImageSize | Enum" default="auto">
      The size of the generated image. Default value: `auto`

      Possible values: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`, `auto`
    </ParamField>

    <ParamField body="num_inference_steps" type="integer" default="8">
      The number of inference steps to perform. Default value: `8`

      Range: `1` to `8`
    </ParamField>

    <ParamField body="seed" type="integer">
      The same seed and the same prompt given to the same version of the model
      will output the same image every time.
    </ParamField>

    <ParamField body="sync_mode" type="boolean" default="false">
      If `True`, the media will be returned as a data URI and the output data won't be available in the request history.
    </ParamField>

    <ParamField body="num_images" type="integer" default="1">
      The number of images to generate. Default value: `1`

      Range: `1` to `4`
    </ParamField>

    <ParamField body="enable_safety_checker" type="boolean" default="true">
      If set to true, the safety checker will be enabled. Default value: `true`
    </ParamField>

    <ParamField body="output_format" type="OutputFormatEnum" default="png">
      The format of the generated image. Default value: `"png"`

      Possible values: `jpeg`, `png`, `webp`
    </ParamField>

    <ParamField body="acceleration" type="AccelerationEnum" default="regular">
      The acceleration level to use. Default value: `"regular"`

      Possible values: `none`, `regular`, `high`
    </ParamField>

    <ParamField body="enable_prompt_expansion" type="boolean" default="false">
      Whether to enable prompt expansion. Note: this will increase the price by 0.0025 credits per request.
    </ParamField>

    <ParamField body="image_url" type="string" required>
      URL of Image for ControlNet generation.
    </ParamField>

    <ParamField body="control_scale" type="float" default="0.75">
      The scale of the controlnet conditioning. Default value: `0.75`

      Range: `0` to `1`
    </ParamField>

    <ParamField body="control_start" type="float" default="0">
      The start of the controlnet conditioning.

      Range: `0` to `1`
    </ParamField>

    <ParamField body="control_end" type="float" default="0.8">
      The end of the controlnet conditioning. Default value: `0.8`

      Range: `0` to `1`
    </ParamField>

    <ParamField body="preprocess" type="Enum" default="none">
      What kind of preprocessing to apply to the image, if any. Default value: `none`

      Possible values: `none`, `canny`, `depth`, `pose`
    </ParamField>

    <ParamField body="loras" type="list<LoRAInput>" default="">
      List of LoRA weights to apply (maximum 3).
    </ParamField>

    ### Output Schema

    <ParamField body="images" type="list<ImageFile>" required>
      The generated image files info.
    </ParamField>

    <ParamField body="timings" type="Timings" required>
      The timings of the generation process.
    </ParamField>

    <ParamField body="seed" type="integer" required>
      Seed of the generated Image. It will be the same value of the one passed in the input or the randomly generated that was used in case none was passed.
    </ParamField>

    <ParamField body="has_nsfw_concepts" type="list<boolean>" required>
      Whether the generated images contain NSFW concepts.
    </ParamField>

    <ParamField body="prompt" type="string" required>
      The prompt used for generating the image.
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "prompt": "A single leopard, its spotted golden coat detailed with black rosettes, cautiously peeks its head through dense green foliage. The leopard’s eyes are alert and focused forward, ears perked, whiskers slightly visible. The bushes consist of thick, leafy shrubs with varying shades of green, some leaves partially obscuring the leopard’s muzzle and forehead. Soft natural daylight filters through the canopy above, casting dappled shadows across the animal’s fur and surrounding leaves. The composition is a medium close-up, centered on the leopard’s head emerging from the undergrowth, with shallow depth of field blurring the background vegetation.",
      "image_size": "auto",
      "num_inference_steps": 8,
      "sync_mode": false,
      "num_images": 1,
      "enable_safety_checker": true,
      "output_format": "png",
      "acceleration": "regular",
      "enable_prompt_expansion": false,
      "image_url": "https://storage.googleapis.com/falserverless/example_inputs/z-image-turbo-controlnet-input.jpg",
      "control_scale": 0.75,
      "control_start": 0,
      "control_end": 0.8,
      "preprocess": "none",
      "loras": []
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "images": [
        {
          "content_type": "image/png",
          "height": 1024,
          "url": "https://storage.googleapis.com/falserverless/example_outputs/z-image-turbo-controlnet-output.jpg",
          "width": 1536
        }
      ],
      "prompt": ""
    }
    ```
  </Tab>
</Tabs>

Tongyi-MAI's Z-Image Turbo delivers ControlNet-guided image generation at \$0.0065 per megapixel through a 6-billion parameter architecture. This model trades raw parameter count for specialized control mechanisms, canny edge detection, depth mapping, and pose guidance, that preserve structural fidelity during image-to-image transformations. Built for designers and developers who need precise spatial control without the inference overhead of larger diffusion models.

**Use Cases:** Product visualization with reference geometry | Character pose transfer workflows | Architectural rendering from depth maps

***

## Performance

Z-Image Turbo operates at roughly 3-5x more cost-effective rates than traditional ControlNet implementations by optimizing the 6B parameter base for rapid inference. At \$0.0065 per megapixel, you're running 153 megapixels per dollar, ideal for batch processing workflows where structural guidance matters more than photorealistic perfection.

| Metric                 | Result                                                                                                                                                            | Context                                                |
| :--------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
| **Model Size**         | 6 billion parameters                                                                                                                                              | Optimized for inference speed vs 70B+ alternatives     |
| **Inference Steps**    | 1-8 configurable                                                                                                                                                  | Default 8 steps balances quality and latency           |
| **Cost per Megapixel** | \$0.0065                                                                                                                                                          | 153 megapixels per \$1.00 on fal                       |
| **Control Methods**    | 4 preprocessing modes                                                                                                                                             | None, canny edge, depth map, pose detection            |
| **Batch Generation**   | Up to 4 images per request                                                                                                                                        | Parallel generation with shared control input          |
| **Related Endpoints**  | [Standard image-to-image](https://fal.ai/models/fal-ai/z-image/turbo/image-to-image), [LoRA variants](https://fal.ai/models/fal-ai/z-image/turbo/controlnet/lora) | ControlNet vs direct transformation vs custom training |

***

## Structural Control Without Compromise

Z-Image Turbo routes your prompt through three parallel conditioning pathways: text embedding, reference image structure, and optional preprocessing filters. Unlike pure text-to-image models that hallucinate spatial relationships, this architecture extracts edge maps, depth channels, or skeletal poses from your input, then enforces those constraints during diffusion.

**What this means for you:**

* **Configurable control strength (0-1 scale):** Dial conditioning intensity from 0.9 for strict adherence to 0.3 for loose interpretation, critical when your reference image has good composition but needs significant style deviation
* **Temporal control windowing:** Apply ControlNet guidance only during steps 0-40% of generation (configurable start/end), letting early diffusion lock structure while late steps refine aesthetics
* **Four preprocessing modes:** Feed raw images directly or auto-extract canny edges (sharp boundaries), depth maps (spatial layering), or pose skeletons (human/character positioning) without external tools
* **Multi-format output with safety:** Generate 1-4 variants simultaneously in JPEG, PNG, or WebP with optional built-in safety filtering, batch testing style variations while maintaining structural consistency

***

## Technical Specifications

| Spec                      | Details                                                          |
| :------------------------ | :--------------------------------------------------------------- |
| **Architecture**          | Z-Image Turbo 6B                                                 |
| **Input Formats**         | Text prompt + reference image URL (JPEG, PNG, WebP, GIF, AVIF)   |
| **Output Formats**        | JPEG, PNG, WebP with configurable dimensions                     |
| **Preprocessing Options** | None, Canny edge detection, Depth estimation, Pose detection     |
| **Control Parameters**    | Scale (0-1), temporal start/end windowing, inference steps (1-8) |
| **License**               | Commercial use permitted                                         |

[API Documentation](https://fal.ai/models/fal-ai/z-image/turbo/controlnet/api) | [Quickstart Guide](https://docs.fal.ai/model-apis/quickstart) | [Enterprise Pricing](https://fal.ai/pricing)

***

## How It Stacks Up

\*\*Z-Image Turbo Standard ($0.0065/MP)** – The [ControlNet variant](https://fal.ai/models/fal-ai/z-image/turbo/controlnet) adds structural guidance preprocessing for $0.0065 per megapixel, same base cost. [Standard image-to-image](https://fal.ai/models/fal-ai/z-image/turbo/image-to-image) prioritizes direct style transfer without intermediate edge/depth extraction, ideal for texture swaps and color grading where spatial relationships already match your target. ControlNet trades processing simplicity for precise geometric control when your reference structure needs enforcement.

**FASHN Virtual Try-On V1.5** – Z-Image Turbo ControlNet offers general-purpose structural conditioning across edge, depth, and pose modalities for diverse creative workflows. [FASHN](https://fal.ai/models/fal-ai/fashn/tryon/v1.5) specializes in garment-to-body fitting with proprietary try-on algorithms optimized for fashion e-commerce, trading generality for domain-specific accuracy in clothing visualization.

## Related

* [Z-Image Turbo](/model-api-reference/image-generation-api/z-image-turbo) — Image Generation
* [Z Image Base](/model-api-reference/image-generation-api/z-image-base) — Image Generation
* [Z Image Base (LoRA)](/model-api-reference/image-generation-api/z-image-base-lora) — Image Generation
* [Z-Image Turbo Seamless Tiling](/model-api-reference/image-generation-api/z-image-turbo-seamless-tiling) — Image Generation

## Limitations

* `image_size` restricted to: `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`, `auto`
* `num_inference_steps` range: 1 to 8
* `num_images` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`, `webp`
* `acceleration` restricted to: `none`, `regular`, `high`
* `control_scale` range: 0 to 1
* `control_start` range: 0 to 1
* `control_end` range: 0 to 1
* `preprocess` restricted to: `none`, `canny`, `depth`, `pose`
* Content moderation via safety checker
