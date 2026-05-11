> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Analytics

> 
Time-bucketed metrics for your serverless app endpoints, including request counts,
success/error rates, and latency percentiles across all inbound traffic.
`prepare_duration` reflects queue/prepare time before execution;
`duration` is request execution time.

This endpoint shows all inbound requests to endpoints you own — not just
your own calls. This is ideal for monitoring your deployed apps, tracking
SLAs, and exporting data to tools like BigQuery or Grafana. You must own
all requested endpoints; returns 403 otherwise.

> **Note:** This endpoint returns analytics across **all callers** of your endpoints.
> If you only need analytics for requests **you made** to a model endpoint,
> use [`GET /v1/models/analytics`](/platform-apis/v1/models/analytics) instead.

**Metric Selection:**
You must specify which metrics to include using the `expand` query
parameter. Only requested metrics will be populated in the response,
allowing you to optimize query performance and data transfer.

**Available Metrics:**
- `request_count`: Total number of requests in the time bucket
- `success_count`: Number of successful requests (2xx responses)
- `user_error_count`: Number of user errors (4xx responses)
- `error_count`: Number of server errors (5xx responses)
- `p50_prepare_duration`: 50th percentile queue/prepare time
- `p75_prepare_duration`: 75th percentile queue/prepare time
- `p90_prepare_duration`: 90th percentile queue/prepare time
- `p50_duration`: 50th percentile request execution duration
- `p75_duration`: 75th percentile request execution duration
- `p90_duration`: 90th percentile request execution duration

**Key Features:**
- See all traffic to your apps across all callers
- Selective metric inclusion via expand parameter
- Performance metrics (latency percentiles, duration stats)
- Reliability metrics (success/error rates, request counts)
- Time-bucketed data for trend analysis
- Flexible date range and timeframe options

**Common Use Cases:**
- Monitor your serverless app performance and reliability
- Export analytics to your own observability tools
- Analyze latency trends across all callers
- Track error rates and SLA compliance
    



## OpenAPI

````yaml /api-reference/platform-apis/openapi/v1.json get /serverless/analytics
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
  /serverless/analytics:
    get:
      tags:
        - Serverless
        - Analytics
      summary: Analytics
      description: >-

        Time-bucketed metrics for your serverless app endpoints, including
        request counts,

        success/error rates, and latency percentiles across all inbound traffic.

        `prepare_duration` reflects queue/prepare time before execution;

        `duration` is request execution time.


        This endpoint shows all inbound requests to endpoints you own — not just

        your own calls. This is ideal for monitoring your deployed apps,
        tracking

        SLAs, and exporting data to tools like BigQuery or Grafana. You must own

        all requested endpoints; returns 403 otherwise.


        > **Note:** This endpoint returns analytics across **all callers** of
        your endpoints.

        > If you only need analytics for requests **you made** to a model
        endpoint,

        > use [`GET /v1/models/analytics`](/platform-apis/v1/models/analytics)
        instead.


        **Metric Selection:**

        You must specify which metrics to include using the `expand` query

        parameter. Only requested metrics will be populated in the response,

        allowing you to optimize query performance and data transfer.


        **Available Metrics:**

        - `request_count`: Total number of requests in the time bucket

        - `success_count`: Number of successful requests (2xx responses)

        - `user_error_count`: Number of user errors (4xx responses)

        - `error_count`: Number of server errors (5xx responses)

        - `p50_prepare_duration`: 50th percentile queue/prepare time

        - `p75_prepare_duration`: 75th percentile queue/prepare time

        - `p90_prepare_duration`: 90th percentile queue/prepare time

        - `p50_duration`: 50th percentile request execution duration

        - `p75_duration`: 75th percentile request execution duration

        - `p90_duration`: 90th percentile request execution duration


        **Key Features:**

        - See all traffic to your apps across all callers

        - Selective metric inclusion via expand parameter

        - Performance metrics (latency percentiles, duration stats)

        - Reliability metrics (success/error rates, request counts)

        - Time-bucketed data for trend analysis

        - Flexible date range and timeframe options


        **Common Use Cases:**

        - Monitor your serverless app performance and reliability

        - Export analytics to your own observability tools

        - Analyze latency trends across all callers

        - Track error rates and SLA compliance
            
      operationId: serverlessGetAnalytics
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
          required: true
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
              - request_count
            description: >-
              Data and metrics to include in the response. Use 'time_series' for
              time-bucketed data, metric names for specific metrics in time
              series, and 'summary' for aggregate statistics. At least one of
              'time_series' or 'summary' and at least one metric are required.
            example:
              - request_count
              - success_count
          required: false
          description: >-
            Data and metrics to include in the response. Use 'time_series' for
            time-bucketed data, metric names for specific metrics in time
            series, and 'summary' for aggregate statistics. At least one of
            'time_series' or 'summary' and at least one metric are required.
          name: expand
          style: form
          explode: true
          in: query
      responses:
        '200':
          description: Analytics data retrieved successfully
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
                                description: Endpoint identifier for these statistics
                              request_count:
                                type: integer
                                minimum: 0
                                description: Total number of requests
                              success_count:
                                type: integer
                                minimum: 0
                                description: Number of successful requests (2xx responses)
                              user_error_count:
                                type: integer
                                minimum: 0
                                description: Number of user errors (4xx responses)
                              error_count:
                                type: integer
                                minimum: 0
                                description: Number of server errors (5xx responses)
                              p50_prepare_duration:
                                type: number
                                minimum: 0
                                description: >-
                                  50th percentile queue/prepare time before
                                  execution in seconds
                              p75_prepare_duration:
                                type: number
                                minimum: 0
                                description: >-
                                  75th percentile queue/prepare time before
                                  execution in seconds
                              p90_prepare_duration:
                                type: number
                                minimum: 0
                                description: >-
                                  90th percentile queue/prepare time before
                                  execution in seconds
                              p50_duration:
                                type: number
                                minimum: 0
                                description: >-
                                  50th percentile request execution duration in
                                  seconds
                              p75_duration:
                                type: number
                                minimum: 0
                                description: >-
                                  75th percentile request execution duration in
                                  seconds
                              p90_duration:
                                type: number
                                minimum: 0
                                description: >-
                                  90th percentile request execution duration in
                                  seconds
                            required:
                              - endpoint_id
                            description: >-
                              Performance and reliability analytics. Only
                              requested metrics (via expand parameter) will be
                              present in the response. 'prepare_duration'
                              reflects queue/prepare time before execution;
                              'duration' is request execution time.
                          description: Analytics records for this time bucket
                      required:
                        - bucket
                        - results
                      description: Time bucket with grouped analytics records
                    description: >-
                      Time series analytics data grouped by time bucket (when
                      expand includes 'time_series'). Each bucket contains all
                      analytics records for that time period.
                  summary:
                    type: array
                    items:
                      type: object
                      properties:
                        endpoint_id:
                          type: string
                          description: Endpoint identifier for these statistics
                        request_count:
                          type: integer
                          minimum: 0
                          description: Total number of requests
                        success_count:
                          type: integer
                          minimum: 0
                          description: Number of successful requests (2xx responses)
                        user_error_count:
                          type: integer
                          minimum: 0
                          description: Number of user errors (4xx responses)
                        error_count:
                          type: integer
                          minimum: 0
                          description: Number of server errors (5xx responses)
                        p50_prepare_duration:
                          type: number
                          minimum: 0
                          description: >-
                            50th percentile queue/prepare time before execution
                            in seconds
                        p75_prepare_duration:
                          type: number
                          minimum: 0
                          description: >-
                            75th percentile queue/prepare time before execution
                            in seconds
                        p90_prepare_duration:
                          type: number
                          minimum: 0
                          description: >-
                            90th percentile queue/prepare time before execution
                            in seconds
                        p50_duration:
                          type: number
                          minimum: 0
                          description: >-
                            50th percentile request execution duration in
                            seconds
                        p75_duration:
                          type: number
                          minimum: 0
                          description: >-
                            75th percentile request execution duration in
                            seconds
                        p90_duration:
                          type: number
                          minimum: 0
                          description: >-
                            90th percentile request execution duration in
                            seconds
                      required:
                        - endpoint_id
                      description: >-
                        Aggregate performance statistics for the entire date
                        range
                    description: Aggregate statistics (when expand includes 'summary')
                required:
                  - next_cursor
                  - has_more
                description: >-
                  Response containing performance analytics with pagination
                  support
              example:
                time_series:
                  - bucket: '2025-01-15T12:00:00-05:00'
                    results:
                      - endpoint_id: your-username/your-app
                        request_count: 1500
                        success_count: 1450
                        p50_duration: 2.5
                        p90_duration: 4.8
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