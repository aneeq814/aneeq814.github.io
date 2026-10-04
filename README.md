# Muhammad Aneeq Khan — Portfolio

Personal portfolio of **Muhammad Aneeq Khan** — UI/UX Designer and aspiring Cybersecurity & AI Security enthusiast, currently exploring the integration of Artificial Intelligence with the cyber world.

🔗 **Live site:** https://aneeq814.github.io/

---

## Design language

An editorial, high-contrast system inspired by contemporary design-studio portfolios:

- **Near-black canvas** (`#101010`) with **warm off-white** type (`#EDEBE6`)
- **Violet accent** (`#B481F8`) used in full-bleed blocks — never lilac-on-lilac
- **Editorial uppercase display** with tight tracking, plus uppercase micro-labels (`letter-spacing: .34em`)
- **Circle geometry** — orbit rings, node map, outline circle + disc motifs, coordinates readout
- **Full-bleed sections that invert** (violet / paper / black), with the fixed chrome re-theming itself to stay legible

## Sections

| Section | Content |
| --- | --- |
| **Hero** | Full-bleed monochrome portrait, oversized name, graphic ring composition, parallax on pointer move |
| **Manifest** | *"complexity is not a feature."* on a violet field — principles, bio, strike-through animation, giant closer line |
| **Capabilities** | Interactive orbit/node map (tilts in 3D toward the cursor) + how-I-work card + six capability rows |
| **Journey** | NUST (present) → Punjab Group of Colleges (A+, 1143/1200, 7th in Lahore Board) → Army Public School for Boys, Sarfaraz Rafiqui Road (A++, 1063/1100, 17th in Federal Board) |
| **Numbers** | Vivid violet stat grid with animated counters and lift-on-hover 3D tiles |
| **Contact** | Social rows, message form that copies itself and opens LinkedIn, coordinates sign-off |

## Highlights

- **Self-contained single file** — images *and* the webfont are inlined as data URIs, so it loads instantly, keeps its exact typography everywhere, and works offline or from a local folder.
- **Responsive** — verified from 390 px phones up to 1440 px desktops, with a full-screen mobile menu.
- **Accessible** — semantic headings, ARIA labels, visible focus rings, `prefers-reduced-motion` support.
- **No dependencies** — no frameworks, no CDNs, no tracking.

## Project structure

```
.
├── index.html                 # the site (self-contained) ← served by GitHub Pages
├── src/index.template.html    # editable source (references assets/ normally)
├── build.py                   # inlines assets + fonts into index.html
└── assets/
    ├── avatar.jpg             # portrait
    ├── nust-logo.png          # NUST
    ├── pgc-logo.png           # Punjab Group of Colleges
    ├── apsacs-logo.png        # Army Public Schools & Colleges System
    └── fonts/                 # Space Grotesk (woff2, latin + latin-ext)
```

### Editing the site

1. Edit `src/index.template.html` (or drop new images into `assets/`).
2. Rebuild the deployable file:

```bash
python3 build.py
```

3. Commit and push — GitHub Pages redeploys automatically in about a minute.

## Credits

- Typeface: **Space Grotesk** (Florian Karsten), used under the SIL Open Font License.
- Logos of NUST, Punjab Group of Colleges and Army Public Schools & Colleges System belong to their respective institutions and are used here for identification purposes only.
