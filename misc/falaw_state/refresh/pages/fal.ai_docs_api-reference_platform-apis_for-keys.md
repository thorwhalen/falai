> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Platform APIs for Keys

> Programmatic access to API key management, creation, and deletion

The **fal Platform APIs** provide programmatic access to API key management, including:

* **List keys** - Retrieve all API keys associated with your account
* **Create keys** - Generate new API keys with custom aliases
* **Delete keys** - Revoke and remove existing API keys

## Available Operations

The Platform APIs provide the following endpoints for managing API keys:

<CardGroup cols={3}>
  <Card title="List API Keys" icon="list" href="/platform-apis/v1/keys/list">
    Retrieve all API keys with pagination support
  </Card>

  <Card title="Create API Key" icon="plus" href="/platform-apis/v1/keys/create">
    Generate a new API key with a friendly alias
  </Card>

  <Card title="Delete API Key" icon="trash" href="/platform-apis/v1/keys/delete">
    Permanently revoke and delete an API key
  </Card>
</CardGroup>

<Note>
  These APIs require **admin API key** authentication. For more information on authentication, see the [Authentication](/reference/platform-apis/authentication) documentation.
</Note>
