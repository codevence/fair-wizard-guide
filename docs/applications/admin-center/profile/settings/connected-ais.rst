FAIR Wizard MCP
===============

The FAIR Wizard MCP server lets you ask natural-language questions about your FAIR Wizard instance and get answers based on your projects, knowledge models, document templates, metrics, and generated documents.

It is especially useful for instance analytics, for example:

* finding projects that need attention,
* reviewing FAIR metrics across projects,
* checking document template usage,
* seeing which knowledge models are used most often,
* listing project documents,
* checking who has access to a project.

.. contents:: On this page
   :local:
   :depth: 2

Before You Start
----------------

In FAIR Wizard, open:

1. ``User Settings``
2. ``Connected AIs``

On that page, FAIR Wizard shows:

* the **Connection URL**,
* the **Authentication** method.

The page currently provides a connection URL in this format:

.. code-block:: text

   https://<your-instance>/mcp

The authentication method is **OAuth**.

Use the connection settings shown on the ``Connected AIs`` page when connecting your AI client. Once connected, your AI agent can access FAIR Wizard and interact with its resources on your behalf.

Connecting in Claude
--------------------

In Claude:

1. Open the menu in the top-left corner and click ``Customize``.
2. Select ``Connectors``.
3. Click ``Add`` in the top-right corner and choose ``Custom connector``.
4. Enter any name for the connector.
5. In FAIR Wizard, open your user profile and go to ``Connected AIs``:

   ``https://<your-instance-url>/admin/users/edit/current/connected-ais``

6. Copy the **Connection URL** shown there.
7. In Claude, paste it into the ``Remote MCP server URL`` field.
8. Leave the ``Advanced settings`` unchanged.
9. After a short while, a ``Connect`` button should appear. Click it to open FAIR Wizard.
10. If you are not already signed in, sign in and authorize the connection. You will then be redirected back automatically.
11. The MCP server is now connected.

Connecting in ChatGPT
---------------------

In ChatGPT:

1. Open ``Settings``.
2. Select ``Plugins`` from the left-hand menu.
3. Click the ``+`` button.
4. Enter any name for the plugin.
5. In FAIR Wizard, open your user profile and go to ``Connected AIs``:

   ``https://<your-instance-url>/admin/users/edit/current/connected-ais``

6. Copy the **Connection URL** shown there.
7. In ChatGPT, paste it into the ``Connection`` field.
8. Leave the remaining settings unchanged and acknowledge the warning that custom MCP servers introduce risk.
9. Click ``Publish`` and accept the terms.
10. After a short while, a ``Connect`` button should appear. Click it to open FAIR Wizard.
11. If you are not already signed in, sign in and authorize the connection. You will then be redirected back automatically.
12. The MCP server is now connected.

Connecting in Codex
-------------------

On the ``Connected AIs`` page, copy the **Connection URL**.

Add FAIR Wizard to your Codex MCP configuration:

.. code-block:: toml

   [mcp_servers.fair_wizard]
   enabled = true
   url = "https://<your-instance>/mcp"

When Codex prompts you to sign in, complete the **OAuth** flow.

Restart Codex if needed, then start a new chat and ask questions such as:

* ``List my FAIR Wizard projects.``
* ``Show me projects with the lowest FAIR metrics.``
* ``List documents generated for project <project-uuid>.``

What You Can Ask
----------------

The FAIR Wizard MCP server is best used for short, direct questions. Good examples include:

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

For the best answers:

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

These prompts work well for dashboards, reporting, and quick reviews:

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

If you already know exactly which project, knowledge model, or document template you want to inspect, include its UUID in your prompt for the fastest result.
