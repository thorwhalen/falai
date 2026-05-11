> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Error Analytics

> Explore, filter, and debug request errors across your applications.

The Error Analytics dashboard gives you a centralized view of all request errors across your deployed applications. Use it to spot error spikes, identify which endpoints or status codes are causing the most failures, and drill into individual failed requests to see full logs and timing.

You can access error analytics per-app (from any app's **Errors** tab) or globally across all apps at [**Dashboard > Apps > Errors**](https://fal.ai/dashboard/apps/errors). Filter by endpoint, status code, and date range to narrow down the issue.

<Frame>
  <iframe className="w-full aspect-video rounded-lg" srcdoc="<style>*{padding:0;margin:0;overflow:hidden}html,body{height:100%}img,span{position:absolute;width:100%;top:0;bottom:0;margin:auto}span{height:1.5em;text-align:center;font:48px/1.5 sans-serif;color:white;text-shadow:0 0 0.5em black}</style><a href='https://www.youtube.com/embed/gDJJ9bppyV8?start=441&end=483&autoplay=1'><img src='/docs/images/video-thumbs/error-analytics.jpg' alt='Error Analytics - fal Serverless'><span>▶</span></a>" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />
</Frame>

## Debugging Errors

When you see errors in the dashboard, click into any individual failed request to see the full details: when it was submitted, how long it took, what status code was returned, and the complete [request logs](/documentation/development/logging). This is the fastest way to go from "something is failing" to "here's the stack trace."

For errors that correlate with a deployment, check [App Events](/documentation/serverless/observability/app-events) to see if a recent deploy or config change caused the issue. If the error rate is tied to a specific status code, see [Retries and Error Handling](/documentation/serverless/reliability/retries) to understand what each code means for your runners and retries.

## Common Error Patterns

| Status  | What it usually means                                                |
| ------- | -------------------------------------------------------------------- |
| **500** | Unhandled exception in your endpoint code. Runner stays alive.       |
| **502** | Runner crashed or connection was lost during processing.             |
| **503** | Runner is in a bad state and was terminated. Request is retried.     |
| **504** | Request exceeded timeout. Often from cold starts or heavy workloads. |
| **429** | Concurrency limit reached. Request is re-queued automatically.       |

For a complete reference on how each status code affects runners, retries, and billing, see [Status Codes](/documentation/serverless/reliability/retries#status-code-reference).

<CardGroup cols={2}>
  <Card title="Status Codes" icon="list-ol" href="/documentation/serverless/reliability/retries#status-code-reference">
    How each HTTP status code affects runners and retries
  </Card>

  <Card title="Retries" icon="rotate" href="/documentation/serverless/reliability/retries">
    How fal automatically retries failed requests
  </Card>
</CardGroup>
