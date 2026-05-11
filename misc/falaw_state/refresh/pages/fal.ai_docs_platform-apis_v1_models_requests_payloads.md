> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete request payloads

> Deletes the IO payloads and associated CDN output files for a specific request.

**Important:**
- Only **output** CDN files are deleted (input files may be used by other requests)
- This action is irreversible
- Requires authentication with an admin API key

**What gets deleted:**
- Request input/output payload data
- CDN-hosted output files (images, videos, etc.)

**What is NOT deleted:**
- Input CDN files (may be referenced by other requests)

**Response:**
- Returns deletion status for each CDN file
- Each result includes the file link and any error that occurred

**Idempotency:**
- Optional Idempotency-Key header prevents duplicate deletions on retries
- Responses cached for 10 minutes per unique key

See [fal.ai docs](https://docs.fal.ai/model-apis/payloads) for more details about request payloads.



## OpenAPI

````yaml /api-reference/platform-apis/openapi/v1.json delete /models/requests/{request_id}/payloads
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
  /models/requests/{request_id}/payloads:
    delete:
      tags:
        - Models
        - Requests
      summary: Delete request payloads
      description: >-
        Deletes the IO payloads and associated CDN output files for a specific
        request.


        **Important:**

        - Only **output** CDN files are deleted (input files may be used by
        other requests)

        - This action is irreversible

        - Requires authentication with an admin API key


        **What gets deleted:**

        - Request input/output payload data

        - CDN-hosted output files (images, videos, etc.)


        **What is NOT deleted:**

        - Input CDN files (may be referenced by other requests)


        **Response:**

        - Returns deletion status for each CDN file

        - Each result includes the file link and any error that occurred


        **Idempotency:**

        - Optional Idempotency-Key header prevents duplicate deletions on
        retries

        - Responses cached for 10 minutes per unique key


        See [fal.ai docs](https://docs.fal.ai/model-apis/payloads) for more
        details about request payloads.
      operationId: deleteRequestPayloads
      parameters:
        - schema:
            type: string
            format: uuid
            description: Unique identifier for the request (UUID format)
            example: a1b2c3d4-e5f6-7890-abcd-ef1234567890
          required: true
          description: Unique identifier for the request (UUID format)
          name: request_id
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
        '200':
          description: Request payloads deleted successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  cdn_delete_results:
                    type: array
                    items:
                      type: object
                      properties:
                        link:
                          type: string
                          description: CDN URL of the file that was targeted for deletion
                          example: https://v3.fal.media/files/example/output.png
                        exception:
                          type:
                            - string
                            - 'null'
                          description: >-
                            Error message if deletion failed for this file, null
                            if successful
                          example: null
                      required:
                        - link
                        - exception
                      description: Result of deleting a single CDN file
                    description: >-
                      Array of deletion results for each CDN file associated
                      with the request output
                required:
                  - cdn_delete_results
                description: >-
                  Response containing the results of deleting request payloads
                  and CDN output files
              example:
                cdn_delete_results:
                  - link: https://v3.fal.media/files/abc123/output.png
                    exception: null
                  - link: https://v3.fal.media/files/def456/output.mp4
                    exception: null
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