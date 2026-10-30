Document template settings
**************************

Edit the template's name, description, identifier, version, source language, license and README in the settings.
The source language describes the template's translatable content; output translations are managed for the released template.

Knowledge model compatibility
=============================

Compatibility patterns use a knowledge model identifier and optional minimum/maximum versions. A null or empty identifier matches any model; a missing bound leaves that side of the version range unrestricted.
The organization ID is no longer a separate filter. Review migrated organization-only patterns, because removing that constraint can broaden the accepted models.

Formats
========

Each output format has a name, icon and ordered generation steps. A step has its implementation name and its options.
Choose the steps required to generate or convert that format, then test it with actual answers, translations and uploaded files where relevant.

The metadata uses document-template metamodel 19.0. Port custom code as described in :doc:`/development/document-templates/document-context`; changing only the metamodel number does not update an old template's field accesses.

Earlier interface
=================

These screenshots show the 4.x interface. They will be replaced with 5.0 screenshots.

.. figure:: /_static/earlier-interface/applications/data-management-planner/document-templates/editors/detail/template/allowed-kms.png
    :alt: Allowed knowledge models specification for a document template.
    :width: 628

    **Outdated screenshot (4.x).** Allowed knowledge models specification for a document template.

.. figure:: /_static/earlier-interface/applications/data-management-planner/document-templates/editors/detail/template/formats.png
    :alt: Markdown format specification with jinja step.
    :width: 628

    **Outdated screenshot (4.x).** Markdown format specification with ``jinja`` step.
