#!/usr/bin/env python3
"""Smoke and structural tests for the bilingual Hugo release artifact."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

BASE = Path(sys.argv[1] if len(sys.argv) > 1 else "public").resolve()
LANGS = ("en", "zh")
SECTIONS = ("about", "research", "publications", "preprints", "projects", "notes", "cv", "contact")


class HTMLCheck(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = False
        self.lang = None
        self.links = []
        self.h1 = 0
        self.main = False
        self.css = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "h1":
            self.h1 += 1
        if tag == "main" and a.get("id") == "main":
            self.main = True
        if tag == "title":
            self.title = True
        if tag in {"a", "link", "script", "img"}:
            for key in ("href", "src"):
                if a.get(key):
                    self.links.append(a[key])
        if tag == "link" and "css/site.css" in a.get("href", ""):
            self.css = True


def test():
    expected = [BASE / "index.html", BASE / "css/site.css", BASE / "images/favicon.svg"]
    for lang in LANGS:
        expected.append(BASE / lang / "index.html")
        expected.extend(BASE / lang / section / "index.html" for section in SECTIONS)
    errors = []

    for p in expected:
        if not p.is_file() or p.stat().st_size == 0:
            errors.append(f"missing output: {p.relative_to(BASE)}")

    if errors:
        raise RuntimeError("\n".join(errors))

    html_files = sorted(BASE.rglob("*.html"))
    for p in html_files:
        raw = p.read_text(encoding="utf-8")
        if "{{" in raw or "}}" in raw:
            errors.append(f"unrendered template in {p.relative_to(BASE)}")
        info = HTMLCheck()
        try:
            info.feed(raw)
        except Exception as exc:
            errors.append(f"invalid HTML parse in {p}: {exc}")
            continue

        rel = p.relative_to(BASE).parts
        if rel[0] in LANGS:
            if info.lang != rel[0]:
                errors.append(f"wrong document language for {p.relative_to(BASE)}: {info.lang}")
            if info.h1 != 1:
                errors.append(f"expected one h1 in {p.relative_to(BASE)}, found {info.h1}")
            if not info.main:
                errors.append(f"missing main landmark in {p.relative_to(BASE)}")
            if not info.css:
                errors.append(f"missing stylesheet in {p.relative_to(BASE)}")

        for link in info.links:
            u = urlsplit(link)
            if u.scheme or u.netloc or link.startswith(("#", "mailto:", "tel:", "data:")):
                continue
            target = unquote(u.path)
            if not target:
                continue
            if target.startswith("/"):
                f = BASE / target.lstrip("/")
            else:
                f = p.parent / target
            if f.is_dir():
                f = f / "index.html"
            elif f.suffix == "":
                f = f / "index.html"
            if not f.exists():
                errors.append(f"broken internal URL: {p.relative_to(BASE)} → {link}")

    if errors:
        raise RuntimeError("\n".join(errors[:100]))
    print(f"PASS: {len(html_files)} HTML pages validated, {len(expected)} required assets and routes present")
    print("PASS: bilingual navigation, page structure and internal links")


if __name__ == "__main__":
    test()
