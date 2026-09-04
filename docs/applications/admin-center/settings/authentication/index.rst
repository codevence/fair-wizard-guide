.. _auth-services:

Authentication
**************

The Authentication Settings page allows you to configure the authentication settings for users.

The **Default role** settings option allows us to define which :ref:`role<roles>` is assigned to new users.

.. WARNING::

    It is recommended to set this to the lowest-privilege role that fits new users. Otherwise, new users may be able to change content or settings for other users in the FAIR Wizard instance.

.. NOTE::

    A role configured as the default role for new users cannot be deleted.


For internal authentication, we can set:

- **Registration** - whether users can sign up on their own or not.
- **Non-Admin Login** - whether non-admin users can log in to the FAIR Wizard instance or not.
- **Two-Factor Authentication** - whether users need to confirm their login with a one-time code sent to their email address or not.
- **Session Expiration** - how long the user session is valid before the user needs to log in again in hours.
- **User Email Link Expiration** - how long the email links (e.g., for password reset) are valid before they expire and cannot be used anymore in hours.

.. NOTE::

    In case we are using OpenID or creating user accounts manually, registrations should be disabled. It is recommended to also disable non-admin login.


For **Two-Factor Authentication** (2FA) we can also configure **Code Length** (how many characters the code has) and **Expiration** period in seconds.

The FAIR Wizard also supports `Shibboleth <https://www.shibboleth.net/>`__ and `eduGAIN <https://edugain.org/>`__.

.. NOTE::

    For configuration of SAML, Shibboleth or eduGAIN please `contact the FAIR Wizard team <mailto:info@fair-wizard.com>`__.


----

.. raw:: html

    <h2>Table of Contents</h2>

.. toctree::
    :maxdepth: 2

    Internal<internal>
    OpenID<openid>
    SAML<saml>
