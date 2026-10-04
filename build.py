#!/usr/bin/env python3
"""
Build step for Muhammad Aneeq Khan's portfolio.

Takes src/index.template.html and inlines every asset — images AND the
self-hosted webfonts — as base64 data URIs, producing a single self-contained
index.html.

Why? A one-file site loads instantly, needs zero configuration on GitHub Pages,
works when opened straight from your file system (no server needed), never
falls back to a different font on someone else's machine, and never shows a
broken image if the folder gets moved around.

Usage:  python3 build.py
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
TEMPLATE = ROOT / "src" / "index.template.html"
OUTPUT = ROOT / "index.html"

MIME = {
    ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
    ".svg": "image/svg+xml", ".webp": "image/webp",
    ".woff2": "font/woff2", ".woff": "font/woff",
}
FONTS = {
    "__FONT_LATIN__": "assets/fonts/sg-latin.woff2",
    "__FONT_LATIN_EXT__": "assets/fonts/sg-latin-ext.woff2",
}


def data_uri(path: pathlib.Path) -> str:
    mime = MIME.get(path.suffix.lower(), "application/octet-stream")
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def main() -> None:
    html = TEMPLATE.read_text(encoding="utf-8")
    missing = []

    # 1. images:  src="assets/whatever.png"
    def sub_img(match: re.Match) -> str:
        rel = match.group(1)
        asset = ROOT / rel
        if not asset.exists():
            missing.append(rel)
            return match.group(0)
        return 'src="' + data_uri(asset) + '"'

    html = re.sub(r'src="(assets/[^"]+)"', sub_img, html)

    # 2. fonts:  url(__FONT_LATIN__)
    for token, rel in FONTS.items():
        asset = ROOT / rel
        if asset.exists():
            html = html.replace(token, data_uri(asset))
        else:
            missing.append(rel)
            html = html.replace(token, rel)

    OUTPUT.write_text(html, encoding="utf-8")
    print(f"✓ built {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size / 1024:.0f} KB)")
    if missing:
        print("! missing assets:", ", ".join(missing))


if __name__ == "__main__":
    main()
