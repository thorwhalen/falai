> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GPU Health

> How fal monitors GPU health, detects failures, and gives you control over runner health through custom health checks.

GPU hardware can degrade or fail during operation. Thermal throttling, memory errors, driver issues, and hardware faults can all cause a runner to produce incorrect results or hang silently. fal monitors GPU health at the platform level and provides tools for you to add application-level health checks that detect problems specific to your workload.

Platform-level monitoring runs continuously across all runners and reacts to hardware problems without any configuration on your part. Application-level [health checks](/documentation/development/add-health-check-endpoint) are optional but recommended for production apps, especially those that hold state or are sensitive to GPU degradation. Together, these ensure that unhealthy runners are replaced before they affect your users.

## Platform GPU Monitoring

fal continuously monitors GPU metrics across all runners, including temperature, clock frequencies, and throttling events. When issues are detected, the operations team is alerted and can cordon the node (preventing new runners from being scheduled), drain existing runners, and perform GPU resets. If the issue persists, the node is escalated for hardware replacement.

This monitoring runs automatically and requires no configuration. You benefit from it regardless of whether you have custom health checks enabled.

## Application Health Checks

Platform monitoring catches hardware-level failures, but it cannot detect application-level problems like a corrupted model state, a leaked GPU memory allocation, or an external dependency that went down. For these, you can define a [health check endpoint](/documentation/development/add-health-check-endpoint) that fal calls periodically to verify your runner is functioning correctly.

```python theme={null}
import fal

class MyApp(fal.App):
    def setup(self):
        self.model = load_model()
        self.db = connect_to_database()

    @fal.endpoint("/health", health_check=fal.HealthCheck(
        failure_threshold=3,
        call_regularly=True,
    ))
    def health(self) -> dict:
        if not self.db.is_alive():
            raise RuntimeError("Database connection lost")
        return {"status": "ok"}
```

When a health check fails for `failure_threshold` consecutive calls (default 3), the runner is terminated and replaced. Health checks run every 15 seconds when `call_regularly=True`.

### Non-Invasive vs Invasive Checks

Health checks with `call_regularly=True` run in parallel with request processing. Keep these lightweight since they share GPU and CPU resources with active requests. Check connection status, memory usage, or simple assertions rather than running inference.

For more thorough checks that need exclusive GPU access (e.g., running a test inference), set `call_regularly=False`. In this mode, the health check only runs when the gateway sends an `x-fal-runner-health-check` header, which happens between requests or after specific error conditions.

```python theme={null}
@fal.endpoint("/health", health_check=fal.HealthCheck(
    call_regularly=False,
    timeout_seconds=10,
))
def health(self) -> dict:
    test_result = self.model.run(self.test_input)
    if not validate(test_result):
        raise RuntimeError("Model producing invalid output")
    return {"status": "ok"}
```

## Handling GPU Errors in Your Code

If your code detects a GPU-level error during request processing (such as an out-of-memory condition or CUDA error), return a [503 status code](/documentation/serverless/reliability/retries#status-code-reference) to signal that the runner should be terminated and replaced. This is the appropriate response when the runner's GPU state is corrupted and it cannot reliably serve further requests.

```python theme={null}
@fal.endpoint("/")
def predict(self, input: dict) -> dict:
    try:
        return self.model.run(input)
    except RuntimeError as e:
        if "out of memory" in str(e).lower() or "CUDA" in str(e):
            from fastapi.responses import JSONResponse
            return JSONResponse(status_code=503, content={"detail": "GPU error"})
        raise
```

For errors where the runner is still functional (e.g., bad input, model inference failure), use [500 instead](/documentation/deployment/readiness-liveness#which-status-code-to-use).

<CardGroup cols={2}>
  <Card title="Health Check Endpoint" icon="heart-pulse" href="/documentation/development/add-health-check-endpoint">
    Full configuration reference for health checks
  </Card>

  <Card title="Status Codes" icon="list-ol" href="/documentation/serverless/reliability/retries#status-code-reference">
    How each HTTP status code affects runners and retries
  </Card>
</CardGroup>
