"""Use a matching dark capture when one exists; keep ordinary figure markup."""
from pathlib import Path
from docutils import nodes
from sphinx import addnodes


def pair_screenshots(app, doctree):
    prefix = '/_static/screenshots/5.0/'
    for image in list(doctree.findall(nodes.image)):
        uri = image.get('uri', '')
        if not uri.startswith(prefix) or uri.startswith(prefix + 'dark/'):
            continue
        dark_uri = prefix + 'dark/' + uri[len(prefix):]
        dark_file = Path(app.srcdir) / dark_uri.lstrip('/')
        if not dark_file.is_file():
            continue
        app.env.note_dependency(str(dark_file))
        dark = image.deepcopy()
        dark['uri'] = dark_uri
        dark['classes'].append('guide-image-dark')
        image['classes'].append('guide-image-light')
        # PDFs and other non-HTML outputs keep the original light capture.
        html_only = addnodes.only(expr='html')
        html_only += dark
        image.parent.insert(image.parent.index(image) + 1, html_only)


def setup(app):
    app.connect('doctree-read', pair_screenshots, priority=200)
    return {'version': '1', 'parallel_read_safe': True, 'parallel_write_safe': True}
