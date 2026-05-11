> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal apps scale

```bash theme={null}
Usage: fal apps scale [-h] [--debug] [--pdb] [--cprofile]
                      [--keep-alive KEEP_ALIVE]
                      [--max-multiplexing MAX_MULTIPLEXING]
                      [--max-concurrency MAX_CONCURRENCY]
                      [--min-concurrency MIN_CONCURRENCY]
                      [--request-timeout REQUEST_TIMEOUT]
                      [--startup-timeout STARTUP_TIMEOUT]
                      [--machine-types MACHINE_TYPES [MACHINE_TYPES ...]]
                      [--regions REGIONS [REGIONS ...]]
                      [--env ENV]
                      app_name

Scale application.

Positional Arguments:
  app_name              Application name.

Options:
  -h, --help            show this help message and exit
  --keep-alive KEEP_ALIVE
                        Keep alive (seconds).
  --max-multiplexing MAX_MULTIPLEXING
                        Maximum multiplexing
  --max-concurrency MAX_CONCURRENCY
                        Maximum concurrency.
  --min-concurrency MIN_CONCURRENCY
                        Minimum concurrency
  --request-timeout REQUEST_TIMEOUT
                        Request timeout (seconds).
  --startup-timeout STARTUP_TIMEOUT
                        Startup timeout (seconds).
  --machine-types MACHINE_TYPES [MACHINE_TYPES ...]
                        Machine types (pass several items to set multiple).
  --regions REGIONS [REGIONS ...]
                        Valid regions (pass several items to set multiple).
  --env ENV             Target environment (defaults to main).
```

<Note>
  **Note:**

  Redeploying the application, by default, will not reset these settings, except for the code-specific settings. See [Code-Specific Settings (Reset on Deploy)](/serverless/deployment-operations/scale-your-application#code-specific-settings-reset-on-deploy) for details.
</Note>
