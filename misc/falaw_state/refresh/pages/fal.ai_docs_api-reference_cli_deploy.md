> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal deploy

```bash theme={null}
Usage: fal deploy [-h] [--output {pretty,json}] [--json] [--team TEAM] [--app-name APP_NAME]
                  [--auth AUTH] [--strategy {recreate,rolling}] [--no-scale] [--reset-scale]
                  [--check] [--yes] [--no-cache] [--env ENV]
                  [app_ref]

Deploy a fal application. If no app reference is provided, the command will look for a pyproject.toml file with a [tool.fal.apps] section and deploy the application specified with the provided app name.

Positional Arguments:
  app_ref               Application reference. Either a file path or a file path and a function name separated by '::'. If no reference is provided, the command will look for a pyproject.toml file with a [tool.fal.apps] section and deploy the application specified with the provided app name.
                        File path example: path/to/myfile.py::MyApp
                        App name example: my-app (configure team in pyproject.toml)

Options:
  -h, --help            show this help message and exit
  --team TEAM           The team to use.
  --app-name APP_NAME   Application name to deploy with.
  --auth AUTH           Application authentication mode (private, public, shared).
  --strategy {recreate,rolling}
                        Deployment strategy.
  --no-scale            Use the previous deployment of the application for scale settings. This is the default behavior.
  --reset-scale         Use the application code for scale settings.
  --check               Show a pre-deployment summary before deploying. Prompts for confirmation unless --yes is also set.
  --yes                 Skip interactive deploy confirmation prompts. When combined with --check, the summary is still shown.
  --no-cache            Do not use the cache for the environment build.
  --env ENV             Target environment (defaults to main). Can also be set via FAL_ENV environment variable.

Output:
  --output {pretty,json}
                        Modify the command output
  --json                Output in JSON format (same as --output json)

Examples:
  fal deploy
  fal deploy path/to/myfile.py
  fal deploy path/to/myfile.py::MyApp
  fal deploy path/to/myfile.py::MyApp --app-name myapp --auth public
  fal deploy path/to/myfile.py::MyApp --check
  fal deploy path/to/myfile.py::MyApp --check --yes
  fal deploy path/to/myfile.py::MyApp --env staging
  fal deploy my-app
```
