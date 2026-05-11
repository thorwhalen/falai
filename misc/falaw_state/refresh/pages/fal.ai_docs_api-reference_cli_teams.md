> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal account

Manage and switch between the personal, team, and organization accounts you belong to. Useful when you're a member of multiple accounts and need to deploy or manage apps under a specific one.

## fal account list

List all accounts you belong to:

```bash theme={null}
fal account list
```

Shows your personal account along with any team and organization accounts, indicating which is currently active.

Supports `--output {pretty,json}` and `--json` for machine-readable output.

## fal account set

Switch to a specific account:

```bash theme={null}
fal account set <account>
```

`<account>` may be either an account nickname or the index shown by `fal account list`. After switching, all CLI operations (`fal deploy`, `fal apps`, `fal secrets`, etc.) run under the selected account.

If no `<account>` is provided, you'll be prompted interactively.

**Arguments:**

| Argument  | Description                                       |
| --------- | ------------------------------------------------- |
| `account` | The account nickname (or list index) to switch to |

**Example:**

```bash theme={null}
# Switch to your company team
fal account set my-company

# Deploy under that team
fal deploy my_app.py::MyApp
```

## fal account unset

Switch back to your personal account:

```bash theme={null}
fal account unset
```
