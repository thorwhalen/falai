> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Logs history (paginated)

> Returns paginated historical logs that match the provided filters.



## OpenAPI

````yaml /api-reference/platform-apis/openapi/v1.json post /serverless/logs/history
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
  /serverless/logs/history:
    post:
      tags:
        - Serverless
        - Logs
      summary: Logs history (paginated)
      description: Returns paginated historical logs that match the provided filters.
      operationId: serverlessLogsHistory
      parameters:
        - schema:
            type: integer
            minimum: 1
            maximum: 1000
            description: Number of results per page
            example: 100
          required: false
          description: Number of results per page
          name: limit
          in: query
        - schema:
            type: string
            description: >-
              Pagination cursor from previous response (timestamp-based). Use as
              'until' parameter for next page.
            example: '2024-11-09T00:00:00.000Z'
          required: false
          description: >-
            Pagination cursor from previous response (timestamp-based). Use as
            'until' parameter for next page.
          name: cursor
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
            anyOf:
              - type: string
              - type: array
                items:
                  type: string
            description: >-
              Filter by specific app ID(s) in '<owner>/<name>' format (e.g.
              'fal-ai/my-app'). Accepts 1-50 app IDs. Supports comma-separated
              values: ?app_id=fal-ai/foo,fal-ai/bar or array syntax:
              ?app_id=fal-ai/foo&app_id=fal-ai/bar
            example:
              - fal-ai/my-app
          required: false
          description: >-
            Filter by specific app ID(s) in '<owner>/<name>' format (e.g.
            'fal-ai/my-app'). Accepts 1-50 app IDs. Supports comma-separated
            values: ?app_id=fal-ai/foo,fal-ai/bar or array syntax:
            ?app_id=fal-ai/foo&app_id=fal-ai/bar
          name: app_id
          style: form
          explode: true
          in: query
        - schema:
            type: string
            description: Filter by revision
            example: rev_abc123
          required: false
          description: Filter by revision
          name: revision
          in: query
        - schema:
            type: string
            enum:
              - grpc-run
              - grpc-register
              - gateway
              - cron
            description: Filter by run source
            example: grpc-run
          required: false
          description: Filter by run source
          name: run_source
          in: query
        - schema:
            type:
              - boolean
              - 'null'
            default: false
            description: Include tracebacks
            example: false
          required: false
          description: Include tracebacks
          name: traceback
          in: query
        - schema:
            type: string
            description: Free-text search
            example: error
          required: false
          description: Free-text search
          name: search
          in: query
        - schema:
            type: string
            description: Minimum log level
            example: error
          required: false
          description: Minimum log level
          name: level
          in: query
        - schema:
            type: string
            description: Filter by job id
            example: job_123
          required: false
          description: Filter by job id
          name: job_id
          in: query
        - schema:
            type: string
            description: Filter by request id
            example: req_abc123
          required: false
          description: Filter by request id
          name: request_id
          in: query
      requestBody:
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  key:
                    type: string
                    description: Label key to filter
                  value:
                    anyOf:
                      - type: string
                      - type: array
                        items:
                          type: string
                    description: Filter value
                  condition_type:
                    type: string
                    enum:
                      - equals
                      - in
                      - not_equals
                      - not_in
                    description: Condition type for label filtering
                required:
                  - key
                  - value
                additionalProperties: false
                description: Filter for log labels
            examples:
              single:
                value:
                  - key: fal_job_id
                    value: job_123
                summary: Filter by a single label
      responses:
        '200':
          description: Logs history retrieved successfully
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
                        timestamp:
                          type: string
                          description: ISO timestamp of the log line
                        level:
                          type: string
                          description: Log level
                        message:
                          type: string
                          description: Log message
                        app:
                          type: string
                          description: App identifier
                        revision:
                          type: string
                          description: Revision identifier
                        labels:
                          type: object
                          additionalProperties:
                            type: string
                          description: Additional labels
                      required:
                        - timestamp
                        - level
                        - message
                        - app
                        - revision
                      additionalProperties: false
                      description: A single log entry
                    description: Array of log entries matching the query
                required:
                  - next_cursor
                  - has_more
                  - items
                description: Paginated logs response
              examples:
                success:
                  value:
                    items:
                      - timestamp: '2024-11-09T10:30:45.123Z'
                        level: info
                        message: Application started
                        app: my-app
                        revision: rev_abc123
                        labels:
                          fal_job_id: job_123
                    next_cursor: '2024-11-09T10:30:44.000Z'
                    has_more: true
                  summary: Paginated logs response
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