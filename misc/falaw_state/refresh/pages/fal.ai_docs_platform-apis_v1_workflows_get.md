> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get workflow details

> 
Get detailed information about a specific workflow, including its full contents/definition.

**Authentication:** Required.

**Common Use Cases:**
- Load a workflow for editing
- View workflow configuration
- Export workflow definition
    



## OpenAPI

````yaml /api-reference/platform-apis/openapi/v1.json get /workflows/{username}/{workflow_name}
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
  /workflows/{username}/{workflow_name}:
    get:
      tags:
        - Workflows
      summary: Get workflow details
      description: >-

        Get detailed information about a specific workflow, including its full
        contents/definition.


        **Authentication:** Required.


        **Common Use Cases:**

        - Load a workflow for editing

        - View workflow configuration

        - Export workflow definition
            
      operationId: getWorkflow
      parameters:
        - schema:
            type: string
            description: The username of the workflow owner
            example: johndoe
          required: true
          description: The username of the workflow owner
          name: username
          in: path
        - schema:
            type: string
            description: The workflow name/slug
            example: my-image-workflow
          required: true
          description: The workflow name/slug
          name: workflow_name
          in: path
      responses:
        '200':
          description: Successfully retrieved workflow details
          content:
            application/json:
              schema:
                type: object
                properties:
                  workflow:
                    type: object
                    properties:
                      name:
                        type: string
                        description: Unique workflow name/slug within the user's namespace
                        example: my-image-workflow
                      title:
                        type: string
                        description: Human-readable workflow title
                        example: My Image Generation Workflow
                      user_nickname:
                        type: string
                        description: Display name/username of the owner
                        example: johndoe
                      created_at:
                        type: string
                        description: ISO8601 timestamp of workflow creation
                        example: '2024-01-15T10:30:00Z'
                      is_public:
                        type: boolean
                        description: Whether the workflow is publicly visible
                        example: true
                      contents:
                        type: object
                        additionalProperties: {}
                        description: The workflow definition/configuration object
                        example:
                          nodes:
                            node_a1b2c3:
                              id: node_a1b2c3
                              type: model
                              app: fal-ai/flux/dev
                              depends: []
                              input:
                                prompt: $input.prompt
                              metadata:
                                position:
                                  x: 300
                                  'y': 100
                            output:
                              id: output
                              type: output
                              depends:
                                - node_a1b2c3
                              fields:
                                image: $node_a1b2c3.images.0.url
                              metadata:
                                position:
                                  x: 600
                                  'y': 100
                    required:
                      - name
                      - title
                      - user_nickname
                      - created_at
                      - is_public
                      - contents
                    description: The workflow details
                    example:
                      name: my-image-workflow
                      title: My Image Generation Workflow
                      user_nickname: johndoe
                      created_at: '2024-01-15T10:30:00Z'
                      is_public: true
                      contents:
                        nodes:
                          node_a1b2c3:
                            id: node_a1b2c3
                            type: model
                            app: fal-ai/flux/dev
                            depends: []
                            input:
                              prompt: $input.prompt
                            metadata:
                              position:
                                x: 300
                                'y': 100
                          output:
                            id: output
                            type: output
                            depends:
                              - node_a1b2c3
                            fields:
                              image: $node_a1b2c3.images.0.url
                            metadata:
                              position:
                                x: 600
                                'y': 100
                required:
                  - workflow
                description: Response containing a single workflow's details
              example:
                workflow:
                  name: my-image-workflow
                  title: My Image Generation Workflow
                  user_nickname: johndoe
                  created_at: '2025-01-15T12:00:00Z'
                  is_public: false
                  contents:
                    nodes: []
                    edges: []
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