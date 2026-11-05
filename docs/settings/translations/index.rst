Application and email translations
**********************************

FAIR Wizard manages application text and email text separately under :guilabel:`Settings` → :guilabel:`Translations`.
Choose :guilabel:`Application` for the interface or :guilabel:`Emails` for outgoing messages. These translations are separate from knowledge-model questionnaire languages and document-template output languages.

Manage languages
================

The list shows installed languages and whether each is enabled. Enable only the languages you want to offer; users choose their interface language in :doc:`/account/language`.
Enable a translation before making it the default. Download an installed language with :guilabel:`Download PO`; use :guilabel:`Download POT`, where available, to start a new translation in a gettext editor. A missing translation falls back to English.

A language uses a PO file containing its metadata and translated messages. Use :doc:`upload` to provide a custom translation.

.. figure:: /_static/screenshots/5.0/guide/settings-locales.png
    :figclass: guide-screenshot
    :alt: Interface translations in FAIR Wizard 5.0
    :width: 800

    Interface translations.

.. figure:: /_static/screenshots/5.0/guide/settings-mail-template-locales.png
    :figclass: guide-screenshot
    :alt: Email translations in FAIR Wizard 5.0
    :width: 800

    Email translations.

Prepare a custom translation
============================

#. Download the POT file for the application or email messages.
#. Open it in a gettext editor, choose the target language and save a PO file in UTF-8.
#. Set the PO file's ``Language`` header to the target language code, such as ``cs``. Keep the ``Project-Id-Version`` from the downloaded template; it identifies the message set and version.
#. Translate the messages, preserving placeholders, markup and plural forms. Untranslated messages fall back to English.
#. :doc:`Upload the PO file <upload>` and enable the language.

Email greetings and footers can be shared by several email types. Changing a shared message affects every email that uses it.

Official and custom translations
================================

Replacing an official translation with your own file makes it custom and stops its automatic official updates.
If we delete an official translation, automatic updates will not reinstall it.
The same rules apply to email translations. We need to keep our custom PO files and update them when new messages are added.

During migration to 5.0, the old interface locale bundles are replaced by the PO-based system and users may need to select their preferred language again. See :doc:`/upgrade/index` for preparation.

.. toctree::
   :maxdepth: 1

   Upload <upload>
