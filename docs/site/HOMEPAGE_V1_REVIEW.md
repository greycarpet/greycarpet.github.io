# greycarpet — Homepage v1 Review Notes

> **Branch:** feature/nocturnal-homepage-v1  
> **Design reference:** [Brand & Website Style Guide v1.0](../brand/STYLE_GUIDE.md)  
> **Deployment status:** Review only — not merged into main.

## Goals achieved in this iteration

- Replace `NET/WORK` and the generic network-engineering hero with **greycarpet** and **Josh Escobar**.
- Apply the approved Nocturnal Lab charcoal/graphite/Signal Ice palette.
- Use the specified Space Grotesk, DM Sans, and DM Mono font families.
- Replace fictional case-study cards and placeholders with three based-on-real-work summaries.
- Present a professional experience section, an About summary, and CompTIA Linux+.
- Simplify navigation and improve mobile-menu keyboard behavior.
- Preserve the lightweight static HTML/CSS/JavaScript architecture.
- Avoid fake case-study links, placeholder email/LinkedIn URLs, and unsupported production-wide encryption claims.
- Keep the carpet creature subtle: no unapproved mascot asset is published.

## Publication claims for owner review

**Please verify wording before this branch is merged:**

| Public copy | Basis | Review question |
|---|---|---|
| Josh Escobar / Linux infrastructure & network engineering | Professional focus | Is this the preferred resume-facing headline? |
| Director of Information Technology · ECA Direct · 2023–Present | Career context | Approve the public employer, title and dates? |
| CompTIA Linux+ | Certification | Confirm public credential wording. |
| Secure voice trunk pilot using Twilio, TLS/SRTP | Actual pilot evidence | Approve this sanitized summary before publication? |
| Python/SQL reporting automation | Existing work | Is the generic description sufficiently sanitized? |
| Ansible/Lubuntu endpoint provisioning | Existing work | Is the generic description sufficiently sanitized? |

### Deliberately deferred

- The original full mascot image (pending public-image treatment and placement approval).
- Final vector logo, favicon, and social sharing artwork.
- Resume download (no approved PDF or HTML resume has been added).
- Personal email or LinkedIn URL (not explicitly confirmed for public use).
- Published long-form project pages: cards are non-clickable and correctly say their write-ups are pending.
- Additional Field Notes: no fictional articles or dead links were added.
- Quantified achievements: avoid specific, potentially sensitive company metrics until verified/approved.

## Static review of feature branch

The current branch has been inspected for:

- One H1; unique HTML IDs.
- All internal navigation targets present.
- No generic placeholders (`Your Name`, `hello@example.com`, `NET/WORK`) remaining.
- External new-tab links include `noopener noreferrer`.
- Responsive breakpoint CSS, visible focus outlines, and reduced-motion behavior.
- No false project destination links.

**Not yet verified:** actual desktop/mobile rendering, browser console warnings, screen-reader walkthrough, zoom/reflow at 200–400%, Lighthouse metrics, and keyboard testing in a browser. These must be reviewed in a local preview before merge.

## Local preview

On an existing clean local clone:

```powershell
cd C:\Users\ecadirect\Documents\GitHub\greycarpet.github.io
git status
git fetch origin
git switch --track origin/feature/nocturnal-homepage-v1
start .\index.html
```

If the branch already exists locally, use `git switch feature/nocturnal-homepage-v1` after fetching. **Do not discard uncommitted work to switch branches.**

The live site remains unchanged until this branch is reviewed and merged.

## Suggested next iteration

1. Review homepage copy and professional identity with Josh.
2. Review desktop and mobile appearance locally.
3. Correct any layout, interaction, accessibility or content issues.
4. Approve the site for deployment, then merge the PR.
5. Prepare the first sanitized full case study and approved mascot placement in a separate PR.
