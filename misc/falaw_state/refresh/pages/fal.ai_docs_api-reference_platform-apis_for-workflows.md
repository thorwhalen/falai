> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Platform APIs for Workflows

> Programmatic access to workflow metadata, listing, and details

The **fal Platform APIs** provide programmatic access to workflow management for the authenticated user, including:

* **List workflows** - Paginated list of your workflows with optional search and filtering
* **Get workflow details** - Retrieve a specific workflow by owner and name, including its full definition

## Available Operations

The Platform APIs provide the following endpoints for Workflows:

<CardGroup cols={2}>
  <Card title="List Workflows" icon="list" href="/platform-apis/v1/workflows">
    List workflows for the authenticated user with optional search and filtering
    by endpoint
  </Card>

  <Card title="Get Workflow Details" icon="info-circle" href="/platform-apis/v1/workflows/get">
    Get detailed information about a specific workflow, including its full
    definition
  </Card>
</CardGroup>

## Authentication

All Workflows endpoints require authentication. Include your API key in the `Authorization` header:

```
Authorization: Key YOUR_API_KEY
```

List workflows returns only workflows owned by the authenticated user. Get workflow details requires access to the workflow (e.g., it is yours or public).

<Note>
  These APIs are for **platform management** of Workflows (listing and reading).
  To run workflows, use the [Model APIs](/model-apis) or workflow execution
  endpoints.
</Note>
