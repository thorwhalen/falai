> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Topaz Upscale API

> API reference for Topaz Upscale. Use the powerful and accurate topaz image enhancer to enhance your images.

**Endpoint:** `POST https://fal.run/fal-ai/topaz/upscale/image`
**Endpoint ID:** `fal-ai/topaz/upscale/image`

<Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/topaz/upscale/image/playground">
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
      "fal-ai/topaz/upscale/image",
      arguments={
          "image_url": "https://storage.googleapis.com/falserverless/model_tests/codeformer/codeformer_poor_1.jpeg"
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  ```

  ```javascript title="JavaScript" theme={null}
  import { fal } from "@fal-ai/client";

  const result = await fal.subscribe("fal-ai/topaz/upscale/image", {
    input: {
        image_url: "https://storage.googleapis.com/falserverless/model_tests/codeformer/codeformer_poor_1.jpeg"
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
    --url https://fal.run/fal-ai/topaz/upscale/image \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data '{
    "image_url": "https://storage.googleapis.com/falserverless/model_tests/codeformer/codeformer_poor_1.jpeg"
  }'
  ```
</CodeGroup>

### Input Schema

<ParamField body="model" type="ModelEnum" default="Standard V2">
  Model to use for image enhancement. Default value: `"Standard V2"`

  Possible values: `Low Resolution V2`, `Standard V2`, `CGI`, `High Fidelity V2`, `Text Refine`, `Recovery`, `Redefine`, `Recovery V2`, `Standard MAX`, `Wonder`
</ParamField>

<ParamField body="upscale_factor" type="float" default="2">
  Factor to upscale the image by (e.g. 2.0 doubles width and height) Default value: `2`

  Range: `1` to `4`
</ParamField>

<ParamField body="crop_to_fill" type="boolean" default="false" />

<ParamField body="image_url" type="string" required>
  Url of the image to be upscaled
</ParamField>

<ParamField body="output_format" type="OutputFormatEnum" default="jpeg">
  Output format of the upscaled image. Default value: `"jpeg"`

  Possible values: `jpeg`, `png`
</ParamField>

<ParamField body="subject_detection" type="SubjectDetectionEnum" default="All">
  Subject detection mode for the image enhancement. Applies to standard enhance and Recovery V2 models. Default value: `"All"`

  Possible values: `All`, `Foreground`, `Background`
</ParamField>

<ParamField body="face_enhancement" type="boolean" default="true">
  Whether to apply face enhancement to the image. Applies to standard enhance and Recovery V2 models. Default value: `true`
</ParamField>

<ParamField body="face_enhancement_creativity" type="float" default="0">
  Creativity level for face enhancement. 0.0 means no creativity, 1.0 means maximum creativity. Ignored if face enhancement is disabled.

  Range: `0` to `1`
</ParamField>

<ParamField body="face_enhancement_strength" type="float" default="0.8">
  Strength of the face enhancement. 0.0 means no enhancement, 1.0 means maximum enhancement. Ignored if face enhancement is disabled. Default value: `0.8`

  Range: `0` to `1`
</ParamField>

<ParamField body="sharpen" type="float">
  Sharpening level (0.0-1.0). Applies to Standard V2, Low Resolution V2, CGI, High Fidelity V2, Text Refine, and Redefine models.

  Range: `0` to `1`
</ParamField>

<ParamField body="denoise" type="float">
  Denoising level (0.0-1.0). Applies to Standard V2, Low Resolution V2, CGI, High Fidelity V2, Text Refine, and Redefine models.

  Range: `0` to `1`
</ParamField>

<ParamField body="fix_compression" type="float">
  Compression artifact removal level (0.0-1.0). Applies to Standard V2, Low Resolution V2, High Fidelity V2, and Text Refine models.

  Range: `0` to `1`
</ParamField>

<ParamField body="strength" type="float">
  Enhancement strength (0.01-1.0). Applies to Text Refine model only.

  Range: `0.01` to `1`
</ParamField>

<ParamField body="creativity" type="integer">
  Creativity level for generative upscaling (1-6). Higher values produce more creative/hallucinated details. Applies to Redefine model only.

  Range: `1` to `6`
</ParamField>

<ParamField body="texture" type="integer">
  Texture detail level for generative upscaling (1-5). Applies to Redefine model only.

  Range: `1` to `5`
</ParamField>

<ParamField body="prompt" type="string">
  Text prompt to guide generative upscaling (max 1024 chars). Applies to Redefine model only.
</ParamField>

<ParamField body="autoprompt" type="boolean">
  Enable automatic prompt generation for generative upscaling. Applies to Redefine model only.
</ParamField>

<ParamField body="detail" type="float">
  Detail recovery level (0.0-1.0). Applies to Recovery V2 model only.

  Range: `0` to `1`
</ParamField>

### Output Schema

<ParamField body="image" type="File" required>
  The upscaled image.
</ParamField>

### Input Example

```json theme={null}
{
  "model": "Standard V2",
  "upscale_factor": 2,
  "crop_to_fill": false,
  "image_url": "https://storage.googleapis.com/falserverless/model_tests/codeformer/codeformer_poor_1.jpeg",
  "output_format": "jpeg",
  "subject_detection": "All",
  "face_enhancement": true,
  "face_enhancement_creativity": 0,
  "face_enhancement_strength": 0.8
}
```

### Output Example

```json theme={null}
{
  "image": {
    "url": "",
    "content_type": "image/png",
    "file_name": "z9RV14K95DvU.png",
    "file_size": 4404019
  }
}
```

## Limitations

* `upscale_factor` range: 1 to 4
* `output_format` restricted to: `jpeg`, `png`
* `subject_detection` restricted to: `All`, `Foreground`, `Background`
* `face_enhancement_creativity` range: 0 to 1
* `face_enhancement_strength` range: 0 to 1
* `sharpen` range: 0 to 1
* `denoise` range: 0 to 1
* `fix_compression` range: 0 to 1
* `strength` range: 0.01 to 1
* `creativity` range: 1 to 6
* `texture` range: 1 to 5
* `detail` range: 0 to 1
