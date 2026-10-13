# greycarpet — Josh Escobar

Personal portfolio for Linux infrastructure, network engineering, security and automation. The site is static HTML, CSS and a small progressive-enhancement script, served by GitHub Pages.

## Read the work

- [Twilio TLS/SRTP production trunk](projects/secure-voice-trunk/index.html)
- [50-workstation Ansible deployment](projects/ansible-linux-deployment/index.html)
- [ECA Reporting Hub](projects/reporting-hub/index.html)
- [HTML resume](resume/index.html) · [Public resume PDF](assets/Josh_Escobar_Resume.pdf)

## Design and content reference

The canonical name is **greycarpet**, lowercase and without a suffix. [The brand guide](docs/brand/STYLE_GUIDE.md) controls identity and editorial decisions. [Asset usage](docs/brand/ASSET_USAGE.md) documents the original creature and the public resume. Project evidence is scoped to what the supporting records establish.

`assets/site-finish.css` provides a shared presentation layer. Existing page styles are preserved in `legacy-*.css` files and imported before that layer. The page-specific narratives are not generated or rewritten by JavaScript. Navigation remains visible without JavaScript; the About mascot and extra PDF shortcuts are optional enhancements. The PDF also has a direct static link here and on the 404 page.

## Preview locally

From the repository root, run:

```powershell
python -m http.server 8000 --bind 127.0.0.1
```

Open `http://localhost:8000/`. Inspect the home, resume, three case studies and `/404.html`. A simple Python server does not automatically serve the custom 404 page for arbitrary missing paths; GitHub Pages handles that separately.

## Updating the PDF

`tools/build_public_resume.py` generates `assets/Josh_Escobar_Resume.pdf` with Python and ReportLab. Keep its approved content synchronized with the HTML resume, inspect both rendered pages, and review before committing. The PDF contains selectable text and links; the HTML resume remains the primary accessible version. PDF/UA compliance is not claimed.

Public email, phone and LinkedIn details are not added without explicit approval. Do not commit private company records, credentials, raw logs, employee data or font files. A feature branch in this repository is public, not private storage.
