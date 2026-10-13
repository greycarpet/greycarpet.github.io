# ECA Reporting Hub — Case Study Review

**Owner:** Josh Escobar  
**Prepared:** October 13, 2026  
**Branch:** `feature/reporting-hub-case-study`  
**Status:** Draft publication candidate; owner approval required before merge.  
**Page:** `projects/reporting-hub/index.html`  
**Brand reference:** [STYLE_GUIDE.md](../brand/STYLE_GUIDE.md)

## Narrative and role

**Headline:** From manual reports. To a reporting platform.  
**Role focus:** Linux Automation & Platform Engineering.

The complete first-person narrative follows the discovery of undocumented reporting rules, Python/SQL automation, the desktop Reporting Hub, the hosted Linux application, controlled deployment, two genuine production maintenance examples, and the reported operational results. Development assistance is described accurately: substantial AI assistance, with Josh responsible for requirements, context, review, deployment and validation.

## Change scope

- Add the full article and its isolated Nocturnal Lab stylesheet under `projects/reporting-hub/`.
- Update only the homepage reporting card's title, summary, technology tags and destination.
- Add this source/QA record.
- Existing Ansible/Twilio case-study files, resume, shared CSS and shared JavaScript remain unchanged.

A draft branch in this public repository is **not private storage**. No raw client/employee data, credentials, private infrastructure addresses or internal source files are committed. No production application, telephony or database configuration is changed by this portfolio work.

## Source and claim mapping

| Source | Classification | Use in article |
|---|---|---|
| S1: September career materials and October 8 professional-experience reference, E09 | Supported retrospective account | Manual business-rule discovery; Python/SQL workflow steps; scripts-to-desktop-to-hosted evolution; comparison with known/manual outputs; operator ownership and AI assistance |
| S2: October 8 reference, E10, and Docker operations reference | Dated architecture/operations documentation | Django/Gunicorn, Celery worker, Celery Beat, PostgreSQL, Redis; separate persistence; controlled application updates |
| S3: Original October 6 response-change deployment result | Execution output | Preflight, candidate and live stages; unchanged-repeat suppression; preservation of response-change behavior, call totals, retained cells and official files; deployment success |
| S4: Original October 6 agent-hours repair result | Execution output | Shared repeatable-read snapshot; selected filters' count/list totals, source-time and Excel parity; mirror refresh commit after checks; readiness |
| S5: October 8 metric register, M04–M06 | Scoped operator/career metrics | Per-report time, combined reporting cycle, estimated weekly labor and error reduction |
| R1–R3: Official Celery, Docker and PostgreSQL documentation | Technical mechanisms, checked October 13 | Scheduler versus worker; volume lifecycle; repeatable-read behavior |

### Public evidence treatment

Two panels contain selected genuine output rather than fabricated terminal imagery:

1. The hours-repair panel copies six original log lines in original order, omitting intervening employee records, host paths and other output.
2. The return-rule panel reformats one original live validation summary as indented JSON. Values are retained; no participant or client identifier is reproduced.

Workflow, evolution and service panels are explanatory HTML layouts. They are not screenshots from the private application, a live topology, or newly executed performance tests. A PASS assertion documents the check recorded by the deployment script; it is not an exhaustive independent audit.

## Metrics must remain separate

| Metric | Accepted scope |
|---|---|
| 32 workflows/projects | Historical reporting-automation coverage; not proof that all 32 were simultaneously live in the hosted application |
| About 8 hours to under 30 minutes | Earlier combined reporting-cycle comparison |
| 15 minutes–2 hours to under 5 seconds | Selected per-project deliverables in the later operator account; not all exports, syncs or dashboards |
| About 20 staff hours/week saved | Operational estimate, not an independently remeasured time study |
| Approximately 90% fewer reporting errors | Reported estimate; not zero defects or an audited defect-rate measurement |
| Five services | Documented hosted application stack, not the number of all infrastructure services |

Do not combine these measures into a new percentage or imply containerization alone caused the earlier automation speedup. Do not claim every project automatically publishes client-ready files, or that every source path, backup, restore and security control has been exhaustively tested.

## Browser QA completed

The exact article and CSS committed to this branch were rendered in Chromium **144.0.7559.96** with the repository's existing navigation script. Rendering used in-memory HTML with inline copies of the stylesheet/script; external Google Font requests were excluded because network navigation was unavailable.

| Test | Result |
|---|---|
| Viewports 1440, 1024, 768, 680, 390 and 320px | No page-level horizontal overflow |
| Semantic structure | One H1; no duplicate IDs; every same-page anchor resolves |
| Keyboard entry | Skip link receives first Tab focus |
| Mobile navigation | Opens; Escape closes it and restores focus to the menu button |
| Reduced motion | Computed scroll behavior becomes `auto` |
| Source reference | Target source note remains visible in the open reference section |
| JavaScript disabled, 320px | Navigation visible; no page-level horizontal overflow |
| Runtime script errors | None in tested rendering |
| Known private-value check | No selected employee/client identifiers, internal paths or live addresses found in article |
| Homepage diff review | Only the reporting card's four content lines changed |

### Exact Git blobs tested

- Article: `3603d743fecb759348d738b4dc635f4103c4ab1e`
- CSS: `74e97330efaffe5ee056f5e96328864f05fc2515`
- Existing `script.js`: `1f9974f25f2351fc41de1377dc44901a2a51f798`

**Remaining QA:** Render with Google Fonts available; confirm actual local/deployed routes, full-site interactions and link behavior; test other browsers, zoom, and assistive technologies. These results are not a claim of complete WCAG conformance, live-server verification, or a new Reporting Hub production test.

## Owner review checklist

- [ ] Narrative represents the actual reporting initiative and personal ownership.
- [ ] Historical workflow/cycle figures and qualified labor/error estimates are approved for public use.
- [ ] Desktop-to-hosted evolution is accurate without implying an all-project cutover.
- [ ] Monthly repeated-response rule is correctly scoped to one workflow family.
- [ ] Selected technical logs and described business logic are permitted for public disclosure.
- [ ] Development assistance is represented accurately.
- [ ] Homepage, article, resume and other case-study navigation reviewed locally.
- [ ] Typography reviewed with the configured web fonts available.
- [ ] Explicit approval before merge into `main`.

## Local preview

From a clean working tree in PowerShell:

```powershell
cd C:\Users\ecadirect\Documents\GitHub\greycarpet.github.io
git status
git fetch origin
git switch --track origin/feature/reporting-hub-case-study
python -m http.server 8000 --bind 127.0.0.1
```

Open `http://localhost:8000/projects/reporting-hub/` and check the homepage reporting card. Stop an existing server on port 8000 before starting another. Do not discard local work to switch branches.

For an existing local branch, use `git switch feature/reporting-hub-case-study` followed by `git pull --ff-only origin feature/reporting-hub-case-study` instead of creating the branch again.

No font files, private source documents or raw operational records are included.
