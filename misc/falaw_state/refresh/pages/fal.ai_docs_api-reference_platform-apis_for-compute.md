> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Platform APIs for Compute

> Programmatic access to compute instance management, lifecycle control, and monitoring

The **fal Platform APIs** provide programmatic access to platform management features for Compute, including:

* **Instance management** - Create, list, and delete compute instances
* **Instance details** - Retrieve detailed information about specific instances

## Available Operations

The Platform APIs provide the following endpoints for managing Compute instances:

<CardGroup cols={2}>
  <Card title="List Instances" icon="list" href="/platform-apis/v1/compute/instances/list">
    List all compute instances with their current status and configuration
  </Card>

  <Card title="Get Instance Details" icon="info-circle" href="/platform-apis/v1/compute/instances/get">
    Retrieve detailed information about a specific compute instance
  </Card>

  <Card title="Create Instance" icon="plus" href="/platform-apis/v1/compute/instances/create">
    Create and provision a new compute instance
  </Card>

  <Card title="Delete Instance" icon="trash" href="/platform-apis/v1/compute/instances/delete">
    Terminate and remove a compute instance
  </Card>
</CardGroup>

<Note>
  These APIs are for **platform management** of Compute instances. For getting started with Compute, see the [Compute documentation](/compute).
</Note>
