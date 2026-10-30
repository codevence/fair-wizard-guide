Connected AIs
*************

We can connect AI clients to FAIR Wizard using the Model Context Protocol (MCP). Depending on our permissions, they can read data and create or edit knowledge models, document templates, projects and other resources.
The built-in AI Assistant provides help based on the guide; connected AI clients can also work with data in our instance.

Connect a client
================

#. Open your account settings and :guilabel:`Connected AIs`.
#. Copy the connection URL shown by FAIR Wizard. The 5.0 MCP endpoint is under the instance API, normally ``https://<instance>/api/mcp``.
#. Add that URL in the AI client's MCP connection settings, or use the supported client package offered by FAIR Wizard.
#. Complete the OAuth sign-in and authorization flow.

Use the connection information shown by your instance rather than an address from a previous release. Existing clients connected to the old MCP service need to be reconnected for 5.0.

Permissions and confirmation
============================

Our role controls :guilabel:`Connect AIs`, :guilabel:`Change Data with Connected AIs` and :guilabel:`Change Sensitive Data with Connected AIs` separately.
The AI client also needs our permission for the action it performs. For example, it can only edit a project if we have permission to edit that project.

Some actions require confirmation. We need to check what will change before confirming, especially when deleting content.
MCP activity is identified in the audit log with the client and tool used.

Disconnect a client
===================

Review the connected clients in account settings and revoke connections you no longer use. See :doc:`/account/api-keys` for API keys used directly by integrations.
