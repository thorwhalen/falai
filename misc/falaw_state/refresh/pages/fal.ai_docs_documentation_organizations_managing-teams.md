> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Teams

> Control team lifecycle, member management, and organization-wide policies.

Organization administrators manage teams and members from the [Organization dashboard](https://fal.ai/dashboard/organization). This page covers the day-to-day operations of running an organization: creating and archiving teams, managing members across teams, and configuring the policies that govern how teams operate.

For an overview of what organizations are and when you need one, see [Organizations](/documentation/organizations/index). For controlling which models teams can access, see [Model Access Controls](/documentation/organizations/access-controls).

## Team Lifecycle

Org admins can create new teams from the Organization dashboard. New teams are automatically associated with your organization and inherit org-wide policies. You can control whether child team admins are also allowed to create teams, or restrict team creation to org admins only.

When a team is no longer needed, org admins can archive it. Archived teams are locked and can no longer deploy apps, make API calls, or create compute instances. Existing deployed apps stop serving requests. To reverse an archive, contact the fal team.

<Warning>
  Archiving a team locks the account and stops all deployed apps from serving requests.
</Warning>

## Team Roles

Every team member has one of three roles. The role determines what they can access within the team.

| Role          | What they can do                                                                                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Admin**     | Full team management: invite and remove members, manage API keys, configure scaling, set up [log drains](/documentation/serverless/observability/log-drains), and access all team settings. |
| **Developer** | Deploy and manage apps, view analytics, access logs, and use the API. This is the default role for new members.                                                                             |
| **Billing**   | View and manage billing: invoices, payment methods, spending alerts, and usage analytics. Cannot deploy apps or manage members.                                                             |

Admin and Billing roles can both access billing-related features. Only Admins can invite members, manage API keys, or configure log drains.

## Member Management

The Organization dashboard provides a unified view of all members across all teams. You can see which teams each member belongs to and their roles, filter by team or status (active, pending, unassigned), change roles or reassign members between teams, and onboard multiple members via CSV upload with team assignments.

Org admins can invite members to any team in the organization. You can also control whether child team admins are allowed to send invites themselves, or require all invitations to go through org admins.

<Tip>
  When SSO is configured, invites can require members to authenticate through your identity provider before joining.
</Tip>

## Organization Policies

These policies are configured from the Organization dashboard and apply across all child teams.

| Policy                     | What it controls                                                                                                                                                          |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Team Creation**          | Whether child team admins can create new teams, or only org admins can.                                                                                                   |
| **Invite Permissions**     | Whether child team admins can invite new members, or all invitations must go through org admins.                                                                          |
| **Cross-Team Visibility**  | Whether admins and billing managers can see analytics and usage across all teams, not just their own.                                                                     |
| **Request Visibility**     | Whether team members see all requests made by their team, or only their own. Useful for organizations handling sensitive data.                                            |
| **SSO Account Visibility** | Whether users can access their personal fal account alongside their SSO-linked team account. Disabling this ensures users only interact through the organization's teams. |

## Billing Across Teams

Each team in an organization maintains its own billing and subscription. Org admins with billing access can view invoices across all teams from the Organization dashboard, set spending alerts for any team, and monitor usage analytics across the organization (when cross-team visibility is enabled).

<Card title="Model Access Controls" icon="arrow-right" href="/documentation/organizations/access-controls">
  Control which models your teams can access
</Card>
