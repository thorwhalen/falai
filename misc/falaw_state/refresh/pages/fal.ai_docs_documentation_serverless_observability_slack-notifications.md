> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack Notifications

> Receive real-time alerts in Slack when your apps fail to start.

Connect Slack to your fal account to receive notifications when your applications encounter startup issues. Get alerted immediately when a runner fails, so you can investigate before users are affected.

<Frame>
  <iframe className="w-full aspect-video rounded-lg" srcdoc="<style>*{padding:0;margin:0;overflow:hidden}html,body{height:100%}img,span{position:absolute;width:100%;top:0;bottom:0;margin:auto}span{height:1.5em;text-align:center;font:48px/1.5 sans-serif;color:white;text-shadow:0 0 0.5em black}</style><a href='https://www.youtube.com/embed/gDJJ9bppyV8?start=570&end=633&autoplay=1'><img src='/docs/images/video-thumbs/slack-notifications.jpg' alt='Slack Notifications - fal Serverless'><span>▶</span></a>" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />
</Frame>

## Setting Up Slack

<Steps>
  <Step title="Go to Notification Settings">
    Navigate to [**Dashboard > Notifications > Settings**](https://fal.ai/dashboard/notifications/settings)
  </Step>

  <Step title="Connect Slack">
    Click **Add to Slack** to begin the OAuth flow. This installs the fal bot into your Slack workspace.
  </Step>

  <Step title="Choose a Channel">
    Select the Slack channel where you want to receive notifications. The fal bot will automatically join this channel.
  </Step>
</Steps>

<Note>
  Any authenticated team member can connect Slack to receive notifications.
</Note>

## What You'll Be Notified About

### App Startup Timeout

Triggered when a runner's `setup()` method doesn't complete within the configured `startup_timeout`. The notification includes:

* App name and runner ID
* The timeout duration that was exceeded
* Link to logs for investigation
* Link to the startup timeout documentation

This typically indicates your model loading or initialization is taking too long. Consider optimizing your `setup()` method or increasing the `startup_timeout` value.

### App Startup Failure

Triggered when a runner's `setup()` method throws an error. The notification includes:

* App name and runner ID
* Link to logs to see the full error traceback

Common causes include missing dependencies, incorrect model paths, or out-of-memory errors during model loading.

### Queue Size Threshold

Triggered when the number of requests waiting in your app's queue exceeds a threshold over a time window. This usually means your app isn't scaling fast enough to meet demand, or callers are sending more traffic than your `max_concurrency` can handle.

### HTTP 5xx Threshold

Triggered when the number of HTTP 5xx responses from your app exceeds a threshold over a time window. A spike in server errors often points to a crashing endpoint, a bad deployment, or resource exhaustion.

## Per-App Notification Settings

You can configure alert thresholds for each app from the dashboard. These control when queue size and error rate notifications fire.

| Setting                         | Default | Description                                       |
| ------------------------------- | ------- | ------------------------------------------------- |
| `queue_size_threshold`          | 100     | Number of queued requests that triggers an alert  |
| `queue_size_threshold_duration` | 1h      | Lookback window for queue size (e.g., `5m`, `1h`) |
| `http_5xx_threshold`            | 100     | Number of 5xx responses that triggers an alert    |
| `http_5xx_threshold_duration`   | 1h      | Lookback window for 5xx count (e.g., `5m`, `1h`)  |

Set a threshold to `null` to disable that notification type. Lower durations (e.g., `5m`) make alerts more sensitive to short spikes; longer durations (e.g., `1h`) smooth out transient errors.

## Managing Your Connection

From the [Notification Settings](https://fal.ai/dashboard/notifications/settings) page you can:

* **View connection status** -- See if Slack is connected, and which workspace and channel are configured
* **Change channel** -- Switch notifications to a different Slack channel
* **Reconnect** -- If the bot token expires or the bot is removed from your workspace, reconnect with one click

## Troubleshooting

**Not receiving notifications?**

* Verify the fal bot is still in your selected channel (it may have been removed)
* Check that your Slack connection hasn't expired in the notification settings
* Ensure the app experiencing issues belongs to your team account

**Bot was removed from workspace?**

* Go to notification settings and click **Reconnect** to re-authorize the fal bot

<Card title="Monitor Performance" icon="arrow-right" href="/documentation/serverless/observability/monitor-performance">
  View real-time metrics and logs in the fal dashboard
</Card>
