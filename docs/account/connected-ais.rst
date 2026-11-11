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

.. figure:: /_static/screenshots/5.0/guide/connected-ais.png
    :figclass: guide-screenshot
    :alt: Connected AIs in FAIR Wizard 5.0
    :width: 800

    Connected AIs.

.. figure:: /_static/screenshots/5.0/guide/mcp-authorization.png
    :figclass: guide-screenshot
    :alt: Connect AI authorization in FAIR Wizard 5.0
    :width: 800

    Connect AI authorization.

Connecting in Claude
====================

#. Open :guilabel:`Customize` → :guilabel:`Connectors` in Claude.
#. Choose :guilabel:`Add` → :guilabel:`Add custom connector` and give it a name.
#. Paste the connection URL from FAIR Wizard into the remote MCP server URL field.
#. Continue through the detected authentication settings. Use OAuth sign-in for FAIR Wizard and complete the configuration.
#. Choose :guilabel:`Connect` when requested, sign in to FAIR Wizard and review the authorization before accepting it.
#. Enable the connector for the conversation where you want to use it.

In a managed Claude organization, an owner may need to add the connector first. Follow the `official Claude connector instructions <https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp>`_ for the controls available to your account.

Connecting in ChatGPT
=====================

#. Open ChatGPT's :guilabel:`Plugins` page.
#. Use the plus button and select :guilabel:`Add custom MCP server`.
#. Enter a name and description, then paste the FAIR Wizard connection URL under :guilabel:`Connection`.
#. Configure OAuth, review the warning and continue if you accept it.
#. Choose :guilabel:`Create as a plugin`, review the discovered tools and install the plugin.
#. Complete FAIR Wizard's sign-in and authorization when prompted.
#. Start a conversation, type ``@`` and select the plugin.

Account and organization policies can restrict custom connections. See the `official ChatGPT connection instructions <https://developers.openai.com/plugins/deploy/connect-chatgpt>`_ if a control is unavailable.

Connecting in Codex
===================

Copy the connection URL from FAIR Wizard, then register it with the Codex CLI:

.. code-block:: shell

   codex mcp add fair_wizard --url https://<your-instance>/api/mcp
   codex mcp login fair_wizard
   codex mcp list

Complete the OAuth sign-in in the browser. Alternatively, add the server to your Codex ``config.toml``:

.. code-block:: toml

   [mcp_servers.fair_wizard]
   enabled = true
   url = "https://<your-instance>/api/mcp"

Use ``codex mcp login fair_wizard`` to authorize a configured server, then start a new session. The `official Codex MCP reference <https://learn.chatgpt.com/docs/extend/mcp>`_ describes configuration and troubleshooting.


What You Can Ask
----------------

The following requests show how to explore projects, metrics, documents and access:

Projects
~~~~~~~~

* ``List my FAIR Wizard projects.``
* ``Which projects need the most attention right now?``
* ``Show projects with low completion or weak FAIR metrics.``
* ``Which projects look stale or inactive?``
* ``Summarize project <project-uuid>.``

Metrics
~~~~~~~

* ``Show FAIR metrics for project <project-uuid>.``
* ``Which projects are doing worst on FAIR metrics?``
* ``Compare FAIR metrics across projects.``

Documents
~~~~~~~~~

* ``List generated documents for project <project-uuid>.``
* ``Which projects have generated documents?``
* ``Which templates produce the most documents?``

Knowledge Models
~~~~~~~~~~~~~~~~

* ``Which projects use knowledge model <knowledge-model-uuid>?``
* ``Show me projects using this knowledge model: <knowledge-model-uuid>.``

Document Templates
~~~~~~~~~~~~~~~~~~

* ``Which projects use document template <document-template-uuid>?``
* ``Show usage of document template <document-template-uuid>.``

Project Access
~~~~~~~~~~~~~~

* ``Who has access to project <project-uuid>?``
* ``List user groups assigned to project <project-uuid>.``

Tips for Better Results
-----------------------

When writing a request:

* ask one question at a time,
* be specific about what you want to compare or list,
* use a project UUID when you want detail for one exact project,
* use a knowledge model or document template UUID when asking about their usage,
* start broad, then narrow down with follow-up questions.

Example workflow:

1. ``List my FAIR Wizard projects.``
2. ``Which of these projects need the most attention?``
3. ``Show FAIR metrics for project <project-uuid>.``
4. ``Who has access to that project?``

Common Analytics Questions
--------------------------

For dashboards and reports, we can ask:

* ``Which projects are incomplete?``
* ``Which projects have the lowest FAIR scores?``
* ``Which projects seem stale?``
* ``Which document templates are used most often?``
* ``Which knowledge models are used across the most projects?``
* ``Which projects have generated the most documents?``
* ``Which projects have many users or groups assigned?``

When to Use FAIR Wizard MCP
---------------------------

Use FAIR Wizard MCP when you want to:

* explore your FAIR Wizard instance conversationally,
* get quick answers without opening multiple screens,
* identify projects that need review,
* compare usage across projects, templates, or knowledge models,
* support reporting or operational monitoring.

If you already know exactly which project, knowledge model, or document template you want to inspect, include its UUID in your prompt so the client can identify it.


Permissions and confirmation
============================

Our role controls :guilabel:`Connect AIs`, :guilabel:`Change Data with Connected AIs` and :guilabel:`Change Sensitive Data with Connected AIs` separately.
The AI client also needs our permission for the action it performs. For example, it can only edit a project if we have permission to edit that project.

Some actions require confirmation. We need to check what will change before confirming, especially when deleting content.
MCP activity is identified in the audit log with the client and tool used.

Disconnect a client
===================

Review the connected clients in account settings and revoke connections you no longer use. See :doc:`/account/api-keys` for API keys used directly by integrations.
