> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Florence 2 Large API

> API reference for Florence 2 Large. Florence-2 is an advanced vision foundation model that uses a prompt-based approach to handle a wide range of vision and vision-language tasks

<Tabs>
  <Tab title="More Detailed Caption">
    **Endpoint:** `POST https://fal.run/fal-ai/florence-2-large/more-detailed-caption`
    **Endpoint ID:** `fal-ai/florence-2-large/more-detailed-caption`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/florence-2-large/more-detailed-caption/playground">
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
          "fal-ai/florence-2-large/more-detailed-caption",
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

      const result = await fal.subscribe("fal-ai/florence-2-large/more-detailed-caption", {
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
        --url https://fal.run/fal-ai/florence-2-large/more-detailed-caption \
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

    <ParamField body="results" type="string" required>
      Results from the model
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
      "results": ""
    }
    ```
  </Tab>

  <Tab title="Detailed Caption">
    **Endpoint:** `POST https://fal.run/fal-ai/florence-2-large/detailed-caption`
    **Endpoint ID:** `fal-ai/florence-2-large/detailed-caption`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/florence-2-large/detailed-caption/playground">
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
          "fal-ai/florence-2-large/detailed-caption",
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

      const result = await fal.subscribe("fal-ai/florence-2-large/detailed-caption", {
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
        --url https://fal.run/fal-ai/florence-2-large/detailed-caption \
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

    <ParamField body="results" type="string" required>
      Results from the model
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
      "results": ""
    }
    ```
  </Tab>

  <Tab title="Caption">
    **Endpoint:** `POST https://fal.run/fal-ai/florence-2-large/caption`
    **Endpoint ID:** `fal-ai/florence-2-large/caption`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/florence-2-large/caption/playground">
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
          "fal-ai/florence-2-large/caption",
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

      const result = await fal.subscribe("fal-ai/florence-2-large/caption", {
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
        --url https://fal.run/fal-ai/florence-2-large/caption \
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

    <ParamField body="results" type="string" required>
      Results from the model
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
      "results": ""
    }
    ```
  </Tab>

  <Tab title="Ocr">
    **Endpoint:** `POST https://fal.run/fal-ai/florence-2-large/ocr`
    **Endpoint ID:** `fal-ai/florence-2-large/ocr`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/florence-2-large/ocr/playground">
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
          "fal-ai/florence-2-large/ocr",
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

      const result = await fal.subscribe("fal-ai/florence-2-large/ocr", {
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
        --url https://fal.run/fal-ai/florence-2-large/ocr \
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

    <ParamField body="results" type="string" required>
      Results from the model
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
      "results": ""
    }
    ```
  </Tab>

  <Tab title="Region To Description">
    **Endpoint:** `POST https://fal.run/fal-ai/florence-2-large/region-to-description`
    **Endpoint ID:** `fal-ai/florence-2-large/region-to-description`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/florence-2-large/region-to-description/playground">
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
          "fal-ai/florence-2-large/region-to-description",
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

      const result = await fal.subscribe("fal-ai/florence-2-large/region-to-description", {
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
        --url https://fal.run/fal-ai/florence-2-large/region-to-description \
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

    <ParamField body="results" type="string" required>
      Results from the model
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
      "results": ""
    }
    ```
  </Tab>

  <Tab title="Region To Category">
    **Endpoint:** `POST https://fal.run/fal-ai/florence-2-large/region-to-category`
    **Endpoint ID:** `fal-ai/florence-2-large/region-to-category`

    <Card title="Try it in the Playground" icon="play" href="https://fal.ai/models/fal-ai/florence-2-large/region-to-category/playground">
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
          "fal-ai/florence-2-large/region-to-category",
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

      const result = await fal.subscribe("fal-ai/florence-2-large/region-to-category", {
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
        --url https://fal.run/fal-ai/florence-2-large/region-to-category \
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

    <ParamField body="results" type="string" required>
      Results from the model
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
      "results": ""
    }
    ```
  </Tab>
</Tabs>

## Related

* [Florence-2 Large](/model-api-reference/vision-api/florence-2-large) — Vision
* [Florence-2 Large](/model-api-reference/image-generation-api/florence-2-large) — Image Generation
