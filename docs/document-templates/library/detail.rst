Document Template Detail
************************

We can open a document template's details by clicking on the template in the :doc:`/document-templates/library/index` (or selecting :guilabel:`View detail` from the right dropdown). The detail shows basic information about the template such as its name, ID, version, license, metamodel version, creation date, or supported document formats.

The main part of the detail is the README of the template that should contain basic information and a changelog for the template. In the right panel under the basic information, we can navigate to other versions of the document template, navigate to the `FAIR Wizard Registry <https://registry.fair-wizard.com/>`__ (if the template is present there), or check which knowledge models are compatible with the template.

In the top bar, we can :guilabel:`Export` the template as a ZIP package or :guilabel:`Delete` this version of the template. We can also quickly navigate to :doc:`/document-templates/editors/create` by clicking :guilabel:`Create editor`; it opens the form for creating an editor for a new version of this document template.

We can also choose :guilabel:`Set deprecated`, which makes this version unavailable for new selections. Deprecation affects the selected version. Other versions retain their own status.

If we are not seeing the latest version of the template, a warning message is shown at the top. Similarly, we will see a notification that an update is available if there is a newer version in the `FAIR Wizard Registry <https://registry.fair-wizard.com/>`__ (if configured).

.. _document-template-locales:

Document Template Locales
=========================

A document template has a source language and can have locales for additional languages. The :guilabel:`Locales` tab lists each imported locale by name and language code.

When the template is prepared for translations, use :guilabel:`Export .pot file` from its actions menu to obtain the source strings, translate them into a PO file, and use :guilabel:`Import` on the :guilabel:`Locales` tab to provide the locale name and PO file. Available actions also allow downloading or deleting an imported locale, subject to permissions.

The template's source language is shown in its detail panel. A locale becomes available when selecting a :ref:`default document language<default-document-template>` for a project or creating a document with that template.


.. figure:: /_static/screenshots/5.0/guide/dt-detail.png
    :figclass: guide-screenshot
    :alt: Document Template details in FAIR Wizard 5.0
    :width: 800

    Document Template details.

Deleting a template in use
==========================

A template can be deleted even when it has generated documents. Deletion removes those documents and clears the selected template in affected projects; the projects remain.
Review all affected content before confirming. Deletion is refused if the acting user cannot view every dependency.
In single-workspace mode this requires Manage Document Templates. With multiple workspaces, organization-library deletion requires Manage Library; local deletion uses the document-template permission.

.. figure:: /_static/screenshots/5.0/guide/dt-delete.png
    :figclass: guide-screenshot
    :alt: Delete Document Template with dependent projects in FAIR Wizard 5.0
    :width: 350

    Delete Document Template with dependent projects.

.. TODO::

    Screenshot pending: Document Template locales list and import dialog; deferred by request.
