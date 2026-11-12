.. _integration-questions:

Integration Questions
*********************

An :ref:`integration question<integration-question>` searches a service or dataset and stores the selected result in the questionnaire. Its integration defines how the result is displayed, including any link or persistent identifier. Examples of external resources include `FAIRsharing <https://fairsharing.org>`_ and `ROR <https://ror.org>`_.

We can connect a question to a source in three ways:

- **API** - using an API provided by the external service to search for the results
- **Widget** - using a specialized widget implemented for the connection with FAIR Wizard
- **Data source** - searching tabular data managed in FAIR Wizard; see :doc:`/knowledge-models/data-sources/detail`



For searchable data hosted within FAIR Wizard, use the built-in **Data source** integration and a dataset from :doc:`/knowledge-models/data-sources/index`. This replaces the earlier Value Integration workflow; a dataset UUID must refer to an available dataset in the intended scope.

.. toctree::
   :maxdepth: 1

   integration-api
