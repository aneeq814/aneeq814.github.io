# Muhammad Aneeq Khan — Portfolio

Personal portfolio of **Muhammad Aneeq Khan** — UI/UX Designer and aspiring Cybersecurity & AI Security enthusiast, working on the integration of Artificial Intelligence with the cyber world. First-semester student at NUST, Islamabad.

🔗 **Live site:** https://aneeq814.github.io/

---

## Design language — "Specimen Viewer"

An interactive **classified lab / dissection file** concept: the visitor inspects the subject rather than reading a résumé.

- **Near-black canvas** (`#0a0907`) with warm off-white type, **acid lime** (`#D4FF00`) for live data and **magenta** (`#FF2E88`) for hazard/warnings
- **Inter Black** display type in tight uppercase — Inter is open-licensed (SIL OFL) and embedded in the page
- **Instrument chrome:** hazard-tape bands, corner-notched panels, HUD bars top and bottom, vertical rail captions, live date/time stamp
- **Boot gate:** an inspection console that types its startup log, then hands over on click (Esc or a 6-second timer also skips it)
- **Working "specimen" wireframe** in the hero — a hand-built SVG neural map in blueprint blue with magenta hazard spikes and a pulsing core
- **Interactive capability probes:** click (or keyboard-tab to) any of the seven nodes to load its readout — code, title, description, stack, signal strength and status. The inline mobile list drives the same readout.

## Sections

| # | Section | Content |
| --- | --- | --- |
| 01 | **Specimen** | Name tags, `UI/UX DESIGNER` display type, availability status, neural-map figure, live portrait plate, vitals telemetry with animated bars and ECG trace, capability ticker |
| 02 | **Manifest** | *"Complexity is not a feature."* with strike-through animation, operator notes, prime directive card, four observed traits |
| 03 | **Data analysis** | Six capability probes + a "how I operate" note with barcode |
| 04 | **Intake records** | NUST (present) → Punjab Group of Colleges (A+, 1143/1200, 7th in Lahore Board) → Army Public School for Boys, Sarfaraz Rafiqui Road (A++, 1063/1100, 17th in Federal Board) — each with its institution logo |
| 05 | **Telemetry** | Animated marks: 1063/1100, 17th FBISE, 1143/1200, 7th BISE Lahore + merit markers |
| 06 | **Subject report** | Behavioural notes and five operating protocols |
| 07 | **Contact** | Channels, transmission form (copies your message and opens LinkedIn), sign-off |

## Verified

- **0 broken images**, **0 JavaScript errors**, **0 horizontal overflow** at 390 px and 1440 px
- Responsive: floating probes on desktop, tappable probe list on phones, compact HUD bars under 820 px
- Accessibility: semantic headings, ARIA labels, visible focus rings, `prefers-reduced-motion` support (boot gate skips, reveals resolve instantly)
- Rebuilds in ~0.2 s with `python3 build.py`

## Project structure

```
.
├── index.html                 # the site (self-contained) ← served by GitHub Pages
├── src/index.template.html    # editable source
├── build.py                   # inlines images + fonts into index.html
└── assets/
    ├── avatar.jpg             # portrait plate
    ├── nust-logo.png
    ├── pgc-logo.png           # Punjab Group of Colleges (supplied file)
    ├── apsacs-logo.png        # Army Public Schools & Colleges System (supplied file)
    └── fonts/                 # Inter woff2 — regular + italic
```

### Editing the site

1. Edit `src/index.template.html` (or drop new images into `assets/`).
2. Rebuild:

```bash
python3 build.py
```

3. Commit and push — GitHub Pages redeploys in about a minute.

## Credits

- Typeface: **Inter** by Rasmus Andersson, used under the SIL Open Font License.
- Logos of NUST, Punjab Group of Colleges and Army Public Schools & Colleges System belong to their respective institutions and are used for identification purposes only.
