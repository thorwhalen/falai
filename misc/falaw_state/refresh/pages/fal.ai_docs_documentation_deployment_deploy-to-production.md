> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy to Production

> Deploy your fal App to production with persistent URLs, authentication, and automatic scaling.

Deploying to production is the step that turns your local app into a permanent, scalable API endpoint. While [`fal run`](/reference/cli/run) gives you a temporary URL for testing, `fal deploy` creates a persistent deployment that stays available until you explicitly remove it. Your app gets a stable endpoint ID (e.g., `your-username/my-model`) that callers use with the [fal client SDKs](/documentation/model-apis/inference) or REST API, automatic [runner scaling](/documentation/deployment/scale-your-application), and built-in [reliability](/documentation/serverless/reliability/retries) through the queue system.

Before deploying, make sure you have [installed the CLI](/documentation/development/getting-started/installation), written your [fal.App](/documentation/development/app-lifecycle), and tested it locally with `fal run`. This page walks through the deployment process from the initial command through build, configuration, and what happens behind the scenes. For managing deployments after they are live, see [Manage Deployments](/documentation/deployment/manage-deployments).

## Development vs Production

During development, use `fal run` to get a temporary endpoint for testing. It creates an ephemeral deployment that is destroyed when you stop the process. By default, `fal run` uses `public` auth mode so you can test without an API key.

```bash theme={null}
fal run path/to/myapp.py::MyApp
```

When you are ready for production, switch to `fal deploy`. This creates a persistent deployment with a permanent URL. By default, `fal deploy` uses `private` auth mode, requiring an API key to call your app.

```bash theme={null}
fal deploy path/to/myapp.py::MyApp
```

## Deploying Your App

The simplest deployment requires just the path to your app file and class:

```bash theme={null}
fal deploy path/to/myapp.py::MyApp
```

fal builds your app into a container image remotely, pushes it to the registry, and makes it available at the endpoint ID `your-username/app-name`. Callers use this ID with `fal_client.subscribe("your-username/app-name", ...)` or via the REST API at `https://queue.fal.run/your-username/app-name`. You do not need Docker installed locally. The build happens entirely in the cloud.

### App Name

By default, your app name is derived from the class name (e.g., `TextToImage` becomes `text-to-image`). You can override it in your code or via the CLI. The app name is the second part of your endpoint ID (`your-username/app-name`).

```python theme={null}
class MyApp(fal.App):
    app_name = "my-custom-name"
```

```bash theme={null}
fal deploy my_app.py::MyApp --app-name my-custom-name
```

### Machine Type

Set the hardware your app runs on using the `machine_type` class attribute. For GPU workloads, you can also specify `num_gpus` for multi-GPU configurations. See [Machine Types](/documentation/deployment/machine-types) for the full list of available hardware and guidance on choosing the right option.

```python theme={null}
class MyApp(fal.App):
    machine_type = "GPU-A100"
    num_gpus = 1
```

You can also specify multiple machine types to expand your available hardware pool, which reduces queue wait times:

```python theme={null}
class MyApp(fal.App):
    machine_type = ["GPU-A100", "GPU-H100"]
```

### Regions

By default, your app can run in any available region. If you need data residency compliance or want to minimize latency for a specific geography, restrict it:

```python theme={null}
class MyApp(fal.App):
    machine_type = "GPU-A100"
    regions = ["us-east"]
```

### Environments

You can deploy to different [environments](/documentation/deployment/manage-environments) (e.g., staging, production) to isolate configurations and [secrets](/documentation/development/manage-secrets-securely):

```bash theme={null}
fal deploy my_app.py::MyApp --env staging
```

## Previewing a Deployment

Use the `--check` command line option or set `FAL_DEPLOY_CHECK` to `true` to review what will change before your app is actually deployed:

```bash theme={null}
fal deploy path/to/myapp.py::MyApp --check
FAL_DEPLOY_CHECK=true fal deploy path/to/myapp.py::MyApp
```

The deployment check shows the target app and environment, current revision, source object, authentication mode, deployment strategy, build-cache behavior, and effective production configuration changes. If the app has not been deployed before, it shows the effective deployment values that will be used for the first revision.

When using the deployment check feature, you will by default be prompted for confirmation before deploying. In non-interactive environments, pass `--yes` to skip the prompt while still printing the summary:

```bash theme={null}
fal deploy path/to/myapp.py::MyApp --check --yes
FAL_DEPLOY_CHECK=true fal deploy path/to/myapp.py::MyApp --yes
```

<Note>
  Scaling parameters such as `keep_alive`, `min_concurrency`, and `max_concurrency` are inherited from the previous deployment unless you pass `--reset-scale`. The deployment check calls out code values that will not apply without `--reset-scale`.
</Note>

## Authentication Modes

Authentication controls who can call your app and who pays for compute. You set it with the `--auth` flag or the `app_auth` class attribute.

**Private** is the default for `fal deploy`. Only the account owner and their [team members](/documentation/organizations/managing-teams) can call the app, and they must include an API key. All compute is billed to the owner.

**Public** is the default for `fal run`. Anyone with the URL can call the app without authentication. All compute is billed to the owner. Use this for open demos or internal tools where you control access at another layer.

**Shared** allows anyone with the URL to call the app, but callers must authenticate with their own API key. Each caller pays for their own usage. This is how all apps in the [Model Gallery](https://fal.ai/models) work. Shared mode requires admin enablement on your account. See [Publishing to the Marketplace](/documentation/serverless/publishing-to-marketplace) for the full process of making your app available as a marketplace model.

```python theme={null}
class MyApp(fal.App):
    app_auth = "private"
```

## Rollout Strategies

When you redeploy an app that is already running, fal needs to transition from the old revision to the new one. You can choose between two strategies:

**Rolling** (default) spins up a runner on the new revision *before* switching traffic. fal waits for this runner to complete `setup()` and become healthy. Only after the new runner is confirmed ready does fal switch the alias. This ensures zero downtime but takes longer to complete. If the new runner fails to start (e.g., `setup()` crashes), the deployment is aborted and traffic stays on the old revision.

**Recreate** instantly switches the app alias to the new revision. No runners are started proactively. The first request after redeployment triggers a cold start on the new revision. If your app has `min_concurrency > 0`, the scaling system will eventually bring runners up to meet that minimum, but this happens through normal scaling, not as part of the deploy itself.

```bash theme={null}
fal deploy path/to/myapp.py::MyApp --strategy recreate
```

<Note>
  With rolling deployments, you will see a runner spin up during `fal deploy` even if there is no traffic. This is the health verification step. The deploy command stays open until the runner is confirmed healthy or fails.
</Note>

For more on managing revisions and rolling back to previous versions, see [Rollbacks](/documentation/deployment/rollbacks).

## How Builds Work

When you run `fal deploy`, your code is built into a container image remotely. You do not need Docker installed locally.

<Steps>
  <Step title="Upload">
    Your app code is sent to fal's build service. For non-container apps, files listed in `app_files` are included. For [container apps](/documentation/development/use-custom-container-image), files referenced by `COPY`/`ADD` in your Dockerfile are included automatically.
  </Step>

  <Step title="Build">
    fal builds your container image in the cloud using [Depot](https://depot.dev), a remote Docker build service.
  </Step>

  <Step title="Cache check">
    A hash is computed from your Dockerfile, dependencies, build args, and container files. If an identical image already exists, the build is skipped entirely.
  </Step>

  <Step title="Push">
    The built image is stored in fal's container registry.
  </Step>

  <Step title="Ready">
    [Runners](/documentation/deployment/runners) pull the image when they start up. Image size directly affects pull time and cold start duration.
  </Step>
</Steps>

<Note>
  Since builds happen remotely, your local machine does not need Docker, GPU drivers, or large amounts of disk space. You only need the `fal` CLI and your code.
</Note>

### Build Caching

fal uses multiple levels of caching to speed up builds. Build hash deduplication checks whether anything changed since the last build -- if not, the previous image is reused with no build at all. Docker layer caching stores layers per-user in the registry, so unchanged layers from previous builds are reused and only modified layers are rebuilt.

To force a full rebuild bypassing all caching:

```bash theme={null}
fal deploy my_app.py --no-cache
```

For tips on structuring your Dockerfile for faster builds, see [Optimize Container Images](/documentation/serverless/optimizations/optimize-container-images).

## What's Next

<CardGroup cols={2}>
  <Card title="Manage Deployments" icon="list" href="/documentation/deployment/manage-deployments">
    List, update, and delete your deployed apps
  </Card>

  <Card title="Rollbacks" icon="rotate-left" href="/documentation/deployment/rollbacks">
    Roll back to previous revisions or roll out new ones gracefully
  </Card>

  <Card title="Scale Your Application" icon="arrows-up-down" href="/documentation/deployment/scale-your-application">
    Configure scaling parameters for production traffic
  </Card>

  <Card title="Optimizing Cold Starts" icon="bolt" href="/documentation/serverless/optimizations/optimize-cold-starts">
    Reduce image size and startup time
  </Card>
</CardGroup>
