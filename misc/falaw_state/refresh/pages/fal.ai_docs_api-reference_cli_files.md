> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal files

```bash theme={null}
fal files [-h] [--debug] [--pdb] [--cprofile] command ...

Manage fal files.

Options:
  -h, --help  show this help message and exit
Commands:
  command
    list (ls)
              List files.
    download  Download files.
    upload    Upload files.
    upload-url
              Upload file from URL.
    mv        Move or rename a remote file or directory.
    rm        Recursively remove a remote file or directory.
```

## List

```bash theme={null}
fal files list [-h] [--debug] [--pdb] [--cprofile] [--team TEAM] [path]

List files.

Positional Arguments:
  path         The path to list

Options:
  -h, --help   show this help message and exit
  --team TEAM  The team to use.

```

## Download

```bash theme={null}
fal files download [-h] [--debug] [--pdb] [--cprofile] [--team TEAM]
                          remote_path local_path

Download files.

Positional Arguments:
  remote_path  Remote path to download
  local_path   Local path to download to

Options:
  -h, --help   show this help message and exit
  --team TEAM  The team to use.
```

## Upload

```bash theme={null}
fal files upload [-h] [--debug] [--pdb] [--cprofile] [--team TEAM]
                        local_path remote_path

Upload files.

Positional Arguments:
  local_path   Local path to upload
  remote_path  Remote path to upload to

Options:
  -h, --help   show this help message and exit
  --team TEAM  The team to use.

```

## Upload URL

```bash theme={null}
fal files upload-url [-h] [--debug] [--pdb] [--cprofile] [--team TEAM]
                            url remote_path

Upload file from URL.

Positional Arguments:
  url          URL to upload
  remote_path  Remote path to upload to

Options:
  -h, --help   show this help message and exit
  --team TEAM  The team to use.
```

## Move

```bash theme={null}
fal files mv [-h] [--team TEAM] source destination

Move or rename a remote file or directory.

Positional Arguments:
  source       Remote source path
  destination  Remote destination path

Options:
  -h, --help   show this help message and exit
  --team TEAM  The team to use.
```

## Remove

```bash theme={null}
fal files rm [-h] [--team TEAM] path

Recursively remove a remote file or directory.

Positional Arguments:
  path         Remote path

Options:
  -h, --help   show this help message and exit
  --team TEAM  The team to use.
```
