> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List files (directory)

> Lists files and folders within the specified directory path.



## OpenAPI

````yaml /api-reference/platform-apis/openapi/v1.json get /serverless/files/list/{dir}
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
  /serverless/files/list/{dir}:
    get:
      tags:
        - Serverless
        - Files
      summary: List files (directory)
      description: Lists files and folders within the specified directory path.
      operationId: serverlessListDirectory
      parameters:
        - schema:
            type: string
            description: Directory path to list
            example: datasets/images
          required: true
          description: Directory path to list
          name: dir
          in: path
      responses:
        '200':
          description: Successfully listed files
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    path:
                      type: string
                      description: Full file or folder path
                      example: datasets/images/cat.jpg
                    name:
                      type: string
                      description: Base name of the file or folder
                      example: cat.jpg
                    created_time:
                      type: string
                      format: date-time
                      description: Creation timestamp (UTC ISO 8601)
                      example: '2024-11-08T00:00:00.000Z'
                    updated_time:
                      type: string
                      format: date-time
                      description: Last update timestamp (UTC ISO 8601)
                      example: '2024-11-09T00:00:00.000Z'
                    is_file:
                      type: boolean
                      description: True if this item is a file, false if it is a folder
                      example: true
                    size:
                      type: number
                      description: File size in bytes (0 for folders)
                      example: 1250023
                    checksum_sha256:
                      type: string
                      description: Optional SHA256 checksum
                      example: >-
                        b1946ac92492d2347c6235b4d2611184d5c3f1f0f44aa7b27d3b1d5b0f5a6a11
                    checksum_md5:
                      type: string
                      description: Optional MD5 checksum
                      example: 9e107d9d372bb6826bd81d3542a419d6
                  required:
                    - path
                    - name
                    - created_time
                    - updated_time
                    - is_file
                    - size
                  additionalProperties: false
                  description: File or folder specification
                description: Array of files and folders for the requested directory
              examples:
                success:
                  value:
                    - path: datasets/images/cat.jpg
                      name: cat.jpg
                      created_time: '2024-11-08T00:00:00.000Z'
                      updated_time: '2024-11-09T00:00:00.000Z'
                      is_file: true
                      size: 1250023
                      checksum_sha256: >-
                        b1946ac92492d2347c6235b4d2611184d5c3f1f0f44aa7b27d3b1d5b0f5a6a11
                  summary: Directory listing
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