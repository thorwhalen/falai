> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal keys

```bash theme={null}
Usage: fal keys [-h] [--debug] [--pdb] [--cprofile] command ...

Manage fal keys.

Options:
  -h, --help  show this help message and exit
Commands:
  command
    create    Create a key.
    list      List keys.
    revoke    Revoke key.
```

## Create

```bash theme={null}
Usage: fal keys create [-h] [--debug] [--pdb] [--cprofile] --scope {ADMIN,API}
                       [--desc DESC]

Create a key.

Options:
  -h, --help           show this help message and exit
  --scope {ADMIN,API}  The privilege scope of the key.
  --desc DESC          Key description (e.g. "My Test Key")
```

## List

```bash theme={null}
Usage: fal keys list [-h] [--debug] [--pdb] [--cprofile]

List keys.

Options:
  -h, --help  show this help message and exit
```

## Revoke

```bash theme={null}
Usage: fal keys revoke [-h] [--debug] [--pdb] [--cprofile] key_id

Revoke key.

Positional Arguments:
  key_id      Key ID.

Options:
  -h, --help  show this help message and exit
```
