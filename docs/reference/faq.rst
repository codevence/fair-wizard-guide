.. _troubleshooting:

Frequently Asked Questions
**************************

What is the difference between a knowledge model, a project and a document template?
====================================================================================

A knowledge model defines the questions. A project contains our answers to those questions. A document template turns the answers into a document, such as a data management plan. See :doc:`/getting-started/index` for an introduction to these three parts.

Are my answers saved automatically?
===================================

Answers in the questionnaire are saved automatically. Check the connection and any saving errors before closing the page. Forms such as project settings and sharing have their own :guilabel:`Save` button.

We can return to the project from the :doc:`project list </projects/list>` after signing in to the same FAIR Wizard instance.

How do I find questions I have not answered yet?
================================================

Open :guilabel:`Unanswered` in the questionnaire toolbar to see the questions that still need answers. If the knowledge model defines phases, the list follows the current phase. Select a question to open it. Questions made irrelevant by earlier answers are not included. See :ref:`unanswered-questions`.

How do I download my plan as PDF or Word?
=========================================

In the project's :guilabel:`Documents` tab, choose :guilabel:`New document`, enter a name, and select a compatible document template and format. After generation finishes, download the document from its row. The available formats depend on the selected template; ask an administrator if the format we need is missing. See :doc:`/projects/detail/documents`.

Why is the questionnaire not in my interface language?
======================================================

The interface and questionnaire have separate language settings. :doc:`User settings → Language </account/language>` changes the interface. To change the questionnaire language, choose an available knowledge model translation in the :doc:`project settings </projects/detail/settings>`. That translation must be available for the project's knowledge model.

An integration question cannot load suggestions
===============================================

The external service may be unavailable, or the integration may need correcting. Contact the person responsible for your knowledge model. For a Data Source integration, check that the referenced dataset exists in the right scope; see :doc:`/knowledge-models/data-sources/detail`.

No document template is available for a project
===============================================

Check that a compatible published template is available to the project. Its knowledge model compatibility rules, version and supported metamodel matter. With multiple workspaces, also check the organization and local libraries.

A template shows unsupported metamodel
======================================

Use a compatible version or update the custom template for context 19.0. Changing the metamodel version in its metadata is not enough; the template code also needs updating. See :doc:`/development/document-templates/document-context`.

A published knowledge model or template is missing
==================================================

Check its publication state, deprecation state and library scope. With multiple workspaces, local content with the same ID and version takes precedence over organization content.

A project template is missing
=============================

Check :doc:`/projects/detail/sharing` and the current workspace. A project template follows project access rules.

For further help, use the support contact configured for your instance; see :doc:`/getting-started/support`.
