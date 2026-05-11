> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cross-Service Tracing

> Propagate trace context between two fal apps so that preprocessing and inference appear as children of a single parent trace

When a request passes through more than one fal app, each app creates its own spans by default and those spans appear as separate, unrelated traces in your backend. Passing W3C trace context between apps connects them under a single trace ID, so preprocessing and inference show up as children of one root span. For single-app tracing, see [Custom Traces](/documentation/serverless/observability/opentelemetry-traces).

## How Context Propagation Works

The W3C Trace Context standard defines a `traceparent` header that carries a trace ID and parent span ID between services. The sending app injects the current span context into a carrier (a plain dict), passes it to the receiving app, and the receiving app extracts the context before creating its span. Both apps end up contributing spans to the same trace ID.

fal apps communicate over HTTP, and the carrier is passed as a field in the JSON request body. Both apps must export to the same OTLP backend for the spans to be correlated.

## Setup

Deploy `TextToImageWorker` first to get its app id, then deploy `ImagePipeline` and pass the app id when calling it.

```bash theme={null}
fal deploy pipeline.py::TextToImageWorker
# Note the app id, e.g. your-username/text-to-image-worker

fal deploy pipeline.py::ImagePipeline
```

Both apps must have `OTEL_EXPORTER_OTLP_ENDPOINT` and `OTEL_EXPORTER_OTLP_HEADERS` set as fal secrets. See [Custom Traces](/documentation/serverless/observability/opentelemetry-traces#prerequisites) for backend options and how to store credentials.

## Implementation

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


# App 1: ImagePipeline - validates and preprocesses the prompt, then calls TextToImageWorker

class PipelineInput(BaseModel):
    prompt: str = Field(description="The prompt to generate an image from")
    worker_app: str = Field(description="Deployed app id of TextToImageWorker")


class PipelineOutput(BaseModel):
    image: Image
    trace_id: str


class ImagePipeline(fal.App):
    machine_type = "S"
    requirements = [
        "opentelemetry-sdk==1.41.0",
        "opentelemetry-exporter-otlp-proto-http==1.41.0",
        "fal-client",
    ]

    def setup(self):
        from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

        self.tracer, self.tracer_provider = setup_tracer("image-pipeline")
        self._propagator = TraceContextTextMapPropagator()

    @fal.endpoint("/")
    def run(self, input: PipelineInput) -> PipelineOutput:
        import fal_client

        with self.tracer.start_as_current_span("image-pipeline") as root:
            with self.tracer.start_as_current_span("preprocess-prompt") as span:
                span.set_attribute("prompt.length", len(input.prompt))
                # Sanitize and enrich the prompt before passing to inference
                enriched_prompt = input.prompt.strip()

            # Inject the current span context into a carrier dict.
            # The carrier will contain {"traceparent": "00-<trace-id>-<span-id>-01"}.
            carrier: dict[str, str] = {}
            self._propagator.inject(carrier)

            with self.tracer.start_as_current_span("call-inference-worker"):
                result = fal_client.subscribe(
                    input.worker_app,
                    {"prompt": enriched_prompt, "trace_context": carrier},
                )

            trace_id = format(root.get_span_context().trace_id, "032x")

        return PipelineOutput(image=Image(**result["image"]), trace_id=trace_id)

    def teardown(self):
        if self.tracer_provider:
            self.tracer_provider.force_flush(timeout_millis=4000)


# App 2: TextToImageWorker - receives context and runs SDXL inference

class WorkerInput(BaseModel):
    prompt: str
    trace_context: dict  # W3C traceparent injected by ImagePipeline


class WorkerOutput(BaseModel):
    image: Image


class TextToImageWorker(fal.App):
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
        from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

        self.tracer, self.tracer_provider = setup_tracer("text-to-image-worker")
        self._propagator = TraceContextTextMapPropagator()
        self.pipe = StableDiffusionXLPipeline.from_pretrained(
            "stabilityai/stable-diffusion-xl-base-1.0",
            torch_dtype=torch.float16,
            variant="fp16",
            use_safetensors=True,
        ).to("cuda")
        self.pipe("warmup")

    @fal.endpoint("/")
    def run(self, input: WorkerInput) -> WorkerOutput:
        # Extract the parent context from the carrier.
        # The new span becomes a child of ImagePipeline's active span.
        ctx = self._propagator.extract(input.trace_context)

        with self.tracer.start_as_current_span("inference", context=ctx) as span:
            span.set_attribute("model.name", "stable-diffusion-xl-base-1.0")
            span.set_attribute("prompt.length", len(input.prompt))

            with self.tracer.start_as_current_span("diffusion"):
                result = self.pipe(input.prompt)

            with self.tracer.start_as_current_span("upload"):
                image = Image.from_pil(result.images[0])

        return WorkerOutput(image=image)

    def teardown(self):
        if self.tracer_provider:
            self.tracer_provider.force_flush(timeout_millis=4000)
```

## Resulting Trace

Both apps export to the same backend using the same trace ID. The trace appears as:

```
image-pipeline                         (ImagePipeline app)
├── preprocess-prompt
├── call-inference-worker
└── inference                          (TextToImageWorker app)
    ├── diffusion
    └── upload
```

The `inference` span in `TextToImageWorker` is a child of `image-pipeline` in `ImagePipeline` because `_propagator.extract(input.trace_context)` reconstructed the parent context before the span was created.

The entity map shows both apps connected, and the span tree shows spans from both services under the same trace ID:

<Frame>
  <img src="https://mintcdn.com/fal-d8505a2e/zo-kE_ST4HOR1zo1/images/observability/opentelemetry-cross-service-traces.png?fit=max&auto=format&n=zo-kE_ST4HOR1zo1&q=85&s=f20142220cd0c39c75d2adac5d1c9763" alt="Cross-service trace showing image-pipeline root span with preprocess-prompt, call-inference-worker, and inference children spanning two fal apps" width="2426" height="1578" data-path="images/observability/opentelemetry-cross-service-traces.png" />
</Frame>

<Note>
  Both apps must export to the same OTLP backend for the trace to appear connected. If each app sends spans to a different backend, they will not be correlated even though they share a trace ID.
</Note>

## What's Next

<CardGroup cols={2}>
  <Card title="Custom Traces" icon="code-branch" href="/documentation/serverless/observability/opentelemetry-traces">
    Instrument a single app with spans for each inference stage
  </Card>

  <Card title="Production Configuration" icon="sliders" href="/documentation/serverless/observability/opentelemetry-production">
    Sampling, batch export tuning, and graceful flush on shutdown
  </Card>
</CardGroup>
