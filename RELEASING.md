# Releasing the FAIR Wizard guide

The release cycle remains **develop → preview → production**. Prepare and review 5.0 on develop. Do not promote an incomplete guide or change production while preparing preview. Pull-request previews are not required.

## Prepare on develop

1. Pull develop and reconcile the supported FAIR Wizard changes. Synchronize applicable upstream DSW guidance selectively; do not overwrite FAIR Wizard workspace behavior or styling with legacy application pages.
2. Set `version` and `release` in `docs/conf.py`. Keep the guide restricted to the release being documented.
3. Update user, administrator, developer and upgrade pages. Use `maintenance/guide-links.develop.json` for the matching 5.0 staging/develop help-link map (73 verified keys), applying it to the guide-links repository with the corresponding application release. Promote the links through that repository's normal release process. Old URL/anchor preservation is not required; the existing redirect cleanup is deferred.
4. Build with strict warnings and review the HTML. GitHub continues to build pushes, including develop. A LaTeX-source build also runs in CI; Read the Docs builds the downloadable PDF.
5. When screenshot work starts, prepare the supplied environment with controlled content, locales, knowledge models, templates and representative activity. Use staging for early preparation and the preview instance for final screenshots after that application release reaches preview. Check both modes only where the workflow differs. Do not clear real customer audit history to prepare media.
6. Review new screenshots and alt text. Until replacements are ready, keep old screenshots visibly marked and retain the media inventory.

## Promote through the channels

1. At the next release, merge the current preview guide into production after review, preserving merge history. Check its Read the Docs build and production URL.
2. After FAIR Wizard 5.0 reaches preview, merge the prepared develop guide into preview. Check its build and rendered pages before tagging the released preview commit with the release version.
3. Promote that reviewed preview to production with the corresponding application production release. For 5.0, the planned application dates are 6 November 2026 (preview) and 4 December 2026 (production).
4. Verify version selection, home, search, a deep page, 404, assets and downloadable PDF in the published Read the Docs version. These hosted checks cannot be replaced by a local build.

Use reviewed pull requests where practical. If a merge must be performed locally, resolve conflicts on the release branch and run the same checks before pushing. Do not force-move an existing published release tag merely to trigger a rebuild; rebuild the relevant Read the Docs version instead.

## Hotfixes

Create production hotfixes from production and merge the reviewed fix into production, preview and develop. Create preview hotfixes from preview and merge into preview and develop. Verify each affected Read the Docs build. Keep release-channel branches; remove only temporary merged working branches.

## Read the Docs

The repository configuration uses Python 3.12 and builds HTML, HTML ZIP and PDF. Retain the develop, preview and production version cycle. No PR-preview setting change is needed. After content review, check the hosted versions point to their intended branches and rebuild only when a build fails or does not reflect the correct commit.
