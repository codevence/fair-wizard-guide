Document Templates
******************

Document templates turn questionnaire answers into documents such as PDF, Word, HTML or machine-readable outputs. Each template defines its supported formats and compatible knowledge models.
We can use published templates in projects and prepare new versions in the editors.

.. admonition:: With multiple workspaces

   Templates can come from the organization library or the project's workspace. If a template with the same ID and version exists in both libraries, the workspace version is used. Organization-library management requires :guilabel:`Manage Library`; local management uses the document-template permissions.

For generating a document, see :doc:`/projects/detail/documents`. Template authors can use the :doc:`/development/document-templates/index` reference.

Make content available across workspaces
========================================

Publish the document template, then export its released version. In the organization area, open the library and :doc:`import the ZIP bundle <library/import>`. This requires :guilabel:`Manage Library`.
Other workspaces can then use it from the organization library. If a workspace already has the same template ID and version locally, its local version takes precedence.

.. toctree::
   :maxdepth: 1

   List <library/index>
   Editors <editors/index>
