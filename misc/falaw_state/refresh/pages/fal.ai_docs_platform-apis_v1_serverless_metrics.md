> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Metrics

> 
Returns Prometheus-compatible metrics in text format for integration into your
observability stack

**Authentication:** Required - Uses API key authentication

**Format:** Returns text/plain in Prometheus exposition format

**Common Use Cases:**
- Export app stats to your observability provider (grafana, datadog etc)
- Track runner health and performance
- Set up alerts and monitoring

See [Prometheus documentation](https://prometheus.io/docs/instrumenting/exposition_formats/) for format details.
    



## OpenAPI

````yaml /api-reference/platform-apis/openapi/v1.json get /serverless/metrics
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
  /serverless/metrics:
    get:
      tags:
        - Serverless
        - Metrics
        - Observability
      summary: Metrics
      description: >-

        Returns Prometheus-compatible metrics in text format for integration
        into your

        observability stack


        **Authentication:** Required - Uses API key authentication


        **Format:** Returns text/plain in Prometheus exposition format


        **Common Use Cases:**

        - Export app stats to your observability provider (grafana, datadog etc)

        - Track runner health and performance

        - Set up alerts and monitoring


        See [Prometheus
        documentation](https://prometheus.io/docs/instrumenting/exposition_formats/)
        for format details.
            
      operationId: serverlessGetMetrics
      responses:
        '200':
          description: Prometheus-compatible metrics retrieved successfully
          content:
            text/plain:
              schema:
                type: string
                description: Prometheus-compatible metrics in text format
                example: |-
                  # HELP fal_app_queue_size Current size of the fal app queue
                  # TYPE fal_app_queue_size gauge
                  fal_requests_total{application="my/app"} 10
              example: >-
                # HELP fal_app_runners Number of fal app runners

                # TYPE fal_app_runners gauge

                fal_app_runners{application="my/app",machine_type="NVIDIA
                B200",state="running"} 21

                # HELP fal_app_queue_size Current size of the fal app queue

                # TYPE fal_app_queue_size gauge

                fal_app_queue_size{application="my/app"} 7

                # HELP fal_app_concurrent_requests Current number of concurrent
                requests being processed

                # TYPE fal_app_concurrent_requests gauge

                fal_app_concurrent_requests{application="my/app"} 3

                # HELP fal_app_requests_completed Number of requests completed
                in the last minute

                # TYPE fal_app_requests_completed gauge

                fal_app_requests_completed{application="my/app",method="POST",status="200"}
                18

                # HELP fal_app_requests_received Number of requests received in
                the last minute

                # TYPE fal_app_requests_received gauge

                fal_app_requests_received{application="my/app",method="POST"} 24

                # HELP fal_app_request_latency Number of requests completed,
                bucketed by latency in seconds

                # TYPE fal_app_request_latency gauge

                fal_app_request_latency{application="my/app",le="1.0"} 5

                fal_app_request_latency{application="my/app",le="+Inf"} 24
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