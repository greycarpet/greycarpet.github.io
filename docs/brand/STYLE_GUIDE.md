# greycarpet — Brand & Website Style Guide

> **Version:** 1.0  
> **Owner:** Josh Escobar  
> **Date:** October 13, 2026  
> **Status:** Brand baseline; website implementation pending review  
> **Repository:** [greycarpet/greycarpet.github.io](https://github.com/greycarpet/greycarpet.github.io)  
> **Applies to:** GitHub Pages portfolio, project case studies, resume presentation, technical writing, brand assets, and related public developer profiles

## How to use this guide

This document is the **single source of truth** for the greycarpet brand and the design direction of Josh Escobar's engineering portfolio. Consult it before changing the site's copy, typography, colors, images, layout, components, or project presentations.

The [Established](#status-of-decisions) decisions below reflect explicit choices made by the site owner. Implementation specifications provide consistent defaults for future work, but are not a claim that the current site has already been updated.

**Important:** Adding this document is a documentation change only. It does not approve or implement a website redesign, publish the mascot image, or revise professional claims.

---

## 1. Brand at a glance

| Attribute | Standard |
|---|---|
| **Official name** | **greycarpet** |
| Capitalization | Always lowercase |
| Wordmark spelling | `greycarpet` |
| Brand category | Personal engineering identity and technical portfolio |
| Person behind the brand | Josh Escobar |
| Professional focus | Linux infrastructure, network engineering, security, and automation |
| Creative direction | **Nocturnal Lab** |
| Appearance | Dark-first; graphite, cool grays, restrained icy blue |
| Mascot | User-provided gray rolled-carpet creature; subtle recurring character |
| Personality | Methodical, credible, curious, inventive; dry humor only in small doses |
| Primary audiences | Engineering hiring managers, technical interviewers, peers, collaborators |
| Primary outcome | Establish trust through clear professional identity and demonstrable work |

### Core statement

**greycarpet is the personal engineering portfolio of Josh Escobar.**

The site should make it immediately clear what Josh does, what systems he works with, how he approaches complex technical problems, and what he has actually delivered. The playful identity supports the portfolio—it does not replace professional evidence.

### Brand promise

**Understand the system. Engineer the solution. Prove the result.**

This is an editorial guiding principle, **not** a mandatory homepage slogan. Any final headline must be approved during the content-design phase.

### What the brand is—and is not

**It is:** practical infrastructure engineering, thoughtful technical documentation, modern but restrained design, a distinctive visual identity, and proof of work.

**It is not:** a gaming persona, a fictitious consulting company, an anonymous studio with an invented team, a novelty mascot site, or a generic template claiming achievements that have not occurred.

---

## 2. Identity hierarchy and positioning

The order of emphasis matters:

1. **Josh Escobar** — the person, engineer, author, and owner of the work.
2. **Expertise and outcomes** — Linux, networking, security, automation, infrastructure operations.
3. **greycarpet** — the recognizable online identity housing the work.
4. **Mascot** — an occasional character that makes the identity memorable.

### Name and attribution

- Use **greycarpet** as the wordmark, website brand, and online moniker.
- Use **Josh Escobar** for the hero's personal identity, resume, job history, bylines, contact details, and professional metadata.
- Acceptable lockup: **greycarpet** with smaller supporting text **Josh Escobar / Engineering Portfolio**.
- Do **not** style the actual brand as `greycarpet_`, `GreyCarpet`, `GREYCARPET`, `grey/carpet`, or `greycarpet.dev`.
- A terminal cursor may appear **beside** the mark as a separate decorative animation, but it is not part of the name, accessible label, SEO title, or copied wordmark.
- Use `greycarpet` as the canonical spelling even if a section headline follows normal sentence capitalization rules.

### Professional positioning

Preferred umbrella description:

**Linux Infrastructure & Network Engineering**

Secondary specialties: security engineering, systems administration, infrastructure automation, VoIP/telephony, operations and troubleshooting.

The portfolio may accurately describe Josh's management and leadership experience without obscuring hands-on engineering work. Use actual job titles in chronological experience; do not rewrite job history to match a target vacancy.

### Audience priorities

| Visitor | Must understand within seconds |
|---|---|
| Recruiter | Josh's name, specialization, location/remote availability if approved, resume link |
| Hiring manager | Technical scope, leadership/ownership, measurable impact, work history |
| Engineer | Real architecture, diagnostics, technical decisions, reproducible evidence where safe |
| Collaborator | Current areas of work, GitHub profile, how to make contact |

---

## 3. Character and voice

### Brand personality

Aim for **80% professional engineering discipline / 20% creative character**.

| Trait | Express through | Avoid |
|---|---|---|
| Methodical | Baselines, constraints, diagnostics, validation | Unsupported certainty |
| Resourceful | Practical designs, scripts, automation | Vague “innovation” claims |
| Curious | Decisions, investigations, lessons learned | Unfocused technical trivia |
| Dependable | Scope, rollback, documentation, known gaps | “Perfect” and “bulletproof” language |
| Distinctive | Typography, mascot easter eggs, subtle humor | Childish gimmicks, noise and clutter |

### Writing voice

Use first-person language on About, Experience, and project narratives. Favor precise verbs: **investigated, implemented, validated, automated, migrated, hardened, documented**.

- Write for technically literate readers without requiring niche vendor knowledge.
- Explain the problem before the solution.
- Prefer short paragraphs, informative subheadings, and real outcomes.
- Distinguish **observed**, **configured**, **tested**, **verified**, **planned**, and **not yet established**.
- Use specific figures only when supportable.
- Disclose constraints and limitations—especially in security and compliance work.
- Avoid résumé clichés: “passionate professional,” “cutting-edge,” “synergy,” “seamless,” “best in class,” and “leveraged” when simpler words fit.
- Prefer **I** for personally completed work and **we** only for collaborative work with accurately described ownership.

### Example: homepage introduction

> **Josh Escobar**  
> **Linux Infrastructure & Network Engineering**  
> I build, secure, troubleshoot, and automate the systems that keep operations running. Here you'll find real projects, engineering decisions, and evidence of the work behind them.

This is a **copy direction**, not approved final homepage text.

### Example: project description

**Weak:** “Implemented world-class secure telephony compliant with all standards.”

**Preferred:** “Designed and verified an isolated SIP-over-TLS and SRTP trunk path using Linux, Asterisk/PJSIP, VICIdial, and Twilio. Validated certificate trust, negotiated encrypted media, and call completion before proposing production routing changes.”

The second example is scoped to the evidence; do not imply all production calls were encrypted by the initial pilot.

### Humor

Reserve humor for secondary, noncritical moments: 404, loading/empty states, a discreet mascot caption, an occasional field note. Never use humor in security warnings, failure notices, professional claims, or accessibility labels where it reduces clarity.

---

## 4. Visual identity — Nocturnal Lab

### Art direction

The site should feel like an independent infrastructure engineer's late-night workshop: charcoal surfaces, carefully composed diagrams, precise labels, real terminal excerpts, subtle texture, and a small, unusual gray creature hiding in the margins.

Keywords: **graphite / tactile / quiet / technical / deliberate / atmospheric**.

Avoid neon hacker imagery, generic glowing circuitry, excessive gradients, fake “matrix” rain, noisy background grids, or a wall of glowing badges.

### Primary palette

| Token | Name | HEX | Intended role |
|---|---|---|---|
| `--gc-bg` | Midnight | **#0C0E11** | Main page background |
| `--gc-surface` | Graphite | **#171B20** | Header, cards, panels |
| `--gc-surface-raised` | Basalt | **#272D34** | Raised areas, code headers, selected surfaces |
| `--gc-neutral` | Carpet Gray | **#737A82** | Decorative lines, subdued large labels; **not normal body text** |
| `--gc-text` | Mist | **#E8EBEF** | Primary text and strong headings |
| `--gc-text-muted` | Slate | **#AAB3BC** | Secondary text and captions |
| `--gc-accent` | Signal Ice | **#A5DFFF** | Links, active states, selected accents and focus outlines |
| `--gc-warm` | Warm Bone | **#D8C9B9** | Rare illustrative accents; mascot-related details |

### Rules for applying color

- Dark backgrounds dominate; light typography provides legibility.
- Use Signal Ice purposefully rather than on every card, heading, border, and badge.
- Warm Bone appears infrequently; it is not a second interface accent.
- Use grays to create hierarchy through contrast and surface elevation, not visual clutter.
- Never communicate status with color alone.
- Avoid red/green status semantics unless explicit labels and sufficient contrast accompany them.
- Do not overlay text on busy fur/fiber textures.

### Tested contrast examples (approximate WCAG ratios)

| Foreground | Background | Contrast | Use |
|---|---|---:|---|
| Mist `#E8EBEF` | Midnight `#0C0E11` | **16.16:1** | Primary text |
| Slate `#AAB3BC` | Midnight | **9.10:1** | Secondary text |
| Signal Ice `#A5DFFF` | Midnight | **13.44:1** | Links and focus |
| Slate | Graphite `#171B20` | **8.14:1** | Panel text |
| Carpet Gray `#737A82` | Midnight | **4.45:1** | **Fails 4.5:1 for normal text** |
| Carpet Gray | Graphite | **3.98:1** | Decoration / sufficiently large text only |

Always reassess contrast against **actual rendered background colors**, especially with transparency, image overlays, hover states, and gradients. Target **WCAG 2.2 AA**. Minimum contrast for normal text: 4.5:1; large text and relevant non-text UI boundaries: 3:1.

### Reference implementation tokens

These variables are the future implementation baseline, not a request to modify `styles.css` now:

```css
:root {
  color-scheme: dark;
  --gc-bg: #0c0e11;
  --gc-surface: #171b20;
  --gc-surface-raised: #272d34;
  --gc-neutral: #737a82;
  --gc-text: #e8ebef;
  --gc-text-muted: #aab3bc;
  --gc-accent: #a5dfff;
  --gc-warm: #d8c9b9;

  --gc-border: #343c44; /* decorative; verify if used as a control boundary */
  --gc-font-display: "Space Grotesk", "Segoe UI", sans-serif;
  --gc-font-body: "DM Sans", "Segoe UI", Arial, sans-serif;
  --gc-font-mono: "DM Mono", "Cascadia Code", Consolas, monospace;

  --gc-radius-sm: 6px;
  --gc-radius-md: 12px;
  --gc-radius-lg: 20px;

  --gc-space-1: 4px;
  --gc-space-2: 8px;
  --gc-space-3: 12px;
  --gc-space-4: 16px;
  --gc-space-6: 24px;
  --gc-space-8: 32px;
  --gc-space-12: 48px;
  --gc-space-16: 64px;

  --gc-container-width: 1160px;
}
```

---

## 5. Typography

The existing site already loads these families; reuse them rather than introducing an unnecessary new font stack.

| Function | Family | Guidance |
|---|---|---|
| Display and wordmark | **Space Grotesk** | Medium/semibold; restrained tracking |
| Body, navigation, résumé | **DM Sans** | Regular/medium; readable line height |
| Code, metadata, labels | **DM Mono** | Compact but never unreadably small |

### Type scale

| Element | Suggested desktop size | Responsive guidance |
|---|---|---|
| Homepage hero | 56–72px | `clamp(2.6rem, 5.5vw, 4.5rem)` |
| Section heading | 32–44px | `clamp(2rem, 3vw, 2.75rem)` |
| Project title | 23–30px | 22px minimum |
| Body | 16–18px | 16px minimum |
| Secondary / captions | 14–16px | 14px minimum where practical |
| Code | 13–15px | 13px minimum; horizontal scroll if needed |
| Eyebrow/metadata | 12–13px | Use sparingly; avoid tiny 8–10px text |

- Body line height: 1.6–1.8; headings: approximately 1.1–1.2.
- Prefer 60–80 characters per long-form text line.
- Avoid large blocks of all-caps or monospace text.
- Use semantic HTML heading order, not visual heading classes alone.
- Typography must respond to user zoom up to at least 200% without losing content.

---

## 6. Wordmark, icon, and mascot system

### 6.1 Wordmark

**Canonical wordmark:** `greycarpet`

- Always lowercase, one word, no suffix.
- Prefer a Space Grotesk medium/semibold wordmark on a dark background.
- Primary color: Mist; occasional Signal Ice may highlight a **separate small mark**, not alter letters or spelling.
- Use enough space around the wordmark for legibility.
- Do not distort, italicize, stretch, outline, or give it a strong glow.
- Lockup with Josh's name is welcome; the name stays secondary to the brand mark in the site's nav.
- No official SVG/vector logo has been approved yet. Use the text wordmark until one is developed and reviewed.

### 6.2 Compact symbol

**Future design direction:** simplified carpet coil/spiral.

Use cases: favicon, tiny avatar, site watermark, diagram signature, compact nav. Keep the shape recognizable at 16, 32, and 64 pixels. The symbol is **proposed**, not an approved final logo asset. Do not claim that a placeholder spiral is the finished logo.

### 6.3 Mascot

**Source concept:** the user-provided original rendering of a gray rolled carpet creature with prominent eyes, textured fabric, and pointed teeth.

**Established direction:** a **subtle recurring character**, not the main hero, centerpiece, or corporate mascot.

| Location | Treatment |
|---|---|
| Home | Small, quiet optional appearance, secondary to Josh's name and work |
| About | Small dedicated explanation of the personal moniker, with original creature |
| Projects | Generally absent; technical evidence remains primary |
| Field notes | Optional discreet appearance or recurring signature |
| 404 | May be prominent as a playful exception |
| Favicon | Use proposed simplified coil, **not** the photorealistic creature |

Rules:

1. Preserve the creature's visual identity, rolled silhouette, gray textile texture, unusual eyes, and overall character.
2. Avoid cartoon recoloring, excessive animation, repetitive placements, and oversized overlays on technical content.
3. Never depict the mascot as an employer's official seal or a compliance certification.
4. Do not assign an official mascot name without Josh's approval.
5. Do not publish or modify the source image until the selected file, cropping, rights/provenance, and final placement are reviewed.
6. Provide concise, contextual alt text; for example, **“Gray rolled-carpet creature, the greycarpet mascot.”** Decorative repetitions should use empty alt text.
7. Use optimized, appropriately sized responsive images when published; retain the original master offline or in an approved assets location.

### Brand asset naming conventions (future)

- `assets/brand/greycarpet-wordmark.svg`
- `assets/brand/greycarpet-symbol.svg`
- `assets/brand/greycarpet-mascot.webp`
- `assets/brand/greycarpet-mascot-original.png` (only if publication is approved)
- `assets/brand/greycarpet-social-card.png`

These are **proposed paths**, not files already in the repository.

---

## 7. Photography, diagrams, and imagery

Prefer authentic technical media over generic stock imagery.

### Preferred imagery

- Sanitized architecture diagrams with clear service boundaries.
- Real Linux commands and diagnostic excerpts, rendered readably.
- Annotated troubleshooting evidence and before/after comparisons.
- Carefully selected site or product screenshots where publication is permitted.
- Subtle gray textile materials as a brand motif on nonreading surfaces.
- Cropped detail shots of the mascot in limited placements.

### Evidence standards

- Label **actual screenshots** as screenshots.
- Label re-created or anonymized terminals as **“Reconstructed, sanitized excerpt”**.
- Do not imply mockups or illustrative outputs are recordings of actual production execution.
- Preserve sequence and context when showing error messages or command output.
- Redact sensitive information **before** adding evidence to the repository.
- Use captions that explain **what the figure proves** and what it does not.
- Include alt text and avoid important information solely inside a raster image.
- For diagrams, provide a text description of major nodes/relationships.

### Avoid

Glowing green binary rain, generic server-room photography, copied vendor dashboards as decoration, fabricated packet captures, security shield clichés, and mascot images behind paragraphs.

---

## 8. UI patterns and components

These rules apply when the existing HTML/CSS/JS template is personalized.

### Navigation and header

- Left: text wordmark **greycarpet**; right: concise navigation.
- Suggested top-level links: **Work, Experience, About, Notes, Resume**.
- Give Contact a clear footer or navigation entry; avoid an overcrowded header.
- Show current location; maintain an obvious focus indicator.
- Mobile menu must be keyboard-accessible and announce expanded state.
- Do not replace accessibility labels with decorative wordmarks or emoji.

### Homepage hero

The hero must answer: **Who is Josh? What does he work on? Why should I keep reading?**

**Required:** Josh Escobar, an accurate professional title/positioning statement, 1–3 lines of substance, a path to selected work, and a resume/contact path.

**Optional:** small mascot appearance and modest visual decoration.

**Not acceptable:** mascot-only splash screen; brand manifesto without Josh's name; a generic placeholder engineer illustration occupying the primary hierarchy.

### Project cards

Each card should contain:

1. Project title.
2. One-sentence technical problem or outcome.
3. Engineering domain/category.
4. 2–5 meaningful technology labels.
5. A real destination to a case study, code repository, or documentation.
6. An explicit state if work is exploratory or in progress.

Project cards should not link to `#contact` as fake “View case study” links.

### Buttons and links

- Primary action: high-contrast Signal Ice fill with Midnight text; use sparingly.
- Secondary action: clear border or text link with hover/focus behavior.
- Distinguish links from surrounding copy through underline or another non-color-only cue.
- No empty, dead, or deceptive actions.
- Visible keyboard focus; target sizes should meet WCAG 2.2 guidelines.

### Tags and metadata

- Use a constrained vocabulary: **Linux, Networking, Security, Automation, Cloud, Telephony, Operations**.
- Technology tags are facts, not decorative buzzwords.
- Use small outlined surfaces with readable text, no gratuitous status badges.
- Avoid using color alone to categorize case studies.

### Code panels

- Use real text, not screenshots when possible.
- Provide filenames/command purpose and context.
- Use horizontal scrolling and a visible copy affordance only if implemented and tested.
- Highlight commands carefully; do not expose secrets or imply destructive commands are safe without caveats.
- Any “Copy” control must perform a working action.

### Sections, grids, and cards

- Max content width: ~1160px.
- Cards: Graphite backgrounds, subtle 1px borders, 12px radius.
- Main body: generous whitespace and readable text.
- On mobile: stack important details before decoration.
- Favor useful technical information over animated gimmicks.

---

## 9. Layout, rhythm, and motion

### Layout

- Use a mobile-first, responsive layout.
- Content width: up to ~1160px; comfortable reading measure for articles.
- Base spacing grid: 4px and 8px increments; standard section spacing 64–112px on desktop, 40–72px on mobile.
- A typical design uses single-column mobile, then two-column projects on medium/large screens.
- The featured case study can span two columns with stronger visual hierarchy.
- No horizontal overflow at 320px viewport width; code blocks may scroll independently.

### Motion

- Favor low-key hover transitions (typically 120–240ms).
- Avoid scroll hijacking, autoplay sound, rapid blinking, and decorative delays.
- Mascot animation, if any, should be rare, subtle, and nonessential.
- Respect `prefers-reduced-motion: reduce`.
- No motion should obscure content, slow down resume access, or prevent interaction.

---

## 10. Information architecture and content priorities

The site must function as both **a human-readable resume** and **a technical body of evidence**.

### Recommended site map

| Destination | Primary job |
|---|---|
| **Home** | Identify Josh, summarize expertise, feature proven work |
| **Work / Projects** | Curated case studies with technical substance |
| **Experience** | Real roles, responsibilities, impact, career progression |
| **About** | Engineering interests, background, certifications, greycarpet identity |
| **Field Notes** | Actual technical writing, experiments, and lessons learned |
| **Resume** | A current accessible resume view/download |
| **Contact** | Verified GitHub, LinkedIn, and preferred public contact route |

One-page layout with anchored sections is acceptable for v1, provided case studies get dedicated readable pages when published. Do not introduce a framework just for routing.

### Homepage content order

1. Clear identity and focused professional statement.
2. Featured projects with real links.
3. Selected evidence of impact / technical strengths.
4. Experience snapshot.
5. About and certification highlights.
6. Field notes (only genuine posts).
7. Resume/contact call to action.

### Case-study editorial pattern

Use this outline for substantive engineering work:

1. **Title / role / date / environment** — accurate scope and ownership.
2. **Executive summary** — what problem mattered and why.
3. **Initial state and constraints** — evidence of the starting condition.
4. **Architecture / design decisions** — options, tradeoffs, and why.
5. **Implementation** — important actions, not a raw command dump.
6. **Troubleshooting** — unexpected behaviors and root-cause confidence.
7. **Validation** — what was independently confirmed.
8. **Outcome** — business and technical impact, measurable where possible.
9. **Limits / remaining work** — unfinished or unverified conditions.
10. **Lessons / technologies / sanitized references**.

Avoid claims that one pilot proves enterprise-wide security or compliance.

### Recommended initial project themes (subject to publication review)

- Encrypted outbound voice trunk on Linux (Asterisk/PJSIP, VICIdial, Twilio TLS/SRTP).
- Python reporting automation and data quality controls.
- Linux workstation configuration and repeatable Ansible deployment.
- Remote access and infrastructure migration design.
- Backup/recovery automation with test-driven documentation.

Use sanitized descriptions; projects from work may require employer/client approval before any specific implementation detail is published.

---

## 11. Resume and professional credibility standards

- The headline must accurately represent Josh's competencies; it need not be identical to every historical job title.
- Preserve real employer names and role titles only where intended for public disclosure.
- Separate leadership ownership from hands-on implementation; both can be strengths.
- List credentials using verified formal names and issuance dates.
- Present figures (time saved, fleet size, cost reduction, uptime, users supported) only after checking the measurement and its publication sensitivity.
- Do not use fictional case studies, filler awards, or generic achievement templates.
- Replace all placeholders (e.g., “Your Name”, `hello@example.com`, generic social links) before declaring the public portfolio complete.
- Use an accessible HTML version where possible in addition to a properly tagged resume PDF.
- Keep case-study dates and current employment status accurate as time passes.

---

## 12. Site metadata and public discoverability

### Identity and metadata

Proposed site title:

**Josh Escobar | Linux Infrastructure & Network Engineering — greycarpet**

Proposed meta description:

**Josh Escobar's engineering portfolio: Linux infrastructure, network engineering, security, automation, and technical case studies.**

Guidelines:

- Include Josh Escobar as text in the page title and main content.
- Include greycarpet in metadata, navigation, and accessible branding.
- Use meaningful per-page titles and descriptions, not duplicates.
- Add canonical URLs and social preview metadata when real pages are published.
- Use descriptive slugs, e.g., `/projects/secure-voice-trunk/`.
- Create a 1200×630 social sharing image **after** the logo and mascot crop are approved.
- Use one descriptive H1 per page.
- Do not claim certifications, employment, experience levels, or compliance status for SEO purposes without evidence.

### GitHub profile alignment

The GitHub profile may mirror the wordmark/palette and link to the portfolio. A pinned case-study repository can emphasize depth. Keep naming and public claims consistent between GitHub, portfolio, resume, and LinkedIn, while allowing different layouts.

---

## 13. Privacy, security, and employer confidentiality

Public project publication must be treated as a deliberate release process.

**Never commit:**

- Passwords, tokens, SIP credentials, private keys, or sensitive certificate material.
- Internal network diagrams that expose unnecessary attack paths.
- Proprietary datasets, customer/member information, recordings, call-detail records, or protected health information.
- Unredacted phone numbers, trunk/account identifiers, server public IPs, VPN peer details, or sensitive paths when their disclosure is not approved.
- Live environment exports that reveal exploitable operational details.
- Employer/client names or logos implying endorsement without permission.

Do publish **reconstructed architecture and sanitized evidence** that accurately supports the story. Never portray anonymized illustrations as untouched production screenshots.

Before a public case study goes live, inspect the Markdown source, images, EXIF/metadata, asset filenames, terminal history, diagram labels, PDF metadata, and repository history. A redaction in the visible page does not remove secrets already committed to Git history.

### Compliance language

A secure connection, encrypted test call, or completed technical control is not equivalent to proving HIPAA compliance, SOC 2 compliance, or any broader organizational certification. State exactly what connection, system, protocol, test, and date were validated.

---

## 14. Accessibility and performance baseline

Target **WCAG 2.2 AA** for the published site.

Minimum expectations:

- Correct heading hierarchy, landmarks, labels, alt text, and skip link.
- Keyboard operation for all controls, with visibly focused states.
- Body text contrast ≥ 4.5:1; large text and meaningful visual controls ≥ 3:1.
- Comfortable font sizing, adequate line height, responsive 200–400% zoom/reflow.
- Reduced-motion support.
- No essential information conveyed only by position, color, or image.
- No blank labels such as “click here” for critical links.
- Appropriate 44px-ish touch-friendly targets as a design preference; test against applicable WCAG 2.2 target-size requirements.
- Deferred or optimized decorative assets so the large mascot never delays the identity and project content.
- Working links, semantic controls, and no console errors from missing optional elements.
- Test Chrome, Firefox, Edge, mobile widths, keyboard-only navigation, and screen-reader basics.

Prioritize HTML/CSS and small progressive JavaScript rather than unnecessary application dependencies.

---

## 15. Existing repository and implementation approach

### Baseline audit (October 13, 2026)

The existing GitHub Pages repository currently contains:

- `index.html` — responsive one-page Network Engineer template with placeholder identity and projects.
- `styles.css` — existing dark green/lime presentation and responsive layout.
- `script.js` — project filtering, mobile navigation, and dynamic copyright year.
- `README.md` — starter instructions identifying the site as a template.

**Keep:** lightweight static architecture, accessible intent, responsive structure, useful filtering where populated with real projects.

**Replace after review:** “NET/WORK” branding, template green palette, placeholder name/bio, fictional project cards, placeholder milestones and notes, default social/contact links, and generic SEO copy.

### Delivery strategy

1. Approve this brand guide and unresolved brand decisions.
2. Approve identity copy and actual resume/project content.
3. Produce a homepage layout concept.
4. Implement changes on a dedicated feature branch.
5. Review desktop/mobile screenshots, interactions, accessibility, and privacy.
6. Publish through an intentional pull request merge into `main`.

**No site source files need to change to adopt this guide as documentation.**

---

## 16. Content and component acceptance checklist

Use this checklist when future PRs alter the site:

- [ ] The canonical name is written **greycarpet**—lowercase and unsuffixed.
- [ ] Josh Escobar is immediately identifiable on the home page.
- [ ] Real professional experience takes priority over decoration.
- [ ] The charcoal/ice palette and approved type system are used consistently.
- [ ] Text and controls meet contrast and focus requirements.
- [ ] The mascot remains a subtle supporting character.
- [ ] All project links work and lead to real content.
- [ ] Claimed outcomes have evidence and appropriate scope.
- [ ] Screenshots/outputs are truthfully labeled and safely redacted.
- [ ] New case studies distinguish verified results from outstanding work.
- [ ] Mobile navigation, filters, keyboard access, and reduced motion work.
- [ ] No placeholder content remains in any section marked complete.
- [ ] No unapproved employer/client confidential information is published.
- [ ] New imagery is optimized and includes correct alt text.
- [ ] SEO title, description, GitHub and resume links are accurate.
- [ ] The change has been reviewed before merging to the live branch.

---

## 17. Status of decisions

### Established by owner

- Brand name is exactly **greycarpet**.
- The brand belongs to **Josh Escobar**.
- The site's intended purpose is a genuine resume/portfolio with technical case studies.
- The uploaded rolled-carpet creature is the reference mascot.
- Mascot role is **subtle recurring character**, not the hero or dominant visual identity.
- Future redesign work should be reviewed before changing the live portfolio.

### Baseline design direction documented in this guide

These are specific recommended defaults resulting from the Nocturnal Lab design discussion; they can be revised through an explicit style-guide version change:

- Dark charcoal/graphite appearance with Signal Ice highlights.
- Space Grotesk, DM Sans, and DM Mono typography.
- Engineering-diagram and technical-evidence visual language.
- The above CSS token set, layout principles, and component hierarchy.
- Distinct personal identity (Josh) and brand identity (greycarpet).

### Not yet approved / outstanding

- Final vector wordmark design and simplified spiral mark.
- Final crop/export/placement of the supplied mascot asset.
- Any proposed mascot nickname.
- Exact homepage hero headline, bio, résumé language, and public contact links.
- Final project selection, publication permissions, and case-study URLs.
- Final page-by-page designs and animations.
- Whether this guide should evolve into a separate visual asset library.

Do not treat outstanding items as finalized decisions merely because a mockup exists.

---

## 18. Governance and future updates

- **Owner and approver:** Josh Escobar.
- **Location:** `docs/brand/STYLE_GUIDE.md`.
- **Change policy:** propose adjustments through PRs with a brief rationale and, for visual changes, before/after references.
- **Versioning:** increase the minor version for nonbreaking refinements; major version for a meaningful repositioning, logo system, or palette overhaul.
- **Record new approvals:** move decisions from “Not yet approved” to “Established” only after explicit owner approval.
- **Do not silently rewrite:** professional identity, name spelling, mascot role, claims standards, or public-safety guidance.

### Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-13 | Initial canonical brand/website style guide; defined exact name, identity hierarchy, Nocturnal Lab defaults, subtle mascot usage, technical/editorial standards, privacy and accessibility principles |

---

**End of style guide — greycarpet / Josh Escobar**
