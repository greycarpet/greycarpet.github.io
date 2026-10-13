# Secure Voice Trunk — Publication Review (v1)

**Branch:** `feature/secure-voice-trunk-case-study`  
**Proposed public URL:** `https://greycarpet.github.io/projects/secure-voice-trunk/`  
**Brand rules:** [greycarpet style guide](../brand/STYLE_GUIDE.md)  
**Status:** Draft publication candidate reflecting the successfully deployed production trunk. Not approved for public release by this PR.

## Included changes

- `projects/secure-voice-trunk/index.html` — full case-study page with eight numbered chapters and four selected diagnostic panels.
- `projects/secure-voice-trunk/case-study.css` — responsive Nocturnal Lab article styles, diagrams, evidence layouts, print and mobile rules.
- `projects/secure-voice-trunk/evidence.html` — public-friendly evidence explanations and limits.
- `projects/secure-voice-trunk/EVIDENCE.md` — Markdown audit/source record for future maintainers.
- `index.html` — featured project card links to the case study and identifies the secure trunk as production deployed.
- `styles.css` — accessible CTA appearance.

No production servers, Twilio settings, or live contact-center services are changed by this portfolio work.

## Claim handling

| Claim | Evidence treatment |
|---|---|
| Legacy SIP transport unencrypted | E01 original discovery excerpt |
| Four TLS handshakes with validated certificates | E02 original targeted preflight |
| Loaded TLS/SDES policy | E03 original Asterisk runtime output |
| Answered SRTP echo pilot | E04 original one-call collector and separate operator confirmation |
| Twilio completed secure 45-second record | E05 prior reviewed Twilio export; raw record intentionally omitted |
| 19 secure-marked call records in follow-up | E06 historical prior review, **not freshly re-parsed** |
| Secure trunk successfully deployed and carrying production calls | E07 **direct environment-owner confirmation** on October 13; detailed cutover/campaign inventory not included |
| Full migration of every campaign or call leg / HIPAA compliance | **Not claimed** |
| Fix of subsequent FastAGI issue | **Not claimed** |

Terminal panels are deliberately **typeset redacted excerpts** and say so. They are neither screenshots from Twilio Console nor untouched terminal captures. Original private call parties, account IDs, certificates and live IP addressing do not appear in the article.

## Release approval checklist

- [ ] Josh approves the case-study narrative and attribution.
- [ ] Employer/client publication permissions are established if required.
- [ ] The 19-entry historical follow-up statement is acceptable with its explicit evidence caveat; otherwise remove it.
- [ ] Production deployment language accurately describes the live secure trunk without suggesting every campaign or call leg migrated.
- [ ] Owner confirms the exact scope/date of rollout if a more detailed deployment timeline will be published.
- [ ] Evidence panels and Markdown source have been reviewed for confidentiality.
- [ ] Desktop layout tested at 1440px and 1024px.
- [ ] Mobile layout tested at 390px and 320px; code/long tables independently scroll.
- [ ] Keyboard-only navigation, visible focus, Escape/menu behavior tested.
- [ ] Screen reader can follow figures, headings, links and the architecture description.
- [ ] Zoom/reflow checked; text is readable and does not overlap.
- [ ] Browser console has no errors; all local and external links work.
- [ ] Main site navigation/homepage card links return correctly.
- [ ] Page metadata, title, alt/figure descriptions and print view reviewed.
- [ ] Feature branch PR reviewed and explicitly approved before merge to `main`.

## Local preview (Windows PowerShell)

From a **clean** worktree:

```powershell
cd C:\Users\ecadirect\Documents\GitHub\greycarpet.github.io
git status
git fetch origin
git switch --track origin/feature/secure-voice-trunk-case-study
start .\projects\secure-voice-trunk\index.html
```

If that local branch already exists, use `git switch feature/secure-voice-trunk-case-study` instead. **Do not discard uncommitted work** to switch branches.

Review the article and `evidence.html`. For realistic path/navigation checks, use a simple local static HTTP server instead of `file://`:

```powershell
python -m http.server 8000
```

Then navigate to `http://localhost:8000/projects/secure-voice-trunk/`. Stop the server with Ctrl+C.

## Production implementation versus portfolio publication

The trunk is now in production; this PR changes only the public portfolio documentation. The operator-confirmed rollout is reported in E07, while E01–E06 document the preflight, pilot and historical follow-up observations. No live system modifications or production-routing changes were made through this GitHub PR.

## Deferred enhancements

- Optional original PNG evidence images may be added in a later PR if approved; the current figures already display authentic selected excerpt text and preserve accessible text.
- A public-safe downloadable Markdown narrative is not bundled with this PR. The existing source-of-truth article is the HTML page with `EVIDENCE.md` for provenance.
- A future site-wide Projects index, print-friendly PDF, richer technical diagrams, and hover states can be designed separately.

No private configuration and no raw call-party records should ever be committed to this public repository.
