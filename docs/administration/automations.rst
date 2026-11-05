Login automations
*****************

A login automation can use OpenID or SAML identity information to decide whether a user may sign in and to assign profile details, roles, workspace membership and user groups.
Manage it through the configured identity provider with :guilabel:`Manage Automations` and the required settings permissions.

Set up a login automation
=========================

#. Open the saved OpenID or SAML provider in :doc:`authentication settings </settings/authentication/index>`.
#. In its :guilabel:`Automation` section, choose :guilabel:`Create automation` or open the linked automation with :guilabel:`View automation`.
#. In :guilabel:`Configuration`, enter the name and Python code, choose whether it is enabled, and save the changes.
#. Test sign-in with a dedicated account. Open the automation's :guilabel:`Logs` tab to inspect its request, response and log output.

The :guilabel:`Automations` list provides access to existing automations. New login automations are created from the provider they belong to.

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

Use the complete response contract and event model in the `Integration SDK documentation <https://integration-sdk.fair-wizard.com/en/develop/>`_; this fragment shows the assignment fields, not the complete login response.
An empty array is valid when no membership should be added. A single-workspace instance still uses the array form.

How access is updated
=====================

Assignments apply on every relevant login. Listed workspace and group memberships are added; memberships omitted from the response remain.
A role value replaces the corresponding role. A missing or null role leaves an existing assignment unchanged, or uses the default for a new user/member.
Groups must belong to the workspace under which they are listed. Duplicate workspace entries or invalid role/group/workspace references make the login fail; validation completes before assignment changes are written.

.. warning::

   An automation can overwrite an organization role on login, including an administrator's role. Test with a dedicated account and keep a working administrative sign-in method before changing the automation.

Review failures in the automation's invocation log. For identity-provider configuration, see :doc:`/settings/authentication/index`.

.. figure:: /_static/screenshots/5.0/guide/automations.png
    :figclass: guide-screenshot
    :alt: Login automations in FAIR Wizard 5.0
    :width: 800

    Login automations.

.. figure:: /_static/screenshots/5.0/guide/automation-openid.png
    :figclass: guide-screenshot
    :alt: OPENID login automation configuration in FAIR Wizard 5.0
    :width: 800

    **Outdated example configuration.** OpenID automation layout; use the current response contract above rather than copying the pictured script.

.. TODO::

    Screenshot pending: OPENID automation invocation log with a controlled example; deferred by request.

.. figure:: /_static/screenshots/5.0/guide/automation-saml.png
    :figclass: guide-screenshot
    :alt: SAML login automation configuration in FAIR Wizard 5.0
    :width: 800

    **Outdated example configuration.** SAML automation layout; use the current response contract above rather than copying the pictured script.

.. TODO::

    Screenshot pending: SAML automation invocation log with a controlled example; deferred by request.
