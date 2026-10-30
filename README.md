# FAIR Wizard Guide

The FAIR Wizard user, administrator and developer guide, written in reStructuredText and built with Sphinx/Furo.

## Local build

Use Python 3.12, matching GitHub and Read the Docs:

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r docs/requirements.txt
sphinx-build -b html -W --keep-going -n -D notfound_urls_prefix=/ docs docs/_build/html
```

Serve `docs/_build/html` locally to review it. The command overrides the 404 prefix only for the local root URL; Read the Docs uses its versioned canonical URL.

For automatic rebuilds, install `docs/requirements.dev.txt` and run `make watch` in `docs`. To validate print sources:

```sh
sphinx-build -b latex -W --keep-going -n docs docs/_build/latex
```

A complete PDF build also needs a TeX installation (`make latexpdf` in `docs`); LaTeX source generation alone does not validate the rendered PDF.

See [CONTRIBUTING.md](CONTRIBUTING.md) for simple RST conventions, [RELEASING.md](RELEASING.md) for the develop → preview → production cycle and [WORKLOG.md](WORKLOG.md) for the current 5.0 work and remaining acceptance.

## Dependencies

`docs/requirements.direct.txt` lists direct dependencies; `docs/requirements.txt` pins the tested environment. Update in an isolated Python 3.12 environment, regenerate the lock file and run both strict builds. Do not upgrade Docutils independently beyond the version supported by Sphinx.

## License

Guide content is licensed under [CC BY-SA](LICENSE). Bundled Nunito fonts retain their OFL license in `docs/_static/fonts`.
