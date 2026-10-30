Login automations
*****************

A login automation can use OpenID or SAML identity information to decide whether a user may sign in and to assign profile details, roles, workspace membership and user groups.
Manage it through the configured identity provider with :guilabel:`Manage Automations` and the required settings permissions.

Assignments in 5.0
==================

An authorized response includes a required ``workspaces`` array. Each entry identifies one workspace, an optional workspace role and the user groups to add there. An optional ``tenantRoleUuid`` assigns the organization role.
The assignment part of a response has this structure (the UUIDs below are illustrative):

.. code-block:: json

   {
     "tenantRoleUuid": null,
     "workspaces": [
       {
         "workspaceUuid": "11111111-1111-4111-8111-111111111111",
         "roleUuid": null,
         "userGroupUuids": []
       }
     ]
   }

Use the complete response contract and event model of the compatible Integration SDK; this fragment shows the assignment fields, not the complete login response.
An empty array is valid when no membership should be added. A single-workspace instance still uses the array form.

How access is updated
=====================

Assignments apply on every relevant login. Listed workspace and group memberships are added; memberships omitted from the response remain.
A role value replaces the corresponding role. A missing or null role leaves an existing assignment unchanged, or uses the default for a new user/member.
Groups must belong to the workspace under which they are listed. Duplicate workspace entries or invalid role/group/workspace references make the login fail; validation completes before assignment changes are written.

.. warning::

   An automation can overwrite an organization role on login, including an administrator's role. Test with a dedicated account and keep a working administrative sign-in method before changing the automation.

Review failures in the automation's invocation log. For identity-provider configuration, see :doc:`/settings/authentication/index`.

Earlier interface
=================

These screenshots show the 4.x interface. They will be replaced with 5.0 screenshots.

.. figure:: /_static/earlier-interface/applications/admin-center/automations/automations/list.png
    :alt: List of Automations with possible actions.

    **Outdated screenshot (4.x).** List of Automations with possible actions.

.. figure:: /_static/earlier-interface/applications/admin-center/automations/automations/openid-configuration.png
    :alt: Example of OpenID Automation configuration.

    **Outdated screenshot (4.x).** Example of OpenID Automation configuration.

.. figure:: /_static/earlier-interface/applications/admin-center/automations/automations/openid-logs.png
    :alt: Each run of an Automation is logged.

    **Outdated screenshot (4.x).** Each run of an Automation is logged.

.. figure:: /_static/earlier-interface/applications/admin-center/automations/automations/saml-configuration.png
    :alt: Example of SAML Automation configuration.

    **Outdated screenshot (4.x).** Example of SAML Automation configuration.

.. figure:: /_static/earlier-interface/applications/admin-center/automations/automations/saml-logs.png
    :alt: Each run of an Automation is logged.

    **Outdated screenshot (4.x).** Each run of an Automation is logged.
