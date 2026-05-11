> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Fastest FLUX Endpoint

> We believe fal has the fastest FLUX endpoint in the planet. If you can find a faster one, we guarantee to beat it within one week. 🤝

<CardGroup>
  <Card title="fal-ai/ flux/schnell" href="https://fal.ai/models/fal-ai/flux/schnell" img="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/image-7.png?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=63ca3f10d0a6a8ed0b743648881b95a1" width="512" height="384" data-path="images/image-7.png">
    `text-to-image`

    FLUX.1 \[schnell] is a 12 billion parameter flow transformer that generates high-quality images from text in 1 to 4 steps, suitable for personal and commercial use.

    `optimized`
  </Card>

  <Card title="fal-ai/ flux/dev" href="https://fal.ai/models/fal-ai/flux/dev" img="https://mintcdn.com/fal-d8505a2e/_1QeqsRe91WUAOCJ/images/image-8.png?fit=max&auto=format&n=_1QeqsRe91WUAOCJ&q=85&s=77817a3db0b964ce72ac78f06b891404" width="512" height="384" data-path="images/image-8.png">
    `text-to-image`

    FLUX.1 \[dev] is a 12 billion parameter flow transformer that generates high-quality images from text. It is suitable for personal and commercial use.

    `flux`
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

const result = await fal.subscribe("fal-ai/flux/dev", {
  input: {
    prompt:
      "photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang",
  },
});
```

<Note>
  **Note:**

  <h4>Image Uploads Should Not Waste GPU Cycles</h4>

  <p>
    We upload the output image in a background thread so we don't charge any GPU
    time for time spent on the GPU that is not directly inference.
  </p>
</Note>
