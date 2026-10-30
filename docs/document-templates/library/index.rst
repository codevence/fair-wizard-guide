Document Template Library
*************************

Open :guilabel:`Document Templates` → :guilabel:`List` to browse published templates. Search or filter the list and open a template to see its versions, README, supported formats and knowledge model compatibility.

Use **Manage Document Templates** for local library management. In multi-workspace mode, managing the organization library requires **Manage Library**. Available actions depend on your permissions.

* :guilabel:`Import` adds a template bundle; see :doc:`import`.
* :guilabel:`Export` downloads a published version as a ZIP bundle.
* :guilabel:`Create editor` starts a draft for further changes.
* Deprecating a version makes it unavailable for new selections. Other installed versions remain separate.
* :guilabel:`Delete` removes a version or the template's versions, according to the selected action. Review the dependent documents and projects before confirming; see :doc:`detail`.

A template marked :guilabel:`unsupported metamodel` needs a compatible version. Publishing an old template without porting its code does not make it compatible with context 19.0.

.. admonition:: Multiple workspaces

   The organization library provides shared templates. Workspace libraries provide local templates. If both contain the same ID and version, the local template takes precedence. Check the current scope before importing, editing or deleting content.

An :guilabel:`update available` badge shows that a newer version is available in the Registry. We can import that version to update the installed template.

Earlier interface
=================

These screenshots show the 4.x interface. They will be replaced with 5.0 screenshots.

.. figure:: /_static/earlier-interface/applications/data-management-planner/document-templates/list/index/list.png
    :alt: List of all document templates with actions.

    **Outdated screenshot (4.x).** List of all document templates with actions.

.. toctree::
   :maxdepth: 1

   detail
   import
