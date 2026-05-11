> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create API Key

> Creates a new API key with the specified alias.

**Requirements:**
- Authentication required via admin API key

**Important Security Notice:**
The `key_secret` is only returned once at creation time. Store it securely immediately
as it cannot be retrieved again. If lost, you must delete the key and create a new one.

**Key Features:**
- Create API keys programmatically without UI access
- Assign meaningful aliases for key identification
- Keys are immediately active upon creation

**Common Use Cases:**
- Programmatic key provisioning for CI/CD pipelines
- Self-serve key generation for team members
- Automated key rotation workflows
- Integration with secret management systems



## OpenAPI

````yaml /api-reference/platform-apis/openapi/v1.json post /keys
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
  /keys:
    post:
      tags:
        - Keys
      summary: Create API Key
      description: >-
        Creates a new API key with the specified alias.


        **Requirements:**

        - Authentication required via admin API key


        **Important Security Notice:**

        The `key_secret` is only returned once at creation time. Store it
        securely immediately

        as it cannot be retrieved again. If lost, you must delete the key and
        create a new one.


        **Key Features:**

        - Create API keys programmatically without UI access

        - Assign meaningful aliases for key identification

        - Keys are immediately active upon creation


        **Common Use Cases:**

        - Programmatic key provisioning for CI/CD pipelines

        - Self-serve key generation for team members

        - Automated key rotation workflows

        - Integration with secret management systems
      operationId: createApiKey
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                alias:
                  type: string
                  minLength: 1
                  maxLength: 255
                  description: Required friendly name for the API key
                  example: Production Key
              required:
                - alias
              description: Request body for creating a new API key
            example:
              alias: Production Key
      responses:
        '201':
          description: >-
            API key created successfully. Store the key_secret securely - it
            will not be shown again.
          content:
            application/json:
              schema:
                type: object
                properties:
                  key_id:
                    type: string
                    description: Unique identifier for the newly created API key
                    example: abc123def456
                  key_secret:
                    type: string
                    description: >-
                      Secret portion of the API key. IMPORTANT: This is only
                      returned once at creation time and cannot be retrieved
                      again.
                    example: sk_live_abc123...
                  key:
                    type: string
                    description: >-
                      Full API key in the format 'key_id:key_secret'. Use this
                      value directly for API authorization. IMPORTANT: This is
                      only returned once at creation time and cannot be
                      retrieved again.
                    example: abc123def456:sk_live_abc123...
                required:
                  - key_id
                  - key_secret
                  - key
                description: >-
                  Response containing the newly created API key credentials. The
                  key_secret is only returned once.
              example:
                key_id: abc123def456
                key_secret: sk_live_abc123def456xyz789
                key: abc123def456:sk_live_abc123def456xyz789
        '400':
          description: Invalid request parameters
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
                  type: validation_error
                  message: Invalid request parameters
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