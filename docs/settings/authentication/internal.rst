Internal
********

Internal Settings allow us to enable or disable registration. Once turned off, users can only register using other ways, e.g. OpenID or SAML.

We can also enable or disable Two-Factor Authentication (2FA) for users. If enabled, users will be required to enter a one-time code sent to their email address after entering their password.

.. figure:: /_static/screenshots/5.0/guide/settings-authentication.png
    :figclass: guide-screenshot
    :alt: Authentication settings in FAIR Wizard 5.0
    :width: 800

    Authentication settings.

Expiration and default role
===========================

Session expiration and user email-link expiration are specified in hours. The emailed two-factor code has its own **Code Length** and **Expiration**, with the latter specified in seconds.

Choose the default role for new users under :guilabel:`Settings` → :guilabel:`Roles`. Give new users only the permissions they need: a broad default role can expose other users' content or application settings. A role selected as the default cannot be deleted.

Disable internal registration when accounts should be created by administrators or through configured external providers. External providers have separate registration controls; review both when deciding how new accounts may be created.
