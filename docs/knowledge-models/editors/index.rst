.. _knowledge-model-editors:

Knowledge Model Editors
***********************

Users with the :ref:`Use Knowledge Model Editor<roles>` role permission can see the knowledge model editors in their permitted scope.

.. figure:: /_static/screenshots/5.0/guide/km-editor-list.png
    :figclass: guide-screenshot
    :alt: Knowledge Model Editors in FAIR Wizard 5.0
    :width: 800

    Knowledge Model Editors.

We can use the search field to search for a specific KM editor. The editors are sorted by when they were last updated but we can change that. We can order the list by name, creation date, or last update date. The list shows each editor's name, version, ID and last update, and indicates unpublished changes and forks of other knowledge models.

We can :ref:`create a new knowledge model editor<create-knowledge-model-editor>` by clicking the :guilabel:`Create` button.

Open an item's three-dot menu to see the available actions:

- **Open Editor** - open the :ref:`editor detail<knowledge-model-editor>`
- **Update** - if there is a newer version of the parent knowledge model, we can use this action to start a :ref:`knowledge model migration<knowledge-model-migration>`, otherwise the action is not visible
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

   Create <create>
   Detail <detail/index>
   Migration <migration>
