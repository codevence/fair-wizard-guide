Edit a data source
******************

A data source needs values, a response item template and at least one search field before it can return suggestions in a questionnaire.

Values
======

Open :guilabel:`Values` to define columns and enter rows, or import a CSV whose first row contains column names. Column names are case sensitive. Review the imported values and save changes.

.. figure:: /_static/screenshots/5.0/guide/data-source-values.png
    :figclass: guide-screenshot
    :alt: Data Source values in FAIR Wizard 5.0
    :width: 800

    Data Source values.

.. figure:: /_static/screenshots/5.0/guide/data-source-import.png
    :figclass: guide-screenshot
    :alt: Import Data Source values in FAIR Wizard 5.0
    :width: 350

    Import Data Source values.

We can also delete individual rows or columns, clear the values, and export the data as CSV. Column order does not affect named fields used by the response template.

Before replacing values, check which integrations use the source. Deleted values will no longer appear in search results.

Display and search
==================

In :guilabel:`Info`, set the :guilabel:`Response Item Template`. It controls how the selected answer is displayed. Use column names as item properties in Jinja notation. For a column named ``name``, for example:

.. code-block:: jinja

   **{{ item.name }}**

Markdown can be used for formatting. The optional :guilabel:`Response Item Template for Selection` controls suggestions in the selection list. If it is empty, the main response item template is used for both displays.

.. figure:: /_static/screenshots/5.0/guide/data-source-info.png
    :figclass: guide-screenshot
    :alt: Data Source response templates in FAIR Wizard 5.0
    :width: 350

    Data Source response templates.

Select at least one column under :guilabel:`Search Fields`, then save. These are the columns searched when someone types in an integration question. Without a search field, the source returns no suggestions.

.. figure:: /_static/screenshots/5.0/guide/data-source-search-fields.png
    :figclass: guide-screenshot
    :alt: Data Source searchable fields in FAIR Wizard 5.0
    :width: 350

    Data Source searchable fields.

Connect the dataset
===================

#. In the knowledge model editor, add or open an integration and choose the built-in :guilabel:`Data source` integration.
#. Select the dataset to search.
#. Assign the integration to an :ref:`integration question<integration-question>`.
#. Try the search in the editor's :doc:`preview </knowledge-models/editors/detail/preview>`, then :doc:`publish </knowledge-models/editors/detail/publish>` the model for use in projects.

.. figure:: /_static/screenshots/5.0/guide/km-datasource.png
    :figclass: guide-screenshot
    :alt: Connect a Data Source to an integration in FAIR Wizard 5.0
    :width: 800

    Connect a Data Source to an integration.
