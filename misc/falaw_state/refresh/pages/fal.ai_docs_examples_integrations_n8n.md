> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using fal within an n8n workflow

> This guide will demonstrate, step-by-step, how to use fal within an n8n workflow.

## Prerequisites

* An n8n account ([https://n8n.io/](https://n8n.io/))
* A fal account ([https://fal.ai/dashboard](https://fal.ai/dashboard))
* A fal API key (generated from your account dashboard)

## Workflow Overview

This n8n workflow consists of three main HTTP requests:

<Steps>
  <Step title="Submit Request">
    Send a POST request to initiate content generation
  </Step>

  <Step title="Check Status">
    Poll the status of your request using GET
  </Step>

  <Step title="Retrieve Result">
    Fetch the final generated content
  </Step>
</Steps>

## Step 1: Create Your Workflow

<Steps>
  <Step>
    In n8n, create a new workflow
  </Step>

  <Step>
    Start with a **Manual Trigger** node to initiate the workflow manually
  </Step>
</Steps>

<Frame>
  <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/n8n/01.webp?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=86505fc90245b94c09161f2a1762d388" alt="" width="2266" height="1646" data-path="images/n8n/01.webp" />
</Frame>

## Step 2: Submit Request (POST)

### Add HTTP Request Node

<Steps>
  <Step>
    Add an **HTTP Request** node after your trigger
  </Step>

  <Step>
    Set the **Method** to `POST`
  </Step>
</Steps>

<Frame>
  <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/n8n/02.webp?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=cd7de677bed6fd24446726e7fdfd5999" alt="" width="2266" height="1646" data-path="images/n8n/02.webp" />
</Frame>

### Configure the URL

<Steps>
  <Step>
    Navigate to [fal.ai](https://fal.ai/dashboard) and select your desired model (e.g., `fal-ai/veo3/fast`)

    <Frame>
      <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/n8n/03.png?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=3f36e5adf0e0359186dc049e83546101" alt="" width="2458" height="1912" data-path="images/n8n/03.png" />
    </Frame>
  </Step>

  <Step>
    Click on the **API** tab, select "HTTP (cURL)" and "Submit a request". Copy and save the URL and data JSON as those will be needed for later.

    <Frame>
      <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/n8n/04.png?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=c9b0c680a03dd7291a1457743c8ebb62" alt="" width="2028" height="906" data-path="images/n8n/04.png" />
    </Frame>
  </Step>

  <Step>
    Copy the URL (e.g., `https://queue.fal.run/fal-ai/veo3/fast`) and paste it into the URL field in n8n

    <Frame>
      <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/n8n/05.png?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=c1d3192e62f6b9d6868d2ae32e4004dd" alt="" width="2266" height="1646" data-path="images/n8n/05.png" />
    </Frame>
  </Step>
</Steps>

### Set Up Authentication

<Steps>
  <Step>
    Navigate to [fal.ai API Keys](https://fal.ai/dashboard/keys), create a new key and copy its value.

    <Frame>
      <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/n8n/06.png?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=d2104fe703ca052d8123a24e5f2a85df" alt="" width="2448" height="1420" data-path="images/n8n/06.png" />
    </Frame>
  </Step>

  <Step>
    Back in n8n, in the **Authentication** section, select **Generic Credential Type**
  </Step>

  <Step>
    Choose **Header Auth** from the dropdown
  </Step>

  <Step>
    Click **+ Create new credential**
  </Step>

  <Step>
    Set:

    * **Name**: `Authorization`
    * **Value**: `Key YOUR_FAL_KEY`
  </Step>

  <Step>
    Save the credential and close

    <Frame>
      <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/n8n/07.webp?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=7dc459c9cb98b714d5faa0e7950ae1dc" alt="" width="2266" height="1646" data-path="images/n8n/07.webp" />
    </Frame>
  </Step>
</Steps>

### Configure Request Body

<Steps>
  <Step>
    Toggle **Send Body** to `ON`
  </Step>

  <Step>
    Set **Body Content Type** to `JSON`
  </Step>

  <Step>
    Choose **Specify Body** as `USING JSON`

    <Frame>
      <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/n8n/08.webp?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=5fc79b5a0908e101aafa7fd35b5d476f" alt="" width="2266" height="1646" data-path="images/n8n/08.webp" />
    </Frame>
  </Step>

  <Step>
    In fal, go again to the model page, select **JSON** from dropdown and copy the payload

    <Frame>
      <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/n8n/09.png?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=6e0c82d5d7c580e9aa49ec9e8ea66ada" alt="" width="2502" height="1646" data-path="images/n8n/09.png" />
    </Frame>
  </Step>

  <Step>
    Copy the JSON payload and paste it into n8n's JSON text box

    <Frame>
      <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/n8n/10.png?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=ad419e143400976fa0a08921b391c968" alt="" width="2266" height="1646" data-path="images/n8n/10.png" />
    </Frame>
  </Step>
</Steps>

### Execute the Node

<Steps>
  <Step>
    Click **Execute Node** to test the request. You should receive a response with a request ID.

    <Frame>
      <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/n8n/11.png?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=c8cdd5bb3f4083774e498441e820dbd9" alt="" width="2266" height="1646" data-path="images/n8n/11.png" />
    </Frame>
  </Step>
</Steps>

## Step 3: Check Status (GET)

### Add Second HTTP Request Node

<Steps>
  <Step>
    Click on the first HTTP Request node and add another **HTTP Request** node
  </Step>

  <Step>
    Set the **Method** to `GET`
  </Step>
</Steps>

### Configure Status Check URL

<Steps>
  <Step>
    In fal, go to your model's **API** section and find the **GET** URL for status checking

    <Frame>
      <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/n8n/12.png?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=d8963881f4ac744d8e40644115f0aeaa" alt="" width="2032" height="542" data-path="images/n8n/12.png" />
    </Frame>
  </Step>

  <Step>
    Copy this URL and paste it into the URL field
  </Step>

  <Step>
    You'll need to replace the request ID from the previous step on this URL, with `{{ $json.request_id }}`

    <Frame>
      <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/n8n/13.webp?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=ded90911ad1c72b9f3dd21e580dfdf63" alt="" width="2266" height="1646" data-path="images/n8n/13.webp" />
    </Frame>
  </Step>
</Steps>

### Set Authentication

<Steps>
  <Step>
    Use the same **Header Auth** credential created earlier
  </Step>

  <Step>
    Select your existing **Authorization** credential
  </Step>
</Steps>

### Execute the Node

1. This will check the status of your generation request.

<Frame>
  <img src="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/n8n/14.webp?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=80f6186759e48b38a2512042c4fa2c79" alt="" width="2266" height="1646" data-path="images/n8n/14.webp" />
</Frame>

## Step 4: Retrieve Result (GET)

### Add Third HTTP Request Node

1. Add a final **HTTP Request** node
2. Set the **Method** to `GET`

### Configure Result URL

1. Use the result URL provided in the status response by setting the URL to `{{ $json.request_url }}`

### Set Authentication

1. Use the same **Header Auth** credential

### Execute the Node

This will retrieve your final generated content.

## Testing Your Workflow

<Steps>
  <Step>
    Save your workflow
  </Step>

  <Step>
    Click **Execute Workflow** to run the complete process
  </Step>

  <Step>
    Monitor each node to ensure successful execution
  </Step>

  <Step>
    Check the final node output for your generated content
  </Step>
</Steps>

## Best Practices

* **Error Handling**: Add error handling nodes to manage failed requests
* **Delays**: Consider adding **Wait** nodes between status checks to avoid overwhelming the API
* **Conditional Logic**: Use **IF** nodes to check status before proceeding to result retrieval
* **Data Transformation**: Use **Set** nodes to extract and format specific data from responses

## Troubleshooting

* **401 Unauthorized**: Check that your API key is correctly set in the authentication header
* **Request ID Missing**: Ensure the first POST request completed successfully and returned a request ID
* **Status Still Processing**: Add appropriate delays between status checks
* **Invalid JSON**: Verify your JSON payload matches the model's expected format

## Next Steps

Once you have a working workflow, you can:

* Connect it to external triggers (webhooks, schedules, etc.)
* Integrate with other services in your n8n workflow
* Add data processing and transformation steps
* Set up notifications for completed generations
