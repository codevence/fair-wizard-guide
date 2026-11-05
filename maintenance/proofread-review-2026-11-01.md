# Guide review — 1 November 2026

Scope: wording and presentation review, all 134 source pages checked structurally, and targeted factual checks against local 5.0 source branches. This is not a live test of every documented operation. No Notion or release-channel changes.

Evidence: frontend `origin/feature/fw` at `8b6d4f125b449662ad8cf5ccbd2985103f5c58b7`; backend `origin/main` at `303ffd8222930608fa7519d7ca5467413f832854`; engine-tools reference `6c159fa862b381890c6a1464be846df4f57fd387`. AI Prefill's request-only availability, Claude use and completion email were confirmed by the user in this review.

## Reconciliation of the previous audit

| Previous finding | Current disposition |
| --- | --- |
| Data Source creation asks for a nonexistent identifier; Search Fields omitted | Fixed: create by name; values → templates → Search Fields → integration/question → preview/publish procedure. Both display templates distinguished |
| Default role on wrong settings page | Fixed: Roles → Set as default; User Settings describes affiliations and links to Roles |
| KM publishing described as read-only | Fixed: version, description and README editable; other changes directed to Settings. License-on-publish discrepancy remains a product question |
| First Analytics view cannot be created through documented menu item | Fixed across all five collection pages: View settings first; Create new view when viewing a saved view. Live Analytics remains deferred |
| Clone/template described as exact copies | Fixed: copied content distinguished from sharing/ownership and generated outputs. Backend ProjectService checks establish the distinction |
| Individual users described as the only possible project owners | Fixed: user-group Owner access explained. Removed unconditional last-owner guarantee; keep an owner as an explicit instruction |
| Signed-in visibility audience inconsistent | Fixed beside the toggle: single-workspace audience versus workspace reachability |
| Translation upload always requires confirmation | Fixed: warnings require review; warning-free uploads finish automatically; uploaded language needs enabling |
| OpenID setup missing FW-side fields | Restored Microsoft/Custom fields, registration/scopes, callback sequencing and automation link. Completed FW-side Microsoft, Custom and ORCID procedures, callback-first registration sequence, sign-in tests and troubleshooting; live provider/federation acceptance remains environment work |
| Automation setup and SDK link absent | Added provider-linked creation/configuration/log procedure and existing Integration SDK URL from frontend GuideLinks |
| POT → PO procedure missing | Added language/header, encoding, placeholder/plural, upload/enable guidance and shared email-message caution |
| Shared-library publishing/use flow disconnected | Added released export → organization import → other-workspace use, Manage Library and local precedence |
| Developer template example/install path incomplete | Python requirement clarified from package metadata. A verified minimal context-19 template example and exact released 5.0-compatible tool installation/container version remain follow-up work |
| Dashboard/menu and login fields too vague | Added actual announcement/link/order/new-window and Login Info/Sidebar Login Info controls |
| New user details and support flow missing | Added timestamps, consent, connected identity information and Admin password-reset requirement. Completed user-facing Report issue/contact procedure and administrator contact configuration in the support/provider follow-up |

Moved API-key migration history to Upgrade, replaced hosted deployment-worker debugging advice with administrator/support escalation, shortened repeated AI Prefill instructions, split long paragraphs, corrected typos, and removed an unfinished image-compression section containing an issue but no answer. Existing captions were updated during screenshot integration. Daily workspace instructions now link to the migration plan instead of mixing it into the procedure.

The old concern that Manage Library / Manage Workspaces cannot be assigned was withdrawn: it inspected the Shared definition without the FAIR Wizard override. It is not an outstanding confirmed product bug.

## Navigation and page coverage

134 source pages: 133 reachable from the root toctree; the 404 page is intentionally orphaned. No unintended orphan, missing toctree target, duplicate parent or cycle. Hidden root toctrees retain sidebar navigation while avoiding duplicate link lists on the home page. Frontend guide-help mappings remain part of the existing versioned guide-links work.

No missing source page was found. That does not establish complete feature coverage: template authoring examples, live provider acceptance and the cases below remain explicit follow-ups. Developer/reference pages do not need screenshots simply because they lack an image.

## Additional or improved screenshots

| Priority | Page / flow | What is needed |
| --- | --- | --- |
| High | Project preview and template-editor preview | Successful rendered output after the documented QA document-serving failures are resolved |
| High | Document submission / personal submission settings | Accessible required-property form and compatible-service selection; current screenshot shows the real no-compatible-service state |
| High | Application/email translations | Installed PO language with enable/default controls; official Registry installation when configuration permits |
| High | KM and document-template Locales | Populated locale list and import dialog; these procedures currently lack specific examples |
| Medium | AI Prefill | Upload, processing/completion and resulting answers on an enabled instance, using synthetic documents |
| Removed | Project migration conflicts | Incorrect proposed task withdrawn: current project migration directly applies model/version/tag selection. Knowledge model editor migration is a separate flow |
| Medium | Assigned comments and connected accounts | Populated assignment and controlled SSO-identity examples, including administrator inspection |
| Medium | Login automation logs | Successful and failed invocation details; current examples have no logs |
| Medium | Questionnaire warnings | A verified state producing the conditional Warnings control; validation-error capture is already present |
| Deferred | Analytics reporting | Populated lists/details/insights, once the user reopens this work |
| Deferred | Enterprise differences | Workspace switcher, membership/roles, shared/local libraries, overrides and workspace-specific sharing; use existing multi-workspace-missing inventory |

Keep the 26 marked legacy placements until their replacements or conceptual-graphic revisions are ready. Rerun temporary QA examples in the dedicated environment before final publication.

## Presentation and dark-image pilot

Home page simplified to a short introduction, compact topic links, account/upgrade/troubleshooting links, website backlink and **DSW community on Discord**. Discord invitation copied from local `dsw-web/src/pug/links.js`.

Application screenshots have a subtle border/shadow. Three actual dark captures added: Support settings, KM list with item menu and Share modal. One shared Sphinx hook discovers matching files under `_static/screenshots/5.0/dark/`; normal RST figures remain unchanged. Shared CSS follows Furo's manual light/dark and system mode. Without a dark counterpart, the original image remains. HTML shares one caption; non-HTML output keeps the light image.

Verification: strict HTML and LaTeX-source builds passed; dark variants are absent from the generated LaTeX source; generated link/image/alt checks passed; browser checks confirmed system-dark, explicit-light and explicit-dark selection on Support, plus the light screenshot frame and revised index. All three raw dark PNGs inspected. Cypress: two guide captures and one Projects capture passed; 13 offline checks passed. Full dark set not requested or generated.
