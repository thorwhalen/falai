> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal apps runners

```bash theme={null}
Usage: fal apps runners [-h] [--team TEAM] [--env ENV]
                        [--since SINCE]
                        [--state {all,idle,running,pending,setup,failure_delay,terminated} [...]]
                        [--output {pretty,json}] [--json]
                        app_name

List application runners.

Positional Arguments:
  app_name              Application name.

Options:
  -h, --help            show this help message and exit
  --team TEAM           The team to use.
  --env ENV             Target environment (defaults to main).
  --since SINCE         Show terminated runners since the given time. Accepts 'now', relative like '30m', '1h', '1d', or an ISO timestamp. Max 24 hours.
  --state {all,idle,running,pending,setup,failure_delay,terminated} [{all,idle,running,pending,setup,failure_delay,terminated} ...]
                        Filter by runner state(s). Choose one or more, or 'all' (default).

Output:
  --output {pretty,json}
                        Modify the command output
  --json                Output in JSON format (same as --output json)

Examples:
  fal apps runners my-app
  fal apps runners my-app --env staging
```

The runner table displays the following columns:

* **Alias** -- Application name
* **Machine Type** -- Hardware type (e.g. `GPU-A100`, `GPU-H100`)
* **Runner ID** -- Unique runner identifier
* **In Flight Requests** -- Number of active requests
* **Expires In** -- Time until runner expires
* **Uptime** -- How long the runner has been running
* **Revision** -- Application revision
* **State** -- Current runner state
