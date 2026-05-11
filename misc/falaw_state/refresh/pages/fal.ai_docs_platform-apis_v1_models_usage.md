> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Usage

> 
Returns paginated usage records for your workspace with filters for endpoint,
user, date range, and auth method. Each item includes the billed unit
quantity and unit price used to compute cost.

**Key Features:**
- Usage data for all endpoints or filtered by specific endpoint(s)
- Flexible date range filtering
- User-specific usage tracking
- Detailed usage line items with unit quantity and price
- Paginated results for large datasets

**Common Use Cases:**
- Generate usage reports for all endpoints or specific models
- Track usage patterns
- Monitor endpoint usage across different auth methods
- Build usage dashboards and visualizations

See [fal.ai docs](https://docs.fal.ai/model-apis/faq) for more details.
    



## OpenAPI

````yaml /api-reference/platform-apis/openapi/v1.json get /models/usage
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
  /models/usage:
    get:
      tags:
        - Models
        - Usage
      summary: Usage
      description: >-

        Returns paginated usage records for your workspace with filters for
        endpoint,

        user, date range, and auth method. Each item includes the billed unit

        quantity and unit price used to compute cost.


        **Key Features:**

        - Usage data for all endpoints or filtered by specific endpoint(s)

        - Flexible date range filtering

        - User-specific usage tracking

        - Detailed usage line items with unit quantity and price

        - Paginated results for large datasets


        **Common Use Cases:**

        - Generate usage reports for all endpoints or specific models

        - Track usage patterns

        - Monitor endpoint usage across different auth methods

        - Build usage dashboards and visualizations


        See [fal.ai docs](https://docs.fal.ai/model-apis/faq) for more details.
            
      operationId: getUsage
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
            default: UTC
            description: >-
              Timezone for date aggregation and boundaries. All timestamps in
              responses are in UTC, but this controls how dates are bucketed.
            example: UTC
          required: false
          description: >-
            Timezone for date aggregation and boundaries. All timestamps in
            responses are in UTC, but this controls how dates are bucketed.
          name: timezone
          in: query
        - schema:
            type: string
            enum:
              - minute
              - hour
              - day
              - week
              - month
            description: >-
              Aggregation timeframe for timeseries data (auto-detected from date
              range if not specified). Auto-detection uses: minute (<2h), hour
              (<2d), day (<64d), week (<183d), month (>=183d).
            example: day
          required: false
          description: >-
            Aggregation timeframe for timeseries data (auto-detected from date
            range if not specified). Auto-detection uses: minute (<2h), hour
            (<2d), day (<64d), week (<183d), month (>=183d).
          name: timeframe
          in: query
        - schema:
            type: string
            enum:
              - 'true'
              - 'false'
            default: 'true'
            description: >-
              Whether to adjust start/end dates to align with timeframe
              boundaries and use exclusive end. Defaults to true. When true,
              dates are aligned to the start of the timeframe period (e.g.,
              start of day) and end is made exclusive (e.g., start of next day).
              When false, uses exact dates provided.
            example: 'true'
          required: false
          description: >-
            Whether to adjust start/end dates to align with timeframe boundaries
            and use exclusive end. Defaults to true. When true, dates are
            aligned to the start of the timeframe period (e.g., start of day)
            and end is made exclusive (e.g., start of next day). When false,
            uses exact dates provided.
          name: bound_to_timeframe
          in: query
        - schema:
            anyOf:
              - type: string
              - type: array
                items:
                  type: string
            description: >-
              Filter by specific endpoint ID(s). Accepts 1-50 endpoint IDs.
              Supports comma-separated values: ?endpoint_id=model1,model2 or
              array syntax: ?endpoint_id=model1&endpoint_id=model2
            example:
              - fal-ai/flux/dev
          required: false
          description: >-
            Filter by specific endpoint ID(s). Accepts 1-50 endpoint IDs.
            Supports comma-separated values: ?endpoint_id=model1,model2 or array
            syntax: ?endpoint_id=model1&endpoint_id=model2
          name: endpoint_id
          style: form
          explode: true
          in: query
        - schema:
            anyOf:
              - type: string
              - type: array
                items:
                  type: string
            default:
              - time_series
            description: >-
              Data to include in the response. Use 'time_series' for
              time-bucketed data, 'summary' for aggregate statistics, and
              'auth_method' to include authentication method information
              (formatted with user key aliases). At least one of 'time_series'
              or 'summary' is required.
            example:
              - time_series
              - auth_method
          required: false
          description: >-
            Data to include in the response. Use 'time_series' for time-bucketed
            data, 'summary' for aggregate statistics, and 'auth_method' to
            include authentication method information (formatted with user key
            aliases). At least one of 'time_series' or 'summary' is required.
          name: expand
          style: form
          explode: true
          in: query
      responses:
        '200':
          description: Usage data retrieved successfully
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
                  time_series:
                    type: array
                    items:
                      type: object
                      properties:
                        bucket:
                          type: string
                          description: >-
                            Time bucket timestamp in user's timezone with offset
                            (ISO8601 datetime)
                        results:
                          type: array
                          items:
                            type: object
                            properties:
                              endpoint_id:
                                type: string
                                description: >-
                                  Endpoint identifier that was used (e.g.,
                                  'fal-ai/flux/dev')
                              unit:
                                type: string
                                description: >-
                                  The billing unit (e.g., 'image', 'video', or a
                                  GPU/compute unit for some models)
                              quantity:
                                type: number
                                minimum: 0
                                description: >-
                                  Quantity of usage in the specified billing
                                  unit
                              unit_price:
                                type: number
                                minimum: 0
                                description: >-
                                  Unit price used to compute charges for this
                                  line item
                              cost:
                                type: number
                                minimum: 0
                                description: Computed cost (quantity × unit_price)
                              currency:
                                type: string
                                minLength: 3
                                maxLength: 3
                                description: >-
                                  Three-letter currency code (ISO 4217, e.g.,
                                  'USD')
                              auth_method:
                                type: string
                                description: >-
                                  Authentication method label (e.g., 'Key 1',
                                  'Key 2', 'User token'). Only populated when
                                  'auth_method' is included in expand parameter.
                            required:
                              - endpoint_id
                              - unit
                              - quantity
                              - unit_price
                              - cost
                              - currency
                            description: Usage line item with billing details
                          description: Usage records for this time bucket
                      required:
                        - bucket
                        - results
                      description: Time bucket with grouped usage records
                    description: >-
                      Time series usage data grouped by time bucket (when expand
                      includes 'time_series'). Each bucket contains all usage
                      records for that time period.
                  summary:
                    type: array
                    items:
                      type: object
                      properties:
                        endpoint_id:
                          type: string
                          description: >-
                            Endpoint identifier that was used (e.g.,
                            'fal-ai/flux/dev')
                        unit:
                          type: string
                          description: >-
                            The billing unit (e.g., 'image', 'video', or a
                            GPU/compute unit for some models)
                        quantity:
                          type: number
                          minimum: 0
                          description: Quantity of usage in the specified billing unit
                        unit_price:
                          type: number
                          minimum: 0
                          description: >-
                            Unit price used to compute charges for this line
                            item
                        cost:
                          type: number
                          minimum: 0
                          description: Computed cost (quantity × unit_price)
                        currency:
                          type: string
                          minLength: 3
                          maxLength: 3
                          description: Three-letter currency code (ISO 4217, e.g., 'USD')
                        auth_method:
                          type: string
                          description: >-
                            Authentication method label (e.g., 'Key 1', 'Key 2',
                            'User token'). Only populated when 'auth_method' is
                            included in expand parameter.
                      required:
                        - endpoint_id
                        - unit
                        - quantity
                        - unit_price
                        - cost
                        - currency
                      description: Aggregate usage statistics for the entire date range
                    description: Aggregate statistics (when expand includes 'summary')
                required:
                  - next_cursor
                  - has_more
                description: Response containing usage data with pagination support
              example:
                time_series:
                  - bucket: '2025-01-15T00:00:00-05:00'
                    results:
                      - endpoint_id: fal-ai/flux/dev
                        unit: image
                        quantity: 4
                        unit_price: 0.1
                        cost: 0.4
                        currency: USD
                        auth_method: Production Key
                next_cursor: null
                has_more: false
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