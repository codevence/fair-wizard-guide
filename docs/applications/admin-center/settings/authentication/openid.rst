Open ID Settings
****************

Using these settings we can add `Open ID <https://openid.net/>`__ configuration to allow logging into the |project_name| instance via external identity provider. Here is a detailed description of the setup:

1. Go to https://portal.azure.com/.
2. Go to ``App registrations``.
3. Click on ``New registration``.
4. Fill in a name.
5. Select ``Accounts in this organizational directory only (Single tenant)``.
6. Keep ``Redirect URI`` empty.
7. Click on ``Register``.
8. Copy and store ``Directory (tenant) ID`` and ``Application (client) ID``.
9. Click on ``Manage`` in the left menu → ``Certificates & Secrets``.
10. Click on ``New client secret``.
11. Fill description, set ``Expires`` and note it somewhere, then click on ``Add``.
12. Copy ``Value`` and store it somewhere. You will not able to view it again.

13. Go to OpenID in FAIR Wizard: :guilabel:`Admin Center` → :guilabel:`Settings` → :guilabel:`Organization OpenID` → :guilabel:`Create`.

14. In :guilabel:`Microsoft` tab fill in :
	- ``Application (client) ID``
	- ``Directory (tenant) ID``
	- ``Client Secret`` → ``<stored secret value>``

15. (optional) fill Icon (``fab fa-microsoft``, or some other from `Font Awesome <https://fontawesome.com/v6/search?o=r&m=free>`_), :guilabel:`Background Color` and :guilabel:`Text Color`.

16. Click on :guilabel:`Save`.

17. Go back to Microsoft Azure.
18. Click on ``Manage`` in the left menu → ``Authentication (Preview)``.
19. Click on ``Add Redirect URI``.
20. Click on ``Web``.
21. Copy ``Redirect URI`` and ``Front-channel logout URL`` from FAIR Wizard.
22. **Do not** check any checkbox.
23. Click on ``Configure``.
24. Click on ``Manage`` in the left menu → ``API permissions``.
25. Click on ``Add a permission``.
26. Click on ``Microsoft Graph`` → ``Delegated permissions``.
27. Under ``OpenId permissions`` check ``email``, ``openid`` and ``profile``. Under ``User`` keep checked ``User.Read``.
28. Click on ``Add permissions``.

29. Click on ``Manage`` in the left menu → ``Token configuration``.
30. Click on ``Add optional claim``.
31. Select ``ID`` and check ``email``, ``family_name`` and ``given_name``.
32. Click on ``Add``.

33. Test your openId in FAIR Wizard (You might need to refresh the login page for the login button to appear).

.. figure:: openid/openid.png
    :width: 700
    
    Example configuration of OpenID service.


Automations
===========

We can use the **Create automation** button to add some extra steps after users use this login option. There are two tabs. Configuration, where we can set up automation using the `Integration SDK <https://integration-sdk.fair-wizard.com/en/latest/>`__ and Logs where we can see logs of the automation. The automation can have its name changed and it can be enabled or disabled. See details in :ref:`automations`.

.. NOTE::

	There can be only one automation per login configuration. However, multiple actions can be set up within a single automation script.

