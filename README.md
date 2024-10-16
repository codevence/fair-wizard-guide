# FAIR Wizard Guide

[![License](https://img.shields.io/github/license/ds-wizard/guide)](LICENSE)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/4975/badge)](https://bestpractices.coreinfrastructure.org/projects/4975)

## Usage

### Install Requirements

```
pip install -r docs/requirements.txt
```

Extra requirements only for development:

```
pip install -r docs/requirements.dev.txt
```

### Generate Guide

```
cd docs
make help
make html
```

### Develop Guide

```
make watch
```

Use [Python Developer’s Guide](https://devguide.python.org/documentation/markup/) as a reference for writing RST, specific rules are listed in the [CONTRIBUTING](CONTRIBUTING.md) file.

### Refresh Dependencies

```
rm -r env
python -m venv env
source env/bin/activate

pip install -r docs/requirements.direct.txt
pip freeze > docs/requirements.txt
```

## References

* [Sphinx Documentation](https://www.sphinx-doc.org/en/master/)
* [reStructuredText Markup Specification](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html)
* [RST Cheatsheet](https://github.com/ralsina/rst-cheatsheet)
* [Git Basics](https://www.atlassian.com/git)
* [How to Write a Git Commit Message](https://cbea.ms/git-commit/)

## License

This project is licensed under the  Creative Commons Attribution-ShareAlike (CC BY-SA) - see the
[LICENSE](LICENSE) file for more details.

## reStructuredText Conventions

### Headings

Headings should use the following syntax for specific levels:

```rst
Chapter (page)
**************

Section
=======

Subsection
----------

Subsubsection
^^^^^^^^^^^^^

Paragraph
"""""""""
```

Always the number of characters should match length of the text.
