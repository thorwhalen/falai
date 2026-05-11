> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Optimize Startup with Compiled Caches

> Reduce cold-start time for compiled PyTorch models by sharing Inductor caches across workers.

When using `torch.compile()` with PyTorch models, the first run compiles optimized CUDA kernels, which can take significant time. By sharing these compiled kernels across workers, you can dramatically reduce startup latency for subsequent workers.

<Frame>
  <iframe className="w-full aspect-video rounded-lg" srcdoc="<style>*{padding:0;margin:0;overflow:hidden}html,body{height:100%}img,span{position:absolute;width:100%;top:0;bottom:0;margin:auto}span{height:1.5em;text-align:center;font:48px/1.5 sans-serif;color:white;text-shadow:0 0 0.5em black}</style><a href='https://www.youtube.com/embed/gDJJ9bppyV8?start=732&end=775&autoplay=1'><img src='/docs/images/video-thumbs/optimize-startup-with-compiled-caches.jpg' alt='Kernel Caching - fal Serverless'><span>▶</span></a>" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />
</Frame>

## The Problem

PyTorch's Inductor compiler (`torch.compile`) generates optimized GPU kernels on first run. Without cache sharing:

* **Every worker recompiles** the same kernels, wasting GPU time
* **Startup latency multiplies** across workers (N workers × compilation time)
* **GPU resources** are used inefficiently during deployment

With Inductor cache sharing:

* **One worker compiles** during initial warmup
* **Other workers load** pre-compiled kernels (significantly faster)
* **Consistent performance** across all workers

## Quick Start

The simplest way to use Inductor caching is with the `synchronized_inductor_cache` context manager:

```python theme={null}
from fal.toolkit import synchronized_inductor_cache

class MyApp(fal.App):
    def setup(self):
        # Load model
        self.model = load_model()
        
        # Wrap compilation + warmup in cache context
        with synchronized_inductor_cache("my-model/v1"):
            self.model = torch.compile(self.model)
            self.warmup()
```

That's it! The first worker compiles and saves to `/data/inductor-caches/<GPU_TYPE>/<cache_key>.zip` (on the shared `/data` filesystem accessible to all workers), while subsequent workers load the pre-compiled kernels.

## API Reference

### `synchronized_inductor_cache(cache_key: str)`

A context manager that handles both loading and syncing of Inductor caches automatically.

**Parameters:**

* `cache_key` (str): A unique identifier for this cache. Use a descriptive name with versioning (e.g., `"my-model/v1"`).

**Usage:**

```python theme={null}
with synchronized_inductor_cache("my-model/v1"):
    # Any torch.compile() calls and warmup inside this block
    # will use the shared cache
    model = torch.compile(model)
    warmup()
```

**Behavior:**

* Loads existing cache from `/data/inductor-caches/` if available
* After the context exits, syncs any newly compiled kernels back to shared storage
* Handles GPU-specific cache organization automatically

### `load_inductor_cache(cache_key: str) -> str`

Explicitly loads an Inductor cache from shared storage.

**Parameters:**

* `cache_key` (str): The cache identifier to load.

**Returns:**

* `str`: A directory hash representing the cache state. Pass this to `sync_inductor_cache()` later.

**Usage:**

```python theme={null}
dir_hash = load_inductor_cache("my-model/v1")
# ... compilation and warmup ...
sync_inductor_cache("my-model/v1", dir_hash)
```

### `sync_inductor_cache(cache_key: str, dir_hash: str) -> None`

Syncs the local Inductor cache back to shared storage.

**Parameters:**

* `cache_key` (str): The cache identifier to sync.
* `dir_hash` (str): The directory hash returned by `load_inductor_cache()`.

**Behavior:**

* Compares local cache with the hash to detect new compiled kernels
* If changes detected, re-packs and uploads entire cache to `/data/inductor-caches/`
* If no changes, skips upload (no-op)

## Complete Working Example

Here's a complete, runnable example using Stable Diffusion Turbo that demonstrates the actual speedup:

```python theme={null}
import fal
from fal.toolkit import Image, synchronized_inductor_cache
from pydantic import BaseModel, Field

class Input(BaseModel):
    prompt: str = Field(
        description="Text prompt for image generation",
        examples=["A serene lake at sunset with mountains"],
    )
    width: int = Field(
        default=512,
        description="Image width",
    )
    height: int = Field(
        default=512,
        description="Image height",
    )

class Output(BaseModel):
    image: Image

class SDTurbo(fal.App):
    machine_type = "GPU-H100"
    keep_alive = 300  # 5 minutes - keep warm between requests
    startup_timeout = 900  # 15 minutes - allow time for compilation
    requirements = [
        "torch==2.5.0",
        "diffusers==0.31.0",
        "transformers",
        "accelerate",
        "nvidia-cuda-nvrtc-cu12",
    ]

    def setup(self) -> None:
        # Workaround for cuDNN SDPA on CUDA 12.x
        # This makes the NVRTC library globally available for cuDNN kernel compilation
        import ctypes
        import os
        from nvidia.cuda_nvrtc import lib as nvrtc_lib
        
        nvrtc_lib_path = os.path.dirname(nvrtc_lib.__file__)
        nvrtc_lib_so = os.path.join(nvrtc_lib_path, "libnvrtc.so.12")
        ctypes.CDLL(nvrtc_lib_so, mode=ctypes.RTLD_GLOBAL)

        import torch
        from diffusers import AutoPipelineForText2Image

        print("Loading SD-Turbo model...")
        self.pipeline = AutoPipelineForText2Image.from_pretrained(
            "stabilityai/sd-turbo",
            torch_dtype=torch.float16,
            variant="fp16",
        ).to("cuda")
        print("Model loaded!")

        # Share compiled kernels across workers
        with synchronized_inductor_cache("sd-turbo/v1"):
            print("Compiling UNet with torch.compile()...")
            self.pipeline.unet = torch.compile(
                self.pipeline.unet,
                mode="default",  
                dynamic=True,
            )

            # Warmup with common resolutions to trigger compilation
            print("Warming up with common resolutions...")
            for width, height in [(512, 512), (768, 512)]:
                self.pipeline(
                    prompt="warmup",
                    num_inference_steps=1,
                    width=width,
                    height=height,
                    guidance_scale=0.0,  # SD-Turbo doesn't use guidance
                )
            print("Warmup complete!")
            
            # Prevent recompilation and CUDA graphs threading issues
            self.pipeline.unet.forward = torch._dynamo.run(self.pipeline.unet.forward)

    @fal.endpoint("/")
    def generate(self, input: Input) -> Output:
        """Generate an image from a text prompt."""
        result = self.pipeline(
            prompt=input.prompt,
            num_inference_steps=1,
            width=input.width,
            height=input.height,
            guidance_scale=0.0,  # SD-Turbo doesn't use guidance
        )
        return Output(image=Image.from_pil(result.images[0]))
```

**Try it yourself:**

```bash theme={null}
# Save as sd_turbo.py
fal run sd_turbo.py

# First worker: Compiles kernels during warmup
# Subsequent workers: Load pre-compiled kernels (much faster)
```

**What you'll observe:**

* First worker takes longer during warmup (compilation happening)
* Subsequent workers warmup significantly faster (loading cached kernels)
* All workers produce identical outputs - only startup time changes

## Manual Approach (Advanced)

For more control over cache loading and syncing, you can use the explicit API:

```python theme={null}
from fal.toolkit import load_inductor_cache, sync_inductor_cache

class MyApp(fal.App):
    def setup(self):
        # Load existing cache (if available)
        dir_hash = load_inductor_cache("my-model/v1")
        
        # Compile and warmup
        self.model = torch.compile(self.model)
        self.warmup()
        
        # Sync back any new kernels
        sync_inductor_cache("my-model/v1", dir_hash)
```

**When to use the manual approach:**

* Multi-stage warmup processes
* Distributed training with controlled sync timing
* Need explicit control over cache load/sync behavior

## How It Works

### Storage Locations & Connection Mechanism

* **Local cache**: `/tmp/inductor-cache/` - Each worker's temporary cache
* **Shared cache**: `/data/inductor-caches/<GPU_TYPE>/<key>.zip` - Persistent, shared across workers

**How torch.compile() finds the cache:**

When `load_inductor_cache()` is called, it sets the environment variable:

```python theme={null}
os.environ["TORCHINDUCTOR_CACHE_DIR"] = "/tmp/inductor-cache/"
```

PyTorch's `torch.compile()` automatically reads this environment variable to locate compiled kernels. You don't need to configure anything - just call `load_inductor_cache()` before `torch.compile()` and the connection happens automatically.

### GPU Separation

Caches are GPU-specific (H100, H200, A100, etc.) and automatically organized by GPU type using `get_gpu_type()`. This ensures compiled kernels match the hardware they'll run on.

### Process Flow

The behavior differs based on whether a cache already exists:

**Cache Miss (First Worker):**

1. Load attempt → Cache not found
2. Compilation phase → torch.compile() generates CUDA kernels
3. Kernels saved to `/tmp/inductor-cache/`
4. Warmup triggers compilation
5. Sync creates `.zip` and uploads to `/data/inductor-caches/<GPU_TYPE>/<cache_key>.zip`

**Cache Hit (Subsequent Workers):**

1. Load attempt → Cache found
2. Extract `.zip` to `/tmp/inductor-cache/`
3. torch.compile() finds existing kernels
4. Warmup uses cached kernels (no compilation)
5. Sync compares hash → Usually no-op (no changes to upload)

**Key Insight:** The "sync" operation is intelligent - it only uploads if new kernels were generated.

<Note>
  This does **not** change model outputs or behavior - only startup speed changes. The compiled model produces identical results to the uncompiled version.
</Note>

## Best Practices

### Warmup Coverage

Warm up with representative input shapes to maximize cache coverage:

```python theme={null}
with synchronized_inductor_cache("my-model/v1"):
    self.model = torch.compile(
        self.model,
        mode="max-autotune",
        dynamic=True,  # Important! Allows flexibility
    )
    
    # Cover common input sizes
    for width, height in [(512, 512), (768, 512), (1024, 1024)]:
        self.warmup(width, height)
```

**Tips:**

* Use `dynamic=True` for flexibility across input variations
* Cover 3-5 representative sizes
* Focus on your most common use cases
* **Tradeoff**: More warmup shapes = longer startup, but faster inference

### When to Skip

Not all models benefit from Inductor caching:

* **CPU-only models** - No GPU compilation involved
* **Models without torch.compile** - No Inductor caching needed
* **Lightweight models** - Minimal compilation overhead, caching may not be worth it

## Troubleshooting

### Workers Still Compiling (Cache Not Working)?

If you see compilation happening on every worker despite using `synchronized_inductor_cache`:

**1. Verify you're calling warmup inside the cache context**

```python theme={null}
# ❌ Wrong - warmup outside cache context
with synchronized_inductor_cache("model/v1"):
    model = torch.compile(model)
# Warmup after context exits - not cached!
warmup()

# ✅ Correct - warmup inside cache context
with synchronized_inductor_cache("model/v1"):
    model = torch.compile(model)
    warmup()  # Triggers compilation, cache is saved
```

**2. Use `dynamic=True` for flexible input shapes**

```python theme={null}
# ❌ Without dynamic - compiles separately for each shape
model = torch.compile(model, mode="max-autotune")
warmup(512, 512)   # Compiles for 512x512
# Later: different size triggers recompilation
generate(768, 768)  # Recompiles for 768x768!

# ✅ With dynamic - handles shape variations
model = torch.compile(model, mode="max-autotune", dynamic=True)
warmup(512, 512)   # Compiles with dynamic shapes
generate(768, 768)  # Uses cached kernels! ✓
```

**3. Cover common input shapes in warmup**

If you see compilation during inference, you can add those shapes to warmup (note: this increases startup time):

```python theme={null}
with synchronized_inductor_cache("model/v1"):
    model = torch.compile(model, dynamic=True)
    
    # Warmup with all commonly used sizes
    for size in [(512, 512), (768, 512), (1024, 1024)]:
        warmup(*size)
```

### Debugging

Enable verbose logging to see what PyTorch is doing:

```python theme={null}
import os
os.environ["TORCH_LOGS"] = "recompiles"
os.environ["TORCHINDUCTOR_VERBOSE"] = "1"

# Now you'll see detailed compilation messages
```

## See Also

<CardGroup cols={2}>
  <Card title="Optimize Model Performance" icon="rocket" href="/serverless/optimizations/optimize-model-performance">
    Learn about torch.compile and the `optimize()` helper
  </Card>

  <Card title="Use Persistent Storage" icon="database" href="/serverless/development/use-persistent-storage">
    Understand the `/data` directory for persistent storage
  </Card>

  <Card title="Deploy Multi-GPU Inference" icon="server" href="/serverless/tutorials/deploy-multi-gpu-inference">
    Deploy large compiled models across multiple GPUs
  </Card>
</CardGroup>
