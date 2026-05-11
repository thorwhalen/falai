> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal runners

```bash theme={null}
Usage: fal runners [-h] command ...

Manage fal runners.

Options:
  -h, --help  show this help message and exit

Commands:
  command
    stop        Stop a runner gracefully.
    kill        Kill a runner.
    list        List runners.
    logs (log)  Show logs for a runner.
    shell       Open an interactive shell in a runner.
```

## List

```bash theme={null}
Usage: fal runners list [-h] [--team TEAM] [--since SINCE]
                        [--state {all,idle,running,pending,setup,failure_delay,terminated} [...]]
                        [--output {pretty,json}] [--json]

List runners.

Options:
  -h, --help            show this help message and exit
  --team TEAM           The team to use.
  --since SINCE         Show terminated runners since the given time. Accepts 'now', relative like '30m', '1h', '1d', or an ISO timestamp. Max 24 hours.
  --state {all,idle,running,pending,setup,failure_delay,terminated} [{all,idle,running,pending,setup,failure_delay,terminated} ...]
                        Filter by runner state(s). Choose one or more, or 'all' (default).

Output:
  --output {pretty,json}
                        Modify the command output
  --json                Output in JSON format (same as --output json)
```

The runner table displays the following columns:

* **Alias** — Application name
* **Machine Type** — Hardware type (e.g. `GPU-A100`, `GPU-H100`)
* **Runner ID** — Unique runner identifier
* **In Flight Requests** — Number of active requests
* **Expires In** — Time until runner expires
* **Uptime** — How long the runner has been running
* **Revision** — Application revision
* **State** — Current runner state

## Logs

```bash theme={null}
Usage: fal runners logs [-h] [--output {pretty,json}] [--json] [--team TEAM]
                        [--search SEARCH] [--since SINCE] [--until UNTIL]
                        [--follow] [--lines LINES]
                        id

Show logs for a runner.

Positional Arguments:
  id                    Runner ID.

Options:
  -h, --help            show this help message and exit
  --team TEAM           The team to use.
  --search SEARCH       Search for string in logs.
  --since SINCE         Show logs since the given time. Accepts 'now', relative like '30m', '1h', or an ISO timestamp. Defaults to runner start time or to '1m ago' in --follow mode.
  --until UNTIL         Show logs until the given time. Accepts 'now', relative like '30m', '1h', or an ISO timestamp. Defaults to runner finish time or 'now' if it is still running.
  --follow, -f          Follow logs live. If --since is not specified, implies '--since 1m ago'.
  --lines, -n LINES     Only show latest N log lines. If '+' prefix is used, show oldest N log lines. Ignored if --follow is used.

Output:
  --output {pretty,json}
                        Modify the command output
  --json                Output in JSON format (same as --output json)
```

## Stop

```bash theme={null}
Usage: fal runners stop [-h] [--team TEAM] id

Stop a runner gracefully.

Positional Arguments:
  id           Runner ID.

Options:
  -h, --help   show this help message and exit
  --team TEAM  The team to use.
```

## Kill

```bash theme={null}
Usage: fal runners kill [-h] [--team TEAM] id

Kill a runner.

Positional Arguments:
  id           Runner ID.

Options:
  -h, --help   show this help message and exit
  --team TEAM  The team to use.
```

## Shell

```bash theme={null}
Usage: fal runners shell [-h] [--team TEAM] id

Open an interactive shell session inside a running runner.

Positional Arguments:
  id           Runner ID.

Options:
  -h, --help   show this help message and exit
  --team TEAM  The team to use.
```

### Use Cases

* **Debug running code**: Inspect the runtime environment of a live runner
* **Check dependencies**: Verify installed packages and their versions
* **Examine state**: Inspect files, environment variables, and runtime state
* **Troubleshoot issues**: Diagnose problems in production runners

### Example

Connect to a running runner:

```bash theme={null}
# Get runner ID from runners list
fal runners list

# Connect to the runner
fal runners shell runner_abc123xyz
```

Once connected, you have full shell access within the runner's container environment. Press `Ctrl+D` or type `exit` to disconnect.
