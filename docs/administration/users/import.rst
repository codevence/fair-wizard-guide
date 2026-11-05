Import Users
************

With **Manage Users**, open the user import action and choose :guilabel:`Download template`.
The CSV columns are ``email``, ``firstName``, ``lastName`` and ``affiliation``. Affiliation can be empty.

Upload the completed CSV. Review each row and select its organization role on the confirmation page; the initial selection is the default role. The 5.0 CSV does not require role UUIDs.
Choose whether to send invitation emails, then import the users. Resolve any reported invalid or already-used addresses.

Save CSV files as UTF-8. With multiple workspaces, assign the required workspace memberships separately; see :doc:`/administration/workspaces`.

.. figure:: /_static/screenshots/5.0/guide/user-import.png
    :figclass: guide-screenshot
    :alt: Import users from CSV in FAIR Wizard 5.0
    :width: 520

    Import users from CSV.

.. figure:: /_static/screenshots/5.0/guide/user-import-preview.png
    :figclass: guide-screenshot
    :alt: Review users before importing in FAIR Wizard 5.0
    :width: 720

    Review users before importing.
