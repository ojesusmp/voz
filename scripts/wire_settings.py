#!/usr/bin/env python3
"""Wire voz to run by default, every session. Idempotent and safe to re-run.

It does two things and nothing else:
  1. Appends a voz pointer to ~/.claude/CLAUDE.md (skips if already there).
  2. Adds a lightweight SessionStart hook to ~/.claude/settings.json that calls
     voz_sessionstart.py (skips if a voz hook is already present).

It never edits, reorders, or removes anything else in your config. If
settings.json is not valid JSON, it leaves the file untouched and tells you.

Usage:
    python wire_settings.py [--python python3]

--python is the interpreter name the hook should call at session start
(defaults to "python"; pass "python3" on most macOS/Linux systems).
"""
import argparse
import json
import os
import sys

HOME = os.path.expanduser("~")
CLAUDE_DIR = os.path.join(HOME, ".claude")
SETTINGS = os.path.join(CLAUDE_DIR, "settings.json")
CLAUDE_MD = os.path.join(CLAUDE_DIR, "CLAUDE.md")
HOOK_SCRIPT = os.path.join(
    CLAUDE_DIR, "skills", "voz", "scripts", "voz_sessionstart.py"
).replace("\\", "/")

POINTER_MARKER = "# voz (ALWAYS-ON for writing"
POINTER = """
# voz (ALWAYS-ON for writing, write like a human)
- **voz** (`~/.claude/skills/voz/SKILL.md`) is the default voice for ALL prose a person reads (docs, READMEs, emails, chat, landing copy, commit messages): empathetic, plain, confident, specific, with varied rhythm. Kill AI-writing tells: the word-cluster (delve, tapestry, underscore, boasts, robust, seamless, leverage, showcase, crucial), the rule-of-three, "not X but Y" negative parallelism, inflated "serves as a" copulas, bold-label bullet spam, emoji headers, and em dashes (use commas, colons, parentheses). These are probabilities not laws, so judge the cluster and keep a word when it is genuinely the most precise. Switch register only when the task or user asks: salesman, corporate, lawyer, journalist, marketing, technical, teacher, motivational. Load the full SKILL.md before any substantial writing. It is writing guidance, never a detector for accusing text.
"""


def wire_pointer():
    existing = ""
    if os.path.exists(CLAUDE_MD):
        with open(CLAUDE_MD, encoding="utf-8") as f:
            existing = f.read()
    if POINTER_MARKER in existing or "skills/voz/SKILL.md" in existing:
        print("  CLAUDE.md: voz pointer already present, skipped")
        return
    with open(CLAUDE_MD, "a", encoding="utf-8") as f:
        f.write(POINTER)
    print("  CLAUDE.md: voz pointer added")


def _has_voz_hook(entry):
    if not isinstance(entry, dict):
        return False
    for h in entry.get("hooks", []):
        cmd = (h or {}).get("command", "")
        if "voz_sessionstart" in cmd or "[VOZ ACTIVE" in cmd:
            return True
    return False


def wire_hook(python_cmd):
    if os.path.exists(SETTINGS):
        try:
            with open(SETTINGS, encoding="utf-8") as f:
                cfg = json.load(f)
        except (ValueError, OSError) as e:
            print(
                f"  settings.json is not valid JSON ({e}); left untouched. "
                f"Add the hook manually: {python_cmd} \"{HOOK_SCRIPT}\"",
                file=sys.stderr,
            )
            return
    else:
        cfg = {}

    hooks = cfg.setdefault("hooks", {})
    session_start = hooks.setdefault("SessionStart", [])
    if any(_has_voz_hook(e) for e in session_start):
        print("  settings.json: voz SessionStart hook already present, skipped")
        return

    session_start.append({
        "hooks": [
            {"type": "command", "command": f'{python_cmd} "{HOOK_SCRIPT}"'}
        ]
    })
    with open(SETTINGS, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)
        f.write("\n")
    print("  settings.json: voz SessionStart hook added")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--python", default="python",
                    help="interpreter the hook should call (e.g. python3)")
    args = ap.parse_args()
    os.makedirs(CLAUDE_DIR, exist_ok=True)
    print("Wiring voz always-on:")
    wire_pointer()
    wire_hook(args.python)
    print("Done. Reload your editor or start a new Claude Code session.")


if __name__ == "__main__":
    main()
