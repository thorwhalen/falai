> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal doctor

```bash theme={null}
Usage: fal doctor [-h] [--debug] [--pdb] [--cprofile]
                  [--output {pretty,json}] [--json]

fal version and misc environment information.

Options:
  -h, --help            show this help message and exit

Output:
  --output {pretty,json}
                        Modify the command output
  --json                Output in JSON format (same as --output json)
```

Outputs the installed `fal` and `isolate` versions, the Python version and platform, and the configured `FAL_HOST` and the prefix of the active `FAL_KEY`. Useful when filing bug reports.
