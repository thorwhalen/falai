> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Machine Types

> Available machine types, specifications, and guidance on choosing the right GPU for your workload.

## CPU Machine Types

For lightweight workloads that don't require GPU acceleration -- routing, preprocessing, API proxies.

| Machine Type | RAM    | CPU Cores |
| :----------- | :----- | :-------- |
| **XS**       | 512 MB | 0.5       |
| **S**        | 1 GB   | 1         |
| **M**        | 2 GB   | 2         |
| **L**        | 15 GB  | 4         |
| **XL**       | 30 GB  | 8         |

## GPU Machine Types

| Machine Type                                                                               | VRAM   | RAM    | CPU | Bandwidth | Video Enc / Dec |
| :----------------------------------------------------------------------------------------- | :----- | :----- | :-- | :-------- | :-------------- |
| [**GPU-RTX4090**](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/) | 24 GB  | 48 GB  | 12  | 1.0 TB/s  | 2 / 2           |
| [**GPU-RTX5090**](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/) | 32 GB  | 60 GB  | 14  | 1.8 TB/s  | 3 / 3 (AV1)     |
| [**GPU-A100**](https://www.nvidia.com/en-us/data-center/a100/)                             | 40 GB  | 60 GB  | 12  | 2.0 TB/s  | -- / 5          |
| [**GPU-L40**](https://www.nvidia.com/en-us/data-center/l40s/)                              | 48 GB  | 100 GB | 6   | 0.9 TB/s  | 3 / 3 (AV1)     |
| [**GPU-H100**](https://www.nvidia.com/en-us/data-center/h100/)                             | 80 GB  | 112 GB | 12  | 3.4 TB/s  | -- / 7          |
| [**GPU-H200**](https://www.nvidia.com/en-us/data-center/h200/)                             | 141 GB | 112 GB | 12  | 4.8 TB/s  | -- / 7          |
| [**GPU-B200**](https://www.nvidia.com/en-us/data-center/b200/)                             | 192 GB | 210 GB | 19  | 8.0 TB/s  | -- / 7          |

Video encode/decode counts refer to hardware [NVENC/NVDEC](https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new) engines -- dedicated hardware units that encode or decode video independently of the GPU's compute cores. GPUs with encoders (RTX 5090, L40) can output video frames without using GPU compute time. GPUs marked `--` for encode have no hardware encoder and require software encoding on the CPU.

### Choosing a GPU

**By VRAM requirement** -- pick the smallest GPU that fits your model:

* **24 GB** (RTX 4090): SDXL, Flux, most LoRA fine-tunes
* **32 GB** (RTX 5090): Larger diffusion models, video generation with [AV1 hardware encode](https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new)
* **40 GB** (A100): General-purpose training and inference at a lower price point than Hopper GPUs
* **48 GB** (L40): AI inference combined with [video transcoding](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/nvidia-l40s-ucsc-gpu-l40s.pdf) and graphics rendering
* **80 GB** (H100): LLM inference and training, [NVLink 4.0 at 900 GB/s](https://resources.nvidia.com/en-us-data-center-overview/nvidia-tensor-core-gpu-datasheet) for multi-GPU scaling
* **141 GB** (H200): Large models and long-context workloads on a single GPU -- [76% more memory and 43% more bandwidth than H100](https://resources.nvidia.com/en-us-dgx-systems/dgx-h200-datasheet)
* **192 GB** (B200): Maximum memory and compute for the largest models, [FP4/FP6/FP8 precision support](https://www.techpowerup.com/gpu-specs/b200.c4210)

**By workload type:**

* **Image generation**: RTX 4090 or RTX 5090 (cost-effective, good throughput)
* **Video generation**: RTX 5090 (3 NVENC encoders, AV1 encode) or L40 (3 NVENC + 3 NVDEC)
* **LLM inference**: H100 or H200 (high bandwidth, large VRAM)
* **Training**: A100, H100, or H200 (depending on model size)
* **Largest models**: B200 or multi-GPU H100/H200

## Configuration

Set the machine type in your application:

```python theme={null}
class MyApp(fal.App):
    machine_type = "GPU-H100"
    num_gpus = 1
```

### Multiple Machine Types

Allow your app to use multiple machine types for a larger pool of available machines:

```python theme={null}
class MyApp(fal.App):
    machine_type = ["GPU-H100", "GPU-A100"]
```

Machine types are tried in order. If the first type has no available capacity, the next is used.

### Multi-GPU

For models that need more than one GPU:

```python theme={null}
class MyApp(fal.App):
    machine_type = "GPU-H100"
    num_gpus = 2
```

<Card title="Multi-GPU Workloads" icon="arrow-right" href="/documentation/serverless/distributed/overview">
  Learn how to distribute inference across multiple GPUs
</Card>

## Changing Machine Types

**Via Code:**

Update `machine_type` and redeploy:

```python theme={null}
class MyApp(fal.App):
    machine_type = "GPU-A100"
```

```bash theme={null}
fal deploy
```

<Note>
  `machine_type` is a code-specific parameter -- it always comes from your code and resets on every deploy. See [Scaling Configuration](/documentation/deployment/scaling-configuration) for details.
</Note>
