Manage workspaces
*****************

This page applies when an Enterprise organization uses multiple workspaces. Professional uses a single workspace; Enterprise can also operate in single-workspace mode.
Existing content initially stays together during the 5.0 migration. Organizing that content into multiple workspaces is a separate, planned step with the FAIR Wizard team.

Create and configure a workspace
================================

In the organization area, open :guilabel:`Workspaces` and create a workspace with its name and description.
Workspace branding can be configured there. Workspace creation and management require :guilabel:`Manage Workspaces`.
Enabling multi-workspace mode is a one-way change; plan the content and membership mapping before it is enabled.

Members and roles
=================

Open the workspace's :guilabel:`Members` page to add existing organization users, assign workspace roles or remove membership. This requires :guilabel:`Manage Members`.
After creating a user account, we also need to add the user to the workspaces they should use.

Removing a member removes their user-group memberships and explicit project access in that workspace. The user may still have access through their organization role. See :doc:`/administration/roles` for how organization and workspace permissions work together.

Notifications
=============

An affected active user is notified when someone else adds them to a workspace, changes their workspace role or removes them. Organization-role changes also have notifications.
Self-changes, unchanged roles and assignments made by login automation do not send these notifications.

Delete a workspace
==================

Review its content and members before deleting a workspace. Deletion removes its workspace-owned content and access assignments; it is not a way to move projects to another workspace.
Use the deletion impact shown by FAIR Wizard and make sure the required content has been preserved before continuing.
