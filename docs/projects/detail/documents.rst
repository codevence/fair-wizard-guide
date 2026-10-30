.. _project-documents:

Documents
*********

In the :guilabel:`Documents` tab in the project detail we can manage the documents related to the project. We can see a list of all the documents with their **format**, **file size**, and **document template** used to create that document.

While we can quickly see how the current state of the questionnaire looks like in the document in the :ref:`preview<preview>` tab, the documents created here are persistent. That means that the once the document is created, it is immutable and you can download it later while it remains stored, after you have changed the questionnaire, and it will still be the same.


.. figure:: /_static/earlier-interface/applications/data-management-planner/projects/list/detail/documents/list.png
    :alt: List of the documents on the project.

    **Outdated screenshot (4.x).** List of the documents on the project.



.. _new-document:

New document
============

We can click on :guilabel:`New document` when we want to create a new document. We need to give a name to our new document (project name is prefilled) and choose the **document template** and **format**. If there is a :ref:`default document template and format<default-document-template>` set for the project, they are prefilled in this form. However, we can change them before creating the document. When the selected template offers :ref:`additional locales<document-template-locales>`, we can also choose the document language; the project's default document language is prefilled when available. Once we hit :guilabel:`Create`, we are taken back to the document list and we'll see the new document there (it might take while before it is generated though).


.. figure:: /_static/earlier-interface/applications/data-management-planner/projects/list/detail/documents/new.png
    :alt: We can choose any compatible document template and format when creating a new document on the project.
    :width: 528

    **Outdated screenshot (4.x).** We can choose any compatible document template and format when creating a new document on the project.


Document Submission
===================

:ref:`Submission services<submission-service>` can be used to quickly submit the document directly from FAIR Wizard to some external service.

.. figure:: /_static/earlier-interface/applications/data-management-planner/projects/list/detail/documents/submission.png
    :alt: Submission service selection for a document.
    :width: 540

    **Outdated screenshot (4.x).** Submission service selection for a document.


If there are any document submission services configured for our FAIR Wizard, we should be able to see :guilabel:`Submit` option when we open document menu in the document list by clicking on the triple dots. Then we choose the desired from the list and click on :guilabel:`Submit`.

We can see all the submissions for each document in the document list as well.

Deleting a generated document, its project or its document template can remove the stored file. A document's persistence does not prevent these deletion actions.
