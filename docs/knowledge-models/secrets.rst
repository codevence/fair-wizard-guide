.. _knowledge-model-secrets:

Knowledge model secrets
***********************

Secrets store values such as API keys used by integrations, without including them in question text or saved answers.
Managing them requires :guilabel:`Manage Knowledge Models`.

Create or replace a secret
==========================

Open :guilabel:`Knowledge Models` → :guilabel:`Secrets`, choose a name and enter the value needed by the integration.
FAIR Wizard does not return existing secret values to the browser. To change a value, supply a replacement; leaving a value unchanged is different from replacing it with an empty value.

.. admonition:: With multiple workspaces

   The organization can provide shared secrets. A workspace can provide its own value with the same name, which takes precedence for integrations in that workspace. Check the current organization/workspace area before editing a credential.

Refer to :doc:`/development/integration-questions/integration-api` when configuring how an integration uses a secret.

Earlier interface
=================

These screenshots show the 4.x interface. They will be replaced with 5.0 screenshots.

.. figure:: /_static/earlier-interface/applications/data-management-planner/knowledge-models/secrets/secrets.png
    :alt: List of knowledge model secrets.

    **Outdated screenshot (4.x).** List of knowledge model secrets.
