> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# App Events

> Track deployments, runner lifecycle, and config changes with a full audit trail.

App Events gives you a chronological timeline of everything that happens to your application -- who deployed, when runners started or failed, and what configuration changed. Use it to debug incidents, audit team activity, and understand your app's lifecycle.

<Frame>
  <iframe className="w-full aspect-video rounded-lg" srcdoc="<style>*{padding:0;margin:0;overflow:hidden}html,body{height:100%}img,span{position:absolute;width:100%;top:0;bottom:0;margin:auto}span{height:1.5em;text-align:center;font:48px/1.5 sans-serif;color:white;text-shadow:0 0 0.5em black}</style><a href='https://www.youtube.com/embed/gDJJ9bppyV8?start=222&end=278&autoplay=1'><img src='/docs/images/video-thumbs/app-events.jpg' alt='App Events - fal Serverless'><span>▶</span></a>" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />
</Frame>

## What You Can Track

Navigate to [**Dashboard > Apps > \[your-app\] > Events**](https://fal.ai/dashboard/apps) to see the timeline. You can search, filter by event category (runner, deployment, config), and set a date range.

App Events tracks three categories of activity:

**Runner events** show the lifecycle of individual runners: when they were scheduled, when they started pulling your image, when `setup()` ran, and when they became ready or failed. Failure events include the stage that failed (SETUP, DOCKER\_PULL, etc.), so you can quickly tell whether the problem is your image, your setup code, or infrastructure.

**Deployment events** track when deployments start, succeed, or fail. Use these to correlate performance changes with deploys. If latency spiked right after a deploy, you know where to look.

**Config change events** record who changed what, with a diff of old vs new values. This is the audit trail for scaling parameter changes, machine type updates, and auth mode switches.

## API Access

Query events programmatically:

```bash theme={null}
curl "https://rest.fal.ai/applications/your-username/your-app/events?since=2026-02-17T00:00:00Z" \
  -H "Authorization: Key $FAL_KEY"
```

### Parameters

| Parameter    | Description                                                     |
| ------------ | --------------------------------------------------------------- |
| `since`      | Start time (ISO 8601)                                           |
| `until`      | End time (ISO 8601)                                             |
| `categories` | Filter by event type (e.g., `runner_started`, `config_changed`) |
| `page`       | Page number                                                     |
| `size`       | Events per page                                                 |

<CardGroup cols={2}>
  <Card title="Error Analytics" icon="arrow-right" href="/documentation/serverless/observability/error-analytics">
    Analyze error patterns across your apps
  </Card>

  <Card title="Slack Notifications" icon="arrow-right" href="/documentation/serverless/observability/slack-notifications">
    Get notified when runners fail
  </Card>
</CardGroup>
