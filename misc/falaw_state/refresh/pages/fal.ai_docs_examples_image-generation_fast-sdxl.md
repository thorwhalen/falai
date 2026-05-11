> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Fastest SDXL Endpoint

> We believe fal has the fastest SDXL endpoint in the planet. If you can find a faster one, we guarantee to beat it within one week. 🤝

<CardGroup>
  <Card title="fal-ai/ fast-sdxl" href="https://fal.ai/models/fal-ai/fast-sdxl" img="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/image-9.png?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=8338fa5c9760a77f4d49345a5d556985" width="1024" height="1024" data-path="images/image-9.png">
    `text-to-image`

    Run SDXL at the speed of light

    `loras` `embeddings`
  </Card>
</CardGroup>

Here is a quick guide on how to use this model from an API in less than 1 minute.

Before we proceed, you need to create an [API key](https://fal.ai/dashboard/keys).

This key secret will be used to authenticate your requests to the fal API.

```js theme={null}
fal.config({
  credentials: "PASTE_YOUR_FAL_KEY_HERE",
});
```

Now you can call our Model API endpoint using the [fal js client](/model-apis/model-endpoints):

```js theme={null}
import { fal } from "@fal-ai/client";

const result = await fal.subscribe("fal-ai/fast-sdxl", {
  input: {
    prompt:
      "photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang",
  },
});
```

A typical inference takes 2.3 seconds and will cost \~\$0.0025.

<Note>
  **Image Uploads Should Not Waste GPU Cycles**

  We upload the output image in a background thread so we don't charge any GPU time for time spent on the GPU that is not directly inference.
</Note>
