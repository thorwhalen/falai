> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding Requests

> How requests flow through fal's infrastructure, from submission through queue, dispatch, processing, and retries.

When you call a model or your own deployed app on fal, the request passes through several layers before your code processes it and returns a result. Understanding these layers helps you reason about latency, retries, timeouts, and why requests behave the way they do. This page covers the request lifecycle from the caller's perspective down to the runner, and how requests interact with [runners](/documentation/deployment/runners) and the [retry system](/documentation/serverless/reliability/retries).

fal's infrastructure is built around a persistent queue that decouples callers from runners. When you use queue-based methods ([`submit()`](/documentation/model-apis/inference/queue), [`subscribe()`](/documentation/model-apis/inference/synchronous)), your request enters the queue and benefits from automatic retries, status tracking, and durability. Direct methods ([`run()`](/documentation/model-apis/inference/synchronous), [`stream()`](/documentation/model-apis/inference/streaming)) bypass the queue and connect straight to a runner, which is faster but means no retries and no status polling. Both paths share the same runner and scaling infrastructure underneath.

## Request Lifecycle (Queue-Based)

When using `submit()` or `subscribe()`, a request moves through three states visible to callers via the [queue status API](/documentation/model-apis/inference/queue#check-status). Direct calls via `run()` and `stream()` bypass the queue entirely and do not have these states.

<div className="max-w-2xl mx-auto">
  ```mermaid theme={null}
  stateDiagram-v2
      [*] --> IN_QUEUE
      IN_QUEUE --> IN_PROGRESS: Runner picks up request
      IN_PROGRESS --> COMPLETED: Response ready
      IN_PROGRESS --> IN_QUEUE: Runner fails, request retried
      COMPLETED --> [*]
  ```
</div>

| State            | What is happening                                       | Caller sees                                                                |
| ---------------- | ------------------------------------------------------- | -------------------------------------------------------------------------- |
| **IN\_QUEUE**    | Request is waiting in the queue for an available runner | `queue_position` indicating how many requests are ahead                    |
| **IN\_PROGRESS** | A runner is executing your endpoint handler             | [`logs`](/documentation/development/logging) from your code (when enabled) |
| **COMPLETED**    | Result is stored and ready for retrieval                | Full response payload                                                      |

Cancellation is handled separately from the status lifecycle. When a caller [cancels a request](/documentation/model-apis/inference/queue#cancel-a-request), queued requests are removed from the queue and in-progress requests receive a [cancellation signal](/documentation/development/handle-cancellations). The cancel API returns `CANCELLATION_REQUESTED` (202) or `ALREADY_COMPLETED` (400) rather than transitioning to a pollable status.

### How Requests Flow

<Steps>
  <Step title="Submission">
    The caller submits a request via the [SDK](/documentation/model-apis/inference) or REST API. fal assigns a [`request_id`](/documentation/model-apis/inference/queue#submit-a-request) and places the request in the persistent queue. The request enters `IN_QUEUE` state. By default there is no queue size limit and requests are never dropped. Callers can optionally set [`fal_max_queue_length`](/documentation/model-apis/common-parameters#fal-max-queue-length) to reject requests with 429 if the queue exceeds a threshold.
  </Step>

  <Step title="Dispatch">
    The dispatcher checks for available IDLE [runners](/documentation/deployment/runners). If a runner is free, the request is routed immediately and enters `IN_PROGRESS`. If all runners are busy, the request waits in the queue while fal [scales up](/documentation/deployment/scale-your-application) new runners. Runners with matching [routing hints](/documentation/serverless/optimizations/optimize-routing-behavior) are preferred when available.
  </Step>

  <Step title="Processing">
    The runner receives the request as a standard HTTP call. Your [endpoint handler](/documentation/development/endpoints-overview) runs, processes the input, and returns a response. The runner transitions from RUNNING back to IDLE. If the runner fails, the request is [retried](/documentation/serverless/reliability/retries) automatically.
  </Step>

  <Step title="Result">
    The response is stored and the request enters `COMPLETED`. The caller retrieves the result by [polling or streaming status](/documentation/model-apis/inference/queue#check-status), or receives it via [webhook](/documentation/model-apis/inference/webhooks). For direct `run()` calls, the response is returned in the same HTTP connection.
  </Step>
</Steps>

Your endpoint code receives every request as a regular HTTP call. It does not matter whether the caller used `run()`, `submit()`, or `stream()`. The queue and dispatch layer are transparent to your app code.

## Requests and Retries

Retries only apply to queue-based requests. Direct calls via `run()` and `stream()` return errors immediately with no retry.

When a runner fails while processing a queued request, the request is placed in a scheduled requeue with a backoff delay, then re-enters the queue and is dispatched to a different runner. This happens automatically for server errors (503), timeouts (504), and connection failures, up to 10 attempts. The retry is transparent to the caller -- they continue polling the same `request_id` and eventually get a result or a final failure.

<div className="max-w-2xl mx-auto">
  ```mermaid theme={null}
  stateDiagram-v2
      [*] --> IN_QUEUE
      IN_QUEUE --> IN_PROGRESS: "Attempt 1"
      IN_PROGRESS --> ScheduledRequeue: Runner returns 503
      ScheduledRequeue --> IN_QUEUE: "After backoff delay"
      IN_QUEUE --> IN_PROGRESS: "Attempt 2"
      IN_PROGRESS --> COMPLETED: Success
      COMPLETED --> [*]
  ```
</div>

The [`start_timeout`](/documentation/model-apis/inference/queue#start-timeout) clock runs continuously across all retry attempts. If you set `start_timeout=30` and the first attempt fails after 20 seconds, the second attempt only has 10 seconds left before the server returns 504. This prevents retries from running indefinitely.

You can control retry behavior at three levels: app-level with [`skip_retry_conditions`](/documentation/serverless/reliability/retries#app-level-skip_retry_conditions), per-response with the [`X-Fal-Needs-Retry`](/documentation/serverless/reliability/retries#per-response-x-fal-needs-retry) header, and per-request with the [`X-Fal-No-Retry`](/documentation/serverless/reliability/retries#per-request-client-side-control) header from the caller.

<CardGroup cols={2}>
  <Card title="Understanding Runners" icon="server" href="/documentation/deployment/runners">
    Runner lifecycle states, startup, shutdown, and scaling
  </Card>

  <Card title="Retries and Error Handling" icon="rotate" href="/documentation/serverless/reliability/retries">
    Status codes, response headers, timeouts, and retry control
  </Card>

  <Card title="Caching" icon="layer-group" href="/documentation/deployment/caching">
    How cold start caching affects request latency
  </Card>

  <Card title="Handle Cancellations" icon="xmark" href="/documentation/development/handle-cancellations">
    Implement cancel endpoints for in-progress requests
  </Card>
</CardGroup>
