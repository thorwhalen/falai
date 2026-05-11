> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Documentation

> Learn how to build and deploy AI applications with fal

<div id="docs-hero-page">
  <div className="fal-hero-section">
    <div className="fal-hero-text">
      <h1 className="fal-hero-title">
        Build with fal
      </h1>

      <p className="fal-hero-subtitle">The generative media platform powering the world's top AI apps.</p>

      <p className="fal-hero-body">
        Call <strong>1,000+ optimized models</strong> through a unified API, or deploy your own on the same infrastructure. Image, video, audio, music, speech, 3D, and real-time streaming. Built to scale to billions of requests.
      </p>

      <button type="button" className="fal-hero-search" onClick={() => document.getElementById('search-bar-entry')?.click()}>
        <svg className="fal-hero-search-icon" viewBox="0 0 20 20" fill="currentColor">
          <path fillRule="evenodd" d="M9 3.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9z" clipRule="evenodd" />
        </svg>

        <span className="fal-hero-search-text">Search or ask...</span>
      </button>

      <div className="fal-stats-row">
        <div className="fal-stat-item">
          <div className="fal-stat-value">99.99%+</div>
          <div className="fal-stat-label">Uptime</div>
        </div>

        <div className="fal-stat-item">
          <div className="fal-stat-value">Billions+</div>
          <div className="fal-stat-label">Requests/day</div>
        </div>

        <div className="fal-stat-item">
          <div className="fal-stat-value">1,000+</div>
          <div className="fal-stat-label">Endpoints</div>
        </div>
      </div>
    </div>

    <div className="fal-hero-image">
      <img src="https://mintcdn.com/fal-d8505a2e/QFO2a4qD7yLWEJFa/images/Hero_image_light.png?fit=max&auto=format&n=QFO2a4qD7yLWEJFa&q=85&s=be84ce69a57abe69927c7453e497768f" alt="Build with fal" className="fal-hero-img-light" width="2140" height="1552" data-path="images/Hero_image_light.png" />

      <img src="https://mintcdn.com/fal-d8505a2e/QFO2a4qD7yLWEJFa/images/Hero_image_dark.png?fit=max&auto=format&n=QFO2a4qD7yLWEJFa&q=85&s=c818dcf171b90cd6b31c46254c72e333" alt="Build with fal" className="fal-hero-img-dark" width="2140" height="1552" data-path="images/Hero_image_dark.png" />
    </div>
  </div>

  <CardGroup cols={3}>
    <Card title="Model APIs" icon="cube" href="/documentation/model-apis/overview" className="fal-feature-card">
      **Call 1,000+ models with one API.** Image, video, audio, and multimodal generation. Optimized and production-ready.
    </Card>

    <Card title="Serverless" icon="rocket" href="/documentation/serverless" className="fal-feature-card">
      **Deploy your own models.** Same infrastructure, same autoscaling, same reliability. From zero to thousands of GPUs.
    </Card>

    <Card title="Compute" icon="microchip" href="/documentation/compute" className="fal-feature-card">
      **Dedicated GPU instances.** Full SSH access for training, fine-tuning, and persistent workloads.
    </Card>
  </CardGroup>

  <Card title="Platform APIs" icon="layer-group" href="/api-reference/platform-apis">
    REST APIs for model metadata, pricing, usage tracking, logs, files, and metrics
  </Card>

  ## Start with a Model API Call

  Most users start here. Pick a model from the [Marketplace](https://fal.ai/models), get an [API key](https://fal.ai/dashboard/keys), and make a request. Three lines of code, no infrastructure to manage.

  <CodeGroup>
    ```python Python theme={null}
    import fal_client

    result = fal_client.subscribe("fal-ai/nano-banana-2", 
        arguments={"prompt": "a sunset over mountains"}
    )
    print(result["images"][0]["url"])
    ```

    ```javascript JavaScript theme={null}
    import { fal } from "@fal-ai/client";

    const result = await fal.subscribe("fal-ai/nano-banana-2", {
      input: { prompt: "a sunset over mountains" }
    });
    console.log(result.data.images[0].url);
    ```

    ```bash cURL theme={null}
    curl -X POST https://queue.fal.run/fal-ai/nano-banana-2 \
      -H "Authorization: Key $FAL_KEY" \
      -H "Content-Type: application/json" \
      -d '{"prompt": "a sunset over mountains"}'
    ```
  </CodeGroup>

  Every model supports [synchronous and async queue](/documentation/model-apis/inference) calls out of the box. Many also support [streaming](/documentation/model-apis/inference/streaming) and [real-time WebSocket](/documentation/model-apis/inference/real-time) connections. You can compare models side-by-side in the [Sandbox](https://fal.ai/sandbox) before committing to one.

  <Card title="Model APIs Quickstart" icon="arrow-right" href="/documentation/model-apis/overview">
    Browse models, see pricing, and start generating
  </Card>

  ***

  ## Deploy Your Own Models

  For teams that need to run custom models, proprietary pipelines, or fine-tuned variants, [fal Serverless](/documentation/serverless) lets you deploy on the same engine that powers the Marketplace. fal has been running this infrastructure for over 3 years, and every model on the platform goes through the same lifecycle below.

  <Steps>
    <Step title="Develop">
      A [fal.App](/documentation/development/app-setup) is a Python class where your `setup()` method runs once per [runner](/documentation/deployment/runners) to load model weights and initialize resources. Your [`@fal.endpoint`](/documentation/development/handle-inputs-and-outputs) methods then serve incoming [requests](/documentation/deployment/requests) using the initialized state. You declare hardware needs and [environment](/documentation/development/container-setup) alongside your code, so infrastructure is versioned with your app.

      ```python theme={null}
      import fal

      class MyModel(fal.App):
          machine_type = "GPU-H100"
          
          def setup(self):
              self.model = load_my_model()
          
          @fal.endpoint("/")
          def generate(self, prompt: str):
              return self.model(prompt)
      ```
    </Step>

    <Step title="Test">
      [`fal run`](/documentation/development/getting-started/quick-start) spins up a cloud GPU [runner](/documentation/deployment/runners) and gives you a temporary URL so you can test on the same hardware you'll use in production. It also generates a [playground UI](/documentation/model-apis/playground) automatically. For CI, [`AppClient`](/documentation/development/test-models-and-endpoints) lets you run tests against ephemeral deployments.

      ```bash theme={null}
      fal run my_app.py
      ```
    </Step>

    <Step title="Deploy">
      [`fal deploy`](/documentation/deployment/deploy-to-production) creates a persistent, authenticated endpoint with autoscaling and built-in [retries](/documentation/serverless/reliability/retries). Every deploy creates a new revision for instant [rollbacks](/documentation/deployment/rollbacks). For staging and production separation, fal supports [multiple environments](/documentation/deployment/manage-environments) per app.

      ```bash theme={null}
      fal deploy my_app.py
      ```
    </Step>

    <Step title="Observe">
      The [dashboard](https://fal.ai/dashboard) gives you real-time logs, request-level [analytics](/documentation/serverless/observability/app-analytics), and [error tracking](/documentation/serverless/observability/error-analytics) out of the box. Trace individual requests, spot latency regressions, and monitor runner utilization. For external stacks, fal supports [Prometheus metrics](/documentation/serverless/observability/exporting-metrics) and [log drains](/documentation/serverless/observability/log-drains) to Datadog, Splunk, and Elasticsearch.
    </Step>

    <Step title="Scale">
      fal scales [runners](/documentation/deployment/runners) from zero to thousands of GPUs based on demand, with a multi-layer [caching](/documentation/deployment/caching) system that reduces cold starts over time. [Scaling parameters](/documentation/deployment/scale-your-application) let you control the tradeoff: `min_concurrency` keeps runners warm, `max_concurrency` caps spend, and `concurrency_buffer` pre-warms ahead of spikes. See [optimizing cold starts](/documentation/serverless/optimizations/optimize-cold-starts) and [machine types](/documentation/deployment/machine-types) for latency-sensitive workloads.

      ```python theme={null}
      class MyModel(fal.App):
          min_concurrency = 2
          max_concurrency = 100
          concurrency_buffer = 3
      ```
    </Step>

    <Step title="Distribute">
      Endpoints start as private. You can deploy in `public` mode for open access, or [`shared` mode](/documentation/deployment/deploy-to-production) where callers pay for their own usage. To list on the [Marketplace](https://fal.ai/models) for broader distribution and revenue, see [publishing to the marketplace](/documentation/serverless/publishing-to-marketplace).

      ```python theme={null}
      class MyModel(fal.App):
          app_auth = "shared"
      ```
    </Step>
  </Steps>

  <Card title="Serverless Quickstart" icon="arrow-right" href="/documentation/development/getting-started/quick-start">
    Deploy your first model in minutes
  </Card>

  ***

  ## Train Your Own Models

  For training runs, fine-tuning, and workloads that need sustained GPU access, [fal Compute](/documentation/compute) gives you dedicated instances with full SSH control. No cold starts, no autoscaling, just raw GPU power billed at a fixed hourly rate.

  <CardGroup cols={2}>
    <Card title="H100 SXM" icon="microchip">
      Single-GPU instances for development, fine-tuning, and single-GPU training
    </Card>

    <Card title="8x H100 SXM" icon="server">
      Multi-GPU instances connected over InfiniBand for distributed training
    </Card>
  </CardGroup>

  |              | Compute                           | Serverless                         |
  | :----------- | :-------------------------------- | :--------------------------------- |
  | **Best for** | Training, fine-tuning, batch jobs | API endpoints, on-demand inference |
  | **Billing**  | Per-hour, fixed rate              | Per-second of execution            |
  | **Scaling**  | Manual                            | Automatic                          |
  | **Access**   | Full SSH                          | Managed runners                    |

  <Card title="Compute Quickstart" icon="arrow-right" href="/documentation/compute/quickstart">
    Provision your first GPU instance in minutes
  </Card>
</div>
