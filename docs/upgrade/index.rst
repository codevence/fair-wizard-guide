Upgrading to FAIR Wizard 5.0
****************************

FAIR Wizard 5.0 combines the former applications into one interface and updates administration, integrations, document templates and translations.
The preview release is scheduled for 6 November 2026 and production for 4 December 2026.

Before the upgrade
==================

* Identify API integrations your team maintains and prepare their changes using the 5.0 API documentation.
* Tell the FAIR Wizard team about custom login automations, SAML/Shibboleth authentication, document templates, interface translations and email templates.
* Port custom document templates to context 19.0 and check representative outputs with compatible tooling. See :doc:`/development/document-templates/document-context`.
* Plan updates to screenshots, videos, bookmarks and instructions that refer to the old interface.
* Request a readable export of legacy audit records from the FAIR Wizard team if you need one.

When the instance is upgraded
=============================

* For OpenID, update the callback URL at the identity provider after the corresponding instance has been upgraded, using the URL shown by its OpenID settings.
* Coordinate SAML/Shibboleth changes with the FAIR Wizard team and your identity administrator; federation approval can take time.
* Update API paths and payloads, login-automation responses and custom integrations. See :doc:`/development/api`.
* Reconnect clients using the previous MCP service and review their permissions.
* Check interface and document languages, custom translations, plugins and document-submission workflows.

Audit and documents
===================

The new audit log records activity from the upgrade onward. Legacy history is outside the new audit view; readable exports are provided on request.
Stored documents and project history will be preserved during the upgrade. Check your custom outputs and files afterward; a temporary preview is not a stored document.

.. admonition:: With multiple workspaces

   The initial migration keeps existing content together in single-workspace mode. Mapping users and content into multiple workspaces is a separate step with the FAIR Wizard team.

Use the current :doc:`/administration/audit-log` and :doc:`/administration/roles` references for the new administration model.
