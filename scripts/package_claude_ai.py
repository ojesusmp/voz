#!/usr/bin/env python3
"""Build the zip that claude.ai (and the Claude desktop app) accepts as a custom skill.

claude.ai wants a zip with ONE top-level folder that holds SKILL.md:

    voz.zip
    └── voz/
        ├── SKILL.md
        ├── LICENSE
        └── references/*.md

Scripts and tests stay out. The SessionStart hook and the CLAUDE.md wiring are Claude
Code mechanics and mean nothing inside a chat, and the tests are for this repo.

    python scripts/package_claude_ai.py            # writes dist/voz.zip
    python scripts/package_claude_ai.py --out /tmp/voz.zip
"""
import argparse
import pathlib
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
INCLUDE = ['SKILL.md', 'LICENSE']
REFERENCES = 'references'


def build(out: pathlib.Path) -> list:
    out.parent.mkdir(parents=True, exist_ok=True)
    members = []
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for name in INCLUDE:
            src = ROOT / name
            if not src.is_file():
                sys.exit("missing %s" % src)
            z.write(src, 'voz/%s' % name)
            members.append('voz/%s' % name)
        for src in sorted((ROOT / REFERENCES).glob('*.md')):
            arc = 'voz/%s/%s' % (REFERENCES, src.name)
            z.write(src, arc)
            members.append(arc)
    return members


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=str(ROOT / 'dist' / 'voz.zip'))
    args = ap.parse_args()
    out = pathlib.Path(args.out)
    members = build(out)
    print("wrote %s (%d files, %d bytes)" % (out, len(members), out.stat().st_size))
    for m in members:
        print("  " + m)
    print("\nUpload it in claude.ai: Settings > Capabilities > Skills > Upload skill.")


if __name__ == '__main__':
    main()
