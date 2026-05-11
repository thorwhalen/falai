> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List requests by endpoint

> Lists requests for endpoints owned by the authenticated user.

**Authentication:** Requires API key.

**Filters:**
- Time range via start / end
- Status (success, error, user_error)
- Request ID
- Pagination via cursor/limit (limit defaults to 50, max 100)

**Sorting:**
- By end time (default) or duration

**Expansions:**
- Include payloads by adding expand=payloads



## OpenAPI

````yaml /api-reference/platform-apis/openapi/v1.json get /serverless/requests/by-endpoint
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
  /serverless/requests/by-endpoint:
    get:
      tags:
        - Serverless
        - Requests
      summary: List requests by endpoint
      description: |-
        Lists requests for endpoints owned by the authenticated user.

        **Authentication:** Requires API key.

        **Filters:**
        - Time range via start / end
        - Status (success, error, user_error)
        - Request ID
        - Pagination via cursor/limit (limit defaults to 50, max 100)

        **Sorting:**
        - By end time (default) or duration

        **Expansions:**
        - Include payloads by adding expand=payloads
      operationId: serverlessListRequestsByEndpoint
      parameters:
        - schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 50
            description: Number of items to return per page (max 100)
            example: 20
          required: false
          description: Number of items to return per page (max 100)
          name: limit
          in: query
        - schema:
            type: string
            description: Pagination cursor encoding the page number
            example: Mg==
          required: false
          description: Pagination cursor encoding the page number
          name: cursor
          in: query
        - schema:
            type: string
            description: Endpoint identifier to filter requests by
            example: fal-ai/flux/dev
          required: true
          description: Endpoint identifier to filter requests by
          name: endpoint_id
          in: query
        - schema:
            anyOf:
              - type: string
                format: date-time
              - type: string
                pattern: ^\d{4}-\d{2}-\d{2}$
            description: >-
              Start date in ISO8601 format (e.g., '2025-01-01T00:00:00Z' or
              '2025-01-01'). Defaults to 24 hours ago.
            example: '2025-01-01T00:00:00Z'
          required: false
          description: >-
            Start date in ISO8601 format (e.g., '2025-01-01T00:00:00Z' or
            '2025-01-01'). Defaults to 24 hours ago.
          name: start
          in: query
        - schema:
            anyOf:
              - type: string
                format: date-time
              - type: string
                pattern: ^\d{4}-\d{2}-\d{2}$
            description: >-
              End date in ISO8601 format, exclusive (e.g.,
              '2025-02-01T00:00:00Z' or '2025-02-01'). Data up to but not
              including this timestamp is returned. Defaults to current time.
            example: '2025-02-01T00:00:00Z'
          required: false
          description: >-
            End date in ISO8601 format, exclusive (e.g., '2025-02-01T00:00:00Z'
            or '2025-02-01'). Data up to but not including this timestamp is
            returned. Defaults to current time.
          name: end
          in: query
        - schema:
            type: string
            enum:
              - success
              - error
              - user_error
            description: Filter by request status
            example: success
          required: false
          description: Filter by request status
          name: status
          in: query
        - schema:
            type: string
            format: uuid
            description: Filter by specific request ID
            example: a1b2c3d4-e5f6-7890-abcd-ef1234567890
          required: false
          description: Filter by specific request ID
          name: request_id
          in: query
        - schema:
            anyOf:
              - type: string
              - type: array
                items:
                  type: string
            description: >-
              Fields to expand in the response. Use payloads to include input
              and output payloads.
            example:
              - payloads
          required: false
          description: >-
            Fields to expand in the response. Use payloads to include input and
            output payloads.
          name: expand
          style: form
          explode: true
          in: query
        - schema:
            type: string
            enum:
              - ended_at
              - duration
            default: ended_at
            description: Sort results by end time or duration
            example: ended_at
          required: false
          description: Sort results by end time or duration
          name: sort_by
          in: query
      responses:
        '200':
          description: Requests listed successfully
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
                  items:
                    type: array
                    items:
                      type: object
                      properties:
                        request_id:
                          type: string
                          format: uuid
                          description: Unique identifier for the request
                          example: a1b2c3d4-e5f6-7890-abcd-ef1234567890
                        endpoint_id:
                          type: string
                          description: Endpoint that was executed for this request
                          example: fal-ai/flux/dev
                        started_at:
                          type: string
                          format: date-time
                          description: Time when request processing started
                          example: '2025-01-01T00:00:05Z'
                        sent_at:
                          type: string
                          format: date-time
                          description: Time when request was sent to the backend
                          example: '2025-01-01T00:00:01Z'
                        ended_at:
                          type:
                            - string
                            - 'null'
                          format: date-time
                          description: Time when request finished processing
                          example: '2025-01-01T00:00:08Z'
                        status_code:
                          type:
                            - integer
                            - 'null'
                          description: HTTP status code returned by the request
                          example: 200
                        duration:
                          type:
                            - number
                            - 'null'
                          description: Total request duration in seconds
                          example: 7.8
                        json_input:
                          description: Input payload for the request
                        json_output:
                          description: Output payload for the request
                        runner_id:
                          type: string
                          format: uuid
                          description: Unique identifier for the runner execution instance
                          example: f1e2d3c4-b5a6-7890-dcba-0987654321fe
                      required:
                        - request_id
                        - endpoint_id
                        - started_at
                        - sent_at
                        - runner_id
                      description: Serverless request item
                    description: List of requests matching the filter
                required:
                  - next_cursor
                  - has_more
                  - items
                description: >-
                  Paginated list of serverless requests for the specified
                  endpoint
              example:
                items:
                  - request_id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
                    endpoint_id: fal-ai/flux/dev
                    runner_id: f1e2d3c4-b5a6-7890-dcba-0987654321fe
                    started_at: '2025-01-01T00:00:05Z'
                    sent_at: '2025-01-01T00:00:01Z'
                    ended_at: '2025-01-01T00:00:08Z'
                    status_code: 200
                    duration: 7.8
                    json_input:
                      prompt: cat astronaut
                    json_output:
                      status: ok
                next_cursor: Mg==
                has_more: true
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
        '404':
          description: Resource not found
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
                  type: not_found
                  message: Resource not found
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
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: Authorization
      description: >-
        API key must be prefixed with "Key ", e.g. Authorization: Key
        YOUR_API_KEY

````