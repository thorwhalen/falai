> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal auth

```bash theme={null}
fal auth [-h] [--debug] [--pdb] [--cprofile] command ...

Authenticate with fal.

Options:
  -h, --help  show this help message and exit

Commands:
  command
    login     Log in a user.
    logout    Log out the currently logged-in user.
    whoami    Show the currently authenticated user.
```

## Login

```bash theme={null}
Usage: fal auth login [-h] [--debug] [--pdb] [--cprofile]
                      [--connection CONNECTION] [--no-browser]

Log in a user.

Options:
  -h, --help               show this help message and exit
  --connection CONNECTION  Auth connection (e.g. github, google, or an SSO domain). Skips the interactive prompt.
  --no-browser             Don't attempt to open a browser. Just print the URL to visit.
```

When `--connection` is omitted, the CLI prompts you to choose between GitHub, Google, or your enterprise SSO domain. The previously used choice is remembered and offered as the default on subsequent logins.

## Logout

```bash theme={null}
Usage: fal auth logout [-h] [--debug] [--pdb] [--cprofile] [--no-browser]

Log out the currently logged-in user.

Options:
  -h, --help    show this help message and exit
  --no-browser  Don't attempt to open a browser. Just print the URL to visit.
```

## Whoami

```bash theme={null}
Usage: fal auth whoami [-h] [--debug] [--pdb] [--cprofile]

Show the currently authenticated user.

Options:
  -h, --help  show this help message and exit

Debug:
  --debug     Show verbose errors.
  --pdb       Start pdb on error.
  --cprofile  Show cProfile report.
```
