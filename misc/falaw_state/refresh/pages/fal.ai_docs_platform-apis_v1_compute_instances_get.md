> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Compute Instance

> Retrieves detailed information about a specific compute instance by its ID.

**Requirements:**
- Requires compute permissions (extra_permissions.compute = true)
- Authentication required via admin API key
- Instance must belong to the authenticated user's workspace

**Key Features:**
- Get current instance status and configuration
- Access instance IP address when available
- View region and sector placement
- Check creator information

**Common Use Cases:**
- Monitor specific instance status
- Retrieve connection details (IP address)
- Check instance readiness before use
- Audit instance configuration

See [fal.ai docs](https://docs.fal.ai/compute) for more details.



## OpenAPI

````yaml /api-reference/platform-apis/openapi/v1.json get /compute/instances/{id}
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
  /compute/instances/{id}:
    get:
      tags:
        - Compute
      summary: Get Compute Instance
      description: >-
        Retrieves detailed information about a specific compute instance by its
        ID.


        **Requirements:**

        - Requires compute permissions (extra_permissions.compute = true)

        - Authentication required via admin API key

        - Instance must belong to the authenticated user's workspace


        **Key Features:**

        - Get current instance status and configuration

        - Access instance IP address when available

        - View region and sector placement

        - Check creator information


        **Common Use Cases:**

        - Monitor specific instance status

        - Retrieve connection details (IP address)

        - Check instance readiness before use

        - Audit instance configuration


        See [fal.ai docs](https://docs.fal.ai/compute) for more details.
      operationId: getComputeInstance
      parameters:
        - schema:
            type: string
            minLength: 1
            description: Unique identifier for the compute instance
            example: inst_abc123xyz
          required: true
          description: Unique identifier for the compute instance
          name: id
          in: path
      responses:
        '200':
          description: Successfully retrieved compute instance details
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: Unique identifier for the compute instance
                    example: inst_abc123xyz
                  instance_type:
                    type: string
                    enum:
                      - gpu_8x_h100_sxm5
                      - gpu_1x_h100_sxm5
                    description: Type of compute instance (GPU configuration)
                    example: gpu_1x_h100_sxm5
                  region:
                    type: string
                    enum:
                      - us-west
                      - us-central
                      - us-east
                      - eu-north
                      - eu-west
                      - other
                    description: Geographical region where the instance is located
                    example: us-west
                  sector:
                    type: string
                    enum:
                      - sector_1
                      - sector_2
                      - sector_3
                    description: >-
                      Sector identifier for instance placement within the region
                      (if applicable)
                    example: sector_1
                  ip:
                    type: string
                    description: >-
                      IP address of the instance (available when instance is
                      ready)
                    example: 203.0.113.42
                  status:
                    type: string
                    enum:
                      - ready
                      - init
                      - pending
                      - provisioning
                      - stopped
                      - unknown
                    description: Current operational status of the instance
                    example: ready
                  creator_user_nickname:
                    type: string
                    description: Nickname of the user who created this instance
                    example: developer
                required:
                  - id
                  - instance_type
                  - region
                  - status
                description: >-
                  Compute instance details including configuration, location,
                  and status
              example:
                id: inst_abc123xyz
                instance_type: gpu_1x_h100_sxm5
                region: us-west
                sector: sector_1
                ip: 203.0.113.42
                status: ready
                creator_user_nickname: developer
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