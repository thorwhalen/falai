> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Parallel File Loading

> Speed up model loading by pre-reading files in parallel from /data.

The `/data` filesystem on fal is a distributed, parallel storage system. It performs best when multiple files are read concurrently. Sequential file reads -- loading one weight file at a time -- significantly underutilize the filesystem and result in slower cold starts.

## The Problem

Most model loading libraries (HuggingFace, PyTorch) read weight files **sequentially** -- one shard at a time. On a distributed filesystem, this leaves most of the available bandwidth idle:

```
Sequential:
  time ──────────────────────────────────►
  ┌──file1──┐┌──file2──┐┌──file3──┐┌──file4──┐

Parallel:
  time ──────────────────►
  ┌──file1──┐
  ┌──file2──┐
  ┌──file3──┐
  ┌──file4──┐
```

## The Solution: Pre-Read Files in Parallel

Before loading your model, pre-read all weight files into the OS page cache using parallel I/O. When the model loader then reads the files, they're already cached in memory and load instantly.

```python theme={null}
import subprocess

MODEL_DIR = "/data/models/my-model"

subprocess.check_call(
    f"find '{MODEL_DIR}' -type f | xargs -P 32 -I {{}} cat {{}} > /dev/null",
    shell=True
)
```

This reads up to 32 files simultaneously, pulling them into the page cache. The subsequent `from_pretrained()` call then reads from cache instead of the network.

## Using It in Your App

Add the pre-read step at the beginning of your `setup()` method, before model loading:

```python theme={null}
import fal
import subprocess

class MyModel(fal.App):
    machine_type = "GPU-H100"

    def setup(self):
        import torch
        from diffusers import StableDiffusionXLPipeline

        model_dir = "/data/models/stable-diffusion-xl"

        # Pre-read all model files in parallel
        subprocess.check_call(
            f"find '{model_dir}' -type f | xargs -P 32 -I {{}} cat {{}} > /dev/null",
            shell=True
        )

        # Now load the model -- files are already in page cache
        self.pipe = StableDiffusionXLPipeline.from_pretrained(
            model_dir,
            torch_dtype=torch.float16,
        ).to("cuda")
```

### Python Helper

For a cleaner approach, wrap it in a function:

```python theme={null}
import subprocess
from pathlib import Path

def preload_files(directory: str, parallelism: int = 32):
    """Pre-read all files in a directory into the OS page cache."""
    subprocess.check_call(
        f"find '{directory}' -type f | xargs -P {parallelism} -I {{}} cat {{}} > /dev/null",
        shell=True
    )
```

```python theme={null}
def setup(self):
    preload_files("/data/models/my-model")
    self.model = load_model("/data/models/my-model")
```

## When to Use This

| Scenario                                                     | Recommendation                                                                                                                                |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Loading HuggingFace models from `/data`                      | Use parallel pre-reading                                                                                                                      |
| Loading custom PyTorch checkpoints with multiple shard files | Use parallel pre-reading                                                                                                                      |
| Loading a single large file                                  | Less benefit -- the bottleneck is single-file transfer speed. Consider [FlashPack](/documentation/serverless/optimizations/flashpack) instead |
| Models already in local node cache (warm runners)            | Minimal benefit -- files are already fast to read                                                                                             |

## How It Works

fal's `/data` is a distributed filesystem that can serve many files concurrently at high throughput. When you read files sequentially, you use only a fraction of the available bandwidth. The `xargs -P 32` approach fires off 32 concurrent `cat` commands, each reading a different file. The OS caches the file contents in memory (page cache), so when your model loader reads the same files moments later, it reads from RAM instead of the network.

<Tip>
  Adjust the parallelism (`-P 32`) based on your model. For models with many small files (e.g., 100+ safetensors shards), higher parallelism helps. For models with a few large files, lower parallelism (8-16) is sufficient.
</Tip>

## Comparison with FlashPack

|                         | Parallel Pre-Reading            | FlashPack                                  |
| ----------------------- | ------------------------------- | ------------------------------------------ |
| **What it does**        | Pre-reads files into OS cache   | Streams tensors directly to GPU            |
| **Works with**          | Any files in any format         | PyTorch models (custom format)             |
| **Requires conversion** | No -- works with existing files | Yes -- must convert to `.flashpack` format |
| **Best for**            | Quick win with existing models  | Maximum performance with converted models  |

Both techniques can be combined -- use parallel pre-reading as a quick improvement, then migrate to FlashPack for even faster loading.

<CardGroup cols={2}>
  <Card title="FlashPack" icon="arrow-right" href="/documentation/serverless/optimizations/flashpack">
    High-throughput tensor loading at up to 25 Gbps
  </Card>

  <Card title="Persistent Storage" icon="arrow-right" href="/documentation/development/use-persistent-storage">
    How /data works and caching behavior
  </Card>
</CardGroup>
