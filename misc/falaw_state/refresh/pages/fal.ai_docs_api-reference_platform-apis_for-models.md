> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Platform APIs for Models

> Programmatic access to model metadata, pricing, usage tracking, and analytics

The **fal Platform APIs** provide programmatic access to platform management features for Model APIs, including:

* **Model metadata** - Search and discover available model endpoints with detailed information
* **Pricing information** - Retrieve real-time pricing and estimate costs
* **Usage tracking** - Access detailed usage line items with unit quantities and prices
* **Analytics** - Query time-bucketed metrics for request counts, success/error rates, and latency

## Available Operations

The Platform APIs provide the following endpoints for managing Model APIs:

<CardGroup cols={2}>
  <Card title="Model Search" icon="grid" href="/platform-apis/v1/models">
    Search and discover available model endpoints with metadata, categories, and capabilities
  </Card>

  <Card title="Model Pricing" icon="dollar-sign" href="/platform-apis/v1/models/pricing">
    Retrieve real-time pricing information for models
  </Card>

  <Card title="Estimate Cost" icon="calculator" href="/platform-apis/v1/models/pricing/estimate">
    Estimate costs for planned operations
  </Card>

  <Card title="Usage" icon="chart-bar" href="/platform-apis/v1/models/usage">
    Access detailed usage line items with unit quantities and prices
  </Card>

  <Card title="Analytics" icon="chart-line" href="/platform-apis/v1/models/analytics">
    Query time-bucketed metrics for requests, success rates, and latency
  </Card>

  <Card title="List Requests by Endpoint" icon="list" href="/platform-apis/v1/models/requests/by-endpoint">
    List recent requests for a specific model endpoint with filters and pagination
  </Card>

  <Card title="Delete Request Payloads" icon="trash" href="/platform-apis/v1/models/requests/payloads">
    Delete IO payloads and CDN output files for a specific request
  </Card>
</CardGroup>

<Note>
  These APIs are for **platform management** of Model APIs. For executing models and generating content, see the [Inference Methods](/documentation/model-apis/inference) documentation.
</Note>
