> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Deployments

> Once your models are deployed to production, you need tools and strategies to manage them effectively. This guide covers listing deployments, monitoring application health, managing multiple versions, and safely removing models.

## Listing Deployments

View all your deployed models to understand your current production environment:

```bash theme={null}
fal apps list
```

This shows all your deployed models with their current status, versions, and basic configuration. Use this to get an overview of your model portfolio and identify which models need attention.

## Organizing Apps with Tags

You can assign custom tags to your apps from the [fal dashboard](https://fal.ai/dashboard) to keep your app list organized. Tags are visual labels — use them to group apps by team, project, model type, or any category that fits your workflow, then filter the app listing to quickly find what you need.

<Info>
  Tags are managed entirely through the dashboard UI — they don't isolate secrets, affect routing, or change app behavior. If you need isolated deployment stages (dev, staging, production) with separate secrets and endpoints, use [Environments](/serverless/deployment-operations/manage-environments) instead.
</Info>

## Managing Versions

### Viewing Model Revisions

Each deployment creates a new revision. List all revisions for a specific model:

```bash theme={null}
fal apps list-rev myapp
```

### Switching Between Revisions

If you need to roll back to a previous model version or switch to a different revision:

```bash theme={null}
fal apps set-rev myapp uuid_of_revision
```

This is useful for quick rollbacks when a new model version has issues in production.

## Scaling Deployments

After deployment, you can adjust scaling parameters without redeploying:

```bash theme={null}
fal apps scale myapp --min-concurrency 2 --max-concurrency 20
```

For comprehensive scaling configuration and strategies, see [Scale Your Application](/serverless/deployment-operations/scale-your-application/).

## Monitoring Health

### Basic Health Checks

Monitor your model's health and performance using the fal dashboard, or check active runners:

```bash theme={null}
fal apps runners myapp
```

<Info>
  For detailed performance monitoring, metrics collection, and alerting strategies, see [Monitor Performance](/serverless/deployment-operations/monitor-performance/).
</Info>

## Removing Deployments

### Safe Deletion Process

Before deleting a model deployment:

<Steps>
  <Step title="Verify dependencies:">
    Ensure no other services or applications depend on this model
  </Step>

  <Step title="Check traffic:">
    Review recent usage to understand impact
  </Step>

  <Step title="Backup if needed:">
    Document model configuration or export important data
  </Step>
</Steps>

### Delete a Deployment

```bash theme={null}
fal apps delete myapp
```

**Warning**: This permanently removes the model deployment. The model cannot be recovered after deletion.

### Delete Specific Revisions

To clean up old revisions while keeping the current deployment:

```bash theme={null}
fal apps delete-rev myapp --revision-id abc123
```
