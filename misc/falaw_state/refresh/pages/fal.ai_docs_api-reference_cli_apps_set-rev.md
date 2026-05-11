> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal apps set-rev

```bash theme={null}
Usage: fal apps set-rev [-h] [--debug] [--pdb] [--cprofile]
                        [--team TEAM] [--auth {public,private,shared}]
                        [--strategy {recreate,rolling}] [--env ENV] app_name
                        app_rev

Set application to a particular revision.

Positional Arguments:
  app_name              Application name.
  app_rev               Application revision.

Options:
  -h, --help            show this help message and exit
  --team TEAM           The team to use.
  --auth {public,private,shared}
                        Application authentication mode.
  --strategy {recreate,rolling}
                        Deployment strategy.
  --env ENV             Target environment (defaults to main). Can also be set via FAL_ENV environment variable.

Debug:
  --debug               Show verbose errors.
  --pdb                 Start pdb on error.
  --cprofile            Show cProfile report.
```
