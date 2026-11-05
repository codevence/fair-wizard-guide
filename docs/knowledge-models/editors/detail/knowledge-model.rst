Knowledge Model
***************

The :guilabel:`Knowledge Model` tab is where we work on the entities (such as questions or answers) that appear in the knowledge model. We define the structure here.

Navigation
==========

In the top row, we can see the breadcrumbs that show us where we are within the knowledge model. This allows us to quickly jump back up in the hierarchy.

On the left side of the editor, there is a navigation tree reflecting the structure of the knowledge model. We can click on the arrows to expand or collapse individual entities, or click on :guilabel:`Expand all` or :guilabel:`Collapse all`. By clicking on the entity name, we open its editor. When some detail is opened either from editor section or from some other place, the tree is always centered on the entity we are currently editing. This allows us to quickly navigate to the parent or child entities.

.. figure:: /_static/screenshots/5.0/guide/km-editor.png
    :figclass: guide-screenshot
    :alt: Knowledge Model Editor in FAIR Wizard 5.0
    :width: 800

    Knowledge Model Editor.

.. TIP::

    There is no search, however, if we want to quickly find an entity by name we can click on :guilabel:`Expand all` in the navigation tree and use search functionality of our web browser.


Editors
=======

The main area of the :guilabel:`Knowledge Model` tab is the actual editor. The form fields change based on the entity we edit, but there are some shared actions:

- **Copy UUID** - every entity has a generated UUID, we can use this button to copy it. We usually need it for :ref:`document template development<document-template-development>`.

- **Move** - we can move entities around the knowledge model. However, not every entity can be put under everything. We can open the move modal window and see where the current entity can be moved to.

- **Delete** - delete is simply used for deleting the entities. This action cannot be undone, so we need to be careful what we delete.

There are different entities we can edit in the knowledge model, the editor shows different fields based on what we edit:

- :ref:`Knowledge Model<knowledge-model>`
- :ref:`Chapter<chapter>`
- :ref:`Question<question>`
- :ref:`Answer<answer>`
- :ref:`Choice<choice>`
- :ref:`Validation<validation>`
- :ref:`Expert<expert>`
- :ref:`Metric<metric>`
- :ref:`Phase<phase>`
- :ref:`Question Tag<question-tag>`
- :ref:`Integration<integration>`
- :ref:`Resource Collection<resource-collection>`

.. figure:: /_static/screenshots/5.0/guide/km-question.png
    :figclass: guide-screenshot
    :alt: Value question configuration in FAIR Wizard 5.0
    :width: 800

    Value question configuration.

Besides their own fields, each entity has so-called **Annotations**. They are arbitrary key value pairs that can be assigned to the entity and used later, when :ref:`developing a document template<document-template-development>`.

.. figure:: /_static/screenshots/5.0/guide/km-integration.png
    :figclass: guide-screenshot
    :alt: API integration configuration in FAIR Wizard 5.0
    :width: 800

    API integration configuration.

.. figure:: /_static/screenshots/5.0/guide/km-validation.png
    :figclass: guide-screenshot
    :alt: Knowledge Model Editor showing the acronym validation rule
    :width: 350

    Value question validation rules.

URL Checker
===========

If we have at least one :ref:`URL Reference<url-reference>` in the knowledge model, a new tab :guilabel:`URL Checker` appears in the knowledge model editor. Here we can check whether each used URL is reachable or not. This allows us to quickly find broken links in the knowledge model and fix them.

.. figure:: /_static/screenshots/5.0/guide/km-url-checker.png
    :figclass: guide-screenshot
    :alt: Knowledge Model URL checker in FAIR Wizard 5.0
    :width: 800

    Knowledge Model URL checker.

Warnings
========

The editor checks for some possible problems, such as empty title for a chapter or no answers for an options question. If there are any, the :guilabel:`Warnings` tab appears and we can quickly navigate to those problems and fix them.

.. figure:: /_static/screenshots/5.0/guide/km-warnings.png
    :figclass: guide-screenshot
    :alt: Knowledge Model warnings in FAIR Wizard 5.0
    :width: 800

    Knowledge Model warnings.

Development with Document Template Editor
=========================================
It is possible to develop the knowledge model together with the document template. Any changes to the knowledge model are immediately reflected in the document template editor. In the Preview tab we can also save the current preview answer values to the knowledge model and make them visible in the document template editor.
