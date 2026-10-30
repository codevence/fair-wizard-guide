Import Users
************

With **Manage Users**, open the user import action and choose :guilabel:`Download template`.
The CSV columns are ``email``, ``firstName``, ``lastName`` and ``affiliation``. Affiliation can be empty.

Upload the completed CSV. Review each row and select its organization role on the confirmation page; the initial selection is the default role. The 5.0 CSV does not require role UUIDs.
Choose whether to send invitation emails, then import the users. Resolve any reported invalid or already-used addresses.

Save CSV files as UTF-8. With multiple workspaces, assign the required workspace memberships separately; see :doc:`/administration/workspaces`.

Earlier interface
=================

These screenshots show the 4.x interface. They will be replaced with 5.0 screenshots.

.. figure:: /_static/earlier-interface/applications/admin-center/import/users/users.png
    :alt: Import users.
    :width: 528

    **Outdated screenshot (4.x).** Import users.

.. figure:: /_static/earlier-interface/applications/admin-center/import/users/users-confirmation.png
    :alt: Import users confirmation with switch to send invitation email.

    **Outdated screenshot (4.x).** Import users confirmation with switch to send invitation email.
