> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal queue

> Manage application queues.

```bash theme={null}
Usage: fal queue [-h] command ...

Manage application queues.

Options:
  -h, --help  show this help message and exit

Commands:
  command
    size      Get queue size for an application.
    flush     Flush all pending requests in an application queue.
```

## Size

```bash theme={null}
Usage: fal queue size [-h] [--output {pretty,json}] [--json] [--team TEAM]
                      [--by-user] app_name

Get queue size for an application.

Positional Arguments:
  app_name              Application name (do not prefix with owner).

Options:
  -h, --help            show this help message and exit
  --team TEAM           The team to use.
  --by-user             Group queue size by user.

Output:
  --output {pretty,json}
                        Modify the command output
  --json                Output in JSON format (same as --output json)
```

## Flush

```bash theme={null}
Usage: fal queue flush [-h] [--team TEAM] [--caller-user-id CALLER_USER_ID] app_name

Flush all pending requests in an application queue.

Positional Arguments:
  app_name              Application name.

Options:
  -h, --help            show this help message and exit
  --team TEAM           The team to use.
  --caller-user-id CALLER_USER_ID
                        Only flush requests from this user ID. If not provided, all requests will be flushed.
```
