> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Why fal?

> Industry-leading inference speed for generative AI, trusted by top AI applications

## Model APIs

**Unified API, 1,000+ models.** One API to access every model on fal. Switch between FLUX, Nano Banana 2, Kling 3.0, Sora 2, Whisper, and more with a single parameter change. No need to integrate separate providers or manage different SDKs. fal moves fast on new model launches too, with day-0 availability the moment a model drops, so you're never waiting to integrate the latest generation.

```python theme={null}
import fal_client

# Switch models by changing one string
result = fal_client.subscribe("fal-ai/flux/schnell", arguments={"prompt": "a sunset over mountains"})
result = fal_client.subscribe("fal-ai/nano-banana-2", arguments={"prompt": "a sunset over mountains"})
```

**Fastest inference for generative media.** Speed is where fal started and where it continues to invest the most. Proprietary optimizations, including custom CUDA kernels, optimized attention layers, and inference engine tuning, consistently deliver the fastest inference for diffusion and generative media workloads. Reliability matches the speed: 99.99% historical uptime, fault tolerance, and intelligent request queuing are built in.

**Test and compare before you commit.** [Sandbox](https://fal.ai/sandbox) lets you run the same prompt across multiple models side by side, estimate costs before running, and share results with your team. Instead of guessing which model fits your use case, you can see the differences visually and make model selection concrete.

***

## Serverless

**Deploy your own models on battle-tested infrastructure.** Every endpoint on the [fal Marketplace](https://fal.ai/models) runs on [fal Serverless](/documentation/serverless), the same infrastructure you deploy your own models on. fal has been running this system for over 3 years, serving tens of millions of requests daily. If fal Serverless breaks, fal's own products break. That alignment means the engine your code runs on is constantly being optimized.

**Scale automatically, or reserve capacity.** fal scales from zero to thousands of GPUs across H100s, H200s, A100s, and more. For teams that need guaranteed capacity, fal also offers reserved GPU allocations.

**Dedicated engineering support.** Every customer gets a dedicated Slack channel with engineers across timezones. For enterprise contracts, fal's ML specialists work directly with your team, optimizing your code, tuning cold starts, and iterating from development through production. Migration is straightforward too: bring your existing [container images](/documentation/development/use-custom-container-image), use the [quickstart](/documentation/development/getting-started/quick-start) to deploy in minutes, or connect to the [MCP](/documentation/serverless/mcp) and migrate in one shot.

***

<CardGroup cols={2}>
  <Card title="Model APIs" icon="cube" href="/documentation/model-apis/overview">
    Start calling 1,000+ models with a single API
  </Card>

  <Card title="Serverless" icon="rocket" href="/documentation/serverless">
    Deploy your own models on fal's infrastructure
  </Card>
</CardGroup>
