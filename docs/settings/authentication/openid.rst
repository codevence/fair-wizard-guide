OpenID
******

Open the organization's :guilabel:`Settings` → :guilabel:`OpenID` to configure an OpenID Connect provider.
Register FAIR Wizard as a client at the identity provider and copy the client credentials and issuer/discovery information into the supported fields.

Configure the callback
======================

Save the provider configuration, then copy the :guilabel:`Callback URL` shown by FAIR Wizard into the provider's allowed redirect URIs.
Use the exact address shown by the instance rather than constructing it from an old guide. In 5.0 it has the form:

.. code-block:: text

   https://<instance>/open-id/<provider-uuid>/callback

Test the sign-in button with a dedicated account. Check claims used for the name and email address and any :doc:`login automation </administration/automations>` attached to the provider.

Upgrade from an earlier release
===============================

The previous application prefix is removed from the callback address. Update the identity provider after the corresponding instance is upgraded to 5.0, then test the full sign-in and logout flow.
Preview and production are separate instances; each needs its own correct registered address.

Use :doc:`/account/connected-accounts` for identities linked to an existing account.

Earlier interface
=================

These screenshots show the 4.x interface. They will be replaced with 5.0 screenshots.

.. figure:: /_static/earlier-interface/applications/admin-center/settings/authentication/openid/openid.png
    :alt: Example configuration of OpenID Microsoft Azure service.
    :width: 700

    **Outdated screenshot (4.x).** Example configuration of OpenID Microsoft Azure service.
