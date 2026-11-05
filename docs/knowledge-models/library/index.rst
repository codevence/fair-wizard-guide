.. _knowledge-model-list:

Knowledge Model Library
***********************

Open :guilabel:`Knowledge Models` → :guilabel:`List` to browse published knowledge models. Search by name or ID and open a model to review its versions, README and metadata.

**Manage Knowledge Models** controls local library management. In multi-workspace mode, managing the organization library requires **Manage Library**. The actions shown depend on your permissions.

* :guilabel:`Open` opens the model's detail, as does clicking its name. The detail includes older versions.
* :guilabel:`Preview` shows the questionnaire created from the model without creating a project.
* :guilabel:`Export` downloads the selected version as a KM bundle; :guilabel:`Export .pot file` downloads its translation template.
* :guilabel:`Compare` compares the selected version with another version.
* :guilabel:`Create KM editor` prepares an editor for another version; :guilabel:`Fork KM` starts a separate model based on it.
* :guilabel:`Create project` opens the creation form with this model selected.
* :guilabel:`Set deprecated` and :guilabel:`Restore` affect the selected version. Other versions remain separate.
* :guilabel:`Set public` and :guilabel:`Set private` control access to the model without signing in.
* :guilabel:`Delete` opens the dependency review. The detail page can target a single version.

Use :doc:`import` to add bundles or registry versions. An update badge signals that a newer registry version is available; it does not migrate existing projects. Use :doc:`/projects/migration` for that.

.. admonition:: Multiple workspaces

   Organization models are shared across workspaces. Local models belong to one workspace. A local model takes precedence when it has the same ID and version as an organization model. Check the current library scope before changing content.

.. figure:: /_static/screenshots/5.0/guide/km-list.png
    :figclass: guide-screenshot
    :alt: Knowledge Model library in FAIR Wizard 5.0
    :width: 800

    Knowledge Model library.

.. toctree::
   :maxdepth: 1

   Compare <compare>
   Detail <detail>
   Import <import>
   Preview <preview>

.. warning::

   Deleting a knowledge model can also delete its versions, dependent editors and projects, including the projects' documents and files. Review the listed dependencies before confirming. This deletion cannot be undone through the application.

Search and updates
==================

Search by name or identifier and sort the list by name or creation date. The list shows the latest version; open the detail for older ones. The actions available depend on the account's permissions.

An :guilabel:`update available` badge identifies a newer version in the connected Registry. Importing it does not migrate existing projects. Multiple KM files can be selected when importing from files.
