Integration through the API
***************************

Use the :guilabel:`API URL` and :guilabel:`API Docs` shown in FAIR Wizard's :doc:`About dialog </account/about>`. The instance's OpenAPI documentation is the reference for its request and response schemas.
FAIR Wizard 5.0 uses one API base, normally ``https://<instance>/api``, instead of separate application APIs.

Authentication
==============

Use an :doc:`API key </account/api-keys>` in the ``Authorization: Bearer <key>`` header. The key acts with its user's current permissions and validity.
Use an account and scope appropriate to the integration; do not put credentials into a knowledge model or commit them to source control.

.. code-block:: python

   import os
   import requests

   api_url = os.environ['FW_API_URL'].rstrip('/')
   response = requests.get(
       f'{api_url}/users/current',
       headers={'Authorization': f'Bearer {os.environ["FW_API_KEY"]}'},
       timeout=30,
   )
   response.raise_for_status()
   print(response.json()['email'])

Workspace scope
===============

Single-workspace operations can use the implicit workspace. For workspace-scoped collection operations in multi-workspace mode, provide the target workspace using the endpoint's ``w`` query parameter.
Organization-library operations use their supported organization scope; UUID-based detail operations can derive scope from the resource. Do not add the same scope flags to every endpoint without checking its schema.
A workspace identifier does not bypass permissions.

Important 5.0 contracts
=======================

* Knowledge models and document templates use separate ``id`` and ``version`` fields; UUID fields still identify stored entities where required.
* Settings are section-based, with effective values and supported override/reset behavior.
* Project CSV imports use the synchronous project-import contract, not the old queued administrative endpoint.
* Login automations require the workspace assignment structure described in :doc:`/administration/automations`.
* Editor and questionnaire event APIs validate structure and references. Handle validation failures and revision conflicts instead of assuming an event was accepted.
* KM secret responses contain metadata, not their existing value. Supply a replacement when updating a secret.

Use :doc:`/development/document-templates/document-context` for context endpoints and :doc:`/account/connected-ais` for MCP connections.
