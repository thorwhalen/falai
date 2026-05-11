> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal run

```bash theme={null}
Usage: fal run [-h] [--team TEAM] [--no-cache] [--app-name APP_NAME]
               [--auth AUTH] [--env ENV] [--local]
               [--machine-type MACHINE_TYPE]
               [--limit-max-requests LIMIT_MAX_REQUESTS]
               func_ref

Run fal function.

Positional Arguments:
  func_ref              Function reference. Configure team in pyproject.toml for app names.

Options:
  -h, --help            show this help message and exit
  --team TEAM           The team to use.
  --no-cache            Do not use the cache for the environment build.
  --app-name APP_NAME   Application name to run with.
  --auth AUTH           Application authentication mode (private, public, shared), defaults to public.
  --env ENV             Target environment (defaults to main).
  --local               Run locally without serverless.
  --machine-type MACHINE_TYPE
                        Machine type to use for this run.
  --limit-max-requests LIMIT_MAX_REQUESTS
                        For fal.App runs, gracefully stop the server after serving N requests.

Examples:
  fal run path/to/myfile.py::myfunc
  fal run path/to/myfile.py::myfunc --env staging
  fal run path/to/myfile.py::MyApp --auth private
  fal run path/to/myfile.py::MyApp --local
  fal run path/to/myfile.py::MyApp --machine-type GPU-A100
```

<Warning>
  `fal run` ignores the `auth` set on `fal.App` and in `pyproject.toml` and defaults to `public` so the app is reachable for testing. Pass `--auth` to override. In a future major release the default will become `private` and the `fal.App`/`pyproject.toml` value will be respected.
</Warning>

## Authentication Modes

The `--auth` flag controls who can access your app while it's running:

* **`public`** (default for `fal run`): Anyone can call your app without authentication. You pay for all usage.
* **`private`**: Only you (or your team) can call the app. Requires a valid API key.
* **`shared`**: Any authenticated fal user can call the app.

By default, `fal run` uses `public` mode for easy testing during development.
