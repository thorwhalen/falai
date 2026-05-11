> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exporting Metrics

> Export Prometheus-compatible metrics to Grafana, Datadog, or any monitoring tool.

fal exposes a Prometheus-compatible metrics endpoint that you can scrape with any monitoring tool. Use it to build custom dashboards, set up alerts on queue depth or error rates, and feed fal metrics into the same observability stack you use for the rest of your infrastructure.

The endpoint returns metrics in [Prometheus exposition format](https://prometheus.io/docs/instrumenting/exposition_formats/), so it works with Grafana, Datadog, New Relic, Splunk, or any tool that can scrape a Prometheus target. Responses are cached for 10 seconds, so set your scrape interval accordingly.

## Endpoint

```bash theme={null}
curl -H "Authorization: Key $FAL_KEY" \
  https://api.fal.ai/v1/serverless/metrics
```

## Available Metrics

| Metric                        | Labels                                 | Description                            |
| ----------------------------- | -------------------------------------- | -------------------------------------- |
| `fal_app_runners`             | `application`, `state`, `machine_type` | Number of runners currently allocated  |
| `fal_app_queue_size`          | `application`                          | Requests waiting in queue              |
| `fal_app_concurrent_requests` | `application`                          | Requests being actively processed      |
| `fal_app_requests_completed`  | `application`, `method`, `status`      | Requests completed in the last minute  |
| `fal_app_requests_received`   | `application`, `method`                | Requests received in the last minute   |
| `fal_app_request_latency`     | `application`, `le`                    | Completed requests bucketed by latency |

The `fal_app_runners` metric tracks runners across three states: `idle` (warm, waiting), `running` (processing), and `pending` (cold start in progress).

## Integration

Add the endpoint as a Prometheus data source in your monitoring tool. The only requirement is passing your API key in the `Authorization: Key ...` header. Set the scrape interval to at least 10 seconds since responses are cached at that frequency.

### Example PromQL Queries

```promql theme={null}
# Active runners by app
fal_app_runners{state="running"}

# Queue depth across all apps
sum(fal_app_queue_size) by (application)

# Request rate (completed per minute)
fal_app_requests_completed

# P99 latency estimation
histogram_quantile(0.99, fal_app_request_latency)
```

<Note>
  All metrics are gauges. The `fal_app_request_latency` metric uses histogram-style buckets (labeled by `le`) for latency distribution analysis.
</Note>

<Card title="Platform API Reference" icon="arrow-right" href="/api-reference/platform-apis/for-serverless">
  Full API specification for the metrics endpoint
</Card>
