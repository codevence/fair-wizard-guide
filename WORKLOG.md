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
- The frontend exposes Manage Library/Manage Workspaces role controls and an Audit Log implication, while backend `assignableRolePermissions` excludes those first two permissions. Confirm intended assignment behavior before publishing custom-role instructions around those controls. The guide does not promise every control can be assigned to an arbitrary custom role.
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
