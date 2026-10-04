# Muhammad Aneeq Khan — Portfolio

A responsive, static one-page portfolio made with vanilla HTML, CSS, and JavaScript. No build step or external libraries are required. The visual direction is an original, dark editorial/security-lab treatment based on the reference's cinematic feel, with custom copy and interaction for Aneeq.

## Preview locally

From this folder, run:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Publish with GitHub Pages

1. Put `index.html`, `.nojekyll`, and the `assets/` folder in the root of the GitHub repository.
2. In the repository, open **Settings → Pages**.
3. Under **Build and deployment**, select **Deploy from a branch**, choose `main` and `/ (root)`, then save.
4. GitHub Pages will show the published URL in that settings page.

This is a static portfolio and can also be hosted by Netlify or Vercel without a build command.

## Included assets

- `assets/aneeq-portrait.jpg` — supplied portrait
- `assets/aneeq-mark.jpg` — supplied Aneeq emblem
- `assets/pgc-logo.png` — supplied Punjab Group of Colleges logo
- `assets/apsacs-logo.jpg` — supplied APSACS logo

The supplied files did not include a NUST logo, so the education card uses a text-only NUST mark for now. The official NUST brand page states that its emblem/signature requires prior written approval for use. If you have an approved logo asset, replace the text-only mark in `index.html` with it.

## Content notes

- LinkedIn and Instagram links are set to the URLs supplied by Aneeq.
- The focus map is interactive; select a focus item or node to change the panel.
- Academic grades, marks, and positions are based on the information supplied for the portfolio.
- There is no contact email on the page because none was provided.
