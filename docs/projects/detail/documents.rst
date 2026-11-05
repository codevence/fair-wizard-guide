.. _project-documents:

Documents
*********

In the :guilabel:`Documents` tab in the project detail we can manage the documents related to the project. We can see a list of all the documents with their **format**, **file size**, and **document template** used to create that document.

While we can quickly see how the current state of the questionnaire looks like in the document in the :ref:`preview<preview>` tab, the documents created here are persistent. Once generated, a stored document does not change when we edit the questionnaire. We can download the same file later while it remains stored.


.. figure:: /_static/screenshots/5.0/projects/documents.png
    :figclass: guide-screenshot
    :alt: Generated documents in the Coastal Biodiversity Survey example
    :width: 800

    Generated documents.

.. _new-document:

New document
============

We can click on :guilabel:`New document` when we want to create a new document. We need to give a name to our new document (project name is prefilled) and choose the **document template** and **format**. If there is a :ref:`default document template and format<default-document-template>` set for the project, they are prefilled in this form. However, we can change them before creating the document.

When the selected template offers :ref:`additional locales<document-template-locales>`, we can also choose the document language; the project's default document language is prefilled when available.

Once we click :guilabel:`Create`, we are taken back to the document list and we'll see the new document there (it might take a while before it is generated though).


.. figure:: /_static/screenshots/5.0/projects/new-document.png
    :figclass: guide-screenshot
    :alt: Create a document in the Coastal Biodiversity Survey example
    :width: 350

    Create a document.

Document Submission
===================

:ref:`Submission services<submission-service>` can be used to quickly submit the document directly from FAIR Wizard to some external service.

.. TODO::

    Screenshot pending: Document submission with a compatible service selected; deferred by request.

If there are any document submission services configured for our FAIR Wizard, we should be able to see :guilabel:`Submit` option when we open document menu in the document list by clicking on the triple dots. Then we choose the desired service from the list and click on :guilabel:`Submit`.

We can see all the submissions for each document in the document list as well.

Deleting a generated document, its project or its document template can remove the stored file. A document's persistence does not prevent these deletion actions.
