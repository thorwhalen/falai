> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deployment Overview

> Ship your fal applications to production, manage revisions and environments, configure scaling, and choose the right machine type.

Deployment is where your [fal App](/documentation/development/app-lifecycle) goes from local development to a production API that serves real traffic. When you run `fal deploy`, fal builds your code into a container image, pushes it to a registry, and makes it available at a permanent endpoint ID. From that point, [runners](/documentation/deployment/runners) spin up on demand to handle requests, scale automatically based on traffic, and shut down when idle. You can roll back to any previous version instantly, deploy to separate [environments](/documentation/deployment/manage-environments) for staging and production, and tune [scaling parameters](/documentation/deployment/scale-your-application) without redeploying.

Before diving into this section, make sure you have [installed the CLI](/documentation/development/getting-started/installation) and built your app following the [Development](/documentation/serverless/index) guides. The pages here cover everything after your code is written: understanding what runners are, deploying to production, managing versions and environments, choosing hardware, and configuring scaling. If you are migrating from another platform, the [migration guides](/documentation/development/migrate-external-docker-server) can help you get started faster.

## Quick Start

The simplest deployment is a single command:

```bash theme={null}
fal deploy path/to/myapp.py::MyApp
```

This builds your app remotely, creates a persistent deployment, and gives you an endpoint ID like `your-username/my-model` that callers use with the [fal client SDKs](/documentation/model-apis/inference).

## Runners and Requests

Before deploying, it helps to understand the execution model. When a caller submits a request, it enters a persistent queue and is dispatched to a runner. Runners are compute instances that pull your container image, run `setup()`, and serve requests until they scale down. Understanding how requests flow through the queue and how runners start, process, and shut down is essential for debugging latency, configuring scaling, and managing costs.

<CardGroup cols={2}>
  <Card title="Understanding Requests" icon="arrow-right-arrow-left" href="/documentation/deployment/requests">
    Request lifecycle, retry interaction, and platform architecture diagram
  </Card>

  <Card title="Understanding Runners" icon="server" href="/documentation/deployment/runners">
    Runner lifecycle states, startup, shutdown, and scaling behavior
  </Card>

  <Card title="Caching" icon="layer-group" href="/documentation/deployment/caching">
    How Docker layers, model weights, and compiled artifacts are cached across runners
  </Card>
</CardGroup>

## Deploying and Managing

Deployment creates a versioned revision of your app. Each deploy creates a new revision, so you can roll back to any previous version instantly if something goes wrong. You choose a rollout strategy (recreate for speed, rolling for zero downtime), configure authentication (private, public, or shared billing), and optionally deploy to separate environments for staging and production.

<CardGroup cols={2}>
  <Card title="Deploy to Production" icon="rocket" href="/documentation/deployment/deploy-to-production">
    Build, configure, and ship your app with rollout strategies and auth modes
  </Card>

  <Card title="Manage Deployments" icon="list-check" href="/documentation/deployment/manage-deployments">
    List, update, and delete deployed apps
  </Card>

  <Card title="Rollbacks" icon="rotate-left" href="/documentation/deployment/rollbacks">
    Switch between revisions or restart runners with rollouts
  </Card>

  <Card title="Environments" icon="sliders" href="/documentation/deployment/manage-environments">
    Isolate staging and production with separate secrets and config
  </Card>
</CardGroup>

## Scaling and Hardware

Once deployed, you control how your app scales. Scaling parameters determine how many runners stay warm, how quickly new ones spin up, and how many requests each runner handles concurrently. Machine types determine the hardware backing each runner, from lightweight CPU instances to H200 and B200 GPUs.

<CardGroup cols={2}>
  <Card title="Scaling Parameters" icon="arrows-up-down" href="/documentation/deployment/scale-your-application">
    Configure concurrency, keep-alive, multiplexing, and scaling delays
  </Card>

  <Card title="Scaling Configuration" icon="gear" href="/documentation/deployment/scaling-configuration">
    Set parameters via code, CLI, or dashboard, and understand --reset-scale
  </Card>

  <Card title="Machine Types" icon="microchip" href="/documentation/deployment/machine-types">
    Choose from CPU and GPU hardware based on memory, compute, and VRAM needs
  </Card>
</CardGroup>
