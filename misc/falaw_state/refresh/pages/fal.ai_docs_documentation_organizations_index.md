> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Organizations

> Centralized management for teams, billing, and model access across your company.

Organizations give enterprise customers a parent account that manages multiple [teams](/documentation/setting-up/teams) under a single umbrella. While standalone teams work well for small groups, organizations add centralized policies, SSO enforcement, cross-team billing visibility, and model access controls. Every team within an organization maintains its own API keys, secrets, deployed apps, and billing, but inherits policies set at the organization level.

If you are already using teams on fal and need centralized control over team creation, member management, or which models your teams can access, an organization is the next step. Organizations are available on enterprise plans. Contact [sales](https://fal.ai/enterprise#contact-sales) to get started.

## Organizations vs Teams

A team is a single group with its own API keys, secrets, apps, and billing. An organization is a parent account that manages multiple teams with shared policies.

```
Organization (root)
├── Team A (e.g., Research)
├── Team B (e.g., Production)
└── Team C (e.g., Platform)
```

Each child team operates independently for day-to-day work. The organization controls policies that apply across all teams, like who can create new teams, whether members need SSO, and which models are allowed.

## What Org Admins Can Do

Organization admins have centralized control over the full team lifecycle. They can create and archive teams, view and manage members across all teams (roles, assignments, invites), and configure policies that apply organization-wide. On the billing side, org admins can view invoices across all teams and set spending alerts. For security, they can enforce SSO for all team members and restrict which models teams can access via the API or Playground.

## Request Visibility

Organizations can enable **restricted request view** to limit team members to only seeing their own request payloads and logs. This is configured in the organization admin dashboard under "Restricted request view."

When enabled, the system tracks how each request was authenticated. When a team member views requests in the dashboard, they only see payloads for requests where their identity matches the request's authentication method.

<Warning>
  **Playground and API key submissions behave differently under restricted view:**

  * **Playground submissions** are authenticated with your personal login token. You can see your own Playground requests.
  * **API key submissions** are authenticated with the team's API key, not your personal identity. You cannot see API-submitted request payloads in the dashboard, even if you submitted them, because the API key identity does not match your personal login.

  If your team needs per-user request isolation for API submissions, contact support to discuss options.
</Warning>

## SSO Account Visibility

Organizations with SSO can restrict whether users can access their personal fal account alongside their SSO-linked team account. This ensures users only interact through the organization's managed teams. See [Managing Teams](/documentation/organizations/managing-teams) for configuration details.

## Next Steps

<CardGroup cols={2}>
  <Card title="Managing Teams" icon="arrow-right" href="/documentation/organizations/managing-teams">
    Team lifecycle, member management, and org-wide policies
  </Card>

  <Card title="Model Access Controls" icon="arrow-right" href="/documentation/organizations/access-controls">
    Restrict which models your teams can use
  </Card>
</CardGroup>
