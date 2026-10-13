# Site finishing pass — review

**Branch:** `feature/site-finishing-pass-v1`  
**Base:** `1a0db6ec6fef36dffbd18d0e393cde8ce56fad9d`  
**State:** Draft for owner review; no merge or deployment authorized yet.

## Included

- Shared navigation, footer, readable code/captions and mobile styles in `assets/site-finish.css`.
- Original page styles preserved byte-for-byte as `legacy-*.css`; small CSS import wrappers load the shared layer afterward. No framework, build step or third-party script added.
- Original greycarpet creature, proportionally resized/encoded only. Small About card; larger appearance on the dedicated 404 page. No mascot hero or mascot inside technical evidence.
- A real two-page public PDF resume and extra download shortcuts. The HTML resume remains available and printable.
- Mobile links visible without JavaScript; collapse only after click/Escape handlers are installed. Source links reveal containing details elements when needed.
- A custom 404 page with root-relative assets and a static PDF link.
- Actual repository README, sitemap and crawler guidance. `robots.txt` is not access control; documentation and branches remain public.

## Unchanged / not inferred

The home, resume and project HTML files are not rewritten by this pass. Their approved facts, career dates and three case-study narratives remain intact. Optional JavaScript improves the About presentation, resume action labels, existing conceptual-diagram label and PDF shortcuts. Without JavaScript the original HTML remains the content fallback; the mascot is still static on the 404 page and the PDF has direct links in the README and 404 page.

Personal phone/email and a LinkedIn URL are not published or guessed. GitHub remains the public profile link. No claim of an active security clearance, organizational compliance, guaranteed performance, or additional technical achievement is added. Contact details require a separate explicit owner decision.

## Assets and PDF

See [ASSET_USAGE.md](../brand/ASSET_USAGE.md). The source image was supplied by Josh; no independent exclusive-rights verification is asserted. The optimized WebP is 320 x 320 pixels, 8,870 bytes. Its Git blob is `92c904b62bb6dd01f5a38619d2aa23e7f4c29aad`.

The PDF is 7,067 bytes with two pages, selectable text and portfolio/project links. Its Git blob is `8d3b8f62ed3ee69eb2b5661a58320bea1af7a77d`. Both pages were rendered and visually inspected with PyMuPDF; no clipping or missing text was observed. It is not tagged/PDF-UA certified. Its content is a condensed public rendering of the approved resume and published project work, not an additional independent verification of career facts.

The generator in `tools/build_public_resume.py` requires ReportLab. Keep the HTML resume and generator aligned when facts change, regenerate locally, inspect both pages, and review the output before committing.

## QA actually performed

Chromium 144.0.7559.96 rendered the finishing component preview, the new 404 page, and fixtures recovered from the prior Ansible/Reporting Hub article previews at 1440, 1024, 768, 390 and 320px.

- No page-level horizontal overflow in those 20 rendered combinations.
- No runtime script errors in the tested fixtures.
- Mobile menu opened; Escape closed it and returned focus to the menu button.
- The 404 navigation remained visible with JavaScript disabled at 320px.
- Generated PDF anchors resolved to `https://greycarpet.github.io/assets/Josh_Escobar_Resume.pdf` with a download filename of `Josh_Escobar_Resume.pdf`.
- The original mascot URL resolved to the intended asset location; rendering used an embedded copy of the verified WebP bytes.
- The two original Ansible/Reporting styles used in the fixtures matched the repository Git blob hashes.
- The PDF was parsed, its two pages extracted and rendered, and both rendered images inspected.

### Explicit limits

Browser network navigation, including localhost navigation, was blocked in this environment. Tests used in-memory HTML, inline CSS/JavaScript, local font fallbacks and an embedded image. They did **not** verify a live HTTP download, GitHub Pages' deployed 404 behavior, Google Font fetching, exhaustive screen-reader behavior, or full-page homepage/resume/Twilio regression. The supplied component preview is labeled as a component preview, not a screenshot of the deployed homepage. The old article HTML remains unchanged in the repository.

## Review before merge

- [ ] Approve original-mascot size/placement and the public asset use.
- [ ] Review the public PDF content, dates and print layout.
- [ ] Verify home, resume, all three articles and evidence page in a local HTTP preview.
- [ ] Confirm the PDF download and 404 page in an actual browser.
- [ ] Review with the normal web fonts loaded and at mobile/desktop sizes.
- [ ] Confirm no personal contact details should be added yet, or supply explicitly approved values separately.
- [ ] Approve the draft PR before merge into `main`.

## Local preview

With a clean working tree:

```powershell
cd C:\Users\ecadirect\Documents\GitHub\greycarpet.github.io
git status
git fetch origin
git switch --track origin/feature/site-finishing-pass-v1
python -m http.server 8000 --bind 127.0.0.1
```

For a branch already checked out locally, use `git switch feature/site-finishing-pass-v1` and `git pull --ff-only origin feature/site-finishing-pass-v1` instead of creating it again. Stop any previous process on port 8000 first. Open `/`, `/resume/`, the three `/projects/` pages and `/404.html`. The basic Python server does not automatically map missing routes to the custom 404 document.
