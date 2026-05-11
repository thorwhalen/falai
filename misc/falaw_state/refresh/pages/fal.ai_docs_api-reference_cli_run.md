> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal run

```bash theme={null}
Usage: fal run [-h] [--team TEAM] [--no-cache] [--app-name APP_NAME]
               [--auth AUTH] [--env ENV] func_ref

Run fal function.

Positional Arguments:
  func_ref             Function reference. Configure team in pyproject.toml for app names.

Options:
  -h, --help           show this help message and exit
  --team TEAM          The team to use.
  --no-cache           Do not use the cache for the environment build.
  --app-name APP_NAME  Application name to run with.
  --auth AUTH          Application authentication mode (private, public), defaults to public.
  --env ENV            Target environment (defaults to main).

Examples:
  fal run path/to/myfile.py::myfunc
  fal run path/to/myfile.py::myfunc --env staging
  fal run path/to/myfile.py::MyApp --auth private
```

## Authentication Modes

The `--auth` flag controls who can access your app while it's running:

* **`public`** (default): Anyone can call your app without authentication. You pay for all usage.
* **`private`**: Only you (or your team) can call the app. Requires a valid API key.

By default, `fal run` uses `public` mode for easy testing during development.
