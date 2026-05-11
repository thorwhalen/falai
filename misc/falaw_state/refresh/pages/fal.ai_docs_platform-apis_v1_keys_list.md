> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List API Keys

> Returns a list of all API keys belonging to the authenticated user's workspace.

**Requirements:**
- Authentication required via admin API key

**Key Features:**
- View all API keys with their aliases and creation dates
- Optionally expand to include creator information
- Paginated results for workspaces with many keys

**Expansion Options:**
- `expand=creator_info`: Include creator_nickname and creator_email for each key

**Common Use Cases:**
- Audit existing API keys
- Find keys by alias
- Monitor key creation activity
- Build key management interfaces



## OpenAPI

````yaml /api-reference/platform-apis/openapi/v1.json get /keys
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
    get:
      tags:
        - Keys
      summary: List API Keys
      description: >-
        Returns a list of all API keys belonging to the authenticated user's
        workspace.


        **Requirements:**

        - Authentication required via admin API key


        **Key Features:**

        - View all API keys with their aliases and creation dates

        - Optionally expand to include creator information

        - Paginated results for workspaces with many keys


        **Expansion Options:**

        - `expand=creator_info`: Include creator_nickname and creator_email for
        each key


        **Common Use Cases:**

        - Audit existing API keys

        - Find keys by alias

        - Monitor key creation activity

        - Build key management interfaces
      operationId: listApiKeys
      parameters:
        - schema:
            type: integer
            minimum: 1
            description: >-
              Maximum number of items to return. Actual maximum depends on query
              type and expansion parameters.
            example: 50
          required: false
          description: >-
            Maximum number of items to return. Actual maximum depends on query
            type and expansion parameters.
          name: limit
          in: query
        - schema:
            type: string
            description: Pagination cursor from previous response. Encodes the page number.
            example: Mg==
          required: false
          description: Pagination cursor from previous response. Encodes the page number.
          name: cursor
          in: query
        - schema:
            anyOf:
              - type: string
              - type: array
                items:
                  type: string
            description: >-
              Fields to expand in the response. Available: creator_info
              (includes creator_nickname and creator_email)
            example:
              - creator_info
          required: false
          description: >-
            Fields to expand in the response. Available: creator_info (includes
            creator_nickname and creator_email)
          name: expand
          style: form
          explode: true
          in: query
      responses:
        '200':
          description: Successfully retrieved API keys
          content:
            application/json:
              schema:
                type: object
                properties:
                  next_cursor:
                    type:
                      - string
                      - 'null'
                    description: Cursor for the next page of results, null if no more pages
                  has_more:
                    type: boolean
                    description: >-
                      Boolean indicating if more results are available
                      (convenience field derived from next_cursor)
                  keys:
                    type: array
                    items:
                      type: object
                      properties:
                        key_id:
                          type: string
                          description: Unique identifier for the API key
                          example: abc123def456
                        alias:
                          type: string
                          description: User-provided friendly name for the key
                          example: Production Key
                        scope:
                          type: string
                          enum:
                            - API
                          description: >-
                            Scope of the API key. Only API scope keys can be
                            managed via this API.
                          example: API
                        created_at:
                          type: string
                          description: ISO8601 timestamp when the key was created
                          example: '2025-01-15T12:00:00Z'
                        creator_nickname:
                          type: string
                          description: >-
                            Nickname of the user who created this key (when
                            expanded)
                          example: developer
                        creator_email:
                          type: string
                          description: >-
                            Email of the user who created this key (when
                            expanded)
                          example: developer@example.com
                      required:
                        - key_id
                        - alias
                        - scope
                        - created_at
                      description: API key information
                    description: Array of API keys belonging to the authenticated user
                required:
                  - next_cursor
                  - has_more
                  - keys
                description: Response containing a list of API keys with pagination support
              example:
                keys:
                  - key_id: abc123def456
                    alias: Production Key
                    scope: API
                    created_at: '2025-01-15T12:00:00Z'
                  - key_id: xyz789ghi012
                    alias: Development Key
                    scope: API
                    created_at: '2025-01-10T09:30:00Z'
                next_cursor: null
                has_more: false
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