> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Optimizing Cold Starts

> Understanding cold starts and how to reduce them.

## Cold Starts vs Warm Starts

A **cold start** occurs when a new runner needs to be created from scratch. The runner goes through `PENDING` → `SETUP` → `IDLE` (or `PENDING` → `DOCKER_PULL` → `SETUP` → `IDLE` if the Docker image isn't [cached](/documentation/deployment/caching)) before it can serve requests.

A **warm start** occurs when an existing IDLE runner is reused to handle a new request: `IDLE` → `RUNNING`.

### What Triggers Cold Starts

* No warm runners available (all busy or expired)
* Traffic spike exceeds warm runner capacity
* First deployment
* Runners expired during low traffic periods

### Factors Affecting Cold Start Duration

* **Image size**: Larger Docker images take longer to pull
* **Model size**: Larger models take longer to download and load
* **Setup complexity**: Complex initialization in `setup()` adds time
* **Cache state**: First runs are slower, subsequent runs benefit from caching
* **Hardware availability**: GPU availability varies by region and time

## How to Reduce Cold Starts

Each of these strategies targets a different phase of the cold start:

<CardGroup cols={2}>
  <Card title="Scaling Parameters" icon="sliders" href="/documentation/serverless/optimizations/cold-start-scaling">
    Keep warm runners available with keep\_alive, min\_concurrency, and buffers
  </Card>

  <Card title="Container Images" icon="docker" href="/documentation/serverless/optimizations/optimize-container-images">
    Reduce image size for faster pulls with multi-stage builds and smaller base images
  </Card>

  <Card title="Compiled Caches" icon="bolt" href="/documentation/serverless/optimizations/optimize-startup-with-compiled-caches">
    Cache compiled kernels to speed up setup() across runners
  </Card>

  <Card title="Persistent Storage" icon="hard-drive" href="/documentation/development/use-persistent-storage">
    Download models to /data for automatic caching between runners
  </Card>
</CardGroup>
