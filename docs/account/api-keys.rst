API keys
********

API keys allow scripts and integrations to use FAIR Wizard with our account's permissions. We can create or revoke keys in :guilabel:`User Settings` → :guilabel:`API Keys`.
When creating a key, we enter a name and choose when it expires. We need to save the generated key securely. Integrations use it as a Bearer token.

A key does not bypass role permissions. With multiple workspaces, API calls still need the correct scope for the operation.
Revoke a key when its integration is retired or its value may have been exposed.

Existing unified keys from 4.35 continue to follow their validity and permissions. Integrations using the older application-specific keys need to replace those keys and update their calls.
Use :doc:`/development/api` for the 5.0 base URL and workspace-scoping rules.

Earlier interface
=================

These screenshots show the 4.x interface. They will be replaced with 5.0 screenshots.

.. figure:: /_static/earlier-interface/applications/admin-center/profile/settings/api-keys/form.png
    :alt: Form for creating an API Key.
    :width: 800

    **Outdated screenshot (4.x).** Form for creating an API Key.
