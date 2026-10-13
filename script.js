/* greycarpet: optional enhancements. Content and navigation work without JS. */
(() => {
  const scriptUrl = document.currentScript?.src;
  const siteRoot = scriptUrl ? new URL('.', scriptUrl) : new URL('/', document.baseURI);
  const menu = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#site-nav');
  const year = document.querySelector('#year');
  if (year) year.textContent = String(new Date().getFullYear());

  if (menu && nav) {
    const setOpen = (open) => {
      menu.setAttribute('aria-expanded', String(open));
      menu.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
      nav.classList.toggle('is-open', open);
    };
    menu.addEventListener('click', () => setOpen(menu.getAttribute('aria-expanded') !== 'true'));
    nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setOpen(false)));
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        menu.focus();
      }
    });
    document.addEventListener('click', (event) => {
      if (event.target instanceof Node && !nav.contains(event.target) && !menu.contains(event.target)) setOpen(false);
    });
    const desktop = window.matchMedia('(min-width: 681px)');
    const resized = () => { if (desktop.matches) setOpen(false); };
    if (desktop.addEventListener) desktop.addEventListener('change', resized);
    else desktop.addListener(resized);
    nav.classList.add('gc-nav-ready');
    menu.classList.add('gc-nav-ready');
    setOpen(false);
  }

  // Expand source notes before jumping to a citation inside a closed <details>.
  const revealFragment = () => {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    if (!id) return;
    const target = document.getElementById(id);
    if (!target) return;
    let changed = false;
    for (let parent = target.parentElement; parent; parent = parent.parentElement) {
      if (parent.tagName === 'DETAILS' && !parent.open) { parent.open = true; changed = true; }
    }
    if (changed) requestAnimationFrame(() => target.scrollIntoView({ block: 'start', behavior: 'auto' }));
  };
  window.addEventListener('hashchange', revealFragment);
  revealFragment();

  // Optional presentation enhancements; the original HTML remains the no-JS fallback.
  const about = document.querySelector('.about-section');
  const oldGraphic = about?.querySelector('.about-visual');
  if (about && oldGraphic) {
    const card = document.createElement('aside');
    card.className = 'gc-identity';
    const image = document.createElement('img');
    image.src = new URL('assets/greycarpet-mascot.webp', siteRoot).href;
    image.alt = 'Gray rolled-carpet creature, the greycarpet mascot.';
    image.width = 160; image.height = 160;
    image.loading = 'lazy'; image.decoding = 'async';
    const text = document.createElement('div');
    const name = document.createElement('strong'); name.textContent = 'greycarpet';
    const caption = document.createElement('p');
    caption.textContent = 'My technical moniker. A little character behind the engineering.';
    text.append(name, caption); card.append(image, text);
    oldGraphic.replaceWith(card); about.classList.add('gc-has-mascot');
  }
  const createDownload = () => {
    const link = document.createElement('a');
    link.className = 'gc-download';
    link.href = new URL('assets/Josh_Escobar_Resume.pdf', siteRoot).href;
    link.download = 'Josh_Escobar_Resume.pdf';
    link.dataset.resumeDownload = '';
    link.textContent = 'Download resume (PDF)';
    return link;
  };
  const resumeTools = document.querySelector('.resume-tools');
  if (resumeTools && !resumeTools.querySelector('[data-resume-download]')) {
    resumeTools.prepend(createDownload());
    const note = resumeTools.querySelector('.resume-note');
    if (note) note.textContent = 'Download the two-page public resume, or use the browser print option for this page.';
    const printButton = resumeTools.querySelector('#print-resume');
    if (printButton) printButton.textContent = 'Print this page';
  }
  const contactCopy = document.querySelector('.contact-copy');
  if (contactCopy && !contactCopy.querySelector('[data-resume-download]')) {
    const actions = document.createElement('div'); actions.className = 'gc-connect-actions';
    actions.append(createDownload()); contactCopy.append(actions);
  }
  document.querySelectorAll('.about-visual-label, .contact-decoration span, .resume-intro .eyebrow').forEach((label) => {
    if (label.textContent.includes('GREYCARPET')) label.textContent = label.textContent.replaceAll('GREYCARPET', 'greycarpet');
  });
  const diagramLabel = document.querySelector('.diagram-live');
  if (diagramLabel) diagramLabel.textContent = 'CONCEPT DIAGRAM';

  // Direct download is also available from the static 404 page and repository README.
  const footerLinks = document.querySelector('.footer-inner > div:last-child');
  if (footerLinks && !footerLinks.querySelector('[data-resume-download]')) {
    const link = document.createElement('a');
    link.href = new URL('assets/Josh_Escobar_Resume.pdf', siteRoot).href;
    link.download = 'Josh_Escobar_Resume.pdf';
    link.dataset.resumeDownload = '';
    link.textContent = 'Resume PDF';
    footerLinks.prepend(link);
  }
})();
