> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal apps rollout

```bash theme={null}
Usage: fal apps rollout [-h] [--debug] [--pdb] [--cprofile] [--team TEAM] 
                        [--force] [--env ENV] app_name

Rollout application by restarting all active runners.

Positional Arguments:
  app_name     Application name.

Options:
  -h, --help   show this help message and exit
  --team TEAM  The team to use.
  --force      Force rollout by killing runners immediately instead of 
               gracefully stopping them.
  --env ENV    Target environment (defaults to main).

Debug:
  --debug      Show verbose errors.
  --pdb        Start pdb on error.
  --cprofile   Show cProfile report.
```

## When to Use

Use `fal apps rollout` when you need to restart all runners for an application without redeploying:

* **Environment variable changes**: Force runners to pick up updated secrets or environment variables
* **Bad state recovery**: Restart runners that may be in an unhealthy state
* **Memory cleanup**: Force garbage collection and memory cleanup across all runners
* **Configuration updates**: Apply changes that require a runner restart

## Graceful vs Force Rollout

### Graceful Rollout (Default)

```bash theme={null}
fal apps rollout myapp
```

Gracefully stops all active runners, allowing them to finish processing current requests before shutting down. This is the recommended approach for most situations.

**How it works:**

1. Identifies all active runners for the application
2. Sends a graceful stop signal to each runner
3. Runners finish their current requests
4. New runners are automatically started by the auto-scaling system as needed

### Force Rollout

```bash theme={null}
fal apps rollout myapp --force
```

Immediately kills all active runners without waiting for current requests to complete. Use this when runners are unresponsive or when you need an immediate restart.

**How it works:**

1. Identifies all active runners for the application
2. Immediately terminates all runners
3. New runners are automatically started by the auto-scaling system

<Warning>
  Force rollout will terminate in-flight requests, potentially causing errors for active users. Use the graceful rollout (without `--force`) unless absolutely necessary.
</Warning>

## Examples

### Rollout after updating a secret

```bash theme={null}
# Update a secret
fal secrets set MY_API_KEY new_value

# Gracefully rollout to pick up the new secret
fal apps rollout myapp
```

### Rollout in a specific environment

```bash theme={null}
# Update a secret in staging
fal secrets set MY_API_KEY staging_value --env staging

# Rollout the staging environment
fal apps rollout myapp --env staging
```

### Force rollout to recover from frozen runners

```bash theme={null}
# Check runners status
fal apps runners myapp

# Force immediate restart if runners are unresponsive
fal apps rollout myapp --force
```

## Difference from Redeployment

`fal apps rollout` is different from `fal deploy`:

* **`fal apps rollout`**: Restarts existing runners without changing the application code or configuration. Useful for applying environment changes or recovering from bad states.
* **`fal deploy`**: Creates a new revision of your application with updated code and configuration. Use this when you've made code changes.

## See Also

* [fal deploy](/serverless/cli/deploy) - Deploy a new revision of your application
* [fal apps scale](/serverless/cli/apps/scale) - Adjust scaling parameters
* [fal apps runners](/serverless/cli/apps/runners) - View active runners for an application
