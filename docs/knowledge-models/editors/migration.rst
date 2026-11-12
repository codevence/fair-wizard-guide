.. _knowledge-model-migration:

Knowledge Model Migration
*************************

A knowledge model can be created from scratch or by customizing an existing model. When customizing a model, we call the original the **Parent KM** and the customized model the **Child KM**. We can create the Child KM from any :ref:`published version <knowledge-model-publish>` of the Parent KM, make changes and publish a version of the Child KM. However, the Parent KM can evolve, and at some point we might want to have those changes in our Child KM, too.

That is what the knowledge model migration is for. Once a new version of the parent KM is published, we can start the KM migration where we go through these changes. We can choose whether we want to apply or reject these modifications to our child KM during migration. At the end, we publish a new version of the child KM with all the selected changes.


.. figure:: /_static/diagrams/km-migration.png
    :alt: Schematic representation of KM migration.

    Schematic representation of KM migration.


Creating a Knowledge Model Migration
====================================

We can start the knowledge model migration from the :ref:`list of knowledge model editors<knowledge-model-editors>`. If there is a newer version of the Parent KM available for a particular knowledge model editor, we can see a yellow :guilabel:`update available` badge next to the name of the editor.

.. WARNING::

    If there are some unpublished changes in the Child KM, we cannot start the migration (there will be no :guilabel:`update available` badge). We need to publish the changes first.

.. figure:: /_static/screenshots/5.0/guide/km-editor-list.png
    :figclass: guide-screenshot
    :alt: Knowledge Model Editors in FAIR Wizard 5.0
    :width: 800

    Knowledge Model Editors.

We can either click on the badge directly, or choose the :guilabel:`Update` option from the dropdown menu. It will open a modal window where we can choose a new version of the Parent KM that we want to migrate our Child KM to. Usually, we want to pick the latest.


.. figure:: /_static/screenshots/5.0/guide/km-update-modal.png
    :figclass: guide-screenshot
    :alt: Update a Knowledge Model Editor in FAIR Wizard 5.0
    :width: 350

    Update a Knowledge Model Editor.

Knowledge Model Migration
=========================

During the migration, we can see all the changes one by one and can choose whether we want to :guilabel:`Apply` or :guilabel:`Reject` the change. We can also choose to :guilabel:`Apply all` to accept all remaining changes.


.. figure:: /_static/screenshots/5.0/guide/km-migration.png
    :alt: Knowledge Model migration in FAIR Wizard 5.0
    :width: 800

    Knowledge Model migration.

Cancelling a Knowledge Model Migration
======================================

We can cancel the knowledge model migration at any point before we publish the new version of the child KM. We need to navigate to the :ref:`list of knowledge model editors<knowledge-model-editors>` and choose :guilabel:`Cancel migration` from the dropdown menu for the desired KM editor.


Finishing a Knowledge Model Migration
=====================================

After we resolve all the changes, we are ready to publish the new version of the child KM. To do that, we need to click on the :guilabel:`Publish` button. This will open the Publish new version screen where we need to provide additional information for the new version of the knowledge model.

The publish screen shows us some information about the knowledge model, such as its **Knowledge Model Name** and **Knowledge Model ID**. We need to choose the new **version number**.

.. NOTE::

    We recommend using a similar approach as in `semantic versioning <https://semver.org>`_. So when we have a version ``<major>.<minor>.<patch>``, change in the major version number indicates some breaking changes (deleting questions, significant changes in the questionnaire structure, etc.), change in minor version number indicates some new changes that are backward compatible (i.e., adding a new question), and change in the patch version number indicates fixes (such as fixing some typos).


The publishing form also contains the following metadata, pre-filled from the editor:

- **License** - this is used when we want to share the knowledge model with other people so they know how they can do that. We recommend using a license identifier from `SPDX License List <https://spdx.org/licenses/>`_.
- **Description** - this should be really short and descriptive. It appears, for example, in selection lists when creating a new project to help researchers choose the best knowledge model for their use case.
- **Readme** - this is where we can describe everything we need about the knowledge model. We can, for example, include a changelog of what changed in what version, etc. We can use :ref:`Markdown<markdown-cheatsheet>` in this field to provide some nice formatting.
