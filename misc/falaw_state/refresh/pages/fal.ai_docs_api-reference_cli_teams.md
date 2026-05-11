> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal teams

Manage and switch between teams you belong to. Useful when you're a member of multiple teams and need to deploy or manage apps under a specific team account.

## fal teams list

List all teams you belong to:

```bash theme={null}
fal teams list
```

Shows your personal account and all team accounts, indicating which is currently active.

## fal teams set

Switch to a specific team:

```bash theme={null}
fal teams set <account>
```

After switching, all CLI operations (`fal deploy`, `fal apps`, `fal secrets`, etc.) will run under the selected team account.

**Arguments:**

| Argument  | Description                |
| --------- | -------------------------- |
| `account` | The team name to switch to |

**Example:**

```bash theme={null}
# Switch to your company team
fal teams set my-company

# Deploy under that team
fal deploy my_app.py::MyApp
```

## fal teams unset

Switch back to your personal account:

```bash theme={null}
fal teams unset
```

<Note>
  You can also use `fal team` as a shorthand alias for `fal teams`.
</Note>
