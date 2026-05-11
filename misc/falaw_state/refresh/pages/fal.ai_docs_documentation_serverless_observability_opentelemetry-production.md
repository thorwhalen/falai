> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenTelemetry in Production

> Configure sampling, batch export tuning, and graceful flush so your traces hold up under production load

Exporting 100% of traces from a high-throughput app generates significant backend ingestion cost, and spans buffered in `BatchSpanProcessor` are silently dropped when a runner shuts down if they are not flushed before `SIGKILL` arrives. For basic tracing setup, start with [Custom Traces](/documentation/serverless/observability/opentelemetry-traces).

## Conditional Tracing

Disable tracing entirely with an environment variable when you do not need it. When no `TracerProvider` is configured, the OpenTelemetry SDK returns a no-op tracer. All `start_as_current_span` calls become zero-cost no-ops and no export threads are started.

```python Python theme={null}
def setup_tracer(service_name: str):
    import os
    from opentelemetry import trace
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor

    if os.environ.get("ENABLE_TRACING", "true").lower() != "true":
        return trace.get_tracer(service_name), None

    resource = Resource.create({"service.name": service_name})
    provider = TracerProvider(resource=resource)
    provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
    trace.set_tracer_provider(provider)
    return trace.get_tracer(service_name), provider
```

Set `ENABLE_TRACING=false` as a fal secret to turn off tracing without redeploying:

```bash theme={null}
fal secrets set ENABLE_TRACING=false
```

## Sampling

Sampling reduces the fraction of traces exported. Use it when your app handles many requests per second and exporting every trace would exceed your backend's ingestion limits or add measurable latency.

`ParentBased(root=TraceIdRatioBased(rate))` is the recommended sampler for services that receive calls from other services. It honours the sampling decision made upstream (so a trace that was sampled by a caller is always sampled here too), and applies ratio-based sampling only to new root spans.

```python Python theme={null}
def setup_tracer(service_name: str):
    import os
    from opentelemetry import trace
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from opentelemetry.sdk.trace.sampling import ParentBased, TraceIdRatioBased

    if os.environ.get("ENABLE_TRACING", "true").lower() != "true":
        return trace.get_tracer(service_name), None

    # OTEL_SAMPLE_RATE=0.1 exports 10% of root spans; default is 1.0 (all spans).
    sample_rate = float(os.environ.get("OTEL_SAMPLE_RATE", "1.0"))
    sampler = ParentBased(root=TraceIdRatioBased(sample_rate))

    resource = Resource.create({"service.name": service_name})
    provider = TracerProvider(resource=resource, sampler=sampler)
    provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
    trace.set_tracer_provider(provider)
    return trace.get_tracer(service_name), provider
```

Start with `OTEL_SAMPLE_RATE=0.1` under heavy load and increase it if you need more coverage for debugging.

## Batch Export Tuning

`BatchSpanProcessor` buffers spans in memory and exports them in bulk. Tune these parameters if you see dropped spans under burst traffic or export timeouts in your backend logs.

```python Python theme={null}
processor = BatchSpanProcessor(
    OTLPSpanExporter(),
    # Drop oldest spans when the in-memory queue is full.
    # Increase this if you see "SpanProcessor queue is full" warnings.
    max_queue_size=2048,
    # Spans per HTTP request to the collector.
    # Larger batches reduce request overhead at the cost of higher memory use.
    max_export_batch_size=512,
    # How often to flush the buffer, in milliseconds.
    schedule_delay_millis=5000,
    # Give up on an export request after this long.
    export_timeout_millis=30_000,
)
```

| Parameter               | Default | When to increase                                   |
| ----------------------- | ------- | -------------------------------------------------- |
| `max_queue_size`        | 2048    | Seeing dropped spans under burst traffic           |
| `max_export_batch_size` | 512     | High span volume with low per-request overhead     |
| `schedule_delay_millis` | 5000    | Backend is overwhelmed by frequent export requests |
| `export_timeout_millis` | 30000   | Backend is slow or on a high-latency network       |

## Flushing on Shutdown

fal gives runners a 5-second grace period between `SIGTERM` and `SIGKILL`. `teardown()` runs during that window, after all in-flight requests finish. See [App Lifecycle](/documentation/development/app-lifecycle) for the full shutdown sequence.

Call `force_flush()` in `teardown()`, not in your endpoint handler. Per-request flushing adds latency on every call; `BatchSpanProcessor` handles periodic exports on its own schedule.

```python Python theme={null}
import os

import fal
from fal.toolkit import Image
from pydantic import BaseModel, Field

def setup_tracer(service_name: str):
    from opentelemetry import trace
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from opentelemetry.sdk.trace.sampling import ParentBased, TraceIdRatioBased

    if os.environ.get("ENABLE_TRACING", "true").lower() != "true":
        return trace.get_tracer(service_name), None

    sample_rate = float(os.environ.get("OTEL_SAMPLE_RATE", "1.0"))
    sampler = ParentBased(root=TraceIdRatioBased(sample_rate))

    resource = Resource.create({"service.name": service_name})
    provider = TracerProvider(resource=resource, sampler=sampler)
    provider.add_span_processor(
        BatchSpanProcessor(
            OTLPSpanExporter(),
            max_queue_size=2048,
            max_export_batch_size=512,
            schedule_delay_millis=5000,
            export_timeout_millis=30_000,
        )
    )
    trace.set_tracer_provider(provider)
    return trace.get_tracer(service_name), provider


class Input(BaseModel):
    prompt: str = Field(description="The prompt to generate an image from")
    num_inference_steps: int = Field(default=20)


class Output(BaseModel):
    image: Image
    trace_id: str


class ProductionApp(fal.App):
    machine_type = "GPU-A100"
    requirements = [
        "hf-transfer==0.1.9",
        "diffusers[torch]==0.32.2",
        "torch==2.10.0",
        "transformers[sentencepiece]==4.51.0",
        "accelerate==1.6.0",
        "opentelemetry-sdk==1.41.0",
        "opentelemetry-exporter-otlp-proto-http==1.41.0",
    ]

    def setup(self):
        # Enable HF Transfer for faster downloads
        os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

        import torch
        from diffusers import StableDiffusionXLPipeline

        self.tracer, self.tracer_provider = setup_tracer("text-to-image")

        self.pipe = StableDiffusionXLPipeline.from_pretrained(
            "stabilityai/stable-diffusion-xl-base-1.0",
            torch_dtype=torch.float16,
            variant="fp16",
            use_safetensors=True,
        ).to("cuda")
        self.pipe("warmup")

    @fal.endpoint("/")
    def run(self, input: Input) -> Output:
        with self.tracer.start_as_current_span("text-to-image") as root:
            root.set_attribute("model.name", "stable-diffusion-xl-base-1.0")

            with self.tracer.start_as_current_span("inference"):
                result = self.pipe(input.prompt, num_inference_steps=input.num_inference_steps)

            with self.tracer.start_as_current_span("upload"):
                image = Image.from_pil(result.images[0])

            trace_id = format(root.get_span_context().trace_id, "032x")

        return Output(image=image, trace_id=trace_id)

    def teardown(self):
        # Flush buffered spans before SIGKILL (5s grace period).
        # Use 4000ms to leave headroom for SIGKILL at 5000ms.
        if self.tracer_provider:
            self.tracer_provider.force_flush(timeout_millis=4000)
```

<Warning>
  The 5-second grace period is a shared budget across `handle_exit()`, remaining in-flight requests, `teardown()`, and `force_flush()`. If your endpoint handles long-running requests, use `handle_exit()` to signal them to stop early so `teardown()` has enough time to flush. See [App Lifecycle](/documentation/development/app-lifecycle) for the full shutdown sequence.
</Warning>

## What's Next

<CardGroup cols={2}>
  <Card title="Custom Traces" icon="code-branch" href="/documentation/serverless/observability/opentelemetry-traces">
    Add spans to trace inference stages end to end
  </Card>

  <Card title="Custom Metrics" icon="chart-bar" href="/documentation/serverless/observability/custom-metrics">
    Counters, histograms, and gauges for your inference workload
  </Card>

  <Card title="Cross-Service Tracing" icon="diagram-project" href="/documentation/serverless/observability/opentelemetry-cross-service">
    Connect traces across multiple fal apps
  </Card>

  <Card title="App Lifecycle" icon="rotate" href="/documentation/development/app-lifecycle">
    Full shutdown sequence and grace period details
  </Card>
</CardGroup>
