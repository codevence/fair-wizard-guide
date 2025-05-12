Create Locale
*************

We can create a new locale directly in |project_name| by pressing :guilabel:`Create` from :doc:`../locales`. We need to fill the details about the new locale: name, description, language code (`RFC5646 <https://www.rfc-editor.org/rfc/rfc5646.html>`__, e.g. ``en`` or ``en-GB``), locale ID, locale version, license, README (with Markdown syntax), and recommended app version. The recommended app version captures for which version of the |project_name| is this locale intended and compatible with (it can be used in other versions as well but may have some untranslated texts).

Finally, a POT files can be downloaded here. From them, we can create PO files in a standard (`gettext <https://www.gnu.org/software/gettext/>`__-based) way. There is a POT file for each app of FAIR Wizard and also for the emails.

We can `download the locales </_static/fw-4-18-0-locales.zip>`_ here.

.. .. figure:: create/form.png
    
..     Detail of a locale.

