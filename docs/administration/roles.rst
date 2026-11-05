.. _roles:

Roles and permissions
*********************

Roles define what a user can do. Organization roles apply across the instance; with multiple workspaces, a member can also have a role in the selected workspace.
The Admin role is fixed. We can create and edit other roles, so their names and permissions can differ between instances.

.. figure:: /_static/screenshots/5.0/guide/settings-roles.png
    :figclass: guide-screenshot
    :alt: Organization roles and default role in FAIR Wizard 5.0
    :width: 800

    Organization roles and default role.

Create or edit a role
=====================

We can create or edit roles in :guilabel:`Roles` settings with the :guilabel:`Manage Roles` permission. We need to enter a name and select the permissions. Changes affect users assigned to the role.
A role cannot be deleted while it is assigned to users or selected as a default.

.. list-table:: Main permission groups
   :header-rows: 1

   * - Group
     - Examples and effect
   * - Projects
     - Create Projects; view, comment on, edit or manage ALL Projects; Manage Project Templates.
   * - Knowledge models
     - Manage Knowledge Models, including secrets and Data Sources; Use Knowledge Model Editor.
   * - Document templates
     - Manage Document Templates; Use Document Template Editor.
   * - People
     - Manage Users; Manage Roles; Create User Groups; Manage User Groups.
   * - Settings and administration
     - Manage Settings; Manage Automations; Use Audit Log.
   * - Analytics
     - Use Analytics.
   * - Connected AI clients
     - Connect AIs; Change Data with Connected AIs; Change Sensitive Data with Connected AIs.

Creating projects requires Create Projects, and creating user groups requires Create User Groups. Permissions to manage existing projects or groups do not replace these permissions.
Editor permissions include the corresponding content-management permission; wider project permissions include the lower project access levels.

.. admonition:: With multiple workspaces

   We get permissions from both our organization role and our role in the selected workspace. Organization permissions can apply across workspaces. Permissions from a workspace role apply only in that workspace.
   Additional organization controls include Manage Workspaces and Manage Library, while Manage Members applies to workspace membership.
   Manage Settings and Manage Workspace Settings are separate. In single-workspace mode the role editor presents one Manage Settings control covering both settings categories.

.. figure:: /_static/screenshots/5.0/guide/role-create.png
    :figclass: guide-screenshot
    :alt: Custom role editor showing project creation and organization-wide project permissions
    :width: 350

    Project permissions in a custom role.

Default role
============

In the organization's Roles list, choose :guilabel:`Set as default` beside the role to use for newly registered users. Choose only the permissions those users need.
With multiple workspaces, this organization default is separate from the role assigned to a workspace member; see :doc:`/administration/workspaces`.

Project sharing is separate
===========================

Viewer, Commenter, Editor and Owner are the fixed sharing roles for an individual project. Organization or workspace roles may independently grant access to all projects in their scope.
Use :doc:`/projects/detail/sharing` to manage a particular project's collaborators.

Examples of custom roles
========================

A support role can receive view or comment access to projects, a content role can prepare knowledge models and document templates, and a user-management role can manage accounts. Choose the actual permissions and their prerequisites from the matrix above rather than relying on a role's name.

Before changing a role, review the people assigned to it. The changed permissions apply to those accounts. Use project sharing for access to a particular project, alongside the wider permissions granted by roles.
