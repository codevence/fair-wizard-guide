Login Screen
************

The organization's Login Screen settings control information and announcements shown before people sign in.
Use :guilabel:`Login Info` for text next to the sign-in form and :guilabel:`Sidebar Login Info` for text underneath it. Both support Markdown. Announcements on this page are visible before sign-in, so include only information suitable for everyone visiting the instance.

Login screen content is organization-level. Workspace-specific dashboard or menu content is configured under :doc:`/settings/dashboard-menu`.

.. figure:: /_static/screenshots/5.0/guide/settings-login-screen.png
    :figclass: guide-screenshot
    :alt: Login Screen settings in FAIR Wizard 5.0
    :width: 800

    Login Screen settings.

.. figure:: /_static/screenshots/5.0/guide/login-announcement.png
    :figclass: guide-screenshot
    :alt: Login screen announcement settings in FAIR Wizard 5.0
    :width: 350

    Login screen announcement settings.

Login information
=================

Use **Login Info** to explain who the instance is for, how people should sign in, or which external identity provider they should choose. **Sidebar Login Info** adds a separate message beneath the sign-in form. Both fields support Markdown.

Login announcements
===================

Use :guilabel:`Add announcement`, choose **Info**, **Warning** or **Critical**, and enter the Markdown content. Announcements appear above the login screen's main content. To display the same message after sign-in, also add it in Dashboard & Menu.
