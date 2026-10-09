.. _import-users:

Users Import
************

Users with the :ref:`Manage Users<roles>` role permission can import users using provided template. The template has five columns: email, firstName, lastName, affiliation and roleUuid. Once it is filled with data, we can import it back to the FAIR Wizard to populate it with users.

.. NOTE::

    We can find the roleUuid for each role in the :ref:`Roles<roles>` section of the FAIR Wizard. Open Role detail and copy the UUID from the URL. For example, if the URL is `https://fair-wizard.com/roles/123e4567-e89b-12d3-a456-426614174000`, then the roleUuid is `123e4567-e89b-12d3-a456-426614174000`.
    

.. figure:: users/users.png
    :width: 528

    Import users.


We can also select if we want to send an invitation email or not by :guilabel:`Send invitation email` switch.

.. figure:: users/users-confirmation.png

    Import users confirmation with switch to send invitation email.


.. WARNING::

    Using Microsoft Excel to edit the template may cause issues with the encoding of the file. If you encounter any issues, please use some other editor to edit the file.
