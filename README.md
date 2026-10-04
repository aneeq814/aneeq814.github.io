# Muhammad Aneeq Khan — Portfolio

Personal portfolio of **Muhammad Aneeq Khan** — UI/UX Designer and aspiring Cybersecurity & AI Security enthusiast, currently exploring the integration of Artificial Intelligence with the cyber world.

🔗 **Live site:** https://aneeq814.github.io/

---

## What's inside

| Section | Content |
| --- | --- |
| **Hero** | Name, roles, 3D portrait card with floating skill chips and NUST badge |
| **About** | Who I am, what I'm working on, how I like to work |
| **Expertise** | UI/UX Design · Design Systems · AI × Security · Security Fundamentals · Python & Tooling · Problem Solving |
| **Journey** | NUST (present) → Punjab Group of Colleges (A+, 1143/1200, 7th in Lahore Board) → Army Public School for Boys, Sarfaraz Rafiqui Road (A++, 1063/1100, 17th in Federal Board) |
| **Achievements** | Animated counters and merit-position highlights |
| **Contact** | LinkedIn, Instagram, GitHub and a message form that hands off to LinkedIn |

## Highlights

- **Clean, professional theme** — deep-space navy with mint / indigo accents.
- **3D touches** — mouse-tracking tilt on the portrait, floating glass chips, parallax grid, card lift on hover.
- **Fully responsive** — tested from 390 px phones up to 1440 px desktops.
- **Accessible** — keyboard focus rings, `prefers-reduced-motion` support, semantic headings, ARIA labels.
- **Single self-contained file** — every image is inlined as a data URI, so the site loads instantly, needs no build step on GitHub Pages, and works even when opened straight from a folder.

## Project structure

```
.
├── index.html                 # the site (self-contained, images inlined) ← served by GitHub Pages
├── src/index.template.html    # editable source (references assets/ normally)
├── build.py                   # inlines assets/* into index.html
└── assets/                    # portrait + institution logos
```

### Editing the site

1. Edit `src/index.template.html` (or drop new images into `assets/`).
2. Rebuild the deployable file:

```bash
python3 build.py
```

3. Commit and push — GitHub Pages serves `index.html` from the `main` branch.

## Credits

Logos of NUST, Punjab Group of Colleges and Army Public Schools & Colleges System belong to their respective institutions and are used here for identification/educational purposes only.
