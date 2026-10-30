.. _knowledge-model-editors:

Knowledge Model Editors
***********************

Users with the :ref:`Use Knowledge Model Editor<roles>` role permission can see the knowledge model editors in their permitted scope.

.. figure:: /_static/earlier-interface/applications/data-management-planner/knowledge-models/editors/index/knowledge-model-editors-list.png
    :alt: List of knowledge model editors.

    **Outdated screenshot (4.x).** List of knowledge model editors.


We can use the search field to search for a specific KM editor. The editors are sorted by when they were last updated but we can change that. We can order the list by name, creation date, or last update date. The list shows the name, version, id, if editor contains unpublished changes, if it is a fork of different KM and last update.

We can :ref:`create a new knowledge model editor<create-knowledge-model-editor>` by clicking the :guilabel:`Create` button.

By clicking the triple dots on each of the item in the list we can access some actions:

- **Open Editor** - simply open the :ref:`editor detail<knowledge-model-editor>`
- **Update** - if there is a newer version of parent knowledge model, we can use update action to start a :ref:`knowledge model migration<knowledge-model-migration>`, otherwise the action is not visible
- **Delete** - to delete the knowledge model editor (cannot be undone)

If there is an ongoing :ref:`knowledge model migration<knowledge-model-migration>`, there are different actions:

- **Continue migration**
- **Cancel migration**

Watch this video to learn more about knowledge model editors:

.. note:: This video accompanies an earlier guide. Its menus and screens may differ in 5.0.

.. youtube:: tYcKRxFNx8U
    :width: 100%
    :align: center

.. toctree::
   :maxdepth: 1

   create
   detail/index
   migration
