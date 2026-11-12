Import a Document Template
**************************

Open the document template library and choose :guilabel:`Import`. You need the management permission for the target library.

From the Registry
=================

Where a Registry connection is available, select :guilabel:`From registry` and enter the desired reference in ``id:version`` form, for example ``example.research-plan:1.0.0``. Replace the example with the identifier and version of an item available in the Registry, then import it.

.. figure:: /_static/screenshots/5.0/guide/dt-import-registry.png
    :figclass: guide-screenshot
    :alt: Import a Document Template from registry in FAIR Wizard 5.0
    :width: 520

    Import a Document Template from registry.

From a file
===========

Select :guilabel:`From file` and choose a ZIP bundle exported from FAIR Wizard or produced by compatible tools. Multiple files can be selected. Review any validation errors before using the imported content.

.. figure:: /_static/screenshots/5.0/guide/dt-import-file.png
    :figclass: guide-screenshot
    :alt: Import a Document Template from file in FAIR Wizard 5.0
    :width: 520

    Import a Document Template from file.

.. admonition:: Multiple workspaces

   Import into the intended organization or workspace library. Local content with the same ID and version takes precedence over organization content.

Importing a new version does not change the template selected in existing projects. Select the new version in the :doc:`project settings </projects/detail/settings>` to use it for previews and future documents.
