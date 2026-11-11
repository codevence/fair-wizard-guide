# FAIR Wizard 5.0 guide work log

Updated 30 October 2026. Work is on **docs/fair-wizard-5-guide**, branched from develop, for review before promotion to preview and production.

## Implemented

- Reorganized the former application-specific guide into tasks: getting started, projects, knowledge models, document templates, groups, account, administration, settings, Analytics, development, upgrade and reference. Consolidated duplicated account/settings pages.
- Updated 5.0 workflows: workspace membership and role scopes, shared/local libraries and precedence, deletion dependencies, Data Sources, secrets, CSV imports, section overrides, plugins, PO-based UI/email translations, authentication, login automations, API keys, audit and MCP.
- Updated template/context/TDK/schema guidance for context 19.0 and KM metamodel 20. Corrected examples and removed obsolete fixed converter-version claims. Documented rendering resource restrictions.
- Applied the approved simple Furo styling, local Nunito heading fonts, system body stack and application illustration on the 404 page. Retained the font license.
- Added contextual cross-page links. Kept native RST; removed raw HTML tables/headings and unnecessary layout structures. Removed unused legacy explicit anchors rather than adding preservation machinery.
- Kept 137 legacy screenshot placements explicitly marked **Outdated screenshot (4.x)**. Retained two conceptual diagrams. All rendered images have nonempty alt text. Five retained videos are labeled as accompanying an earlier guide; they have not been watched for acceptance. Media inventories are in `maintenance/`.
- Added authoring and release instructions. Retained develop → preview → production and the existing push builds. No Notion writes, hosted setting changes, branch promotion, commit or push.

## Evidence

Specifications: read-only WEP 24–41 snapshot/register checked 30 October; no last-edit changes against the saved sources. WEPs supersede the broad draft. Future console/5.1/5.2 features are excluded.

Implementation revisions used:

- Backend `main`: `d2bedfa9ba56728d80f12cf6cb396ad4a6abead0`.
- Frontend `feature/fw`: `fd30b4173b2ac5f6260c4acf1abcac4c618f0add`.
- Engine tools `main`: `6c159fa862b381890c6a1464be846df4f57fd387`.

Key checks include frontend `Fw/Layouts/AppLayout.elm`, `Fw/Data/RolePermission.elm`, shared settings/role/group/import/editor pages, backend project ACL and role-permission definitions, and engine-tools context/schema/TDK/renderer sources. The template references pin the engine-tools revision to make their evidence reviewable. Scope and backend/frontend mismatches must be resolved before treating the guide as runtime acceptance.

## Verification

- Pinned requirements installed in a clean Python 3.12 environment, matching CI/Read the Docs. `pip check` passed. Retained the tested dependency pins; no new extension or major dependency upgrade was needed.
- Strict full HTML and LaTeX-source builds passed (`-W --keep-going -n`).
- Generated guide links, local assets and anchors checked; all rendered image alt attributes checked. Results are in `maintenance/validation.json`.
- Browser review covers home, a changed workflow and 404 in the approved theme. Full runtime, accessibility and PDF acceptance are separate release checks.

## Remaining acceptance and deferred work

- Supply the screenshot environment, adapt the capture automation and replace the labeled screenshots. Review/replace the five retained videos.
- Review rendered PDF on Read the Docs: local TeX/latexmk is not installed, so only LaTeX source generation has been validated.
- Runtime-check guide workflows on 5.0 with representative single/multi-workspace accounts. In particular, test notifications with actual mail templates, login automations, destructive dependency previews, template output and customer integrations. Code presence is not a runtime pass.
- WEP 25 describes Reporting DB exports, but a customer-facing download workflow was not located in the reviewed branches. No speculative how-to was added; developers must confirm the delivery/access mechanism.
- Withdrawn after source review: the earlier assignable-role concern inspected the Shared definition without the FAIR Wizard override. Manage Library and Manage Workspaces are included by the FAIR Wizard definition; this is not an outstanding confirmed defect.
- WEP 41 toolset consent selection is not present in the reviewed frontend flow; no instructions for that selector were added.
- Actual document-size limits depend on deployment overrides; the source default is not presented as every hosted customer's limit.
- Prepared `maintenance/guide-links.develop.json`: 73 legacy and current frontend help keys, all resolving to generated pages/anchors (the external Integration SDK URL is retained). Apply it through the normal versioned guide-links release process. Redirect cleanup remains deferred; the three existing incorrect legacy redirects are unchanged and excluded from the generated-guide link check.
- Hosted channel/version and downloadable-PDF acceptance must be performed when promoting the reviewed guide. No PR-preview change is required.

## Navigation correction — 30 October 2026

- Removed the redundant toctree from `docs/projects/list.rst`; its children already belong to `docs/projects/index.rst`. This fixes the repeated Projects sidebar branches.
- Removed duplicate generation-step entries from `docs/development/document-templates/index.rst`; the steps remain under their specification page.
- Verification: strict full HTML build passed. Audited the built toctree graph across all 134 source pages: no page has multiple toctree parents. Browser review confirms the Projects sidebar now shows one branch for each page. Earlier link-count totals above describe the initial implementation build.
- No commit, push or release-channel promotion. Screenshot/runtime/PDF acceptance work remains as listed above.

## Wording and PR preparation — 30 October 2026

- Simplified the rewritten user and administrator pages to match the original guide style: explanatory “we can” instructions, concrete feature/control names and less abstract wording. The pass touched 57 pages, including a shorter shared warning above old screenshots. It retains the 5.0 behavior and permission details.
- Created `docs/fair-wizard-5-guide` from develop for a PR back to develop. Preview and production are unchanged.
- Verification after the wording pass: strict HTML and LaTeX-source builds passed in Python 3.12; 22,411 generated local references checked with no missing target/anchor or image alt; the built toctree has no duplicate parents across 134 source pages.
- Screenshot replacement, live single/multi-workspace checks, rendered PDF review and the product questions listed above remain open.

## Screenshot integration — 1 November 2026

- Copied all 143 available Professional captures from fw-screenshots into docs/_static/screenshots/5.0, with 147 figure placements across 82 pages. Kept the source PNGs and approved crops unchanged; broad views fit within 800 CSS pixels, smaller crops keep their native logical width
- Replaced corresponding legacy figures and added captured examples for roles, Connected AIs, Data Sources, additional question inputs and other new flows. Added captions and descriptive alt text; removed obsolete shared Earlier interface headings on updated pages. Twenty-six remaining old placements retain their individual Outdated screenshot labels
- Kept explanatory guide prose and multi-workspace sections. All current images are Professional QA examples, including partial/empty states; the dedicated-environment rerun remains necessary. Analytics reporting, Enterprise variants and blocked captures were not invented or replaced
- Added maintenance/screenshot-integration.json linking captures to pages and recording partial states; maintenance/screenshot-render-validation.json records checks. Existing legacy assets remain available; no unrelated image cleanup or redirect changes
- Verification: strict Sphinx HTML build passed; 27,603 generated local references checked with zero missing file/anchor/image-alt errors after normalizing the 404 page’s Read the Docs /en/latest prefix to the local root. Existing redirect pages remain excluded as previously agreed; external destinations were not live-tested. Inspected rendered project creation and sharing pages for readable image sizing and native modal backdrop
- Local rendered guide: http://127.0.0.1:8769/index.html. Changes remain on docs/fair-wizard-5-guide; no commit, push or release-channel promotion

## Proofread, index and dark screenshot pilot — 1 November 2026

- Corrected previously recorded factual errors and reconciled every numbered item in the earlier content audit in maintenance/proofread-review-2026-11-01.md; unresolved procedures and product questions remain explicitly listed there
- Simplified the front page with compact topic links, existing illustration, FAIR Wizard website backlink and exact DSW community Discord label/invitation from dsw-web. Added a restrained screenshot frame
- Kept all 143 light captures and 147 RST figure placements. Added three real dark captures using the same Cypress data/scenarios/crops. A single Sphinx hook detects matching dark files; one shared CSS rule follows explicit/system theme. No duplicated page markup or new dependency
- AI Prefill retained as a supported 5.0 flow following user confirmation; removed repeated instructions while preserving request-only availability, Claude and completion-email details
- Strict HTML build, local links/images/alt checks and navigation graph checks passed. 134 source pages, 133 navigable plus intentional 404; no duplicate parents, missing targets, cycles or unintended orphans. Visual checks covered the tidied index, screenshot frame and actual theme switching. Three dark capture checks and 13 offline Cypress-scaffold tests passed
- Further screenshots, provider walkthroughs, minimal template example, support walkthrough and product questions are listed in the review. Analytics and Enterprise remain deferred. No push, PR update, release promotion or Notion changes

## Getting Started template overview — 1 November 2026

- User accepted the index. Expanded Document Template to mirror the Knowledge Model page's conceptual approach: structure, metadata, compatibility, formats, generation steps, files, languages and authoring/use. Kept detailed technical procedures on linked pages
- Replaced the introductory library-list image with the existing template-detail capture; updated its placement inventory. No new screenshot or product behavior invented
- Rechecked Sharing in a fresh browser load: guide Dark mode selects sharing1.png (the real dark capture), visually confirmed. Existing tab state was not assumed; reload suggested if the earlier white image remains visible

## Cropped screenshot sizing — 1 November 2026

- Reduced 57 cropped figure placements to at most 500 CSS pixels, keeping already-smaller crops at their existing width. Full application/settings views retain their current width
- Used the standard RST width option; original PNGs, crops and the single dark-variant mechanism are unchanged. Dark copies inherit the same width

## Screenshot and backlog correction — 1 November 2026

- Reduced cropped examples again, to 350 CSS pixels maximum where they were previously at 500 or below; full-page/settings views unchanged. Original PNGs/crops and dark-pair handling remain unchanged
- Removed the incorrect project-migration conflict task after checking Common.Pages.Projects.CreateMigration and the current guide. Project migration applies model/version/tags directly; KM editor migration is separate
- Remaining dark captures explicitly deferred until switching to the dedicated environment; this is a dependency checkpoint, not a timed reminder
- QA preview/download failures are dated observations from 30 October, not a claim of current failure or proven root cause

## Sidebar jumping — 1 November 2026

- Reproduced the reported menu jump: navigating Questionnaire → Settings reset left-menu scrollTop from 377 to 0 and collapsed the previous branch, moving the clicked row from y=580.39 to y=445.39
- Added one sidebar-position script, loaded with the sidebar template before paint, to retain open branches and scroll position for the browser tab. Active ancestors remain open; manually changing branches is still available. Disabled smooth scrolling only for the left menu
- Verification: real Cypress/Chrome navigation check now keeps scrollTop at 377 and the clicked row at y=580.39 on both pages. Strict HTML build and local reference/image checks pass; evidence recorded in maintenance/menu-navigation-check.json
- No new dependency, application changes, release promotion or push. Reload an already-open page once to load the new menu behavior

## Support/report-issue and provider documentation finished — 1 November 2026

- Added Getting Started → Get Help and Report an Issue: actual profile-menu contact flow, website/email behavior, useful report details and help when sign-in is unavailable. Linked from Profile and Troubleshooting; one toctree parent
- Finished administrator Support configuration: exact fields, defaults, icon, save/check procedure and organization/workspace permissions/overrides
- Expanded OpenID: Microsoft/Custom fields, ORCID and callback-first client registration, ID-token profile fields, scope/registration behavior, distinct redirect/logout labels, test and troubleshooting procedures, linked-account flow and update guidance
- Expanded SAML: single-provider and discovery modes, metadata/entity IDs, discovery placeholders/return parameter, allowed-provider behavior, SP metadata/ACS/logout registration, attribute coordination, test/troubleshooting and upgrade coordination
- Evidence is recorded in maintenance/support-provider-evidence.json against pinned 5.0 FE/BE revisions and the original guide. No external portal-screen instructions invented. Actual provider/federation sign-in validation remains environment acceptance, not unfinished documentation
- Verification: strict HTML build passes; 28,036 generated local references checked without missing target/anchor/image-alt errors (existing redirect exclusions, 404 RTD prefix normalized); 135 source pages, no unintended orphan, duplicate parent, missing toctree target or cycle. Rendered user support page reviewed
- No customer messages, credential entry, provider/settings mutation, new screenshot capture, Notion edit, push or release-channel promotion. Add a Report issue dialog capture in the dedicated screenshot batch

## Downloadable PDF rendered and inspected — 1 November 2026

- Built the real Sphinx/LaTeX guide with Tectonic 0.17.0 (XeLaTeX-compatible), not browser printing. Installed the local compiler and required ICU library; hosted Read the Docs build/publication remains untested and unchanged
- Set an explicit Unicode engine, A4 one-sided layout, Nunito headings with bundled licensed static fonts, FreeSans body and FreeMono code. The first local render used pdfTeX-oriented sources with a XeTeX compiler; missing punctuation in that render was an engine mismatch, not evidence that the published PDF was broken
- Corrected the Contents label/page-number width, excluded web-only home cards and illustration from print, retained a short print preface and the screenshot warning. Simplified chapter styling, replaced the Search emoji with its control label and shortened/wrapped an overflowing font-loading HTML example
- Inspected all 192 final pages as contact sheets and selected contents, sharing, roles and code pages at higher resolution. Final audit finds no off-page/near-edge text or images, empty pages, replacement glyphs, missing glyph warnings, overfull boxes or undefined references; 817 named destinations. Some image-only pages and short continuation pages retain ordinary pagination whitespace
- Strict HTML rebuild passed; 28,040 local references passed with the existing agreed redirect exclusions/404 prefix normalization. Navigation: 135 source pages, no unintended orphan, duplicate parent, missing target or cycle
- Evidence: maintenance/pdf-review.json. Generated PDF remains outside Git at Downloads/fw-guide-update/output/pdf/fair-wizard-guide-5.0.pdf. README documents local reproduction; no new Python runtime dependency
- Known limitations: temporary QA and individually marked 4.x screenshots remain until dedicated-environment capture. Decorative FontAwesome ToUnicode warnings remain; the PDF is untagged and PDF/UA conformance was not tested. No push, release promotion, hosted setting change or Notion edit

## Menu flicker follow-up — 2 November 2026

- User still observed flicker. The earlier regression compared only settled positions and missed transient paint changes
- Reproduced the defect in Chrome by forcing an uncached sidebar script response with a 700ms delay and sampling the menu on animation frames: scroll varied by 377px before restoration
- Moved the existing restoration code from docs/_static/js/sidebar-position.js to docs/_templates/sidebar/position.js and included it inline immediately after the tree in sidebar/navigation.html. One implementation, no additional request/dependency, visibility trick or navigation interception
- Strict HTML build passed. Both Chrome/Cypress checks pass: the cold-load rendering regression and the existing final-position regression. Across 63 recorded post-fix frames, scrollTop stayed 377 and the clicked row stayed at y=580.390625. Evidence: maintenance/menu-navigation-check.json
- Preview updated at http://127.0.0.1:8769/index.html. Reload an already-open page once. No commit, push, deployment, application change or Notion edit

## Search-box layout shift — 2 November 2026

- User clarified the remaining flicker is in the guide at port 8769, specifically Search moving up/down. Prior tests measured menu scroll/rows, not the logo/search block
- Reproduced a separate layout shift with an uncached SVG response delayed 900ms: logo container height changed 0 → 34.34375px, moving Search top from 40 → 74.34375px
- Added intrinsic width/height attributes from the existing 1000×159 logo viewBoxes in sidebar/brand.html and responsive width:100%, height:auto in style.css. No new JavaScript, hiding, delay, dependency or navigation interception
- Strict HTML build passes. All four Chrome/Cypress regressions pass: delayed-logo Search checks in light/dark mode, prior transient-menu test and final menu-position test. Search top remains exactly 74.34375px over 119 light and 67 dark sampled frames; logo height remains 34.34375px throughout. Evidence updated in maintenance/menu-navigation-check.json
- Local preview rebuilt at http://127.0.0.1:8769/index.html; no commit, push, release, app settings or screenshot-data changes

## Targeted screenshot layout review — 2 November 2026

- Reviewed all 143 current light screenshots via five contact sheets and selected full-size images. Fixed oversized blank bottoms in project creation and nine create/import forms with content-bounded captures; collapsed global navigation in selected questionnaire/project-detail views while retaining it on lists
- Changed only selected assets: 17 successful mediakit scenes (5 project + 12 guide), 16 differing PNG hashes, 127 unchanged light PNGs. Capture recipes updated in fw-screenshots; no save/import/invite requests submitted
- Value Question now has one screenshot; validation example moved under Warnings. Project Settings images increased from 350px to 600px. Import/create images use 500–520px and user-import review 720px. KM/DT import images now sit with their matching sections
- Updated screenshot inventory and maintenance/screenshot-layout-review.json. Eight omitted typed-value images remain stored for possible reuse; 139 placements use 135 unique light images
- Strict HTML build passed; 27,998 local references checked without errors under the existing redirect exclusions. Navigation: no unexpected orphan, duplicate parent, missing target or cycle. Fourteen offline screenshot-scaffold tests and changed-JavaScript syntax checks pass; git diff --check clean
- Visually reviewed rendered project creation, settings and user import. Recorded further candidates without recapturing: Comments/Version History panel whitespace, some KM/DT editor navigation, AI consent surrounding space. No full regeneration, dark-mode, Analytics or Enterprise batch; no PDF rebuild, commit, push or deployment

## Compact navigation labels — 3 November 2026

- Restored context-specific toctree titles: List, Editors, Create, Detail, Compare, Import, Preview, Migration, Templates and Settings; applied across Knowledge Models, Document Templates, Projects and related feature menus
- Kept descriptive article titles, URLs, anchors and the actual Knowledge Model editor-tab name unchanged. Native toctree labels only; no new CSS or JavaScript
- Both guide previews retained on separate ports: FW 8769, DSW 8772. Strict HTML builds and rendered navigation-label checks run before delivery

## Full nested TOC verification — 3 November 2026

- Reproduced stale long labels on the generated FW Compare page despite correct source aliases. Earlier incremental builds did not rewrite every dependent sidebar
- Completed the nested Publish alias and rebuilt with native Sphinx -E -a, refreshing every HTML page. Documented this rebuild in README; no extra runtime mechanism
- Compared all explicit toctree aliases on every rendered sidebar, including 404 prefixes: 137 pages and 4795 labels pass. No missing targets, unexpected orphans, duplicate parents or cycles; standalone 404 is intentional
- Evidence: maintenance/toc-render-check.json. Article titles/URLs retained. Both preview servers continue running; no push or publication

## Settings navigation and legacy integration page removal — 3 November 2026

- Grouped Settings into Users & Access, Projects, Appearance, Features & Integrations, Translations, and Plan & Usage, matching the 5.0 app menu. Used native Sphinx group pages because nested toctree captions do not appear in Furo's sidebar; existing article URLs retained
- Removed the Legacy API Integration migration page and its toctree entry; removed stale generated HTML/source/doctree from the preview output. Project and knowledge-model migration pages retained
- Placed the existing Roles article under Settings → Users & Access, retaining its URL. Analytics belongs to Features & Integrations; Plans follows Usage, verified in origin/feature/fw Settings extensions
- Verification: full strict HTML rebuild, every rendered sidebar alias, internal links and toctree topology pass; both groups visually inspected. Evidence in maintenance/toc-render-check.json. No outstanding issue for this request; previews remain on DSW 8772 and FW 8769

## Restore original OpenID setup instructions — 3 November 2026

- Restored the original numbered Microsoft Azure (34 steps), ORCID (18 steps) and Custom provider (12 steps) instructions and advanced scope explanations from the pre-5.0 guide, following the user's wording and sequence
- Limited 5.0 edits to the current Settings navigation, root callback URL, Client Secret Value and Advanced configuration labels, and Create versus Save. Retained current FW captures / DSW screenshot TODOs; restored the existing FW automation section with its current internal guide link
- Strict HTML and LaTeX-source builds pass in both guides. Provider instructions were restored from the original guide, not independently revalidated against live provider portals. No identity-provider or application configuration changed

## Full content-retention audit — 3 November 2026

- Compared all 156 original pages against mapped 5.0 pages; restored/corrected 40 pages. Retained useful reference detail, examples, warnings and metamodel history rather than replacing them with short summaries or external links
- Re-read restored pages and compared against the pre-audit 5.0 text to retain newer migration/security/source/workspace cautions too
- Corrected outdated examples and publishing metadata against current code. Kept exact OpenID steps, current navigation, supported 5.0 flows and authorized legacy migration-page removal
- Detailed decisions, evidence, limitations and verification: maintenance/content-retention-audit.md, content-retention-audit.json and content-retention-validation.json
- No screenshot capture/regeneration, application-data change, deployment, Notion edit, commit or push in this audit

Final verification: strict HTML and LaTeX-source builds passed; 30440 local references checked; no link/image errors, missing toctree targets, or rendered alias errors. All 21 earlier template-metamodel entries and 62 schema-history rows retained. OpenID pages match the preceding fix exactly. `git diff --check` passed. Browser review covered restored technical-reference layout. The existing previews were rebuilt.

## Finalize FW using the completed DSW checks — 3 November 2026

- Scope: FW content, structure, factual/source checks and Professional single-workspace screenshots. Enterprise-only captures remain deferred by explicit confirmation
- Ported current shared Document Context 19.0, TDK and template-development references and diagrams from the combined DSW PR. Kept FW-only pages and workspace distinctions
- Added the five shared user FAQ answers while retaining FW troubleshooting. Aligned sidebar section closing with DSW; existing FW branding and screenshot theme mechanism retained
- Next: enrich uniquely named example projects and real Analytics data, finish Professional captures, review image framing, then run strict builds, links, app-help and navigation checks

### Dedicated instance and Analytics verification

- User approved enriching three existing projects and creating five named examples. All were populated with synthetic answers, datasets, tags and phases; 13 project names are unique. Existing empty, migration and validation examples retained
- Requested a real Analytics synchronization. Reports now return the populated projects and both KM versions; all 17 Analytics capture scenes pass, including an opened question and its answer distribution
- Added a reproducible compact Projects overview saved view. No chart data or report responses were mocked
- Reproduced the existing URL-domain validation bug on mediakit: a valid https://zenodo.org/ URL is rejected by the zenodo.org domain rule. Omitted this answer from demo data; no backend change. Evidence in fw-screenshots/ISSUES.md VAL-01
- Refreshed 134 guide scenes successfully after adapting current tree selectors and increasing one form's viewport. Four automation scenes have no controlled examples in the mediakit fixture; their existing images are retained pending a suitable configuration/log example
- Strict HTML and LaTeX-source builds pass after shared content updates. Initial local link/topology check only identified the intentional standalone 404; validator adjusted to exempt it

### Final review and remaining work

- Integrated 157 mediakit scenes in both themes (314 PNGs): 135 guide scenes and 22 project scenes. Reviewed contact sheets and selected full-size captures. Populated Analytics detail views use relevant projects, templates, collaborators and groups
- Project HTML preview and template-editor preview now work in both themes. Stored HTML and PDF downloads still return HTTP 500 on GET /documents/{uuid}/download; documented as DOC-02. Preview success was not used to claim download success
- Submission is disabled here, explaining the missing Submit action and personal submission settings. Translation Registry remains Not Allowed; no questionnaire Warnings control appears for this example. Automation examples/logs and current approved News content still need suitable fixture content. Existing applicable images remain; Enterprise captures deferred
- Fixed the local preview server's stale output directory: port 8769 now serves the freshly rebuilt current-html output. Old generated pages were excluded with a fresh build
- Final strict HTML and LaTeX-source builds pass. Checked 31,538 local references, 140 source pages (139 navigable plus intentional 404), no unintended orphans/cycles/duplicate parents, and 5,538 rendered menu aliases. All images have alt text. Current frontend help page destinations exist locally; normal release URL updates remain outside this guide-only task
- Rendered the updated 232-page PDF with Tectonic. Reviewed all pages as contact sheets plus selected tables and Analytics pages at higher resolution. No off-page/near-edge content, empty pages, replacement glyphs, final-pass undefined references or missing glyphs. Small table-box warnings remain within page margins; ordinary image/continuation-page whitespace remains
- Evidence: maintenance/finalization-summary.json, finalization-validation.json, finalization-toc.json, finalization-app-help.json, finalization-pdf.json and mediakit-finalization-screenshots.json. No commit, push, hosted release promotion or Notion modification

## Remaining OS fix parity — 3 November 2026

- Compared the DSW source-review corrections and screenshot fixes with FW rather than relying on the earlier shared-reference port
- Fixed seven FW pages: owner-only history actions and permission matrix; retained named versions during KM migration; explicit irreversible revert effects on later events/versions/files; project-template creation permissions; read-only published-model preview, questionUuid links and copied preview values; current file-editor controls/unsaved indicators; integration links and custom replies
- Preserved FW workspace rules, existing screenshots and original OpenID provider steps. Shared backend owner/revert checks and current frontend controls support the corrections
- Verified sidebar scripts differ only in the product-specific storage key. Chrome window sizing, measured crops and saved-image dimension safeguards are already present in FW
- These are documentation and capture-tool fixes. No application bug was fixed in the OS guide work; the URL-domain validator, stored-download HTTP 500, report-template label and legacy gateway issues remain separately tracked and are not claimed resolved
- Strict HTML build and current guide validation pass; final printable output is refreshed with the same corrected text. No screenshot regeneration, instance mutation, commit or push

## Deferred screenshot notes — 4 November 2026

- User no longer requires submission, automation-log, questionnaire-warning and remaining translation captures for this pass; Enterprise stays deferred
- Added 9 `.. TODO::` directives across 8 relevant source pages, explicitly hidden with todo_include_todos=False
- Replaced the empty submission-service dialog, two fallback automation-log figures, old questionnaire Warnings figure and old Registry translation-import illustration with source-only follow-up notes. Screenshot files and useful text/current images retained
- Clarified the unintegrated asset count: 28 refreshed views × 2 themes = 56 files; four new views produce 6 files because the two newest closed-filter question-column views have light captures only
- Reconciled fw-screenshots/TODO.md. No screenshot regeneration or integration performed in this step
- Strict HTML build passed; confirmed “Screenshot pending:” appears in no rendered HTML page. Final visual/PDF review is left to the user as requested

## Current screenshot integration — 4 November 2026

- Copied the 56 refreshed and 6 new image files from the current mediakit Cypress output; checked each copied file against its source
- Added a broad Projects overview, retained the item-actions example beside the actions instructions, and added Analytics question values, sensitive-data Yes/No answers and the opened answer filter
- Existing theme pairing handles light/dark files. The two newest closed-filter views retain the normal light fallback in dark mode because their dark variants have not been captured
- Full fresh strict HTML build passed; preview at http://127.0.0.1:8769/ responds. Verified all four new views appear in their rendered pages and hidden TODO text stays absent
- Integration inventory: maintenance/current-screenshot-integration.json. No new captures, final visual/PDF audit, commit, push or release promotion; user will review the rendered guide

## 4 November 2026 — Review corrections and populated examples

- Removed merger-related Getting started wording and the former Integration Hub placement from operational instructions. Removed the obsolete component-overview diagram; retained historical upgrade material
- Corrected the KM migration diagram's false outdated-screenshot label. Moved that diagram and the conceptual KM schema under diagrams; these are not interface captures
- Four old UI visuals remain to recreate: Registry catalogue, News modal, unsupported-format download preview, and API integration's old screenshot-based illustration. The latter was previously unmarked and is now labelled honestly
- Populated FW integration-secret list with two clearly fake example values; values are not returned by the API or displayed in the screenshot
- Added screenshot-only Czech UI/mail translations from the DSW examples, rebased against the installed FW POT files so product/version metadata is accurate. English remains default
- Created short-lived demo API keys in the two screenshot environments only for capture, then revoked both. Expired-only keys were hidden by the UI. No generated token value was stored or shown
- Applied the author's fixed Questionnaire Report files to existing FW/DSW preview drafts with private backups. The FW preview capture now waits for the iframe resource to finish loading in the browser; an HTTP 200 check alone had accepted the blank frame
- Refreshed six FW views in both themes (12 images), including secrets, API-key list, language choice, UI/mail translation lists and populated template-editor preview; synced them to the guide and Downloads screenshot folder
- Final focused Cypress runs passed; changed screenshots inspected. DSW-only matching fixes are in open PR #291 to main and #292 to develop from the same hotfix branch. No DSW merger wording or actual legacy-UI images found
- HTML rebuild and diff whitespace checks pass. Remaining old captures were not regenerated. No FW commit/push or release promotion; DSW PRs remain unmerged

## 4 November 2026 — Populated assigned comments

Added three synthetic comments across Coastal Biodiversity Survey, Coastal Habitat Mapping and Coastal Water Quality Monitoring, assigned to the screenshot administrator. Saved reusable example records in fw-screenshots/fixtures/guide/assigned-comments.json. Captured both themes with the sidebar collapsed and the unused space below the list excluded; integrated both images into the FW guide and current screenshot collection. Cypress checks passed for both themes.

## 4 November 2026 — Remove News screenshot

Removed the outdated News modal figure from the What's New page at the user's request. Kept the feature description.

## 4 November 2026 — Remove administrator password screenshot

Removed the Administrator password setting figure from Edit a user at the user's request. Kept the password-setting description and user profile screenshot.

## 4 November 2026 — Remove SAML providers screenshot

Removed the SAML providers list figure at the user's request. Kept the configuration form screenshot and all setup instructions.

## 4 November 2026 — Populate settings screenshots

Filled Dashboard & Menu and Login Screen forms with synthetic research-support announcements, a menu link and sign-in guidance for screenshot capture only; no configuration was saved. Refreshed those two settings views in both themes and integrated them into the guide and current screenshot collection. No dashboard announcement screenshot was created. Cypress checks passed for both themes.

## 4 November 2026 — Remove Installed plugins screenshot

Removed the Installed plugins figure at the user's request. Kept all plugin guidance.

## 4 November 2026 — Remove Official translations page

Removed the Official translations page, its TOC entry and the link from the translations overview. Updated the maintained application help-link mapping to the translations overview. Retained the overview's guidance on official/custom translation updates. Removed stale rendered page files before rebuilding.

## 4 November 2026 — Remove translation upload screenshots

Removed the Upload email translation and Upload interface translation figures at the user's request. Kept the upload instructions.

## 4 November 2026 — Guide spacing review

Source scan found 159 figures on 90 pages, with consecutive figures on 14 pages. Browser inspection confirmed figures had zero outer margin. Added shared 24px spacing before figures, 32px after, 12px before captions and 24px around callouts in docs/_static/style.css. Kept existing screenshot sizes, prose and heading/list styles. Strict full HTML build passed. Visually checked translations, project settings and sharing; checked computed gaps in dark mode and light-mode rendering at 1280px and 480px without horizontal overflow on the inspected pages. Saved a review image to Downloads/fw-guide-update/spacing-review.png. Refreshed generated image timestamps to avoid stale local-preview copies. PDF was not rebuilt for this CSS-only change.

## 4 November 2026 — Complete Analytics Projects dark images

The question-answer and sensitive-data views lacked dark counterparts and therefore fell back to light images. Captured both missing dark views with Cypress (2/2 passed), inspected their contents, and copied them into the guide and current screenshot collection. Retained the existing single automatic light/dark pairing mechanism.

Verification: strict full HTML build passed; all six Analytics Projects figures have dark image nodes linked to the correct source bytes. Visually inspected both new captures and the existing overview.

## 4 November 2026 — Marek reference parity and schema links

Compared Marek Suchánek's DSW Document Context 19.0 and TDK updates (1b2aa0c, 2c209b5) with the FW reference pages. The substantive context, Jinja, Excel/Pandoc, specification, worker plugin and TDK material was already present; retained FW workspace additions and adapted links. Applied the remaining editor-settings link correction in FW. Checked dsw-schemas master through GitHub: the newer context/template schema files remain absent. Restored JSON Schema links for versions 18.1, 18.2, 18.3 and 19.0 in both schema tables as explicitly requested, despite expected 404 responses.

Verification: strict HTML and LaTeX-source builds passed for both guides. The schema 19.0 absence was confirmed by GitHub API HTTP 404; the repository tree lists no context/template schemas for 18.1–18.3 or 19.0. No full PDF render or external linkcheck was run; these missing links are intentional per request.

## Final guide review — 2026-11-04

- Read through shared and product-specific prose, preserving technical reference material, historical upgrade notes and the original OpenID procedure
- Corrected wording, cross-reference markup, screenshot captions and small factual inconsistencies; changes are limited to documentation and screenshot presentation
- Verified strict HTML and LaTeX-source builds with warnings treated as errors; checked local links, anchors, image mappings and TOC reachability
- Visually reviewed all raster-image contact sheets and selected full-size images; inspected representative rendered pages. This review did not rerun every application flow, render a fresh PDF or recrawl all external URLs
- Intentionally retained links to not-yet-published metamodel schemas as requested
- FW: 139 source pages, 31,174 local references and 313 HTML image mappings pass; 152 dark screenshot nodes checked. All six Analytics Projects dark counterparts load correctly
- Refreshed current-plan screenshots in both themes, removed old plan-history clutter, aligned shared wording with DSW and corrected the Document Context files reference
- Five older visuals remain explicitly labelled: Registry catalogue, unsupported-format preview, API integration illustration, OpenID automation and SAML automation. Enterprise-only captures and previously deferred hidden screenshot TODOs remain out of scope
- FW changes remain local on the existing guide branch; no merge or deployment performed

## Develop merge preparation — 2026-11-05

- Include the reviewed 5.0 guide content, screenshot themes and final proofreading fixes in PR #317 before merging to develop
- Check open dependency updates separately; preserve the preview and production branches
- Dependency blockers found in CI: substitution extension requires beartype >=0.23.0rc2; docutils 0.23 conflicts with pinned Sphinx 9.1.0 (<0.23)

## Dependency compatibility — 2026-11-05

- Guide PR #317 and dependency PRs #316, #314 and #313 merged into develop after passing CI
- Update beartype to 0.23.1, satisfying sphinx-substitution-extensions 2026.10.9; the combined dependency set passes strict local HTML and LaTeX-source builds
- Update certifi to the first patched version 2026.10.18 for the reported bundled-root certificate alert
- Keep docutils 0.22.4: Sphinx 9.1.0 requires docutils <0.23, so PR #273 remains incompatible; no unrelated Sphinx upgrade attempted
- Preview and production branches remain unchanged


## 2026-11-11 — Guide proofreading

- Base: `origin/preview` at `f2767595ee64fcd6fa7d86eb80b573d4eb6c8d39`; isolated branch `codex/guide-proofread`.
- Reviewed guide prose for grammar, unclear instructions, internal contradictions and repetitive AI-style wording. Shared prose was checked across DSW and FAIR Wizard while retaining product-specific scope and features.
- Edited 53 RST source files. Corrected import guidance, ORCID save instructions, rendering-reference wording, and language in knowledge-model and project workflows. Corrected the private-project icon description, shortened MCP examples and AI Prefill instructions, and clarified Analytics prose.
- Checked OpenID editing and user-group save behavior against the local shared frontend source at `4a4c858c`; rendering options and worker configuration against engine-tools `origin/main` at `bea50b8`.
- Verification: strict Sphinx HTML and LaTeX source builds passed with warnings treated as errors; `git diff --check` passed. All 43 code blocks in the edited RST files are unchanged.
- Limits: no live application or third-party sign-in test, external link audit, full implementation audit, or rendered PDF check. Release dates, the Analytics Insights count wording and Word image-compression advice still need confirmation. Third-party AI-client screens were preserved and were not tested live.
- Original working copies and existing unfinished edits were left intact.


### Information-preservation recheck

- Rechecked the proofreading diff against its original base after the user asked about factual changes and accidental loss.
- The first pass did include intentional factual corrections and abridgement, rather than language-only edits. Restored the empty-secret distinction, preview/project workflow tip and first-tab detail. Corrected a sentence introduced in the metamodel overview.
- Restored the MCP prompt examples and associated guidance that had been removed. Restored the clear, well-structured source-document advice in AI Prefill and clarified the retained custom-reply workflow.
- Retained explicit, documented factual corrections to contradictory instructions. Code examples and screenshots remain unchanged against the original base.
- Recheck verification: strict HTML and LaTeX source builds and diff whitespace checks passed. 43 code blocks and 94 image references, plus all 24 original MCP example requests were compared with the original base and retained. This does not establish the truth of every factual statement in the guide.


### Pandoc image-compression experiment

- Tested locally with Pandoc 3.9.0.2 using 1800×1200 PNG and JPEG images displayed at three inches. Used a default reference plus references with 72-DPI, 150-DPI and disabled-compression settings. Repeated the low-DPI case with Markdown input. A font-size change confirmed each custom reference was used.
- In all five original-image output cases, embedded PNG/JPEG bytes, SHA-256 hashes and dimensions matched the source files. The doNotAutoCompressPictures flag was copied; defaultImageDpi and discardImageEditingData were not. Independently resizing the two source images before generation reduced the embedded media and output size.
- Checked the result against Pandoc's 3.9.0.2 DOCX writer and Microsoft's OOXML/image-compression documentation. The guide now recommends optimizing source images or using Word's compression on the generated document, instead of promising compression through reference.docx.
- Scope: local Pandoc generation, not the deployed worker binary or a Microsoft Word open/save test. The shared worker source delegates conversion to Pandoc. The low-DPI output was rendered with bundled LibreOffice and its single page inspected.
