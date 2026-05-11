> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal environments

```bash theme={null}
Usage: fal environments [-h] [--debug] [--pdb] [--cprofile] command ...

Manage fal environments.

Options:
  -h, --help  show this help message and exit

Commands:
  command
    list      List environments.
    create    Create an environment.
    delete    Delete an environment.
```

<Note>
  The `environments` command also has an alias `envs` for convenience:

  ```bash theme={null}
  fal envs list
  ```
</Note>

## List

```bash theme={null}
Usage: fal environments list [-h] [--debug] [--pdb] [--cprofile]
                             [--output {pretty,json}] [--json]

List environments.

Options:
  -h, --help            show this help message and exit

Output:
  --output {pretty,json}
                        Modify the command output
  --json                Output in JSON format (same as --output json)

Examples:
  fal environments list
  fal envs list --output json
```

## Create

```bash theme={null}
Usage: fal environments create [-h] [--debug] [--pdb] [--cprofile]
                               [--description DESCRIPTION]
                               name

Create an environment.

Positional Arguments:
  name                  Environment name.

Options:
  -h, --help            show this help message and exit
  --description DESCRIPTION
                        Environment description.

Examples:
  fal environments create staging
  fal envs create dev --description "Development environment"
```

## Delete

```bash theme={null}
Usage: fal environments delete [-h] [--debug] [--pdb] [--cprofile] [--yes]
                               name

Delete an environment.

Positional Arguments:
  name        Environment name.

Options:
  -h, --help  show this help message and exit
  --yes       Skip confirmation prompt.

Debug:
  --debug     Show verbose errors.
  --pdb       Start pdb on error.
  --cprofile  Show cProfile report.
```

<Warning>
  Deleting an environment permanently removes all apps and secrets in that environment. You will be prompted to confirm by typing the environment name unless `--yes` is provided.
</Warning>

## Using Environments with Other Commands

Once you've created environments, you can target them using the `--env` flag in other commands:

```bash theme={null}
# Deploy to an environment
fal deploy path/to/myapp.py::MyApp --env staging

# Manage secrets per environment
fal secrets set API_KEY=value --env staging
fal secrets list --env staging

# Manage apps per environment
fal apps list --env staging
fal apps scale my-app --min-concurrency 1 --env staging
fal apps runners my-app --env staging
fal apps delete my-app --env staging

# Run functions with environment-specific secrets
fal run path/to/myapp.py::MyApp --env staging
```
