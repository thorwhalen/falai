> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Florence 2 Large API

> API reference for Florence 2 Large. Florence-2 is an advanced vision foundation model that uses a prompt-based approach to handle a wide range of vision and vision-language tasks

<Tabs>
  <Tab title="Object Detection">
    **Endpoint:** `POST https://fal.run/fal-ai/florence-2-large/object-detection`
    **Endpoint ID:** `fal-ai/florence-2-large/object-detection`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/florence-2-large/object-detection/playground">
      Run this model interactively with your own prompts.
    </Card>

    ### Quick Start

    <CodeGroup>
      ```python title="Python" theme={null}
      import fal_client

      def on_queue_update(update):
          if isinstance(update, fal_client.InProgress):
              for log in update.logs:
                 print(log["message"])

      result = fal_client.subscribe(
          "fal-ai/florence-2-large/object-detection",
          arguments={
              "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/florence-2-large/object-detection", {
        input: {
            image_url: "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
          },
        logs: true,
        onQueueUpdate: (update) => {
          if (update.status === "IN_PROGRESS") {
            update.logs.map((log) => log.message).forEach(console.log);
          }
        },
      });
      console.log(result.data);
      console.log(result.requestId);
      ```

      ```bash title="cURL" theme={null}
      curl --request POST \
        --url https://fal.run/fal-ai/florence-2-large/object-detection \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The URL of the image to be processed.
    </ParamField>

    ### Output Schema

    <ParamField body="results" type="BoundingBoxes" required>
      Results from the model
    </ParamField>

    <ParamField body="image" type="Image">
      Processed image
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "results": {
        "bboxes": [
          {
            "label": ""
          }
        ]
      }
    }
    ```
  </Tab>

  <Tab title="Open Vocabulary Detection">
    **Endpoint:** `POST https://fal.run/fal-ai/florence-2-large/open-vocabulary-detection`
    **Endpoint ID:** `fal-ai/florence-2-large/open-vocabulary-detection`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/florence-2-large/open-vocabulary-detection/playground">
      Run this model interactively with your own prompts.
    </Card>

    ### Quick Start

    <CodeGroup>
      ```python title="Python" theme={null}
      import fal_client

      def on_queue_update(update):
          if isinstance(update, fal_client.InProgress):
              for log in update.logs:
                 print(log["message"])

      result = fal_client.subscribe(
          "fal-ai/florence-2-large/open-vocabulary-detection",
          arguments={
              "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
              "text_input": ""
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/florence-2-large/open-vocabulary-detection", {
        input: {
            image_url: "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
            text_input: ""
          },
        logs: true,
        onQueueUpdate: (update) => {
          if (update.status === "IN_PROGRESS") {
            update.logs.map((log) => log.message).forEach(console.log);
          }
        },
      });
      console.log(result.data);
      console.log(result.requestId);
      ```

      ```bash title="cURL" theme={null}
      curl --request POST \
        --url https://fal.run/fal-ai/florence-2-large/open-vocabulary-detection \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
        "text_input": ""
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The URL of the image to be processed.
    </ParamField>

    <ParamField body="text_input" type="string" required>
      Text input for the task
    </ParamField>

    ### Output Schema

    <ParamField body="results" type="BoundingBoxes" required>
      Results from the model
    </ParamField>

    <ParamField body="image" type="Image">
      Processed image
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
      "text_input": ""
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "results": {
        "bboxes": [
          {
            "label": ""
          }
        ]
      }
    }
    ```
  </Tab>

  <Tab title="Ocr With Region">
    **Endpoint:** `POST https://fal.run/fal-ai/florence-2-large/ocr-with-region`
    **Endpoint ID:** `fal-ai/florence-2-large/ocr-with-region`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/florence-2-large/ocr-with-region/playground">
      Run this model interactively with your own prompts.
    </Card>

    ### Quick Start

    <CodeGroup>
      ```python title="Python" theme={null}
      import fal_client

      def on_queue_update(update):
          if isinstance(update, fal_client.InProgress):
              for log in update.logs:
                 print(log["message"])

      result = fal_client.subscribe(
          "fal-ai/florence-2-large/ocr-with-region",
          arguments={
              "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/florence-2-large/ocr-with-region", {
        input: {
            image_url: "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
          },
        logs: true,
        onQueueUpdate: (update) => {
          if (update.status === "IN_PROGRESS") {
            update.logs.map((log) => log.message).forEach(console.log);
          }
        },
      });
      console.log(result.data);
      console.log(result.requestId);
      ```

      ```bash title="cURL" theme={null}
      curl --request POST \
        --url https://fal.run/fal-ai/florence-2-large/ocr-with-region \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The URL of the image to be processed.
    </ParamField>

    ### Output Schema

    <ParamField body="results" type="OCRBoundingBox" required>
      Results from the model
    </ParamField>

    <ParamField body="image" type="Image">
      Processed image
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "results": {
        "quad_boxes": [
          {
            "label": ""
          }
        ]
      }
    }
    ```
  </Tab>

  <Tab title="Caption To Phrase Grounding">
    **Endpoint:** `POST https://fal.run/fal-ai/florence-2-large/caption-to-phrase-grounding`
    **Endpoint ID:** `fal-ai/florence-2-large/caption-to-phrase-grounding`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/florence-2-large/caption-to-phrase-grounding/playground">
      Run this model interactively with your own prompts.
    </Card>

    ### Quick Start

    <CodeGroup>
      ```python title="Python" theme={null}
      import fal_client

      def on_queue_update(update):
          if isinstance(update, fal_client.InProgress):
              for log in update.logs:
                 print(log["message"])

      result = fal_client.subscribe(
          "fal-ai/florence-2-large/caption-to-phrase-grounding",
          arguments={
              "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
              "text_input": ""
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/florence-2-large/caption-to-phrase-grounding", {
        input: {
            image_url: "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
            text_input: ""
          },
        logs: true,
        onQueueUpdate: (update) => {
          if (update.status === "IN_PROGRESS") {
            update.logs.map((log) => log.message).forEach(console.log);
          }
        },
      });
      console.log(result.data);
      console.log(result.requestId);
      ```

      ```bash title="cURL" theme={null}
      curl --request POST \
        --url https://fal.run/fal-ai/florence-2-large/caption-to-phrase-grounding \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
        "text_input": ""
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The URL of the image to be processed.
    </ParamField>

    <ParamField body="text_input" type="string" required>
      Text input for the task
    </ParamField>

    ### Output Schema

    <ParamField body="results" type="BoundingBoxes" required>
      Results from the model
    </ParamField>

    <ParamField body="image" type="Image">
      Processed image
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
      "text_input": ""
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "results": {
        "bboxes": [
          {
            "label": ""
          }
        ]
      }
    }
    ```
  </Tab>

  <Tab title="Referring Expression Segmentation">
    **Endpoint:** `POST https://fal.run/fal-ai/florence-2-large/referring-expression-segmentation`
    **Endpoint ID:** `fal-ai/florence-2-large/referring-expression-segmentation`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/florence-2-large/referring-expression-segmentation/playground">
      Run this model interactively with your own prompts.
    </Card>

    ### Quick Start

    <CodeGroup>
      ```python title="Python" theme={null}
      import fal_client

      def on_queue_update(update):
          if isinstance(update, fal_client.InProgress):
              for log in update.logs:
                 print(log["message"])

      result = fal_client.subscribe(
          "fal-ai/florence-2-large/referring-expression-segmentation",
          arguments={
              "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
              "text_input": ""
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/florence-2-large/referring-expression-segmentation", {
        input: {
            image_url: "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
            text_input: ""
          },
        logs: true,
        onQueueUpdate: (update) => {
          if (update.status === "IN_PROGRESS") {
            update.logs.map((log) => log.message).forEach(console.log);
          }
        },
      });
      console.log(result.data);
      console.log(result.requestId);
      ```

      ```bash title="cURL" theme={null}
      curl --request POST \
        --url https://fal.run/fal-ai/florence-2-large/referring-expression-segmentation \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
        "text_input": ""
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The URL of the image to be processed.
    </ParamField>

    <ParamField body="text_input" type="string" required>
      Text input for the task
    </ParamField>

    ### Output Schema

    <ParamField body="results" type="PolygonOutput" required>
      Results from the model
    </ParamField>

    <ParamField body="image" type="Image">
      Processed image
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
      "text_input": ""
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "results": {
        "polygons": [
          {
            "label": ""
          }
        ]
      }
    }
    ```
  </Tab>

  <Tab title="Dense Region Caption">
    **Endpoint:** `POST https://fal.run/fal-ai/florence-2-large/dense-region-caption`
    **Endpoint ID:** `fal-ai/florence-2-large/dense-region-caption`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/florence-2-large/dense-region-caption/playground">
      Run this model interactively with your own prompts.
    </Card>

    ### Quick Start

    <CodeGroup>
      ```python title="Python" theme={null}
      import fal_client

      def on_queue_update(update):
          if isinstance(update, fal_client.InProgress):
              for log in update.logs:
                 print(log["message"])

      result = fal_client.subscribe(
          "fal-ai/florence-2-large/dense-region-caption",
          arguments={
              "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/florence-2-large/dense-region-caption", {
        input: {
            image_url: "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
          },
        logs: true,
        onQueueUpdate: (update) => {
          if (update.status === "IN_PROGRESS") {
            update.logs.map((log) => log.message).forEach(console.log);
          }
        },
      });
      console.log(result.data);
      console.log(result.requestId);
      ```

      ```bash title="cURL" theme={null}
      curl --request POST \
        --url https://fal.run/fal-ai/florence-2-large/dense-region-caption \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The URL of the image to be processed.
    </ParamField>

    ### Output Schema

    <ParamField body="results" type="BoundingBoxes" required>
      Results from the model
    </ParamField>

    <ParamField body="image" type="Image">
      Processed image
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "results": {
        "bboxes": [
          {
            "label": ""
          }
        ]
      }
    }
    ```
  </Tab>

  <Tab title="Region To Segmentation">
    **Endpoint:** `POST https://fal.run/fal-ai/florence-2-large/region-to-segmentation`
    **Endpoint ID:** `fal-ai/florence-2-large/region-to-segmentation`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/florence-2-large/region-to-segmentation/playground">
      Run this model interactively with your own prompts.
    </Card>

    ### Quick Start

    <CodeGroup>
      ```python title="Python" theme={null}
      import fal_client

      def on_queue_update(update):
          if isinstance(update, fal_client.InProgress):
              for log in update.logs:
                 print(log["message"])

      result = fal_client.subscribe(
          "fal-ai/florence-2-large/region-to-segmentation",
          arguments={
              "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
              "region": {
                  "x1": 100,
                  "x2": 200,
                  "y1": 100,
                  "y2": 200
              }
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/florence-2-large/region-to-segmentation", {
        input: {
            image_url: "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
            region: {
              x1: 100,
              x2: 200,
              y1: 100,
              y2: 200
            }
          },
        logs: true,
        onQueueUpdate: (update) => {
          if (update.status === "IN_PROGRESS") {
            update.logs.map((log) => log.message).forEach(console.log);
          }
        },
      });
      console.log(result.data);
      console.log(result.requestId);
      ```

      ```bash title="cURL" theme={null}
      curl --request POST \
        --url https://fal.run/fal-ai/florence-2-large/region-to-segmentation \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
        "region": {
          "x1": 100,
          "x2": 200,
          "y1": 100,
          "y2": 200
        }
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The URL of the image to be processed.
    </ParamField>

    <ParamField body="region" type="Region" required>
      The user input coordinates
    </ParamField>

    ### Output Schema

    <ParamField body="results" type="PolygonOutput" required>
      Results from the model
    </ParamField>

    <ParamField body="image" type="Image">
      Processed image
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
      "region": {
        "x1": 100,
        "x2": 200,
        "y1": 100,
        "y2": 200
      }
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "results": {
        "polygons": [
          {
            "label": ""
          }
        ]
      }
    }
    ```
  </Tab>

  <Tab title="Region Proposal">
    **Endpoint:** `POST https://fal.run/fal-ai/florence-2-large/region-proposal`
    **Endpoint ID:** `fal-ai/florence-2-large/region-proposal`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/florence-2-large/region-proposal/playground">
      Run this model interactively with your own prompts.
    </Card>

    ### Quick Start

    <CodeGroup>
      ```python title="Python" theme={null}
      import fal_client

      def on_queue_update(update):
          if isinstance(update, fal_client.InProgress):
              for log in update.logs:
                 print(log["message"])

      result = fal_client.subscribe(
          "fal-ai/florence-2-large/region-proposal",
          arguments={
              "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
          },
          with_logs=True,
          on_queue_update=on_queue_update,
      )
      print(result)
      ```

      ```javascript title="JavaScript" theme={null}
      import { fal } from "@fal-ai/client";

      const result = await fal.subscribe("fal-ai/florence-2-large/region-proposal", {
        input: {
            image_url: "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
          },
        logs: true,
        onQueueUpdate: (update) => {
          if (update.status === "IN_PROGRESS") {
            update.logs.map((log) => log.message).forEach(console.log);
          }
        },
      });
      console.log(result.data);
      console.log(result.requestId);
      ```

      ```bash title="cURL" theme={null}
      curl --request POST \
        --url https://fal.run/fal-ai/florence-2-large/region-proposal \
        --header "Authorization: Key $FAL_KEY" \
        --header "Content-Type: application/json" \
        --data '{
        "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
      }'
      ```
    </CodeGroup>

    ### Input Schema

    <ParamField body="image_url" type="string" required>
      The URL of the image to be processed.
    </ParamField>

    ### Output Schema

    <ParamField body="results" type="BoundingBoxes" required>
      Results from the model
    </ParamField>

    <ParamField body="image" type="Image">
      Processed image
    </ParamField>

    ### Input Example

    ```json theme={null}
    {
      "image_url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
    }
    ```

    ### Output Example

    ```json theme={null}
    {
      "results": {
        "bboxes": [
          {
            "label": ""
          }
        ]
      }
    }
    ```
  </Tab>
</Tabs>

## Related

* [Florence-2 Large](/model-api-reference/vision-api/florence-2-large) — Vision
* [Florence-2 Large](/model-api-reference/image-generation-api/florence-2-large) — Image Generation
