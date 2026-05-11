> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Publish Custom Metrics with Prometheus Pushgateway

> Publish custom metrics on fal using Prometheus Pushgateway with direct port exposure and persistent storage.

Serverless workers are usually short-lived, which makes them a poor direct scrape target for Prometheus.
[Prometheus Pushgateway](https://github.com/prometheus/pushgateway) solves this by letting your jobs push metrics to a stable endpoint that Prometheus scrapes on its own schedule.

In this example, you deploy Pushgateway itself on fal as a small always-available service with persistent storage for metric state. Then your apps push custom metrics to it, and Prometheus scrapes from one predictable URL.

## 🚀 Try this Example

**Steps to run:**

1. Save this as `pushgateway.py`:

```python theme={null}
import os
import subprocess

import fal
from fal.container import ContainerImage

PORT = 8080
PERSISTENCE_DIR = "/data/pushgateway"
PERSISTENCE_FILE = f"{PERSISTENCE_DIR}/metrics.dat"

@fal.function(
    image=ContainerImage.from_dockerfile_str(
        r"""
FROM prom/pushgateway:v1.11.0 AS pushgateway_stage

FROM python:3.10-slim-bookworm
COPY --from=pushgateway_stage /bin/pushgateway /usr/local/bin/pushgateway
"""
    ),
    machine_type="M",
    exposed_port=PORT,
    max_concurrency=1,
    min_concurrency=1,
    max_multiplexing=256,
)
def pushgateway() -> None:
    os.makedirs(PERSISTENCE_DIR, exist_ok=True)
    subprocess.run(
        [
            "pushgateway",
            f"--web.listen-address=0.0.0.0:{PORT}",
            f"--persistence.file={PERSISTENCE_FILE}",
            "--persistence.interval=5m",
        ],
        check=True,
    )
```

2. Deploy it:

```bash theme={null}
fal deploy pushgateway.py::pushgateway --name pushgateway
```

After deploy, your gateway is available at:

```text theme={null}
https://fal.run/<your-username>/pushgateway
```

Opening that URL in a browser (`/`) shows the Pushgateway web interface, which is useful for quickly checking pushed metric groups.

## Push and Scrape Metrics

Set your base URL:

```bash theme={null}
BASE_URL="https://fal.run/<your-username>/pushgateway"
```

Push a sample metric:

```bash theme={null}
cat <<'EOF' | curl -X PUT \
  -H "Content-Type: text/plain" \
  -H "Authorization: Key $FAL_KEY" \
  --data-binary @- \
  "$BASE_URL/metrics/job/example/instance/local"
# TYPE demo_jobs_total counter
demo_jobs_total 1
EOF
```

Scrape all metrics:

```bash theme={null}
curl -H "Authorization: Key $FAL_KEY" "$BASE_URL/metrics"
```

Check health:

```bash theme={null}
curl -H "Authorization: Key $FAL_KEY" "$BASE_URL/-/healthy"
```

## Prometheus Scrape Configuration

Use `fal.run` as the target host and include your app path in `metrics_path`:

```yaml theme={null}
scrape_configs:
  - job_name: fal_pushgateway
    honor_labels: true
    scheme: https
    static_configs:
      - targets: ["fal.run"]
    metrics_path: /<your-username>/pushgateway/metrics
    authorization:
      type: Key
      credentials: <your-fal-key>
```
