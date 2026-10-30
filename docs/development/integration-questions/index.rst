.. _integration-questions:

Integration Questions
*********************

FAIR Wizard can be integrated with other services using so called :ref:`integration question<integration-question>`. The answer to that type of question does not contain only the answer itself but also a link to that external resource (which can be done, for example, using a persistent identifier). Therefore, these answers help clearly understand what the researchers use and promotes interoperability.

Examples of such integrations that are used within the common knowledge model is `FAIRsharing <https://fairsharing.org>`_ or `ROR <https://ror.org>`_.

There are two ways of how we can connect FAIR Wizard to these services:

- **API** - using an API provided by the external service to search for the results
- **Widget** - using a specialized widget implemented for the connection with the FAIR Wizard



For searchable data hosted within FAIR Wizard, use the built-in **Data source** integration and a dataset from :doc:`/knowledge-models/data-sources/index`. This replaces the earlier Value Integration workflow; a dataset UUID must refer to an available dataset in the intended scope.

.. toctree::
   :maxdepth: 1

   integration-api
   migration
