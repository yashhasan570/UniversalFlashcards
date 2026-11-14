#!/usr/bin/env python3
"""Re-apply the Universal Flashcards rebrand after each upstream sync (idempotent).

Protected anchors (kept intact on every run):
- LICENSE (AGPL, untouched)
- ankiweb.net domains (sync/account/media service endpoints)
- ankihub / AnkiHub (third-party addon service)
- AnkiDroid / AnkiMobile (other official clients, sync protocol compat)
- .github/ and scripts/ are excluded from the sweep entirely
"""
from pathlib import Path
import re, shutil

SKIP_EXT = {".png",".jpg",".jpeg",".ico",".webp",".woff",".woff2",".ttf",".eot",".otf",".gif",".pdf",".gz",".zip",".mp4"}
KEEP = {"LICENSE", "migrate.py"}
DELETE = ["docs-site", "docs", "SECURITY.md", "AGENTS.md", "CLAUDE.md", "CONTRIBUTORS",
          ".github/FUNDING.yml", ".github/ISSUE_TEMPLATE", ".github/PULL_REQUEST_TEMPLATE"]


def sweep(t):
    t = t.replace("ankitects/anki", "yashhasan570/UniversalFlashcards")
    t = t.replace("ankitects", "yashhasan570")
    t = t.replace("net.ankiweb.dtop", "net.universalflashcards.dtop")
    t = t.replace("ANKI_", "UNIVERSALFLASHCARDS_")
    t = re.sub(r"ankiweb\.net", "__AWNET__", t)
    t = re.sub(r"ankihub", "__AHUB__", t, flags=re.I)
    t = re.sub(r"AnkiDroid", "__ADROID__", t)
    t = re.sub(r"AnkiMobile", "__AMOB__", t)
    t = re.sub(r"ankidroid", "__adroid__", t)
    t = re.sub(r"ankimobile", "__amob__", t)
    t = re.sub(r"Anki(?=[A-Za-z])", "UniversalFlashcards", t)
    t = re.sub(r"ANKI", "UNIVERSALFLASHCARDS", t)
    t = re.sub(r"anki(?=[A-Za-z0-9])", "universalflashcards", t)
    t = re.sub(r"\bAnki\b", "Universal Flashcards", t)
    t = re.sub(r"\banki\b", "universalflashcards", t)
    t = t.replace("__AWNET__", "ankiweb.net").replace("__AHUB__", "ankihub").replace("__ADROID__", "AnkiDroid").replace("__AMOB__", "AnkiMobile").replace("__adroid__", "ankidroid").replace("__amob__", "ankimobile")
    return t


def display(t):
    return t.replace("UniversalFlashcards", "Universal Flashcards")


def main():
    for d in DELETE:
        p = Path(d)
        if p.is_dir():
            shutil.rmtree(p, ignore_errors=True)
        elif p.exists():
            p.unlink()
    for p in Path(".").rglob("*"):
        if ".git" in p.parts or not p.is_file() or p.name in KEEP or p.suffix in SKIP_EXT or "ankihub" in p.name.lower():
            continue
        if str(p).startswith((".github/", "scripts/")):
            continue
        try:
            t = p.read_text()
        except Exception:
            continue
        nt = sweep(t)
        if p.suffix in (".ftl", ".md", ".html"):
            nt = display(nt)
        if nt != t:
            p.write_text(nt)
    for p in list(Path(".").rglob("*anki*")) + list(Path(".").rglob("*Anki*")):
        if ".git" in p.parts or p.is_dir() or "ankihub" in p.name.lower():
            continue
        nb = re.sub(r"anki", "universalflashcards", p.name)
        nb = re.sub(r"Anki", "UniversalFlashcards", nb)
        if nb != p.name:
            p.rename(p.with_name(nb))
    readme = Path("README.md")
    if readme.exists() and not readme.read_text().startswith("# Universal Flashcards"):
        print("README drifted - rewrite needed")
    print("migrate done")


if __name__ == "__main__":
    main()
