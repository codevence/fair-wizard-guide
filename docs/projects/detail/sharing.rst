.. _sharing:

Sharing
*******

Project owners can share a project with other FAIR Wizard users or external collaborators. Open :guilabel:`Share` in the project header to change access.

.. figure:: /_static/screenshots/5.0/projects/sharing.png
    :figclass: guide-screenshot
    :alt: Project sharing in the Coastal Biodiversity Survey example
    :width: 350

    Project sharing.

.. NOTE::

    Keep at least one owner with access to the project. Before removing yourself as an owner, give another collaborator Owner access.


If we want to only see how sharing is set up or copy the project link, we can use the arrow button which is a part of the :guilabel:`Share` button.

Changes made in the sharing modal are saved after clicking :guilabel:`Save`. We can close the modal without saving by clicking :guilabel:`Cancel`.

When we search for users to add to project sharing, FAIR Wizard also shows user affiliation when it is available.


There are different project sharing roles that grant access to different project features:

.. NOTE::

    These are project sharing roles. They apply to this specific project and are separate from global :ref:`roles<roles>`. A global role can also grant access to all projects, depending on its permissions.


.. list-table::
   :header-rows: 1

   * - —
     - Viewer
     - Commenter
     - Editor
     - Owner
   * - View project
     - ✔
     - ✔
     - ✔
     - ✔
   * - Metrics
     - ✔
     - ✔
     - ✔
     - ✔
   * - Preview
     - ✔
     - ✔
     - ✔
     - ✔
   * - View documents
     - ✔
     - ✔
     - ✔
     - ✔
   * - Comment on project
     - —
     - ✔
     - ✔
     - ✔
   * - Change answers
     - —
     - —
     - ✔
     - ✔
   * - TODOs
     - —
     - —
     - ✔
     - ✔
   * - Version history
     - —
     - —
     - ✔
     - ✔
   * - Create documents
     - —
     - —
     - ✔
     - ✔
   * - Editor notes
     - —
     - —
     - ✔
     - ✔
   * - Name, rename or delete a named version
     - —
     - —
     - —
     - ✔
   * - Revert to an earlier version
     - —
     - —
     - —
     - ✔
   * - Sharing settings
     - —
     - —
     - —
     - ✔
   * - Project settings
     - —
     - —
     - —
     - ✔

The following video tutorial explains and showcases sharing options and tools that can be used while collaborating with others. Some features mentioned in the video are also explained in the :ref:`project questionnaire<project-questionnaire>`.

.. note:: This video accompanies an earlier guide. Its menus and screens may differ in 5.0.

.. youtube:: ykxHWsjCTEQ
    :width: 100%
    :align: center

.. NOTE::

    Some of the following options might be globally disabled in the application settings for the whole FAIR Wizard, therefore not visible on the project level.


Users
=====

We can choose specific users from the FAIR Wizard and their project sharing role to grant them access to project features based on the table above. This is a good way to add other collaborators that work together with us on the project. A user group can also be given Owner access; owning the group and having Owner access to a project are separate roles.


Visible by all other logged-in users
====================================

We can enable the :guilabel:`Visible by other logged-in users` toggle to grant access without listing each user. In single-workspace mode, this applies to other signed-in users. With multiple workspaces, it applies to users who can access the project's workspace. Then, we can also choose what the users can do -- **view**, **comment**, or **edit** the project. We cannot grant **owner** access this way though.

This can be useful, when we want to have an example project accessible by everybody. We can simply enable this and choose that other users can **view** the project. We also want to set this up when we create a :ref:`project template<project-templates>`.


Public link
===========

We can enable the :guilabel:`Public link` toggle to grant access to the project to anyone who has the link. We can again choose what they can do -- **view**, **comment**, or **edit** the project. Also, the public link is visible there, so we can simply copy it and send to whoever we want to collaborate with. Then, they don't need a FAIR Wizard account and still be able to access our project.

Workspace access
================

With multiple workspaces, ordinary visibility to signed-in users applies to members who can reach the project's workspace. Add collaborators from that workspace; a project invitation or user group does not replace workspace membership. Organization-wide project permissions can grant wider access.

Public links are a separate choice: anyone with an enabled public link can receive the selected access, including people outside the workspace. A public link can therefore make a project accessible beyond its ordinary membership.

User groups
===========

Add a user group to share the project with its members and choose the group's project role. Group ownership and the role on this project are separate. With multiple workspaces, use groups from the project's workspace; see :doc:`/user-groups/index`.
