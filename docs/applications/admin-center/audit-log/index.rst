.. _audit-log:

Audit Log
*********

Audit log is a feature that allows admins to track everything that is happening in the FAIR Wizard.

Users need the :ref:`Use Audit Log<roles>` role permission to view the Audit Log.

.. NOTE::

    For now, audit log is available for Admin Center, Analytics and Integration Hub. Data Management Planner will be added in the future updates.


List can be searched based using content of audit logs. The dropdown menu can be used to select which app logs we want to display. Then we can also select which component we want to see. In the list we can see what particular action has been done, who did it and when it happened.

.. NOTE::

    Audit log cannot see user logging in the system, until the user is logged in. So actions connected to account creation and logging are placed under Anonymous user. This is not a system user, but it is used to show that the action was done by someone who is not logged in yet. After logging in, all actions are connected to the user account.


.. figure:: index/list.png

    Audit log.


A log item detail can be opened by clicking any log record. Based on which log record has been opened, detail contains information on what was changed and how. Some things, such as performer of the change can be clicked to open a detail of that user.

.. figure:: index/detail.png

    Audit log detail.
