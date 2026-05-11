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

Log in a user.

Options:
  -h, --help  show this help message and exit
```

## Logout

```bash theme={null}
Usage: fal auth logout [-h] [--debug] [--pdb] [--cprofile]

Log out the currently logged-in user.

Options:
  -h, --help  show this help message and exit
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
