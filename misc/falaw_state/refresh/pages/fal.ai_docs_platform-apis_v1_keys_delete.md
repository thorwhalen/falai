> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete API Key

> Deletes an API key by its ID. This action is irreversible.

**Requirements:**
- Authentication required via admin API key
- Key must belong to the authenticated user's workspace

**Key Features:**
- Permanently revoke API key access
- Idempotent operation (safe to retry)
- Optional Idempotency-Key header for safe retries

**Important:**
- This action cannot be undone
- Any applications using this key will immediately lose access
- Returns 204 even if the key doesn't exist (idempotent behavior)

**Common Use Cases:**
- Revoke compromised keys
- Clean up unused keys
- Implement key rotation (delete old, create new)
- Offboard team members



## OpenAPI

````yaml /api-reference/platform-apis/openapi/v1.json delete /keys/{key_id}
openapi: 3.1.0
info:
  title: Platform APIs
  version: v1
  description: fal REST API for programmatic access to platform resources.
servers:
  - url: https://api.fal.ai/v1
    description: Production server
security: []
paths:
  /keys/{key_id}:
    delete:
      tags:
        - Keys
      summary: Delete API Key
      description: |-
        Deletes an API key by its ID. This action is irreversible.

        **Requirements:**
        - Authentication required via admin API key
        - Key must belong to the authenticated user's workspace

        **Key Features:**
        - Permanently revoke API key access
        - Idempotent operation (safe to retry)
        - Optional Idempotency-Key header for safe retries

        **Important:**
        - This action cannot be undone
        - Any applications using this key will immediately lose access
        - Returns 204 even if the key doesn't exist (idempotent behavior)

        **Common Use Cases:**
        - Revoke compromised keys
        - Clean up unused keys
        - Implement key rotation (delete old, create new)
        - Offboard team members
      operationId: deleteApiKey
      parameters:
        - schema:
            type: string
            minLength: 1
            description: Unique identifier of the API key to delete
            example: abc123def456
          required: true
          description: Unique identifier of the API key to delete
          name: key_id
          in: path
        - schema:
            type: string
            description: Optional idempotency key for safe request retries
            example: 550e8400-e29b-41d4-a716-446655440000
          required: false
          description: Optional idempotency key for safe request retries
          name: Idempotency-Key
          in: header
      responses:
        '204':
          description: API key deleted successfully (or already deleted)
        '401':
          description: Authentication required
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - authorization_error
                          - validation_error
                          - not_found
                          - rate_limited
                          - server_error
                          - not_implemented
                        description: The category of error that occurred
                      message:
                        type: string
                        description: Human-readable error message
                      docs_url:
                        type: string
                        format: uri
                        description: Link to relevant documentation
                      request_id:
                        type: string
                        description: Unique request identifier for debugging
                    required:
                      - type
                      - message
                    description: Error details
                required:
                  - error
                description: Standard error response format
              example:
                error:
                  type: authorization_error
                  message: Authentication required
        '403':
          description: Access denied
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - authorization_error
                          - validation_error
                          - not_found
                          - rate_limited
                          - server_error
                          - not_implemented
                        description: The category of error that occurred
                      message:
                        type: string
                        description: Human-readable error message
                      docs_url:
                        type: string
                        format: uri
                        description: Link to relevant documentation
                      request_id:
                        type: string
                        description: Unique request identifier for debugging
                    required:
                      - type
                      - message
                    description: Error details
                required:
                  - error
                description: Standard error response format
              example:
                error:
                  type: authorization_error
                  message: Access denied
        '429':
          description: Rate limit exceeded
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - authorization_error
                          - validation_error
                          - not_found
                          - rate_limited
                          - server_error
                          - not_implemented
                        description: The category of error that occurred
                      message:
                        type: string
                        description: Human-readable error message
                      docs_url:
                        type: string
                        format: uri
                        description: Link to relevant documentation
                      request_id:
                        type: string
                        description: Unique request identifier for debugging
                    required:
                      - type
                      - message
                    description: Error details
                required:
                  - error
                description: Standard error response format
              example:
                error:
                  type: rate_limited
                  message: Rate limit exceeded
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - authorization_error
                          - validation_error
                          - not_found
                          - rate_limited
                          - server_error
                          - not_implemented
                        description: The category of error that occurred
                      message:
                        type: string
                        description: Human-readable error message
                      docs_url:
                        type: string
                        format: uri
                        description: Link to relevant documentation
                      request_id:
                        type: string
                        description: Unique request identifier for debugging
                    required:
                      - type
                      - message
                    description: Error details
                required:
                  - error
                description: Standard error response format
              example:
                error:
                  type: server_error
                  message: An unexpected error occurred
      security:
        - adminApiKey: []
components:
  securitySchemes:
    adminApiKey:
      type: apiKey
      in: header
      name: Authorization
      description: >-
        Admin API key must be prefixed with "Key ", e.g. Authorization: Key
        YOUR_ADMIN_API_KEY

````