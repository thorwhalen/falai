> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal secrets

```bash theme={null}
Usage: fal secrets [-h] [--debug] [--pdb] [--cprofile] command ...

Manage fal secrets.

Options:
  -h, --help  show this help message and exit
Commands:
  command
    set       Set a secret.
    list      List secrets.
    unset     Unset a secret.
```

## Set

```bash theme={null}
Usage: fal secrets set [-h] [--debug] [--pdb] [--cprofile] [--env ENV]
                       NAME=VALUE [NAME=VALUE ...]

Set a secret.

Positional Arguments:
  NAME=VALUE  Secret NAME=VALUE pairs.

Options:
  -h, --help  show this help message and exit
  --env ENV   Target environment (defaults to main).

Examples:
  fal secrets set HF_TOKEN=hf_***
  fal secrets set API_KEY=key123 --env staging
```

## List

```bash theme={null}
Usage: fal secrets list [-h] [--debug] [--pdb] [--cprofile] [--env ENV]

List secrets.

Options:
  -h, --help  show this help message and exit
  --env ENV   Target environment (defaults to main).

Examples:
  fal secrets list
  fal secrets list --env staging
```

## Unset

```bash theme={null}
Usage: fal secrets unset [-h] [--debug] [--pdb] [--cprofile] [--env ENV] NAME

Unset a secret.

Positional Arguments:
  NAME        Secret's name.

Options:
  -h, --help  show this help message and exit
  --env ENV   Target environment (defaults to main).

Debug:
  --debug     Show verbose errors.
  --pdb       Start pdb on error.
  --cprofile  Show cProfile report.

Examples:
  fal secrets unset HF_TOKEN
  fal secrets unset API_KEY --env staging
```
