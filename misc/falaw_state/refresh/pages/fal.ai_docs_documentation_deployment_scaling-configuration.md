> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Updating Your Configuration

> How to set scaling parameters via code, CLI, or dashboard -- and how they behave across deploys.

## How to Set Parameters

You can set scaling parameters in three ways.

### In Your Code

```python theme={null}
import fal

class MyApp(fal.App):
    machine_type = "GPU-A100"
    max_multiplexing = 1
    startup_timeout = 600

    keep_alive = 300
    min_concurrency = 2
    max_concurrency = 10
    concurrency_buffer = 2
    scaling_delay = 30
```

### Via CLI

Adjust parameters for a deployed app without redeploying:

```bash theme={null}
fal apps scale myapp \
  --min-concurrency 5 \
  --max-concurrency 20 \
  --keep-alive 600 \
  --concurrency-buffer 3
```

### Via Dashboard

Navigate to [**Dashboard > Apps > \[your-app\]**](https://fal.ai/dashboard/apps) and adjust scaling parameters from the app settings.

***

## How Parameters Behave Across Deploys

Not all parameters behave the same when you deploy. Understanding this prevents surprises.

### Runtime-tunable parameters

`keep_alive`, `min_concurrency`, `max_concurrency`, `concurrency_buffer`, `concurrency_buffer_perc`, `scaling_delay`, `request_timeout`, `regions`

These affect **cost and performance** and are safe to change without understanding the code. When you adjust them via CLI or dashboard:

* Changes take effect immediately
* Changes **persist across deploys** -- your next `fal deploy` inherits the CLI/dashboard values, not what's in your code

### Code-specific parameters

`max_multiplexing`, `startup_timeout`, `machine_type`

These affect **correctness** -- changing them without updating code can break your app:

* **`max_multiplexing`**: Your code must handle concurrent requests. Setting this to 4 via CLI when your handlers are synchronous would break things.
* **`startup_timeout`**: Depends on what your `setup()` does. Only the code author knows the right value.
* **`machine_type`**: Your model is sized for specific GPU memory. Switching GPUs without code changes risks OOM crashes.

You can change these via CLI for **immediate but temporary** testing, but they **reset to code values on the next deploy**.

<Warning>
  CLI changes to code-specific params take effect immediately but reset on deploy. To make changes permanent, update your application code.
</Warning>

***

## `--reset-scale`

By default, `fal deploy` inherits runtime-tunable params from the previous revision. If you want to discard all CLI/dashboard overrides and go back to what's in your code:

```bash theme={null}
fal deploy --reset-scale
```

This resets **all parameters** to code values.

**When to use:**

* You want to go back to the values in your code after tuning via CLI
* You're making a major change and want a clean slate
* You've updated scaling values in code and want them to take effect

***

## Example

```python theme={null}
class MyApp(fal.App):
    min_concurrency = 1
    keep_alive = 60
```

1. **Deploy**: `min_concurrency=1`, `keep_alive=60`
2. **CLI**: `fal apps scale myapp --min-concurrency 5 --keep-alive 300`
   * Now: `min_concurrency=5`, `keep_alive=300`
3. **Deploy again** (`fal deploy`):
   * `min_concurrency=5`, `keep_alive=300` (inherited from step 2)
4. **Deploy with reset** (`fal deploy --reset-scale`):
   * `min_concurrency=1`, `keep_alive=60` (reset to code)

<Card title="Parameter Reference" icon="arrow-right" href="/documentation/deployment/scale-your-application">
  See what each scaling parameter does
</Card>
