SAML / Shibboleth
*****************

SAML authentication connects the instance to an institutional identity provider or federation. Open the organization's :guilabel:`SAML / Shibboleth` settings where this service is enabled.
Configure the provider metadata and the supported sign-in-button details. Use the service-provider metadata and addresses from the instance when registering it with the identity provider or federation.

For 5.0, the unified API changes addresses used by the service-provider entity and assertion-consumer endpoint. The FAIR Wizard team will coordinate the change with your identity administrator. Federation approval may take time, so include it in preparation for the relevant instance's upgrade.

Test with a real institutional account and review any :doc:`login automation </administration/automations>`. Keep a working administrative recovery sign-in method while making authentication changes.

Earlier interface
=================

These screenshots show the 4.x interface. They will be replaced with 5.0 screenshots.

.. figure:: /_static/earlier-interface/applications/admin-center/settings/authentication/saml/saml.png
    :alt: Example configuration of SAML service.
    :width: 700

    **Outdated screenshot (4.x).** Example configuration of SAML service.

.. figure:: /_static/earlier-interface/applications/admin-center/settings/authentication/saml/saml-detail.png
    :alt: Configured SAML service (with hidden details).
    :width: 700

    **Outdated screenshot (4.x).** Configured SAML service (with hidden details).
