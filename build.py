#!/usr/bin/env python3
"""
Build step for Muhammad Aneeq Khan's portfolio.

Takes src/index.template.html and inlines every image from assets/ as a base64
data URI, producing a single self-contained index.html.

Why? A one-file site loads instantly, needs zero configuration on GitHub Pages,
works when opened straight from your file system (no server needed), and never
shows a broken image if someone moves the folder around.

Usage:  python3 build.py
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
TEMPLATE = ROOT / "src" / "index.template.html"
OUTPUT = ROOT / "index.html"
MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".svg": "image/svg+xml", ".webp": "image/webp"}


def to_data_uri(path: pathlib.Path) -> str:
    mime = MIME.get(path.suffix.lower(), "application/octet-stream")
    payload = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{payload}"


def main() -> None:
    html = TEMPLATE.read_text(encoding="utf-8")
    missing = []

    def replace(match: re.Match) -> str:
        rel = match.group(1)
        asset = ROOT / rel
        if not asset.exists():
            missing.append(rel)
            return match.group(0)
        return 'src="' + to_data_uri(asset) + '"'

    html = re.sub(r'src="(assets/[^"]+)"', replace, html)
    OUTPUT.write_text(html, encoding="utf-8")

    kb = OUTPUT.stat().st_size / 1024
    print(f"✓ built {OUTPUT.relative_to(ROOT)} ({kb:.0f} KB)")
    if missing:
        print("! missing assets:", ", ".join(missing))


if __name__ == "__main__":
    main()
