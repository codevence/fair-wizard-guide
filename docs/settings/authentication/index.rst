Authentication
**************

Configure sign-in methods in the organization's authentication settings. FAIR Wizard supports internal accounts and configured external providers; SAML/Shibboleth availability depends on the instance.
Keep a tested administrative sign-in method when changing identity-provider settings.

Use :doc:`internal` for internal authentication, :doc:`openid` for OpenID and :doc:`saml` for SAML/Shibboleth.
A provider can also have a :doc:`login automation </administration/automations>` to assign profile details and access.

.. toctree::
   :maxdepth: 1

   internal
   openid
   saml
