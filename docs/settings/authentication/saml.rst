SAML / Shibboleth
*****************

For help with SAML, Shibboleth or eduGAIN setup, contact the `FAIR Wizard team <mailto:info@fair-wizard.com>`_.

SAML connects FAIR Wizard to an institutional identity provider or federation. Open the organization's :guilabel:`Settings` → :guilabel:`SAML / Shibboleth` with :guilabel:`Manage Settings`, where the service is available. Authentication configuration is shared across workspaces.

Before changing institutional authentication, agree the setup with the identity administrator and keep a working administrative sign-in method.

Create a configuration
======================

#. Choose :guilabel:`Create` and enter a **Name** for the sign-in button.
#. Enter **Metadata URL Identity Provider**: the XML metadata address supplied by the institution or federation.
#. Choose one of the two modes below and complete its fields.
#. Under :guilabel:`Advanced configuration`, choose whether new users may register through this provider.
#. Set the sign-in button's **Icon**, **Background Color** and **Text Color**, check **Button Preview**, then click :guilabel:`Create`.

Single identity provider
------------------------

Select :guilabel:`SAML / Shibboleth` and enter the institution's identity-provider entity ID in **Default Identity Provider**. When editing the saved configuration, this field is labeled **Identity Provider Entity ID**.

The entity ID must match a provider in the XML metadata. Users selecting this sign-in method are directed to that identity provider.

Federation discovery
--------------------

Select :guilabel:`Shibboleth (Discovery Service / WAYF Federation)` when users should choose their institution through a discovery service.

* **Metadata URL Identity Provider** must provide metadata for the identity providers being offered.
* **Discovery URL** is the federation's discovery-service URL template. FAIR Wizard fills its first ``%s`` placeholder with the service-provider entity ID and its second with the return URL.
* **Allowed Identity Providers** can restrict sign-in to listed identity-provider entity IDs. An empty list leaves this restriction unset.

Obtain the discovery URL template from the federation administrator. Its return flow must send the selected provider's entity ID in the ``entityID`` parameter. Each allowed entity ID must also be present in the supplied metadata.

.. figure:: /_static/screenshots/5.0/guide/create-saml.png
    :figclass: guide-screenshot
    :alt: Create SAML configuration in FAIR Wizard 5.0
    :width: 800

    Create SAML configuration.

Register FAIR Wizard with the institution
=========================================

Open the saved configuration. It shows the addresses to register with the identity provider or federation:

* **Entity ID** identifies this FAIR Wizard service provider.
* **Assertion Consumer Service (ACS) URL / Response URL** receives the authentication response.
* **Single Logout URL** is the logout endpoint.

Use the values displayed by the instance. Service-provider XML metadata is available at the displayed Entity ID with ``/metadata`` appended. Provide that metadata and the displayed addresses to the identity or federation administrator for registration.

Agree which user attributes will be released, including email and name information. If the institution uses different attribute names or needs custom access assignments, arrange the mapping with the FAIR Wizard team and review the :doc:`login automation </administration/automations>`.

Test the connection
===================

#. Use a separate browser session and select the configured sign-in button.
#. For a federation, choose an allowed institution. Complete authentication at its identity provider.
#. Check that FAIR Wizard opens the intended account. Test new-user registration separately if it is enabled.
#. Check profile details, roles, user groups and workspace access, including any assignments made by login automation.
#. Test signing out and signing in again.

If sign-in fails, check the registered Entity ID and ACS address, the metadata URL, the selected institution's entity ID and any allowed-provider restriction. If a login automation is attached, inspect its invocation log as well. Report the displayed error through :doc:`/getting-started/support`.

Updating an existing configuration
==================================

Open the configuration from the list, make changes and save. Coordinate changes to institutional metadata, discovery or registered addresses with the identity administrator, then repeat the sign-in test.

For the 5.0 upgrade, the FAIR Wizard team will coordinate the changed service-provider addresses with your identity administrator. Federation approval may take time; see :doc:`/upgrade/index`.
