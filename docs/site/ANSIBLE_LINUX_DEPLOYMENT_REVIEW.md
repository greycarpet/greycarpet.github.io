# Ansible Linux Deployment — Case Study Review

**Branch:** `feature/ansible-linux-deployment-case-study`  
**Owner:** Josh Escobar  
**Prepared:** October 13, 2026  
**Status:** Draft publication candidate. Do not merge without owner approval.  
**Page:** `projects/ansible-linux-deployment/index.html`  
**Brand reference:** [STYLE_GUIDE.md](../brand/STYLE_GUIDE.md)

## Narrative

**Title:** Standardizing 50 Linux Workstations with Ansible  
**Display headline:** 50 workstations. One defined baseline.

The first-person article follows the completed endpoint project from aging Windows hardware through Lubuntu selection, baseline definition, Ansible configuration, identity/access testing, clean-install validation, targeted domain-join recovery, and production rollout. It positions the work as Linux infrastructure and automation engineering.

## Change scope

1. Add the complete article at `/projects/ansible-linux-deployment/` with seven narrative sections and inline source notes.
2. Add isolated `case-study.css` using the existing Nocturnal Lab palette and type families. Shared `styles.css` is unchanged.
3. Update only the existing Ansible homepage card's title, summary and destination link.
4. Add this review record. The existing resume, Twilio case study, and shared navigation script are unchanged.

The repository is public: a feature branch and draft PR are review controls, **not privacy controls**. Only public-safe narrative and illustrative content are committed. No production playbooks are executed or infrastructure settings changed by this work.

## Source handling

| Source | Evidence classification | Supported use |
|---|---|---|
| S1: October 8 operator account retained in the professional-experience reference, E02 | Retrospective firsthand account, supported by career materials | 50 fresh Lubuntu installations; documented reference configuration; Ansible APT/package/setup work; clean-install validation; fleet application; hardware reuse |
| S2: Same reference, E03 | Retrospective firsthand account | Domain components, short-name login, selected domain/local account tests, rejected root-login test, successful per-host domain-join retries |
| S3: September infrastructure handover, section 4.3 | Later documented controller context | Windows/WSL administration, SSH and inventory arrangement; not the original fleet-wide execution transcript |
| R1/R2: Official Ansible playbook and apt-module documentation | Platform behavior, checked October 13, 2026 | Explains ordered tasks, desired package state and idempotence boundaries; not evidence that historical code ran |

The article contains no original fleet-wide recap or production playbook snapshot. Workflow panels and comparison tables are editorial summaries. The four-line YAML task is explicitly illustrative and has an undefined package variable; it is not a deployable recipe or claimed original source code. No successful Ansible terminal output or desktop screenshot has been fabricated.

## Accuracy boundaries retained

- Fresh OS installation happened before Ansible configuration; do not recast this as PXE, zero-touch imaging, or automated bare-metal OS installation.
- Clean-install testing supports rebuild repeatability. A complete second pass on an already-configured machine was not established; do not call every playbook proven idempotent.
- Package/component checks are separate from successful login or application tests. Do not equate Zoiper installation with a verified end-to-end call on every endpoint.
- realmd, SSSD and Winbind are recorded installed components, not a claim that all three were the active authentication provider or universally required.
- A rejected root-login attempt is scoped to the tested login path. Do not invent an exact SSH, PAM or password-lock mechanism.
- Individual domain-join retries succeeded. Directory congestion remains a hypothesis; no invented error, packet capture or simultaneous 50-host test is included.
- No exact original deployment date, first-rollout distribution release, financial saving, setup-time reduction, zero-downtime claim, or fleet-wide compliance certification is introduced.
- Later VPN/RustDesk extensions and a separate 15-host rollout are not merged into the original 50-workstation story.

## Completed QA

The exact new article and stylesheet were rendered offline in Chromium 144.0.7559.96. Their Git blob hashes matched the committed files. The existing `script.js` used for the test also matched the repository blob `1f9974f25f2351fc41de1377dc44901a2a51f798`.

| Check | Result |
|---|---|
| 1440 x 1000 desktop viewport | No page-level horizontal overflow |
| 1024 x 900 viewport | No page-level horizontal overflow |
| 390 x 844 mobile viewport | No page-level horizontal overflow |
| 320 x 800 mobile viewport | No page-level horizontal overflow |
| Heading and anchor structure | One H1, no duplicate IDs, no missing same-page anchors |
| Keyboard entry | Skip link receives first Tab focus |
| Mobile menu | Opens; Escape closes it and restores focus to menu button |
| References inside collapsed details | Native fragment navigation reveals the target |
| JavaScript-disabled mobile layout | Navigation remains visible; no horizontal overflow |
| Runtime script errors | None in the offline test |
| Existing homepage | Commit diff reviewed: only the three Ansible card lines changed |

**QA limits:** Network access was unavailable in the rendering environment. Tests used the declared local font fallbacks, not downloaded Google Fonts, and rendered in-memory HTML/CSS rather than fetching a deployed site. These results do not constitute live HTTP/link verification, full-site regression coverage, screen-reader certification, exhaustive contrast/zoom testing, or testing in every browser. Review the installed-font presentation locally before merge.

## Owner review

- [ ] Narrative accurately represents the completed project and personal ownership.
- [ ] Scope of the 50-workstation result and the hardware-reuse outcome is approved.
- [ ] Baseline, identity, clean-install and troubleshooting descriptions are accurate.
- [ ] Source notes and explicit limits are suitable for a public portfolio.
- [ ] Visual layout reviewed with Google Fonts available, on desktop and mobile.
- [ ] Homepage card and routes to the article, resume and Twilio project work in the local site.
- [ ] Employer/client disclosure requirements satisfied where applicable.
- [ ] Explicit approval before merging this PR into `main`.

## Local preview

From a clean working tree in PowerShell:

```powershell
cd C:\Users\ecadirect\Documents\GitHub\greycarpet.github.io
git status
git fetch origin
git switch --track origin/feature/ansible-linux-deployment-case-study
python -m http.server 8000 --bind 127.0.0.1
```

Open `http://localhost:8000/projects/ansible-linux-deployment/` and the homepage card. Stop an existing local server using that port before starting a second one. Do not discard uncommitted work to switch branches.

For an existing local branch, use `git switch feature/ansible-linux-deployment-case-study` followed by `git pull --ff-only origin feature/ansible-linux-deployment-case-study` instead of creating it again.

No font files, raw internal documents, production inventory or employee-specific configuration are included in this change.
