> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal profile

### Managing Profiles

The `fal` CLI allows you to manage multiple profiles, making it easy to switch between different fal accounts. This is particularly useful if you have multiple environments or projects.

#### Adding a New Profile

To add a new profile, set it as the default and then add the key:

```sh theme={null}
❯ fal profile set example
Default profile set to example.
No key set for profile. Use fal profile key to set a key.

❯ fal profile key
Enter the key: invalid
Invalid key. The key must be in the format key:value.
Enter the key: 112f05b4-6ee8-4d06-bdb1-7ba38789ef8e:954285993fa8e651dac37a03ea2efbc9
Key set for profile example.
```

<Note>
  **Note:**

  The key used in the example above is no longer valid. 😉
</Note>

#### Listing Profiles

To list all available profiles, use the `fal profile list` command:

```sh theme={null}
❯ fal profile list
```

| Default | Profile | Settings |
| ------- | ------- | -------- |
|         | me      | key      |
|         | comfy   | key      |
| \*      | example | key      |

#### Setting a Default Profile

To set a default profile, use the `fal profile set` command followed by the profile name:

```sh theme={null}
❯ fal profile set comfy
Default profile set to comfy.

❯ fal profile list
```

| Default | Profile | Settings |
| ------- | ------- | -------- |
|         | me      | key      |
| \*      | comfy   | key      |
|         | example | key      |

After setting the default profile, you can directly access the account information without specifying the profile name.

```sh theme={null}
❯ fal app list
```

| Name   | Revision           | Auth   | Min Concurrency | Max Concurrency | Max Multiplexing | Keep Alive | Request Timeout | Startup Timeout | Machine Type | Runners | Regions |
| ------ | ------------------ | ------ | --------------- | --------------- | ---------------- | ---------- | --------------- | --------------- | ------------ | ------- | ------- |
| my-app | 11111111-2222-333… | shared | 0               | 10              | 1                | 300        | 3600            | 600             | ........     | 0       |         |

#### Deleting a Profile

To delete a profile, use the `fal profile delete` command followed by the profile name:

```sh theme={null}
❯ fal profile delete example
Profile example deleted.
```

## Command Reference

```bash theme={null}
Usage: fal profile [-h] command ...

Profile management.

Commands:
  command
    list      List all profiles.
    set       Set default profile. If the profile doesn't exist, you'll be prompted to create it.
    unset     Unset default profile.
    key       Set key for profile.
    host      Set fal host.
    create    Create a new profile.
    delete    Delete profile.
```

<Note>
  `fal profiles` is an alias for `fal profile`.
</Note>

### create

Create a new named profile and set it as the default:

```bash theme={null}
fal profile create <PROFILE>
```

If the profile already exists the command is a no-op. After creation you'll typically run `fal profile key` to attach an API key.

### unset

Clear the default profile selection:

```bash theme={null}
fal profile unset
```

After unsetting, `fal` falls back to environment variables (`FAL_KEY`, `FAL_HOST`).

### host

Override the fal API host for the active profile. Most users don't need this — it's primarily useful for self-hosted or staging deployments:

```bash theme={null}
fal profile host <HOST>
```

### list

```bash theme={null}
Usage: fal profile list [-h] [--output {pretty,json}] [--json]
```

Supports JSON output for scripting:

```bash theme={null}
fal profile list --json
```
