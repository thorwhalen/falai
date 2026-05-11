> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Caching

> How fal's multi-layer caching system reduces cold start times by caching Docker images, model weights, and compiled artifacts.

Every time a new [runner](/documentation/deployment/runners) starts, it needs Docker image layers, model weights, and potentially compiled model caches before it can serve requests. Without caching, each runner would download everything from scratch, leading to cold starts that can take minutes for large models. fal's caching system stores these artifacts at multiple levels so that subsequent runners start faster, and cold start times improve progressively as your app serves traffic.

Docker layers and files on [`/data`](/documentation/development/use-persistent-storage) are cached automatically -- you don't need to configure anything. Compiled model caches (PyTorch Inductor) require explicit use of the [`synchronized_inductor_cache()`](/documentation/serverless/optimizations/optimize-startup-with-compiled-caches) API. Understanding the cache layers helps you reason about why cold starts improve over time and how to structure your app for the best startup performance. For strategies to reduce cold starts further, see [Optimizing Cold Starts](/documentation/serverless/optimizations/optimize-cold-starts).

## Cache Layers

Docker images and `/data` storage use different caching mechanisms.

### `/data` Storage Cache

Files on [`/data`](/documentation/development/use-persistent-storage) (model weights, compiled caches, any files your app writes) go through a three-layer cache:

| Cache Layer           | Speed      | Scope                  | Use Case                            |
| :-------------------- | :--------- | :--------------------- | :---------------------------------- |
| **Local Node Cache**  | 10-15 GB/s | Same physical machine  | RAID 5 NVMe drives on the node      |
| **Distributed Cache** | 6-8 GB/s   | Same datacenter/region | 100 Gbps network across all servers |
| **Object Store**      | 1.5-8 GB/s | Global                 | Backing store for all files         |

When a runner reads a file from `/data`, it checks the local node cache first. If the file isn't found locally, it checks the distributed datacenter cache. If that also misses, it fetches from the object store and populates both caches on the way back. This means the first runner in a region pays the full download cost, but every runner after it benefits from progressively faster access.

### Docker Image Cache

Docker images are cached separately using the node's Docker daemon. The scheduler [prefers nodes](/documentation/deployment/scale-your-application) that already have your image cached. If no cached node is available, the image is pulled from the container registry. Build-time layer caching is handled through BuildKit's registry cache, so rebuilds after small Dockerfile changes only rebuild the affected layers.

## What Gets Cached

**Docker Image Layers** -- container images are split into layers, and each layer is cached independently. If you change a single dependency in your Dockerfile, only the affected layers are re-pulled. The base image and unchanged layers come from cache. See [Optimize Container Images](/documentation/serverless/optimizations/optimize-container-images) for tips on structuring your Dockerfile for better layer caching.

**Model Weights** -- files downloaded to `/data` are automatically cached across runners through the three-layer `/data` cache described above. This includes Hugging Face models (cached at `/data/.cache/huggingface` via the `HF_HOME` [environment variable](/documentation/development/environment-variables)), weights downloaded with [`download_model_weights()`](/documentation/development/working-with-files#downloading-model-weights), and any other files you write to `/data`. The first runner downloads the weights; subsequent runners read from the local or distributed cache.

**Compiled Model Caches** -- PyTorch Inductor compiled models and other JIT compilation artifacts. If you use [`torch.compile()`](https://pytorch.org/docs/stable/generated/torch.compile.html), you can persist and share the resulting compiled kernels across runners using [`synchronized_inductor_cache()`](/documentation/serverless/optimizations/optimize-startup-with-compiled-caches). This stores the cache on `/data` (at `/data/inductor-caches/<GPU_TYPE>/`), where it benefits from the same three-layer cache. See [Compiled Kernel Caching](/documentation/serverless/optimizations/optimize-startup-with-compiled-caches) for setup instructions.

## How Caches Warm Up

Caches warm progressively as your application serves traffic:

1. **First runner** -- pulls the Docker image from the registry and downloads model weights from the object store. Populates the local and distributed `/data` caches. This is the slowest cold start.
2. **Second runner on the same node** -- Docker image is already in the node's Docker cache, and model weights are in the local NVMe cache. Cold start is significantly faster.
3. **Runners on other nodes** -- model weights are served from the distributed `/data` cache. The scheduler prefers nodes where the Docker image is already cached, but may pull from the registry if needed.
4. **Over time** -- as more nodes serve your app, caches spread across the region. Cold starts converge to the time it takes to run `setup()` with all files already available locally.

<Note>
  Caches are not permanent. Local caches may be evicted when nodes are recycled or under memory pressure. If your app hasn't had traffic for a while, the first cold start after a quiet period may be slower as caches are repopulated.
</Note>
