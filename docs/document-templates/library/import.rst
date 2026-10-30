Import a Document Template
**************************

Open the document template library and choose :guilabel:`Import`. You need the management permission for the target library.

From the Registry
=================

Where a Registry connection is available, select :guilabel:`From registry` and enter the desired reference in ``id:version`` form, for example ``example.research-plan:1.0.0``. This is an illustrative identifier, not a bundled item.
Use the Registry to find an available item and version, then import it.

From a file
===========

Select :guilabel:`From file` and choose a ZIP bundle exported from FAIR Wizard or produced by compatible tools. Multiple files can be selected. Review any validation errors before using the imported content.

.. admonition:: Multiple workspaces

   Import into the intended organization or workspace library. Local content with the same ID and version takes precedence over organization content.

Importing a new version does not update the model or template selected in existing projects. Review project settings and use :doc:`/projects/migration` when changing a project's knowledge model.

Earlier interface
=================

These screenshots show the 4.x interface. They will be replaced with 5.0 screenshots.

.. figure:: /_static/earlier-interface/applications/data-management-planner/document-templates/list/import/registry.png
    :alt: Input for importing a document template from FAIR Wizard Registry.
    :width: 500

    **Outdated screenshot (4.x).** Input for importing a document template from FAIR Wizard Registry.

.. figure:: /_static/earlier-interface/applications/data-management-planner/document-templates/list/import/file.png
    :alt: Input for importing a document template using a ZIP package.
    :width: 500

    **Outdated screenshot (4.x).** Input for importing a document template using a ZIP package.
