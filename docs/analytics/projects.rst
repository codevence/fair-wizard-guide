Projects
********

Users with the :ref:`Use Analytics<roles>` role permission can view analytics of projects. Choose fields and filters to create a view of projects. Save the view to return to it later, or export its data as CSV.

.. figure:: /_static/screenshots/5.0/guide/analytics-projects-list.png
    :figclass: guide-screenshot
    :alt: Analytics: Projects in FAIR Wizard 5.0
    :width: 800

    Analytics: Projects.

To configure the first view, open :guilabel:`View settings`, enter a name and choose the fields. Save the settings and use :guilabel:`Save changes` in the toolbar to keep the view.

To create another view while a saved view is selected, open the :guilabel:`View` menu and choose :guilabel:`Create new view`. We can return to saved views from the same menu.

.. figure:: /_static/screenshots/5.0/guide/analytics-projects-settings.png
    :figclass: guide-screenshot
    :alt: Analytics: Projects view settings in FAIR Wizard 5.0
    :width: 520

    Analytics: Projects view settings.

To compare answers across projects, add a :guilabel:`Question answer` field while editing a view and select a knowledge model question by title or UUID. The new column displays each project's reply and can be filtered by answer or reply status. We can also add :guilabel:`Knowledge Model Version` and :guilabel:`Document Template Version` fields and filter by specific versions. :guilabel:`Created At` and :guilabel:`Updated At` offer date range filters.

.. figure:: /_static/screenshots/5.0/guide/analytics-projects-question-values.png
    :figclass: guide-screenshot
    :alt: Projects Analytics with research-output answers and no filter menu open
    :width: 800

    Question answers shown as a column.

A Yes/No question can be used in the same way.

.. figure:: /_static/screenshots/5.0/guide/analytics-projects-sensitive-data.png
    :figclass: guide-screenshot
    :alt: Projects Analytics with seven Yes and two No answers about sensitive data, sorted by Answered
    :width: 800

    Answers about sensitive data.

Various fields have filters that can be used to narrow down the data.

.. figure:: /_static/screenshots/5.0/guide/analytics-projects-question-filter.png
    :figclass: guide-screenshot
    :alt: Projects Analytics filtered to research outputs that include Dataset, with the answer filter open
    :width: 800

    Filtering projects by a question answer.

We can also resize all rows by clicking on the double arrow in the top left corner. If we want to change individual column widths or row heights, we can do it using drag-and-drop on the borders. We can choose how many rows are on the page by clicking on the :guilabel:`Items per page` dropdown menu.

.. NOTE::

    Click :guilabel:`Save changes` in the toolbar to keep changes to the view.


The data of a view can be exported to a CSV file by clicking on :guilabel:`Export CSV`.

Project details
---------------

By clicking on the project name, we can open that project's details. The project detail has four tabs:

- Metrics
- Users
- User Groups
- Documents

The :guilabel:`Metrics` tab shows all metrics that are used in the selected project. It also shows who contributed to the project, when they contributed and their share of the contributions. The :guilabel:`Users` tab shows all users that are part of the selected project and their roles. The :guilabel:`User Groups` tab shows all user groups that are part of the selected project and their role. The :guilabel:`Documents` tab shows all documents that were generated using the project. It also shows document metadata, such as format, size, and author.

The project details on the right side show additional project metadata, such as description, phase, sharing options, numbers of comments and TODOs, project tags, knowledge model, and question tags.

Click :guilabel:`Go to project` to open the project.

.. figure:: /_static/screenshots/5.0/guide/analytics-projects-detail.png
    :figclass: guide-screenshot
    :alt: Analytics: Project details in FAIR Wizard 5.0
    :width: 800

    Analytics: Project details.
