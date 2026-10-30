Knowledge Models
****************

A knowledge model defines the chapters, questions, guidance, integrations and other content used by a project's questionnaire.
The library contains published knowledge models. We can create and edit knowledge models in the editors and publish new versions.

Knowledge model identifiers and versions are separate values. A new version can update content without changing the model's identifier.

.. admonition:: With multiple workspaces

   Workspaces can use their local content and the organization library. If a knowledge model with the same ID and version exists in both libraries, the workspace version is used. Manage organization-library content with :guilabel:`Manage Library`; manage local content with the relevant knowledge-model permissions.

Use :doc:`/knowledge-models/data-sources/index` for datasets used by integration questions, and :doc:`/knowledge-models/secrets` for credentials used by integrations.

.. toctree::
   :maxdepth: 1

   library/index
   editors/index
   secrets
   data-sources/index
