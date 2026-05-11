> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# FlashPack

> High-throughput tensor loading for PyTorch -- load models at up to 25Gbps without GDS.

[FlashPack](https://github.com/fal-ai/flashpack) is an open-source library by fal that dramatically speeds up model loading by streaming weights directly from disk to GPU with zero-copy reconstruction. Use it in your `setup()` method to reduce cold start times.

<Frame>
  <iframe className="w-full aspect-video rounded-lg" srcdoc="<style>*{padding:0;margin:0;overflow:hidden}html,body{height:100%}img,span{position:absolute;width:100%;top:0;bottom:0;margin:auto}span{height:1.5em;text-align:center;font:48px/1.5 sans-serif;color:white;text-shadow:0 0 0.5em black}</style><a href='https://www.youtube.com/embed/gDJJ9bppyV8?start=633&end=732&autoplay=1'><img src='/docs/images/video-thumbs/flashpack.jpg' alt='FlashPack - fal Serverless'><span>▶</span></a>" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />
</Frame>

## How It Works

### 1. Flatten weights into contiguous macroblocks

At save/convert time, FlashPack takes the model's entire `state_dict`, groups tensors by data type, then flattens them into one contiguous stream of bytes. A compact weight map at the end of the file stores every parameter's key, shape, and offset.

### 2. Stream with overlapping disk, CPU, and GPU transfers

When loading, FlashPack memory-maps the file and divides it into mid-sized CPU buffers (up to 64MB each). These buffers load in a round-robin pattern, keeping disk reads continuous. Each CPU buffer is paired with a dedicated CUDA stream -- while one stream writes to VRAM, another buffer is already being loaded from disk.

### 3. Rebuild parameters as zero-copy views

Once data is on the GPU, FlashPack reconstructs each tensor as a view into the flat memory block and creates new `nn.Parameter` instances with direct references to the loaded bytes. No copies, no moves -- the model is immediately ready to run.

***

## Integration Methods

### Direct Function Calling

The simplest approach when you don't want to modify your module code:

```python theme={null}
from flashpack import pack_to_file, assign_from_file

flashpack_path = "/data/models/my-model.flashpack"
model = MyModel(...)

pack_to_file(model, flashpack_path)
assign_from_file(model, flashpack_path)
```

### PyTorch Mixin

Add `FlashPackMixin` to your module for `save_flashpack` and `from_flashpack` methods:

```python theme={null}
from flashpack import FlashPackMixin

class MyModule(nn.Module, FlashPackMixin):
    def __init__(self, some_arg: int = 4) -> None:
        ...

module = MyModule(some_arg=4)
module.save_flashpack("model.flashpack")

loaded_module = MyModule.from_flashpack("model.flashpack", some_arg=4)
```

### Diffusers Models

Use `FlashPackDiffusersModelMixin` for diffusers models with `from_pretrained_flashpack` and `save_pretrained_flashpack`:

```python theme={null}
from flashpack.integrations.diffusers import FlashPackDiffusersModelMixin
from diffusers.models import AutoencoderKL

class FlashPackAutoencoderKL(FlashPackDiffusersModelMixin, AutoencoderKL):
    pass

# Load from original weights
sdxl_vae = FlashPackAutoencoderKL.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    variant="fp16",
    subfolder="vae",
)

# Save as FlashPack (optionally push to HuggingFace)
sdxl_vae.save_pretrained_flashpack(
    "/path/to/save/directory",
    push_to_hub=True,
    repo_id="my-org/sdxl-vae-flashpack",
)

# Load from FlashPack
sdxl_vae = FlashPackAutoencoderKL.from_pretrained_flashpack(
    "my-org/sdxl-vae-flashpack",
    device_map="cuda",
)
```

### Transformers Models

Works the same way with `FlashPackTransformersModelMixin`:

```python theme={null}
from flashpack.integrations.transformers import FlashPackTransformersModelMixin
from transformers import CLIPTextModel

class FlashPackCLIPTextModel(FlashPackTransformersModelMixin, CLIPTextModel):
    pass

# Load, convert, and save
clip = FlashPackCLIPTextModel.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    variant="fp16",
    subfolder="text_encoder",
)
clip.save_pretrained_flashpack(
    "/path/to/save/directory",
    push_to_hub=True,
    repo_id="my-org/sdxl-text-encoder-flashpack",
)

# Load from FlashPack
clip = FlashPackCLIPTextModel.from_pretrained_flashpack(
    "my-org/sdxl-text-encoder-flashpack",
    device_map="cuda",
)
```

### Diffusers Pipelines

FlashPack pipelines are made of FlashPack-enabled models. You don't need to enable FlashPack on every model in a pipeline -- it automatically uses `from_pretrained_flashpack` for FlashPack-enabled models and `from_pretrained` for the rest.

```python theme={null}
from typing import Optional
from diffusers import AutoencoderKL, StableDiffusionXLPipeline, UNet2DConditionModel
from diffusers.schedulers import KarrasDiffusionSchedulers
from flashpack.integrations.diffusers import (
    FlashPackDiffusersModelMixin,
    FlashPackDiffusionPipeline,
)
from flashpack.integrations.transformers import FlashPackTransformersModelMixin
from transformers import (
    CLIPImageProcessor,
    CLIPTextModel,
    CLIPTextModelWithProjection,
    CLIPTokenizer,
    CLIPVisionModelWithProjection,
)

# Define FlashPack-enabled classes
class FlashPackCLIPTextModel(FlashPackTransformersModelMixin, CLIPTextModel):
    pass

class FlashPackCLIPTextModelWithProjection(
    FlashPackTransformersModelMixin, CLIPTextModelWithProjection
):
    pass

class FlashPackAutoencoderKL(FlashPackDiffusersModelMixin, AutoencoderKL):
    pass

class FlashPackUNet2DConditionModel(FlashPackDiffusersModelMixin, UNet2DConditionModel):
    pass

class FlashPackStableDiffusionXLPipeline(
    FlashPackDiffusionPipeline, StableDiffusionXLPipeline
):
    def __init__(
        self,
        vae: FlashPackAutoencoderKL,
        text_encoder: FlashPackCLIPTextModel,
        text_encoder_2: FlashPackCLIPTextModelWithProjection,
        tokenizer: CLIPTokenizer,
        tokenizer_2: CLIPTokenizer,
        unet: FlashPackUNet2DConditionModel,
        scheduler: KarrasDiffusionSchedulers,
        feature_extractor: Optional[CLIPImageProcessor] = None,
        image_encoder: Optional[CLIPVisionModelWithProjection] = None,
        add_watermarker: Optional[bool] = None,
        force_zeros_for_empty_prompt: bool = True,
    ) -> None:
        super().__init__(
            vae=vae,
            text_encoder=text_encoder,
            text_encoder_2=text_encoder_2,
            tokenizer=tokenizer,
            tokenizer_2=tokenizer_2,
            unet=unet,
            scheduler=scheduler,
            feature_extractor=feature_extractor,
            image_encoder=image_encoder,
            add_watermarker=add_watermarker,
            force_zeros_for_empty_prompt=force_zeros_for_empty_prompt,
        )

# Save entire pipeline as FlashPack
pipeline = FlashPackStableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    variant="fp16",
)
pipeline.save_pretrained_flashpack(
    "flashpack-sdxl",
    push_to_hub=True,
    repo_id="my-org/sdxl-flashpack",
)

# Load from FlashPack -- immediately ready to use
pipeline = FlashPackStableDiffusionXLPipeline.from_pretrained_flashpack(
    "my-org/sdxl-flashpack",
    device_map="cuda",
)
image = pipeline("A sunset over mountains", num_inference_steps=50).images[0]
```

<Note>
  Use `Optional[]` syntax (not `| None`) for optional pipeline parameters. This is a limitation in diffusers, not FlashPack.
</Note>

***

## CLI Commands

FlashPack includes a CLI for converting, inspecting, and reverting files.

### Convert a model

```bash theme={null}
# Convert a local model
flashpack convert ./my_model ./my_model.flashpack

# Convert from HuggingFace
flashpack convert stabilityai/stable-diffusion-xl-base-1.0 \
  --subfolder unet --use-diffusers

# Convert with specific dtype
flashpack convert ./my_model ./my_model.flashpack --dtype float16
```

### Inspect metadata

```bash theme={null}
flashpack metadata ./my_model.flashpack
flashpack metadata ./my_model.flashpack --show-index --json
```

### Revert to safetensors

```bash theme={null}
flashpack revert ./my_model.flashpack ./my_model.safetensors
```

***

## Using FlashPack on fal

Convert your model to FlashPack format, store it on `/data` or HuggingFace, and load in `setup()`:

```python theme={null}
import fal
from flashpack import assign_from_file

class MyModel(fal.App):
    machine_type = "GPU-A100"
    requirements = ["flashpack", "torch", "diffusers"]

    def setup(self):
        import torch
        from my_model import build_model

        self.model = build_model()
        assign_from_file(self.model, "/data/models/my-model.flashpack")

    @fal.endpoint("/")
    def generate(self, prompt: str) -> dict:
        return self.model(prompt)
```

Or with the Diffusers integration:

```python theme={null}
import fal

class SDXLApp(fal.App):
    machine_type = "GPU-A100"
    requirements = ["flashpack", "torch", "diffusers", "transformers"]

    def setup(self):
        from my_flashpack_classes import FlashPackStableDiffusionXLPipeline

        self.pipe = FlashPackStableDiffusionXLPipeline.from_pretrained_flashpack(
            "my-org/sdxl-flashpack",
            device_map="cuda",
        )

    @fal.endpoint("/")
    def generate(self, prompt: str) -> dict:
        image = self.pipe(prompt, num_inference_steps=30).images[0]
        return {"image": fal.toolkit.Image.from_pil(image)}
```

<Tip>
  Store FlashPack files on `/data` for automatic caching across cold starts. The first runner downloads the file, and subsequent runners load from the cached copy.
</Tip>

<Card title="GitHub Repository" icon="github" href="https://github.com/fal-ai/flashpack">
  View source, benchmarks, and contribute on GitHub
</Card>
