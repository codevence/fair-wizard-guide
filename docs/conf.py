# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'FAIR Wizard'
copyright = '2024, FAIR Wizard Team'
author = 'FAIR Wizard Team'

project_name = 'FAIR Wizard'
project_name_full = 'FAIR Wizard'
registry_name = 'FAIR Wizard Registry'

# The full version, including alpha/beta/rc tags
version = release = '4.4'

rst_prolog = f"""

.. |compose_ver| replace:: {release}
.. |project_name| replace:: {project_name}
.. |project_name_full| replace:: {project_name_full}
.. |registry_name| replace:: {registry_name}

"""

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx-prompt',
    'sphinx_substitution_extensions',
    'sphinx_reredirects',
    'sphinxcontrib.youtube',
    'sphinx.ext.todo',
    'sphinx_toolbox.confval',
    'sphinx.ext.imgconverter',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_favicon = '_static/favicon.ico'
html_theme_options = {
    'light_logo': 'logo/logo-light-mode.svg',
    'dark_logo': 'logo/logo-dark-mode.svg',
    'light_css_variables': {
        'color-brand-primary': '#019AD6',
        'color-brand-content': '#019AD6',
        'sidebar-item-spacing-horizontal': '.75rem',
    },
    'dark_css_variables': {
        'color-brand-primary': '#019AD6',
        'color-brand-content': '#019AD6',
        'sidebar-item-spacing-horizontal': '.75rem',
    },
    'sidebar_hide_name': True,
    'top_of_page_button': None,
}
html_js_files = [
    'js/track.js',
]


def setup(app):
    app.add_css_file('style.css')

suppress_warnings = [
    # Suppress "WARNING: unknown mimetype (issue with .ico)
    'epub.unknown_project_files',
]

redirects = {
     'more/changelog': 'https://fair-wizard.com/changelog',
     'application/knowledge-models/editors/create': 'applications/data-management-planner/knowledge-models/editors/create',
     'application/document-templates/editors/create': 'applications/data-management-planner/document-templates/editors/create',
     'application/projects/list/detail/questionnaire/#integration-question': '/applications/data-management-planner/projects/list/detail/questionnaire/#integration-question'
 }
