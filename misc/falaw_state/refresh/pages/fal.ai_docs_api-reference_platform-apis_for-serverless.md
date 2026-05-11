> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Platform APIs for Serverless

> Programmatic access to serverless apps metadata and analytics

## Available Operations

The Platform APIs provide the following endpoints for Serverless Apps:

## Files

<CardGroup cols={5}>
  <Card title="List Root Directory Contents" icon="list" href="/platform-apis/v1/serverless/files/list">
    List the contents of the root directory of your Serverless storage.
  </Card>

  <Card title="List Directory Contents" icon="grid" href="/platform-apis/v1/serverless/files/list/directory">
    List the contents of any nested directory by providing its path.
  </Card>

  <Card title="Download File" icon="database" href="/platform-apis/v1/serverless/files/file/download">
    Download any file from Serverless storage.
  </Card>

  <Card title="Upload from URL" icon="plus" href="/platform-apis/v1/serverless/files/file/upload-from-url">
    Upload a file from a URL into Serverless storage.
  </Card>

  <Card title="Upload Local File" icon="server" href="/platform-apis/v1/serverless/files/file/upload-local">
    Upload a local file into Serverless storage.
  </Card>
</CardGroup>

## Requests

<CardGroup cols={1}>
  <Card title="List Requests by Endpoint" icon="list" href="/platform-apis/v1/serverless/requests/by-endpoint">
    List recent requests for your serverless endpoints with filtering, sorting, and pagination.
  </Card>
</CardGroup>

## Logs

<CardGroup cols={2}>
  <Card title="Logs History" icon="diagram-project" href="/platform-apis/v1/serverless/logs/history">
    Query paginated logs with powerful label filters, time ranges, and search keywords.
  </Card>

  <Card title="Logs Stream" icon="signal-stream" href="/platform-apis/v1/serverless/logs/stream">
    Stream live logs that match the provided filters using Server-Sent Events.
  </Card>
</CardGroup>

## Analytics

<CardGroup cols={1}>
  <Card title="Analytics" icon="chart-line" href="/platform-apis/v1/serverless/analytics">
    Query time-bucketed metrics across all inbound traffic to your apps, including request counts, success/error rates, and latency percentiles. Ideal for exporting to your own observability tools.
  </Card>
</CardGroup>

## Metrics

<CardGroup cols={2}>
  <Card title="Queue Size" icon="grid" href="/platform-apis/v1/serverless/apps/queue">
    Read the current queue backlog for your serverless applications.
  </Card>

  <Card title="Metrics" icon="grid" href="/platform-apis/v1/serverless/metrics">
    Export app metrics (runners, queue size, concurrent requests, throughput, and latency) in Prometheus format for custom dashboards and monitoring.
  </Card>
</CardGroup>
