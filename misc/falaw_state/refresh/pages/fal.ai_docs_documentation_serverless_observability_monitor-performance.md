> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Observability Overview

> Monitor your fal applications using the dashboard, CLI, and programmatic integrations.

Once your app is deployed and serving traffic, you need visibility into how it is performing. fal provides three interfaces for observability, each suited to different workflows. The [dashboard](https://fal.ai/dashboard) gives you visual, real-time insight into requests, runners, and errors. The [CLI](/api-reference/cli/runners) lets you check runner states and stream logs from your terminal. And the programmatic integrations (Prometheus metrics, log drains, Slack notifications) let you pipe fal's data into your existing monitoring stack.

Understanding which interface to use for which task saves you from digging through the wrong tool. The dashboard is best for investigating specific issues and getting a quick overview. The CLI is best for quick operational checks and scripting. The integrations are best for production alerting, long-term metrics storage, and centralized logging.

## Dashboard

The [fal dashboard](https://fal.ai/dashboard) is the primary interface for visual monitoring. It provides several views depending on what you need to understand.

**App Analytics** shows request volume, latency, runner counts, and queue depth for each deployed app. Use it to understand traffic patterns, identify slow endpoints, and verify that scaling is working correctly. The Requests tab shows individual request history with status, duration, and logs. The Runners tab shows runner lifecycle events and state transitions.

**Error Analytics** breaks down failures by error type, status code, and time. Use it to spot error spikes, identify recurring failure patterns, and understand which errors are transient vs systemic.

**App Events** tracks deployment events, configuration changes, and runner lifecycle events. Use it to correlate performance changes with deployments (e.g., "latency increased right after this deploy").

**Logs** streams runner logs in real-time and lets you filter by runner ID, request ID, version, and source. For understanding how request-level logs work, see [Logging](/documentation/development/logging).

<CardGroup cols={2}>
  <Card title="App Analytics" icon="chart-mixed" href="/documentation/serverless/observability/app-analytics">
    Request metrics, runner states, and per-app performance
  </Card>

  <Card title="Error Analytics" icon="triangle-exclamation" href="/documentation/serverless/observability/error-analytics">
    Error rates, patterns, and failure breakdown
  </Card>

  <Card title="App Events" icon="timeline" href="/documentation/serverless/observability/app-events">
    Deployment, config, and runner lifecycle events
  </Card>
</CardGroup>

## CLI

The fal CLI provides quick access to runner states, logs, and queue status from your terminal. This is useful for operational checks, scripting, and CI pipelines.

<Frame>
  <iframe className="w-full aspect-video rounded-lg" srcdoc="<style>*{padding:0;margin:0;overflow:hidden}html,body{height:100%}img,span{position:absolute;width:100%;top:0;bottom:0;margin:auto}span{height:1.5em;text-align:center;font:48px/1.5 sans-serif;color:white;text-shadow:0 0 0.5em black}</style><a href='https://www.youtube.com/embed/gDJJ9bppyV8?start=1195&end=1296&autoplay=1'><img src='/docs/images/video-thumbs/monitor-performance.jpg' alt='CLI Updates - fal Serverless'><span>▶</span></a>" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />
</Frame>

```bash theme={null}
# Runner monitoring
fal runners list                        # all runners with current states
fal runners list --state idle           # filter by state
fal runners list --since "1h"           # view history
fal runners logs <runner-id>            # stream logs from a runner

# Queue monitoring
fal queue size my-app                   # current queue depth
fal queue flush my-app                  # clear stuck requests

# App management
fal apps list                           # all deployed apps
fal apps runners my-app                 # runners for a specific app
fal apps scale my-app                   # view/update scaling config
```

See the CLI reference for [`fal runners`](/api-reference/cli/runners), [`fal queue`](/api-reference/cli/queue), and [`fal apps`](/api-reference/cli/apps/list).

## Programmatic Integrations

For production monitoring, you can pipe fal's data into your existing observability stack. This gives you long-term retention, custom dashboards, and alerting that the built-in dashboard does not provide.

**Prometheus Metrics** -- fal exposes a Prometheus-compatible metrics endpoint that you can scrape with Grafana, Datadog, or any Prometheus-compatible tool. Available metrics include runner counts, queue depth, concurrent requests, request throughput, and latency buckets.

**Log Drains** -- forward all runner logs to an external service (Datadog, Splunk, or any HTTP endpoint) in real-time via NDJSON over HTTPS. Logs include request IDs, timestamps, and structured metadata for correlation.

**Slack Notifications** -- receive alerts in Slack when runners fail to start, deployments complete, or configuration changes occur.

<CardGroup cols={2}>
  <Card title="Exporting Metrics" icon="chart-line" href="/documentation/serverless/observability/exporting-metrics">
    Prometheus endpoint, Grafana setup, and Datadog integration
  </Card>

  <Card title="Log Drains" icon="arrow-right-from-bracket" href="/documentation/serverless/observability/log-drains">
    Forward logs to external services in real-time
  </Card>

  <Card title="Slack Notifications" icon="bell" href="/documentation/serverless/observability/slack-notifications">
    Alert on deployments, failures, and config changes
  </Card>
</CardGroup>
