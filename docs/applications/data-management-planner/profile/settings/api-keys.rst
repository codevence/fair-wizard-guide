.. _api-keys:

API Keys
********

When we want to access the FAIR Wizard through FAIR Wizard API we have to set up an API Key. The API Key has an :guilabel:`API Key Name` so we can remember for what purpose this Key is used and :guilabel:`Expiration` which is a date from when the API Key will no longer be valid.

.. figure:: api-keys/form.png
    :width: 800

    Form for creating an API Key.


After filling out the :guilabel:`API Key Name` and :guilabel:`Expiration`, an **API Key** is generated. In this step we have to copy the API Key, because after seeing it once, it is no longer possible to access it again.

After we click on Done button, the new API Key is hidden and the information about this key is added to the table below, that contains all Active API Keys.

.. NOTE::

    API Keys are shared across FAIR Wizard applications. To replace a key created before version 4.35, create a new API Key in :ref:`Admin Center<api-keys-admin>` and update the applications and scripts that use it.
