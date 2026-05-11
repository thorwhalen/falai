> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pricing

> How billing works for fal Serverless.

When you deploy your own applications on fal Serverless, you are billed for the **total time your runners are alive**, measured per-second by machine type.

## Billing by runner state

Every runner transitions through the states below during its lifecycle. You are billed for the states marked **Yes** at the per-second rate for your machine type.

| State            | Billed | Description                                                            |
| ---------------- | ------ | ---------------------------------------------------------------------- |
| **PENDING**      | No     | Waiting to be scheduled on available hardware                          |
| **DOCKER\_PULL** | No     | Pulling your container image from the registry                         |
| **SETUP**        | Yes    | Running your `setup()` method — loading models, initializing resources |
| **IDLE**         | Yes    | Runner is ready but waiting for requests (includes `keep_alive` time)  |
| **RUNNING**      | Yes    | Actively processing one or more requests                               |
| **DRAINING**     | Yes    | Finishing in-flight requests before shutdown                           |
| **TERMINATING**  | Yes    | Running your `teardown()` method                                       |
| **TERMINATED**   | No     | Runner has stopped and resources are released                          |

5xx errors (HTTP 500+) are also not charged.

See [Runners](/documentation/deployment/runners) for full details on each state and transitions.

## GPU count multiplier

Multi-GPU instances are billed as `gpu_count x duration`. For example, a runner using 2x A100 GPUs for 60 seconds is billed as 120 GPU-seconds.

## Monitoring your usage

<CardGroup cols={2}>
  <Card title="Dashboard Billing" icon="chart-line" href="https://fal.ai/dashboard/billing">
    View your overall spend, invoices, and payment methods.
  </Card>

  <Card title="App Analytics" icon="chart-bar" href="/documentation/serverless/observability/app-analytics">
    See per-app cost breakdown, request counts, and runner utilization.
  </Card>
</CardGroup>
