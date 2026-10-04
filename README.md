# Muhammad Aneeq Khan — Portfolio

Personal portfolio of **Muhammad Aneeq Khan** — UI/UX designer and aspiring cybersecurity & AI-security enthusiast, exploring the meeting point of design, artificial intelligence and security. First-semester student at NUST, Islamabad.

🔗 **Live site:** https://aneeq814.github.io/

---

## What this site is

A responsive, static one-page portfolio built with **vanilla HTML, CSS and JavaScript** — no build step and no external libraries. The visual direction is a dark editorial / security-lab treatment with custom copy and interaction.

| # | Section | Content |
| --- | --- | --- |
| — | **Header** | Fixed nav + status rail |
| 01 | **Hero** | Name, role, short pitch, portrait plate |
| 02 | **About** | *Curiosity at the meeting point of design, intelligence and security* |
| 03 | **Focus** | *Three fields. A strong foundation.* — interactive focus map (node / list driven panel) |
| 04 | **Education** | NUST → Punjab Group of Colleges → Army Public Schools & Colleges System, each with its institution mark |
| 05 | **Contact** | LinkedIn, Instagram and a closing call to action |

## Project structure

```
.
├── index.html          # the site (single file) ← served by GitHub Pages
├── .nojekyll           # serve assets as-is, no Jekyll processing
├── favicon.ico         # logo favicon (16 / 32 / 48 px layers)
├── favicon-32.png      # logo favicon, PNG fallback for browsers that prefer it
├── apple-touch-icon.png  # 180 px home-screen icon (opaque, per Apple guidance)
├── assets/
│   ├── aneeq-portrait.jpg
│   ├── aneeq-mark.jpg
│   ├── pgc-logo.png
│   └── apsacs-logo.jpg
└── previous-design/    # the previous "specimen viewer" build, archived whole
    ├── index.html      # byte-identical to what was live before this change
    ├── src/index.template.html
    ├── build.py
    └── assets/
```

## Preview locally

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Rolling back to the previous design

`previous-design/` holds the earlier "specimen viewer" build, complete and rebuildable:

```bash
cd previous-design
python3 build.py     # regenerates index.html from src/index.template.html + assets/
```

Running its `build.py` reproduces the archived `index.html` byte-for-byte. To restore it site-wide, move those files back to the repository root.

## Published with GitHub Pages

The site is deployed from the `main` branch, root folder (`/`), and serves at **https://aneeq814.github.io/**. To change it, edit `index.html` (or swap files in `assets/`) and push to `main` — Pages redeploys in about a minute.

## Notes on content and assets

- LinkedIn and Instagram links are the URLs supplied by Aneeq.
- The focus map is interactive: select a focus item or a node to change the panel.
- Academic grades, marks and positions reflect the information supplied for the portfolio.
- There is no contact email on the page because none was provided.
- The supplied files did not include a NUST logo, so the education card uses a text-only NUST mark. NUST states that its emblem/signature requires prior written approval for use — if you have an approved asset, drop it in `assets/` and reference it from `index.html`.
- Institution logos belong to their respective institutions and are used for identification purposes only.

## Credits

- Reference fonts shown by CSS stack: **Arial Narrow / Impact** for display type, **Inter** for body copy.
- Site content and design: Muhammad Aneeq Khan.
