Audit Log
*********

The audit log records actions such as creating projects, changing access, working in knowledge model and document template editors, generating documents, uploading files and changing sharing settings.
Open :guilabel:`Administration` → :guilabel:`Audit Log` with the :guilabel:`Use Audit Log` permission.

Search the audit log
====================

Filter activity by the available user, date, component and action fields. We can open a record to see who performed the action, when it happened and what changed.
Actions performed through a connected AI client identify the MCP source, client and tool.

The audit log does not record every screen visit or answer change. We can see questionnaire changes in the project's version history.

.. admonition:: With multiple workspaces

   Audit records can identify the workspace involved. In multi-workspace mode, the role editor makes **Use Audit Log** imply **Manage Workspaces**. Review that broader permission before assigning the role.

Earlier audit history
=====================

The 5.0 audit view contains records created after the upgrade. A readable export of legacy records is available from the FAIR Wizard team on request.

.. figure:: /_static/screenshots/5.0/guide/audit-log.png
    :figclass: guide-screenshot
    :alt: Audit Log in FAIR Wizard 5.0
    :width: 800

    Audit Log.

.. figure:: /_static/screenshots/5.0/guide/audit-detail.png
    :figclass: guide-screenshot
    :alt: Audit event details in FAIR Wizard 5.0
    :width: 350

    Audit event details.
