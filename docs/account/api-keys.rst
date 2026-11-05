.. _api-keys:

API keys
********

API keys allow scripts and integrations to use FAIR Wizard with our account's permissions. We can create or revoke keys in :guilabel:`User Settings` → :guilabel:`API Keys`.
When creating a key, we enter a name and choose when it expires. We need to save the generated key securely. Integrations use it as a Bearer token.

A key does not bypass role permissions. With multiple workspaces, API calls still need the correct scope for the operation.
Revoke a key when its integration is retired or its value may have been exposed.

Use :doc:`/development/api` for API addresses and workspace-scoping rules. For changes to existing integrations, see :doc:`/upgrade/index`.

.. figure:: /_static/screenshots/5.0/guide/api-key-create.png
    :figclass: guide-screenshot
    :alt: Create an API key in FAIR Wizard 5.0
    :width: 350

    Create an API key.

.. figure:: /_static/screenshots/5.0/guide/account-api-keys.png
    :figclass: guide-screenshot
    :alt: API keys in FAIR Wizard 5.0
    :width: 800

    API keys.
