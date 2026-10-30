Edit a data source
******************

The source detail contains its metadata, result display template and values.
Define columns before entering rows, or import a CSV whose first row contains column names. Column names are case sensitive.
Review the import result and save the changes.

Display selected results
========================

The response item template controls how a matching row is shown in a questionnaire. Use the column names as item properties in Jinja notation, with Markdown where supported. For a column named ``name``, for example:

.. code-block:: jinja

   **{{ item.name }}**

Use the values view to add, change, remove, import or export data. Before replacing the values, we should check which integrations use the data source. Deleted values will no longer appear in search results.

Connect the dataset
===================

In the knowledge model editor, choose the built-in Data source integration and select the intended dataset.
The previous Integration Hub plugin is no longer required for this integration. Existing definitions can still identify their source by UUID, so keep the referenced dataset available when moving or reusing a knowledge model.

Earlier interface
=================

These screenshots show the 4.x interface. They will be replaced with 5.0 screenshots.

.. figure:: /_static/earlier-interface/applications/integration-hub/value-integrations/detail/info.png
    :alt: Value integration detail info.
    :width: 700

    **Outdated screenshot (4.x).** Value integration detail info.

.. figure:: /_static/earlier-interface/applications/integration-hub/value-integrations/detail/values.png
    :alt: Value integration detail values.
    :width: 700

    **Outdated screenshot (4.x).** Value integration detail values.

.. figure:: /_static/earlier-interface/applications/integration-hub/value-integrations/detail/import-modal.png
    :alt: Value integration import.
    :width: 400

    **Outdated screenshot (4.x).** Value integration import.
