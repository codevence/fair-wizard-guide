# Writing the guide

Write against the supported release and verify changed workflows against its specifications and frontend/backend implementation. Record source conflicts in WORKLOG.md rather than inventing a workflow. Documentation is not evidence of runtime acceptance.

Use ordinary reStructuredText: page/section headings, paragraphs, lists, `toctree`, `note`, `warning`, `admonition`, `list-table` and code blocks. No custom layout is needed for workspace differences. Explain shared behavior once and add a “With multiple workspaces” note only when behavior changes.

Use `:doc:` for a useful link to another page and `:ref:` for a specific labeled section. Use descriptive link text. Do not add a link to every mention of a feature.

All informative images need meaningful `:alt:` text. Retained 4.x screenshots must have an **Outdated screenshot (4.x)** caption. Conceptual diagrams can remain when still valid. Capture replacements only after the 5.0 environment is supplied; track them in `maintenance/media-review.csv`. Earlier videos are labeled for review too.

Keep headings simple:

```rst
Page title
**********

Section
========

Subsection
----------
```

Build before review (see README.md). Warnings and unresolved references fail the checks. Review both light and dark HTML and the print output. A successful build does not verify permissions, customer-specific integrations or screenshot accuracy.
