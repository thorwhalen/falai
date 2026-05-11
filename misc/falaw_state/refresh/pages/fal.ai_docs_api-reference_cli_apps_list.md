> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal apps list

```bash theme={null}
Usage: fal apps list [-h] [--debug] [--pdb] [--cprofile]
                     [--sort-by-runners] [--filter FILTER]
                     [--env ENV] [--regions REGIONS [REGIONS ...]]
                     [--output {pretty,json}] [--json]

List applications.

Options:
  -h, --help            show this help message and exit
  --sort-by-runners     Sort by number of runners ascending.
  --filter FILTER       Filter applications by alias contents.
  --env ENV             Target environment (defaults to main).
  --regions REGIONS [REGIONS ...]
                        Valid regions (pass several items to filter on multiple).

Output:
  --output {pretty,json}
                        Modify the command output
  --json                Output in JSON format (same as --output json)

Examples:
  fal apps list
  fal apps list --env staging
  fal apps list --filter myapp --sort-by-runners
  fal apps list --json
```
