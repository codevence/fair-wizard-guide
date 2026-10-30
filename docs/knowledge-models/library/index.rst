.. _knowledge-model-list:

Knowledge Model Library
***********************

Open :guilabel:`Knowledge Models` → :guilabel:`List` to browse published knowledge models. Search by name or ID and open a model to review its versions, README and metadata.

**Manage Knowledge Models** controls local library management. In multi-workspace mode, managing the organization library requires **Manage Library**. The actions shown depend on your permissions.

* Preview a questionnaire before using the model in a project.
* Export a KM bundle or a POT translation template.
* Compare versions, create an editor for a new version or fork the model.
* Create a project from the model.
* Deprecate or restore the selected version. Other versions are separate.
* Set public visibility when the model should be accessible without signing in.
* Delete a model or version after reviewing its dependencies. Deletion can remove dependent content; see :doc:`detail`.

Use :doc:`import` to add bundles or registry versions. An update badge signals that a newer registry version is available; it does not migrate existing projects. Use :doc:`/projects/migration` for that.

.. admonition:: Multiple workspaces

   Organization models are shared across workspaces. Local models belong to one workspace. A local model takes precedence when it has the same ID and version as an organization model. Check the current library scope before changing content.

Earlier interface
=================

These screenshots show the 4.x interface. They will be replaced with 5.0 screenshots.

.. figure:: /_static/earlier-interface/applications/data-management-planner/knowledge-models/list/index/list.png
    :alt: List of all knowledge models with actions.

    **Outdated screenshot (4.x).** List of all knowledge models with actions.

.. toctree::
   :maxdepth: 1

   compare
   detail
   import
   preview
