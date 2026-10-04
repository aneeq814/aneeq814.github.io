# Muhammad Aneeq Khan — Portfolio

Personal portfolio of **Muhammad Aneeq Khan** — UI/UX Designer and aspiring Cybersecurity & AI Security enthusiast, working at the intersection of Artificial Intelligence and the cyber world.

🔗 **Live site:** https://aneeq814.github.io/

---

## Design language — "Specimen Viewer"

A classified-lab / dissection-file interface, in the spirit of interactive creative-developer portfolios:

- Near-black canvas (`#0a0907`) with acid-lime (`#D4FF00`), magenta (`#FF2E88`) and wireframe blue (`#2F45FF`) data accents
- **Inter 24pt** display type (open-source, self-hosted) — heavy uppercase headlines with italic lime emphasis
- HUD chrome: file header, live clock, hazard-class readout, vertical data rails, 7-number section navigation
- Hazard tape dividers, notched instrument panels, corner ticks, barcode blocks, scanlines and grid
- A **boot gate** that "initialises the subject viewer", an SVG wireframe specimen figure, and an interactive capability mesh with probe readouts

## Sections

| # | Section | Content |
| --- | --- | --- |
| 01 | **Specimen** | Name/occupation tags, `UI/UX DESIGNER` display headline, threat level, wireframe specimen figure, portrait plate, live vitals telemetry, skill ticker |
| 02 | **Manifest** | *"complexity is not a feature"* with strike-through; operator notes; prime directive card; observed traits |
| 03 | **Data analysis** | Six interactive capability probes (click/keyboard) with a live readout panel |
| 04 | **Intake records** | NUST (present) → Punjab Group of Colleges (A+, 1143/1200, 7th Lahore Board) → Army Public School for Boys, Sarfaraz Rafiqui Road (A++, 1063/1100, 17th Federal Board) |
| 05 | **Telemetry** | Animated score counters and merit markers |
| 06 | **Subject report** | Behavioural notes and five operating protocols |
| 07 | **Contact** | Channels, message form that copies itself and opens LinkedIn, sign-off |

## Highlights

- **Self-contained single file** — images *and* fonts inlined as data URIs: instant load, exact typography everywhere, works offline.
- **Responsive** — verified from 390 px phones to 1440 px+ desktops; horizontal rails hide gracefully on small screens.
- **Accessible** — keyboard-operable probes, ARIA labels, visible focus, `prefers-reduced-motion` support, Esc skips the boot gate.
- **No dependencies** — no frameworks, no CDNs, no tracking, no external requests.

## Project structure

```
.
├── index.html                 # the site (self-contained) ← served by GitHub Pages
├── src/index.template.html    # editable source (references assets/ normally)
├── build.py                   # inlines images + fonts into index.html
└── assets/
    ├── avatar.jpg             # portrait
    ├── nust-logo.png          # NUST
    ├── pgc-logo.png           # Punjab Group of Colleges
    ├── apsacs-logo.png        # Army Public Schools & Colleges System
    └── fonts/                 # Inter (woff2, latin, roman + italic)
```

### Editing the site

1. Edit `src/index.template.html`, or drop new images into `assets/`.
2. Rebuild: `python3 build.py`
3. Commit and push — GitHub Pages redeploys in about a minute.

## Credits

- Typeface: **Inter** (Rasmus Andersson), SIL Open Font License.
- Logos of NUST, Punjab Group of Colleges and Army Public Schools & Colleges System belong to their respective institutions and are used for identification purposes only.
