Troubleshooting
***************

An integration question cannot load suggestions
===============================================

The external service may be unavailable, or the integration may need correcting. Contact the person responsible for your knowledge model. For a Data Source integration, check that the referenced dataset exists in the right scope; see :doc:`/knowledge-models/data-sources/detail`.

No document template is available for a project
===============================================

Check that a compatible published template is available to the project. Its knowledge model compatibility rules, version and supported metamodel matter. With multiple workspaces, also check the organization and local libraries.

A template shows unsupported metamodel
======================================

Use a compatible version or update the custom template for context 19.0. Changing the metamodel version in its metadata is not enough; the template code also needs updating. See :doc:`/development/document-templates/document-context`.

A published knowledge model or template is missing
==================================================

Check its publication state, deprecation state and library scope. With multiple workspaces, local content with the same ID and version takes precedence over organization content.

A project template is missing
=============================

Check :doc:`/projects/detail/sharing` and the current workspace. A project template follows project access rules.

For further help, contact `FAIR Wizard support <mailto:support@fair-wizard.com>`_.
