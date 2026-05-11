> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction to Compute

> Dedicated GPU instances for training, fine-tuning, and workloads that need sustained access to hardware.

fal Compute gives you dedicated GPU instances that run continuously under your control. Unlike [Serverless](/documentation/deployment/deploy-to-production), where runners scale automatically and you pay per-second of execution, Compute instances stay running for as long as you need them. You SSH in, install your stack, and use the GPU directly. This makes Compute the right choice for training runs, long-running fine-tuning jobs, batch processing, and any workload where you need sustained, predictable access to hardware rather than on-demand scaling.

Compute runs on NVIDIA H100 SXM GPUs with high-speed SSD storage. For distributed workloads, 8-GPU instances can be provisioned in the same sector, connecting them over InfiniBand for low-latency multi-node communication. Instances are billed per-hour at fixed rates, so your costs are predictable regardless of how you use the GPU. For workloads that are better served by autoscaling and pay-per-use, see [Serverless](/documentation/serverless/pricing) instead.

## Instance Types

Two instance types are available, both built on H100 SXM GPUs:

| Instance Type  | GPUs | vCPU | RAM      | VRAM   | Storage  |
| :------------- | :--- | :--- | :------- | :----- | :------- |
| **1xH100-SXM** | 1    | 16   | 200 GB   | 80 GB  | 1 TB SSD |
| **8xH100-SXM** | 8    | 128  | 1,600 GB | 640 GB | 8 TB SSD |

The **1xH100** is suited for development, single-GPU fine-tuning, and inference workloads. The **8xH100** is designed for large-scale training, multi-GPU inference, and distributed computing. Resources scale proportionally: the 8-GPU instance has 8x the CPU cores, memory, VRAM, and storage of the single-GPU instance.

## Multi-Node and InfiniBand

When you need to distribute a workload across multiple machines, provision 8xH100 instances in the same **sector**. Instances within a sector are connected over InfiniBand, providing ultra-low latency and high bandwidth for frameworks like PyTorch DDP, DeepSpeed, and Horovod.

<Note>
  InfiniBand and sector placement are only available on 8xH100 instances. 1xH100 instances run as standalone machines without inter-node connectivity.
</Note>

## When to Use Compute vs Serverless

The two products serve different workload profiles:

|                 | Compute                                     | Serverless                                      |
| :-------------- | :------------------------------------------ | :---------------------------------------------- |
| **Billing**     | Per-hour, fixed rate                        | Per-second of runner lifetime                   |
| **Scaling**     | Manual (you manage instances)               | Automatic (runners scale with traffic)          |
| **Access**      | Full SSH access to the machine              | Code runs inside managed runners                |
| **Best for**    | Training, fine-tuning, batch jobs, research | API endpoints, on-demand inference, autoscaling |
| **Cold starts** | None (instance is always running)           | Yes (new runners need startup time)             |

Use Compute when you need sustained GPU access for hours or days at a time. Use Serverless when you need an API that scales to zero and handles traffic spikes automatically.

## Getting Started

Provisioning an instance takes about 2-3 minutes. You choose an instance type, select a sector (for multi-node setups), paste your SSH public key, and click create. Once the instance is ready, you SSH in and have full control.

<CardGroup cols={2}>
  <Card title="Quickstart" icon="rocket" href="/documentation/compute/quickstart">
    Provision your first instance and run a GPU workload
  </Card>

  <Card title="Pricing" icon="credit-card" href="/documentation/compute/pricing">
    Per-hour rates by instance type
  </Card>
</CardGroup>
