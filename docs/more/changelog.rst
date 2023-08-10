Changelog
*********

..
    This is a workaround to random anchor links generation by Sphinx
    https://github.com/sphinx-doc/sphinx/issues/1961#issuecomment-1322281847

.. _frontend-backend:
.. _frontend:
.. _backend:
.. _tools:


.. _v3.26:

3.26
====

* *Release: 1 August 2023*

* **Features:**

  * Added explicit info when there are no questions in a chapter.
  * Comments tab is now highlighted when comments are open on a specific question.

* **Bugfixes:**
  
  * Fixed cursor on radio input in the document template format selection.
  * Fixed file upload UI in the document template editor.
  * Fixed description in Markdown inputs.
  * Fixed deleting queued documents (the dropdown menu was sometimes disappearing).
  * Fixed link to document template development from the Data Steward dashboard.
  * Fixed displaying of alphabetical identifiers for answers, choices, and items.

* **Misc:**

  * Default role was changed to Researcher when running a fresh instance.
  * Deleting users is now much faster.
  * Upgraded Bootstrap to 5.3.0 in frontend.

* **More:**

  * `API Changelog 3.25.0 ➔ 3.26.0 <https://api-docs.fair-wizard.com/changelogs/3.25.0-3.26.0.html>`__


.. _v3.25.3-frontend:

3.25.3 (frontend)
=================

* *Release: 10 August 2023*

* **Bugfixes:**
  
  * Fixed the knowledge model filter on the project list.



.. _v3.25.1-backend:

3.25.1 (backend)
=================

* *Release: 19 July 2023*

* **Bugfixes**
  
  * Fixed user activation when logging in for the first time using OpenID, and no Terms of Service or Privacy Policy were set.



.. _v3.25.2-fronted:

3.25.2 (frontend)
=================

* *Release: 18 July 2023*

* **Bugfixes**
  
  * Fixed preview of item questions in KM Editor that could sometimes cause two items to have the same value when filling them in.



.. _v3.25.1-fronted:

3.25.1 (frontend)
=================

* *Release: 6 July 2023*

* **Bugfixes**
  
  * Fixed change logo button in settings.



.. _v3.25:

3.25
====

* *Release: 4 July 2023*

* **Features:**

  * Added revoke all to :ref:`active sessions<active-sessions>`.
  * Added Terms of Service and/or Privacy agreement confirmation during SSO signup when they are set.
  * :ref:`Preview in KM Editor<km-editor-preview>` now opens on current question (corresponding answers are pre-selected if the question is nested).
  * Improved :ref:`phase selection<questionnaire-current-phase>` in questionnaire and phase description is now used.
  * Improved question tags selection when :ref:`creating a new project<create-project-custom>` to make it more clear which questions will be used.
  * Added support for uploading more files in document template editor.
  
* **Bugfixes:**
  
  * Fixed links from TODOs or comments to questions in collapsed items (they now expand).
  * Fixed SMTP configuration without username and password for authentication.

* **Misc:**

  * Added *robots.txt* to client and server to prevent indexing of the applications.

* **More:**

  * `API Changelog 3.24.0 ➔ 3.25.0 <https://api-docs.fair-wizard.com/changelogs/3.24.0-3.25.0.html>`__


.. _v3.24.1-backend:

3.24.1 (backend)
================

* *Release: 14 June 2023*

* **Bugfixes**
  
  * Fixed generating documents that contain more than one whitespace in the filename.

* **More:**

  * `API Changelog 3.24.0 ➔ 3.24.1 <https://api-docs.fair-wizard.com/changelogs/3.24.0-3.24.1.html>`__ 


.. _v3.24:

3.24
====

* *Release: 30 May 2023*

* **Features:**

  * List views (such as project list or knowledge model list) have been reworked so that only the results are reloaded instead of the whole page. Therefore, the search field should not loose focus when typing slowly.
  * Added warning before the user session expires.
  * Improved information on detail pages (such as knowledge model or document template).

* **Bugfixes:**
  
  * Fixed document generation when there were inconsistent replies after questionnaire migration.
  * Fixed icon alignment in questionnaire import.
  * Fixed color transition for menu icons.

* **Misc:**

  * All document templates from DSW Registry now use WeasyPrint instead of wkhtmltopdf for PDF formats.
  * It is recommended to migrate your existing PDF template to `WeasyPrint <https://github.com/ds-wizard/engine-tools/blob/develop/packages/dsw-document-worker/support/steps/weasyprint.md>`__ as wkhtmltopdf will be removed in the future.

* **More:**

  * `API Changelog 3.23.0 ➔ 3.24.0 <https://api-docs.fair-wizard.com/changelogs/3.23.0-3.24.0.html>`__


.. _v3.23.3-backend:

3.23.3 (backend)
================

* *Release: 14 June 2023*

* **Bugfixes**
  
  * Fixed generating documents that contain more than one whitespace in the filename.

* **More:**

  * `API Changelog 3.23.2 ➔ 3.23.3 <https://api-docs.fair-wizard.com/changelogs/3.23.2-3.23.3.html>`__ 


.. _v3.23.2-backend:

3.23.2 (backend)
================

* *Release: 25 May 2023*

* **Bugfixes:**

  * Fixed API key expiration to use the value set when creating it.

* **More:**

  * `API Changelog 3.23.1 ➔ 3.23.2 <https://api-docs.fair-wizard.com/changelogs/3.23.1-3.23.2.html>`__ 



.. _v3.23.1-backend:

3.23.1 (backend)
================

* *Release: 4 May 2023*

* **Bugfixes:**

  * Fixed loading RSA private key if set only in the ENV variable.

* **More:**

  * `API Changelog 3.23.0 ➔ 3.23.1 <https://api-docs.fair-wizard.com/changelogs/3.23.0-3.23.1.html>`__ 



.. _v3.23:

3.23
====

* *Release: 2 May 2023*

* **Features:**
  
  * Added the possibility to generate :ref:`API keys<api-keys>` to access the API instead of using username and password. The API keys also work when 2FA is enabled.
  * Added an overview of all :ref:`active sessions<active-sessions>`.
  * It is now possible to use HTML for :ref:`login info<login-info>`.
  * Added possibility for :ref:`sidebar login info<sidebar-login-info>` under the login box.
  * Welcome warning and info have been reworked to :ref:`announcements<announcements>` -- it is now possible to have an unlimited list of announcements of different levels and choose if they are visible on the dashboard and/or login screen.
  * Added sort by created to document template list.
  * Improved progress bar in project migration.
  * The warnings tab in the knowledge model editor is now automatically closed when the last one is resolved.
  * Improved form actions to make them more visible when forms change.
  
* **Bugfixes:**

  * Fixed project indication calculation after import or project migration.
  * Fixed double error message when deleting failed in list views.
  * Fixed buttons in email templates in Outlook.
  * Fixed phase in a questionnaire after project migration if the phase no longer exists.
  * Fixed dropdown menus in the sidebar when the page was scrolled.
  * Fixed knowledge model export from the knowledge model list.

* **Misc:**

  * Changed the path of configuration files.
  * Sped up processing and generating of documents.

* **More:**
  
  * `API Changelog 3.22.0 ➔ 3.23.0 <https://api-docs.fair-wizard.com/changelogs/3.22.0-3.23.0.html>`__ 



.. _v3.22.1-tools:

3.22.1 (tools)
==============

* *Release: 14 April 2023*

* **Bugfixes:**

  * Fixed sending mails when configuration is loaded from database.



.. _v3.22.3-backend:

3.22.3 (backend)
================

* *Release: 13 April 2023*

* **Bugfixes:**

  * Fixed the selected phase in projects when migrating from a knowledge model without phases to a knowledge model with phases.

* **More:**

  * `API Changelog 3.22.2 ➔ 3.22.3 <https://api-docs.fair-wizard.com/changelogs/3.22.2-3.22.3.html>`__ 



.. _v3.22.2-backend:

3.22.2 (backend)
================

* *Release: 12 April 2023*

* **Bugfixes:**

  * Fixed an issue that sometimes caused suggesting the same knowledge model multiple times when creating a new project or knowledge model editor.

* **More:**

  * `API Changelog 3.22.1 ➔ 3.22.2 <https://api-docs.fair-wizard.com/changelogs/3.22.1-3.22.2.html>`__ 



.. _v3.22.1:

3.22.1 (frontend, backend)
==========================

* *Release: 11 April 2023*

* **Bugfixes:**

  * Fixed database migration of existing KM editors after 3.22 that could cause unexpected KM editor version or missing metadata (such as readme).
  * Fixed publish process in KM editor and Document Template Editor that could be confusing after 3.22 changes.
  * Fixed deleting KM editor when it is migrating.

* **More:**

  * `API Changelog 3.22.0 ➔ 3.22.1 <https://api-docs.fair-wizard.com/changelogs/3.22.0-3.22.1.html>`__ 



.. _v3.22:

3.22
====

* *Release: 4 April 2023*

* **Features:**

  * Added the possibility to set a knowledge model as deprecated so researchers cannot use it to create new projects.
  * Added :ref:`phase editor<km-editor-phases>` to KM Editor (similar to Tag editor).
  * Renamed :guilabel:`Template` tab to :guilabel:`Settings` in the document template editor to make it consistent with KM Editor or Project.
  * Added link to selected project in document template editor preview.
  * Position in the questionnaire is now remembered when switching tabs in the project (such as going to preview and back to the questionnaire).
  * Warnings tab in the project is now automatically closed when the last one is resolved.
  * Projects are no longer filtered by current user if the user is admin.
  * Improved accessibility of unanswered question indications and metrics (as well as adding an option to hide non-desirable questions).
  * Added information about a version of all components in the About modal.
  * Improved add button labels in various forms to make it easier to understand what they add.
  * Added support for DKIM signing for emails.
  * Added experimental `weasyprint step <https://github.com/ds-wizard/engine-tools/blob/develop/packages/dsw-document-worker/support/steps/weasyprint.md>`__ in document templates for better PDF documents generation. 
  * User details are now updated in the menu after editing your own profile.
  * Added link to the DSW Registry from locale detail.

* **Bugfixes:**

  * Fixed visible first chapter in KM Editor preview when deleted.
  * Fixed inconsistent update label for badge and action for KM migration.
  * Fixed failing to publish knowledge models due to wrong event squashing in some cases.
  * Fixed redirect to login when opening the project after the session has expired.
  * Fixed a visual bug in the project selection dropdown in the document template editor preview.
  * Fixed text overflow for long questions/answers in the project import view.
  * Fixed image previews in the document template editor.
  * Fixed downloading document template with DSW TDK.
  * Fixed dropdown menu separators in list views.

* **Misc:**

  * Added support for RO-Crates (`RO-Crate Importer <https://github.com/ds-wizard/dsw-ro-crate-importer>`__ and `RO-Crate Template <https://github.com/ds-wizard/ro-crate-template>`__)
  * Improved default English locale metadata.
  * Added support for arm64 builds for most of the Docker images.

* **More:**

  * `API Changelog 3.21.0 ➔ 3.22.0 <https://api-docs.fair-wizard.com/changelogs/3.21.0-3.22.0.html>`__ 
