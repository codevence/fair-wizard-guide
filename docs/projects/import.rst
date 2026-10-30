Import projects from CSV
************************

Open :guilabel:`Projects` and its import action. This requires the :guilabel:`Manage ALL Projects` permission for the selected workspace.
All rows are checked before creating the projects. If a row is invalid or the import would exceed the plan's project limit, no projects are created.

Prepare the file
================

The columns describe the project name, knowledge model, optional document template and owner email addresses:

.. list-table::
   :header-rows: 1

   * - Field
     - Meaning
   * - ``name``
     - Project name.
   * - ``knowledgeModelId``
     - Knowledge model identifier, without its version.
   * - ``knowledgeModelVersion``
     - Optional; leave empty for the latest released version available in the target workspace.
   * - ``documentTemplateId``
     - Optional document template identifier.
   * - ``documentTemplateVersion``
     - Optional version, used with a template identifier; empty selects the latest released version.
   * - ``emails``
     - Email addresses of the existing users who will own the project. Separate multiple addresses with commas and quote that CSV field.

Use :guilabel:`Download template` in the import screen, complete the rows, then select the CSV file and submit the import. Correct the reported errors and import the complete file again if validation fails.
Imported projects use the target area's default visibility and sharing settings.

.. admonition:: With multiple workspaces

   Select the target workspace first. Every owner named in the file must already be a member of that workspace. All projects in one import go into that workspace.

If owner addresses are left empty, no explicit project owner is assigned by the import. We need to assign owners afterward if the projects should have explicit owners.

Earlier interface
=================

These screenshots show the 4.x interface. They will be replaced with 5.0 screenshots.

.. figure:: /_static/earlier-interface/applications/admin-center/import/projects/projects.png
    :alt: Import projects.
    :width: 528

    **Outdated screenshot (4.x).** Import projects.
