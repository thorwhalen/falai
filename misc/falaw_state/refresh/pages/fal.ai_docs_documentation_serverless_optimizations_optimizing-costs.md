> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Optimizing Costs

Since Serverless billing covers the entire runner lifetime, the most effective cost optimizations focus on reducing idle time, maximizing utilization, and minimizing setup duration.

## Reduce Idle Time

Idle time is the single biggest cost lever. Every second a runner is alive but not processing requests is billed.

### Tune `keep_alive`

The `keep_alive` parameter controls how long a runner stays alive after finishing its last request. Lower values reduce idle billing but increase cold starts.

```python theme={null}
class MyApp(fal.App, keep_alive=30):  # 30 seconds (default: 60)
    ...
```

| `keep_alive`    | Trade-off                           |
| --------------- | ----------------------------------- |
| High (300s+)    | Low latency, higher idle costs      |
| Medium (30-60s) | Balanced for moderate traffic       |
| Low (10-30s)    | Cost-efficient for bursty workloads |

### Set `min_concurrency` carefully

Each runner in `min_concurrency` runs continuously and is billed 24/7. Only use it for latency-critical applications that cannot tolerate cold starts.

```python theme={null}
class MyApp(fal.App, min_concurrency=0):  # No always-on runners
    ...
```

## Maximize Runner Utilization

Runners that process one request at a time have idle gaps between sequential requests. Multiplexing eliminates these gaps.

### Use multiplexing

`max_multiplexing` allows a single runner to process multiple requests concurrently, filling idle time while one request waits on I/O.

```python theme={null}
class MyApp(fal.App, max_multiplexing=4):
    ...
```

This is especially effective for workloads with I/O waits (network calls, file downloads) where the GPU would otherwise sit idle between operations.

### Concurrency buffer

`concurrency_buffer` pre-warms runners before existing ones reach capacity. This reduces latency spikes but keeps more runners alive.

```python theme={null}
class MyApp(fal.App, max_multiplexing=4, concurrency_buffer=2):
    ...
```

Use conservatively — each buffered runner is billed while alive.

## Reduce Setup Time

Since `setup()` time is billed, faster initialization directly reduces cost per cold start. This matters most for applications with frequent cold starts (low `keep_alive`, bursty traffic).

<CardGroup cols={2}>
  <Card title="FlashPack" icon="bolt" href="/documentation/serverless/optimizations/flashpack">
    High-throughput tensor loading for faster model initialization.
  </Card>

  <Card title="Optimizing Cold Starts" icon="gauge-high" href="/documentation/serverless/optimizations/optimize-cold-starts">
    Strategies for reducing container startup and setup time.
  </Card>

  <Card title="Compiled Caches" icon="database" href="/documentation/serverless/optimizations/optimize-startup-with-compiled-caches">
    Cache compiled kernels to skip recompilation on startup.
  </Card>

  <Card title="Persistent Storage" icon="hard-drive" href="/documentation/development/file-storage">
    Use /data to cache downloads across runner restarts.
  </Card>
</CardGroup>

## Right-Size Your Machine Type

Don't over-provision GPU resources. A model that runs fine on an A6000 doesn't need an H100.

* Compare inference latency across machine types to find the smallest GPU that meets your requirements
* Consider that a cheaper machine running slightly longer may cost less than a faster, more expensive one
* See [Machine Types](/documentation/deployment/machine-types) for available options

## Use Scaling Parameters Wisely

### `scaling_delay`

Prevents spinning up new runners for short traffic spikes. The platform waits this duration before provisioning additional runners.

```python theme={null}
class MyApp(fal.App, scaling_delay=15):  # Wait 15s before scaling up
    ...
```

Useful for workloads with brief bursts that don't justify new runners.

### `max_concurrency`

Caps the total number of concurrent runners. This sets a hard ceiling on your spend but may increase queue times during traffic spikes.

```python theme={null}
class MyApp(fal.App, max_concurrency=5):  # At most 5 runners
    ...
```

## Monitor and Iterate

Use the platform's observability tools to identify cost optimization opportunities:

* **[App Analytics](/documentation/serverless/observability/app-analytics)**: Identify apps with low utilization (high idle time relative to processing time)
* **[Error Analytics](/documentation/serverless/observability/error-analytics)**: Find apps with high error rates that waste compute on failed requests
* **[Exporting Metrics](/documentation/serverless/observability/exporting-metrics)**: Set up alerts for unusual spending patterns

<Tip>
  Start with the defaults, then monitor your App Analytics for a few days. Look for runners with high idle-to-processing ratios — those are your best candidates for `keep_alive` and `min_concurrency` adjustments.
</Tip>
