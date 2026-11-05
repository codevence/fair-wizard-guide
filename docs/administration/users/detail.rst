.. _user-roles:

Edit a user
***********

Open :guilabel:`Administration` → :guilabel:`Users` and select the user. :guilabel:`Manage Users` is required to edit another account.
Review the profile details, active state and organization role. Changes to a role affect the permissions the user receives; see :doc:`/administration/roles` before assigning broad access.

The detail also shows when the account was created and updated, when the user was last online and when consent was accepted. Missing visits and consent are shown as :guilabel:`Never` and :guilabel:`Not accepted`. Connected external accounts are listed with their provider. Users manage their own connections in :doc:`/account/connected-accounts`.

If internal authentication is enabled, an Admin can also change the user's password.

.. admonition:: With multiple workspaces

   The organization role is separate from membership and roles in individual workspaces. Use the workspace's Members page to change those assignments.

Active users can receive a notification when another person changes their organization role. Self-changes, unchanged roles and login-automation assignments are not notified.

.. figure:: /_static/screenshots/5.0/guide/user-profile.png
    :figclass: guide-screenshot
    :alt: Administrator view of a user in FAIR Wizard 5.0
    :width: 800

    Administrator view of a user.
