.. _create-project:

.. _from-project-template:

.. _create-project-custom:

Create a project
****************

We can create a new project by opening :guilabel:`Projects` in the main menu and clicking :guilabel:`Create`. This requires the :guilabel:`Create Projects` permission. Depending on the instance settings, we can create a project from a project template, a knowledge model, or both.

From a project template
=======================

Project templates are prepared projects with pre-selected knowledge models and settings. They can also contain pre-filled answers, comments and TODOs. To create a project from a template, we need to enter a **name** and select a **project template**.

.. figure:: /_static/screenshots/5.0/projects/create-template.png
    :figclass: guide-screenshot
    :alt: Create a project from a template in the Coastal Biodiversity Survey example
    :width: 350

    Create a project from a template.

From a knowledge model
======================

To create a project from a knowledge model, we need to enter a **name** and select a **knowledge model**. The selector shows its ID and version to help distinguish similarly named models.
If the knowledge model has question tags, we can include all questions or filter them by tag. If it has translations, we can also choose the questionnaire language.
We can then choose a document template in the :doc:`project settings </projects/detail/settings>`.

.. figure:: /_static/screenshots/5.0/projects/create-custom.png
    :figclass: guide-screenshot
    :alt: Create a project from a knowledge model in the Coastal Biodiversity Survey example
    :width: 350

    Create a project from a knowledge model.

.. admonition:: With multiple workspaces

   The project is created in the selected workspace. Content offered there comes from its local library and the organization library. A local item takes precedence when both have the same identifier and version.

Cloning a project keeps it in the source project's workspace. For bulk creation, see :doc:`/projects/import`.

The knowledge model's source language is selected by default. Alternative languages are offered when translations are available. A project created directly from a knowledge model starts without pre-filled questionnaire replies; choose its document template and other defaults in the project settings.

Where available, the dashboard's create-project shortcut opens the same creation workflow.
