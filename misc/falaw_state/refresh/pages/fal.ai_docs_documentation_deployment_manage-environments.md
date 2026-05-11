> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Environments

> Organize your fal Serverless applications, secrets, and configurations across different stages of your development workflow using environments. Create isolated spaces for development, staging, and production deployments.

Environments let you isolate applications, secrets, and configurations for different stages of your workflow. By default, all resources are deployed to the `main` environment. You can create additional environments like `staging` or `dev` to test changes separately from production.

<Note>
  **Each app is attached to a single environment.** To deploy the same application code to multiple environments (e.g., dev, staging, and main), you must create a separate app deployment for each environment. Apps cannot be promoted or moved between environments—instead, deploy your code to each target environment independently.
</Note>

## Why Use Environments?

* **Isolation**: Keep development, staging, and production completely separate
* **Safe testing**: Test new configurations and secrets without affecting production
* **Team workflows**: Different team members can work in isolated environments
* **Staged deployments**: Deploy and test in staging before deploying to production

## Creating Environments

Create a new environment using the CLI:

```bash theme={null}
fal environments create staging --description "Staging environment"
```

## Listing Environments

View all your environments:

```bash theme={null}
fal environments list
```

| Name    | Description         | Default | Created At                 |
| ------- | ------------------- | ------- | -------------------------- |
| main    |                     | Yes     | 2024-01-01 00:00:00.000000 |
| staging | Staging environment |         | 2024-01-15 10:30:00.000000 |
| dev     | Development         |         | 2024-01-15 11:00:00.000000 |

## Using Environments

### Deploying to an Environment

Use the `--env` flag with `fal deploy` to create an app in a specific environment:

```bash theme={null}
# Deploy to staging (creates app in staging environment)
fal deploy path/to/myapp.py::MyApp --env staging

# Deploy to production (creates app in main environment)
fal deploy path/to/myapp.py::MyApp
```

Each deployment creates a separate app instance in the target environment. To have your application running in multiple environments, deploy it to each environment independently.

### Managing Secrets per Environment

Secrets are scoped to environments. Set different API keys or configurations for each environment:

```bash theme={null}
# Set a secret in the staging environment
fal secrets set API_KEY=staging-key-123 --env staging

# Set a different secret in production
fal secrets set API_KEY=production-key-456

# List secrets for a specific environment
fal secrets list --env staging
```

### Managing Apps per Environment

All app operations support the `--env` flag:

```bash theme={null}
# List apps in staging
fal apps list --env staging

# Scale an app in staging
fal apps scale my-app --min-concurrency 1 --env staging

# View runners for an app in staging
fal apps runners my-app --env staging

# Delete an app from staging
fal apps delete my-app --env staging
```

### Running Functions in an Environment

Use `fal run` with the `--env` flag to test functions with environment-specific secrets:

```bash theme={null}
fal run path/to/myapp.py::MyApp --env staging
```

## Deleting Environments

<Warning>
  **Deleting an environment is destructive and cannot be undone.**

  When you delete an environment, the following resources are **permanently deleted**:

  * All applications deployed to that environment
  * All secrets stored in that environment
  * All revision history for apps in that environment
</Warning>

```bash theme={null}
fal environments delete staging
```

You'll be prompted to confirm by typing the environment name. Use `--yes` to skip the confirmation:

```bash theme={null}
fal environments delete staging --yes
```

<Note>
  The `main` environment cannot be deleted.
</Note>

## Environment Workflow Example

Here's a typical workflow using environments. Note that deploying to different environments creates separate app instances—each with its own configuration, secrets, and endpoint:

```bash theme={null}
# 1. Create a staging environment
fal environments create staging

# 2. Set up staging secrets
fal secrets set DATABASE_URL=postgres://staging-db.example.com/app --env staging

# 3. Deploy to staging for testing (creates a separate app in the staging environment)
fal deploy path/to/myapp.py::MyApp --app-name my-app --env staging

# 4. Test the staging deployment (note the --staging suffix in the URL)
curl https://fal.run/your-user/my-app--staging

# 5. Once verified, deploy the same code to production (creates a separate app in main)
fal deploy path/to/myapp.py::MyApp --app-name my-app

# 6. Test the production deployment
curl https://fal.run/your-user/my-app

# 7. Clean up staging app when no longer needed
fal apps delete my-app --env staging
```

<Tip>
  When you deploy an app to a non-main environment, its endpoint URL includes an environment suffix (e.g., `my-app--staging`). Apps in the `main` environment have no suffix (e.g., `my-app`).
</Tip>

## Best Practices

* **Use descriptive names**: Name environments clearly (`staging`, `dev`, `qa`) so their purpose is obvious
* **Mirror production**: Keep staging as close to production configuration as possible
* **Separate secrets**: Never share secrets between environments; use environment-specific values
* **Clean up unused environments**: Delete environments that are no longer needed to avoid confusion
* **Document environment usage**: Make sure your team knows which environment to use for what purpose

## Reference

<CardGroup cols={2}>
  <Card title="CLI Reference" icon="terminal" href="/reference/cli/environments">
    Complete CLI documentation for `fal environments`
  </Card>

  <Card title="Secrets Guide" icon="key" href="/documentation/development/manage-secrets-securely">
    Managing secrets across environments
  </Card>
</CardGroup>
