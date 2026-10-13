# greycarpet — Experience & Resume v1 Review

**Feature branch:** `feature/resume-experience-v1`  
**Status:** Draft, owner review required before merging to `main`  
**Live URL after approval:** `https://greycarpet.github.io/resume/`  
**Brand source:** [STYLE_GUIDE.md](../brand/STYLE_GUIDE.md)

## Scope

- A real career timeline on the homepage replaces the previous Director-only experience card.
- A dedicated, responsive and printer-friendly resume page provides detailed roles, supported results, technical competencies, education and certifications.
- A working **Print / Save as PDF** action invokes the browser print dialog; **no PDF file is currently hosted**.
- Navigation on the homepage, case-study pages and resume page links correctly within GitHub Pages.
- Personal email, mobile phone and unverified LinkedIn profile are excluded from public source.
- No employer-only infrastructure diagrams, live addresses, keys, internal file paths, or raw datasets were added.

## Career source and wording decisions

The career timeline is based on Josh's existing resume and professional-experience reference. The records distinguish *formal job title timing* from the overall employment period.

| Public statement | Reasoning / approval point |
|---|---|
| ECA Direct — **Lead IT Support Specialist**, Oct 2023–Nov 2025 | Role-separated historical resume; verify exact title and transition month |
| ECA Direct — **Director of Information Technology**, Nov 2025–Present | The formal-appointment period, not the entire ECA employment period |
| United States Coast Guard — Information Systems Technician, Dec 2019–Dec 2021 | Separate IT billet dates from total military service |
| United States Coast Guard — Fireman, Nov 2017–Dec 2019 | Earlier non-IT service correctly distinguished |
| B.S. User Experience — Full Sail University, Nov 2024 | Completed degree from existing resume |
| CyberTex Network Engineering — in progress, expected Feb 2027 | Not presented as completed |
| CompTIA A+, Network+, Linux+ | Earned certifications in the existing resume |
| 50 Linux workstations standardized | Past deployment scope, not current fleet count |
| ~20 staff hours/week reporting work saved | Estimated outcome, not audited timekeeping |
| 74% lower **affected toll-free inbound charges** | Applies to specified toll-free expense after IVR/queue fix, not all IT spending |
| Production Twilio TLS/SRTP connection | Links to the accepted case study; no all-call encryption claim |

### Review requirements

- [ ] Josh confirms the Lead-to-Director title transition dates.
- [ ] Josh confirms current employer naming and permission for public professional detail.
- [ ] Josh approves certifications and school/dates for public display.
- [ ] Josh approves the qualified 50 / ~20 hrs / 74% metrics as suitable for public use.
- [ ] Resume stays in first person only for summary; career bullets remain factual, not exaggerated.
- [ ] No claim that every infrastructure component was individually engineered without collaboration or automated assistance.
- [ ] Future email/phone/LinkedIn information is added only after explicit public-contact approval.
- [ ] Print output reviewed in Chrome/Edge: page breaks, visible text, section order, and selectable text.
- [ ] Desktop viewport (~1440 and 1024) reviewed for layout and legibility.
- [ ] Mobile (~390 and 320) reviewed for navigation, no unintended horizontal scrolling.
- [ ] Keyboard navigation, mobile-menu Escape behavior, and focus indicators tested.
- [ ] All internal links and GitHub destination checked; no placeholder/empty buttons.
- [ ] Browser console has no errors.
- [ ] Confirm site and case study navigation works from nested `/resume/` page.
- [ ] Explicit owner approval before merging PR.

## Local preview

From a clean PowerShell worktree:

```powershell
cd C:\Users\ecadirect\Documents\GitHub\greycarpet.github.io
git status
git fetch origin
git switch --track origin/feature/resume-experience-v1
python -m http.server 8000
```

If the branch already exists locally, run `git switch feature/resume-experience-v1` and `git pull --ff-only origin feature/resume-experience-v1` after fetching instead.

Open `http://localhost:8000/` and `http://localhost:8000/resume/` in a browser. Use the resume page's **Print / Save as PDF** button to inspect the printer-friendly version.

## Deferred content

- A hosted PDF resume download, pending approved final contact details and printed layout.
- Verified personal email and LinkedIn link.
- Additional dated achievements and supporting public case studies.
- Final real mascot artwork, still intentionally deferred under the brand guide.

All changes are limited to the portfolio repository, not ECA production systems.
