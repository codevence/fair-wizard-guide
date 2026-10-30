Application and email translations
**********************************

FAIR Wizard manages application text and email text separately under :guilabel:`Settings` → :guilabel:`Translations`.
Choose :guilabel:`Application` for the interface or :guilabel:`Emails` for outgoing messages. These translations are separate from knowledge-model questionnaire languages and document-template output languages.

Manage languages
================

The list shows installed languages and whether each is enabled. Enable only the languages you want to offer; users choose their interface language in :doc:`/account/language`.
Enable a translation before making it the default. Download an installed language with :guilabel:`Download PO`; use :guilabel:`Download POT`, where available, to start a new translation in a gettext editor. A missing translation falls back to English.

A language uses a PO file containing its metadata and translated messages. Use :doc:`upload` to provide a custom translation, or :doc:`registry` for available official translations.

Official and custom translations
================================

Replacing an official translation with your own file makes it custom and stops its automatic official updates.
If we delete an official translation, automatic updates will not reinstall it.
The same rules apply to email translations. We need to keep our custom PO files and update them when new messages are added.

During migration to 5.0, the old interface locale bundles are replaced by the PO-based system and users may need to select their preferred language again. See :doc:`/upgrade/index` for preparation.

Earlier interface
=================

These screenshots show the 4.x interface. They will be replaced with 5.0 screenshots.

.. figure:: /_static/earlier-interface/applications/admin-center/settings/system/locales/list.png
    :alt: List of all locales.

    **Outdated screenshot (4.x).** List of all locales.

.. toctree::
   :maxdepth: 1

   registry
   upload
