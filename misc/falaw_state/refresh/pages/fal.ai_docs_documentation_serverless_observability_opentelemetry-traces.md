> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Traces with OpenTelemetry

> Add OpenTelemetry spans to your fal app to trace inference stages like warmup, diffusion, and image upload

fal apps run on standard Python, so you can instrument them with the OpenTelemetry SDK the same way you would any other service. Add the SDK to `requirements`, initialize a tracer in `setup()`, and wrap your inference stages with spans. For custom metrics instrumentation, see [Custom Metrics](/documentation/serverless/observability/custom-metrics). For tracing across multiple fal apps, see [Cross-Service Tracing](/documentation/serverless/observability/opentelemetry-cross-service).

## Prerequisites

You need an OTLP-compatible backend. Any of the following work:

| Backend        | OTLP endpoint                                         | Auth header                                      |
| -------------- | ----------------------------------------------------- | ------------------------------------------------ |
| New Relic (US) | `https://otlp.nr-data.net:4318`                       | `api-key=<INGEST_LICENSE_KEY>`                   |
| New Relic (EU) | `https://otlp.eu01.nr-data.net:4318`                  | `api-key=<INGEST_LICENSE_KEY>`                   |
| Datadog (US)   | `https://otlp.datadoghq.com`                          | `dd-api-key=<API_KEY>`                           |
| Datadog (EU)   | `https://otlp.datadoghq.eu`                           | `dd-api-key=<API_KEY>`                           |
| Grafana Cloud  | `https://otlp-gateway-prod-<region>.grafana.net/otlp` | `Authorization=Basic <base64(instanceId:token)>` |
| Honeycomb      | `https://api.honeycomb.io`                            | `x-honeycomb-team=<API_KEY>`                     |

Store your credentials as fal secrets so they are available as environment variables on the runner without being embedded in your code.

<Tabs>
  <Tab title="Datadog (US)">
    ```bash theme={null}
    fal secrets set OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.datadoghq.com
    fal secrets set OTEL_EXPORTER_OTLP_HEADERS="dd-api-key=<YOUR_API_KEY>"
    ```
  </Tab>

  <Tab title="Datadog (EU)">
    ```bash theme={null}
    fal secrets set OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.datadoghq.eu
    fal secrets set OTEL_EXPORTER_OTLP_HEADERS="dd-api-key=<YOUR_API_KEY>"
    ```
  </Tab>

  <Tab title="New Relic (US)">
    ```bash theme={null}
    fal secrets set OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.nr-data.net:4318
    fal secrets set OTEL_EXPORTER_OTLP_HEADERS="api-key=<YOUR_LICENSE_KEY>"
    ```
  </Tab>

  <Tab title="New Relic (EU)">
    ```bash theme={null}
    fal secrets set OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.eu01.nr-data.net:4318
    fal secrets set OTEL_EXPORTER_OTLP_HEADERS="api-key=<YOUR_LICENSE_KEY>"
    ```
  </Tab>

  <Tab title="Grafana Cloud">
    ```bash theme={null}
    fal secrets set OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp-gateway-prod-<region>.grafana.net/otlp
    fal secrets set OTEL_EXPORTER_OTLP_HEADERS="Authorization=Basic <base64(instanceId:token)>"
    ```
  </Tab>

  <Tab title="Honeycomb">
    ```bash theme={null}
    fal secrets set OTEL_EXPORTER_OTLP_ENDPOINT=https://api.honeycomb.io
    fal secrets set OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=<YOUR_API_KEY>"
    ```
  </Tab>
</Tabs>

See [Managing Secrets](/documentation/development/manage-secrets-securely) for details on how fal secrets work.

## Adding Traces to Your App

Add `opentelemetry-sdk` and `opentelemetry-exporter-otlp-proto-http` to your app's `requirements`. The exporter reads `OTEL_EXPORTER_OTLP_ENDPOINT` and `OTEL_EXPORTER_OTLP_HEADERS` from the environment automatically, no endpoint or auth code required.

Initialize the tracer in `setup()`. The provider and export connection are created once per runner, not once per request.

The example below builds on the [Stable Diffusion XL quickstart](/documentation/development/getting-started/deploy-your-first-image-generator) and adds spans around each stage of a text-to-image request.

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

    resource = Resource.create({"service.name": service_name})
    provider = TracerProvider(resource=resource)
    provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
    trace.set_tracer_provider(provider)
    return trace.get_tracer(service_name), provider


class Input(BaseModel):
    prompt: str = Field(description="The prompt to generate an image from")
    num_inference_steps: int = Field(default=20)


class Output(BaseModel):
    image: Image
    trace_id: str


class TextToImageApp(fal.App):
    machine_type = "GPU-H100"
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

        # Warmup runs once per runner at startup - not per request.
        # It compiles CUDA kernels so the first real request does not pay that cost.
        with self.tracer.start_as_current_span("warmup") as span:
            span.set_attribute("model.name", "stable-diffusion-xl-base-1.0")
            self.pipe("warmup")

    @fal.endpoint("/")
    def run(self, input: Input) -> Output:
        with self.tracer.start_as_current_span("text-to-image") as root:
            root.set_attribute("model.name", "stable-diffusion-xl-base-1.0")
            root.set_attribute("prompt.length", len(input.prompt))
            root.set_attribute("num_inference_steps", input.num_inference_steps)

            with self.tracer.start_as_current_span("inference") as span:
                span.set_attribute("num_inference_steps", input.num_inference_steps)
                result = self.pipe(
                    input.prompt,
                    num_inference_steps=input.num_inference_steps,
                )

            with self.tracer.start_as_current_span("upload"):
                image = Image.from_pil(result.images[0])

            trace_id = format(root.get_span_context().trace_id, "032x")

        return Output(image=image, trace_id=trace_id)

    def teardown(self):
        # Flush buffered spans before SIGKILL (5s grace period).
        # For sampling, batch tuning, and conditional tracing see Production Configuration.
        if self.tracer_provider:
            self.tracer_provider.force_flush(timeout_millis=4000)
```

## Span Structure

The example above produces a tree of spans under a single root:

```
text-to-image
├── inference
└── upload
```

The `warmup` span appears in your backend attached to the runner's startup trace, not to individual requests. Each request produces its own `text-to-image` root span. The parent span's duration covers all of its children, so `text-to-image` reflects the total request time including upload.

The trace appears in your backend like this, with `inference` and `upload` shown as timed children of the root span:

<Frame>
  <img src="https://mintcdn.com/fal-d8505a2e/zo-kE_ST4HOR1zo1/images/observability/opentelemetry-traces.png?fit=max&auto=format&n=zo-kE_ST4HOR1zo1&q=85&s=2afe2c89b16cc8ab8b5752e316f61b69" alt="Span tree showing text-to-image root span with inference and upload children in a trace backend" width="2426" height="1578" data-path="images/observability/opentelemetry-traces.png" />
</Frame>

## Span Attributes

Call `span.set_attribute(key, value)` to attach metadata to a span. Attributes appear as filterable fields in your backend's trace viewer, so you can search for all traces where `num_inference_steps` is above a threshold or `prompt.length` exceeds a limit.

```python Python theme={null}
with self.tracer.start_as_current_span("inference") as span:
    span.set_attribute("model.name", "stable-diffusion-xl-base-1.0")
    span.set_attribute("num_inference_steps", input.num_inference_steps)
    span.set_attribute("prompt.length", len(input.prompt))
    span.set_attribute("guidance_scale", 7.5)
```

Attribute keys follow the [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/) where applicable. For model-specific attributes, use a consistent namespace like `model.*` or `inference.*`.

## Marking Errors

Use `record_exception` and `set_status` to mark a span as failed. This is the portable OpenTelemetry pattern — all OTLP backends interpret `StatusCode.ERROR` as a failed span, whereas a custom `error` attribute is backend-specific metadata.

```python Python theme={null}
from opentelemetry.trace import Status, StatusCode

with self.tracer.start_as_current_span("inference") as span:
    try:
        result = self.pipe(input.prompt)
    except RuntimeError as e:
        span.record_exception(e)
        span.set_status(Status(StatusCode.ERROR, str(e)))
        raise
```

<Note>
  `BatchSpanProcessor` exports spans asynchronously in the background. On a long-running runner, spans are batched and exported on a schedule. On shutdown, spans still in the buffer are flushed in `teardown()`. See [Production Configuration](/documentation/serverless/observability/opentelemetry-production) for how to configure this flush.
</Note>

## What's Next

<CardGroup cols={2}>
  <Card title="Custom Metrics" icon="chart-bar" href="/documentation/serverless/observability/custom-metrics">
    Add counters, histograms, and gauges to your app
  </Card>

  <Card title="Cross-Service Tracing" icon="diagram-project" href="/documentation/serverless/observability/opentelemetry-cross-service">
    Connect traces across two fal apps into a single parent trace
  </Card>

  <Card title="Production Configuration" icon="sliders" href="/documentation/serverless/observability/opentelemetry-production">
    Sampling, batch export tuning, and graceful flush on shutdown
  </Card>

  <Card title="App Lifecycle" icon="rotate" href="/documentation/development/app-lifecycle">
    How setup() and teardown() fit into the runner lifecycle
  </Card>
</CardGroup>
