> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Publishing to the Marketplace

> Make your serverless app available on the fal Marketplace so anyone can call it with their own API key.

Every model on the [fal Marketplace](https://fal.ai/models) is a `fal.App` running on Serverless. You can publish your own app to the marketplace, making it callable by any fal user who authenticates with their own API key and pays for their own usage.

Publishing involves deploying your app in `shared` auth mode, defining billable units so callers are charged correctly, and working with the fal team to get listed. Before publishing, your app should be [deployed](/documentation/deployment/deploy-to-production) and stable, [scaled](/documentation/deployment/scaling-configuration) for your expected traffic, and have [health checks](/documentation/development/add-health-check-endpoint) and [analytics](/documentation/serverless/observability/app-analytics) enabled.

## Set your app to shared mode

Shared mode means callers must authenticate with their own fal API key. Each caller is billed for their own usage — the app owner is not charged for caller compute.

```python theme={null}
class MyModel(fal.App):
    app_auth = "shared"
```

Or via the CLI:

```bash theme={null}
fal deploy my_app.py::MyModel --auth shared
```

<Note>
  Shared mode requires admin enablement on your account. Contact the fal team to get it enabled before deploying with `app_auth = "shared"`.
</Note>

## Define billable units

When your app runs in shared mode, you control how callers are charged by setting the `x-fal-billable-units` response header. This tells the platform how many billing units to charge for each request.

```python theme={null}
response.headers["x-fal-billable-units"] = str(units)
```

The cost per unit is configured separately by the fal team in the billing system — your code only reports **how many units** each request consumed. If you don't set the header, the platform falls back to per-second billing based on the GPU machine type used.

### Common patterns

**Per image (flat rate)**

Charge one unit per generated image, regardless of resolution:

```python theme={null}
response.headers["x-fal-billable-units"] = str(input.num_images)
```

**Per megapixel**

Scale the charge with output resolution. Higher resolutions cost proportionally more:

```python theme={null}
resolution_factor = math.ceil(
    (image_size.width * image_size.height) / (1024 * 1024)
)
response.headers["x-fal-billable-units"] = str(
    resolution_factor * input.num_images
)
```

**Per video second**

Charge based on the duration of generated video:

```python theme={null}
response.headers["x-fal-billable-units"] = str(video_duration_seconds)
```

**Per text chunk**

For text-based models (TTS, LLMs), scale with input length:

```python theme={null}
response.headers["x-fal-billable-units"] = str(max(1, len(prompt) // 1000))
```

**Flat per request**

Charge a fixed amount regardless of input or output:

```python theme={null}
response.headers["x-fal-billable-units"] = "1"
```

## Get listed on the Marketplace

Once your app is deployed in shared mode with billable units configured, contact the fal team to get listed on [fal.ai/models](https://fal.ai/models). The team will configure:

* **Model card** — name, description, category, and example inputs/outputs
* **Pricing** — the cost per billable unit, visible on your model's page and at [fal.ai/pricing](https://fal.ai/pricing)
* **Visibility** — when and how your model appears in the marketplace

After listing, callers see your model's pricing on its page and the `X-Fal-Billable-Units` header in every response, so they can track their usage programmatically.

<CardGroup cols={2}>
  <Card title="Deploy to Production" href="/documentation/deployment/deploy-to-production">
    Deployment strategies and authentication modes.
  </Card>

  <Card title="Model APIs Pricing" href="/documentation/model-apis/pricing">
    How marketplace model pricing works from the caller's perspective.
  </Card>
</CardGroup>
