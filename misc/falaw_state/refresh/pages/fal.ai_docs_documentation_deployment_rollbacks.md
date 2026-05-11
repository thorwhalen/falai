> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Rollbacks & Revisions

> Manage app revisions, roll back to previous versions, and restart runners.

Every time you run `fal deploy`, a new **revision** is created. Your app's alias (e.g., `my-model`) always points to one active revision. You can switch between revisions to roll back to a previous version instantly.

<Frame>
  <iframe className="w-full aspect-video rounded-lg" srcdoc="<style>*{padding:0;margin:0;overflow:hidden}html,body{height:100%}img,span{position:absolute;width:100%;top:0;bottom:0;margin:auto}span{height:1.5em;text-align:center;font:48px/1.5 sans-serif;color:white;text-shadow:0 0 0.5em black}</style><a href='https://www.youtube.com/embed/gDJJ9bppyV8?start=483&end=570&autoplay=1'><img src='/docs/images/video-thumbs/rollbacks.jpg' alt='Deployment Rollbacks - fal Serverless'><span>▶</span></a>" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />
</Frame>

## Viewing Revisions

### CLI

```bash theme={null}
fal apps list-rev my-model
```

This shows all revisions with their IDs, creation dates, machine types, and scaling configuration.

### Dashboard

Navigate to [**Dashboard > Apps > \[your-app\] > Versions**](https://fal.ai/dashboard/apps). The versions page shows:

* All revisions with creation timestamps
* Status badges: **Deployed**, **Failed**, **Deploying**, **Suspended**
* The current active revision marked with a **Current** badge

***

## Rollouts

A rollout **restarts all runners** without changing the revision. Your app stays on the same code, but all runners are recycled.

### CLI

```bash theme={null}
# Graceful rollout (runners finish current requests before stopping)
fal apps rollout my-model

# Force rollout (runners are killed immediately)
fal apps rollout my-model --force
```

### When to Use Rollouts

* **After changing secrets** -- Runners need to restart to pick up new environment variable values
* **Clearing bad state** -- A runner is stuck or has corrupted in-memory state
* **Memory cleanup** -- Long-running runners have accumulated memory that won't be freed
* **After a config change** -- You changed scaling params via CLI and want runners to restart cleanly

<Warning>
  A force rollout (`--force`) kills runners immediately, dropping any in-progress requests. Use graceful rollouts in production unless you need an emergency restart.
</Warning>

***

## Rolling Back

Switch your app to a previous revision. The old code starts serving requests immediately -- no rebuild needed.

### CLI

```bash theme={null}
# List revisions to find the ID you want
fal apps list-rev my-model

# Switch to a specific revision
fal apps set-rev my-model <revision_id>
```

### Dashboard

1. Go to **Dashboard > Apps > \[your-app] > Versions**
2. Find the revision you want to roll back to
3. Click **Rollback**
4. Confirm in the dialog

<Note>
  When you roll back, runtime-tunable scaling parameters (`keep_alive`, `min_concurrency`, etc.) are inherited from the currently active revision. Code-specific parameters (`max_multiplexing`, `startup_timeout`, `machine_type`) come from the target revision's code.
</Note>

### Rollback Strategies

When you roll back with `fal apps set-rev`, you can also choose how fal rolls traffic to the target revision:

```bash theme={null}
# Switch only after the target revision has a healthy runner
fal apps set-rev my-model <revision_id> --strategy rolling

# Switch immediately and let runners start on demand
fal apps set-rev my-model <revision_id> --strategy recreate
```

* **Rolling** starts a runner on the target revision first and waits for it to complete `setup()` and become healthy before switching the alias. Use this when you want the safest rollback with the least user-visible interruption.
* **Recreate** switches the alias to the target revision immediately. No runner is started proactively, so the next request may cold start the rolled-back revision. Use this when speed matters more than avoiding a brief interruption.

<Note>
  These strategies control how the rollback is applied. A rollback still switches your app to a different revision; a rollout still restarts runners without changing revisions.
</Note>

### When to Roll Back

* A new deploy introduced a bug
* Model performance regressed after an update
* You need to quickly revert while investigating an issue

***

## Deleting Revisions

Clean up old revisions you no longer need.

### CLI

```bash theme={null}
fal apps delete-rev my-model <revision_id>
```

### Dashboard

On the **Versions** page, use the delete option on any non-current revision.

<Note>
  You cannot delete the currently active revision. Switch to a different revision first if you need to delete it.
</Note>

***

## Rollback vs Rollout

|                    | Rollback                                          | Rollout                               |
| ------------------ | ------------------------------------------------- | ------------------------------------- |
| **What changes**   | Switches to a different revision (different code) | Restarts runners on the same revision |
| **Use case**       | Revert to a previous version                      | Refresh runner state                  |
| **Rebuild needed** | No (previous image already exists)                | No                                    |
| **Downtime**       | Brief (new runners start on the old revision)     | Brief (runners restart)               |
| **CLI**            | `fal apps set-rev`                                | `fal apps rollout`                    |
