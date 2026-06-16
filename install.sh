#!/usr/bin/env bash
# voz installer (macOS / Linux).
# Installs the voz skill into ~/.claude/skills/voz, which both the Claude Code CLI
# and the VSCode extension read.
#
#   bash install.sh              install the skill only (invoke it when you want it)
#   bash install.sh --always-on  also wire the global CLAUDE.md pointer + SessionStart
#                                hook so the default voice applies every session
#
# Idempotent: safe to re-run. The --always-on wiring needs Python on your PATH.
set -euo pipefail

REPO="https://github.com/ojesusmp/voz.git"
ALWAYS_ON=0
for arg in "$@"; do
  case "$arg" in
    --always-on) ALWAYS_ON=1 ;;
    -h|--help) echo "Usage: bash install.sh [--always-on]"; exit 0 ;;
    *) echo "Unknown option: $arg" >&2; exit 1 ;;
  esac
done

CLAUDE_DIR="$HOME/.claude"
DEST="$CLAUDE_DIR/skills/voz"

# Resolve the source: the repo this script sits in, or a fresh shallow clone.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLONED=""
if [ -f "$SCRIPT_DIR/SKILL.md" ]; then
  SRC="$SCRIPT_DIR"
else
  CLONED="$(mktemp -d)"
  echo "Cloning voz from $REPO ..."
  git clone --depth 1 "$REPO" "$CLONED" >/dev/null 2>&1
  [ -f "$CLONED/SKILL.md" ] || { echo "Clone failed: SKILL.md not found" >&2; exit 1; }
  SRC="$CLONED"
fi

# Copy the skill files.
mkdir -p "$DEST/references" "$DEST/scripts"
cp "$SRC/SKILL.md" "$SRC/README.md" "$SRC/LICENSE" "$DEST/"
cp "$SRC"/references/* "$DEST/references/"
cp "$SRC"/scripts/* "$DEST/scripts/"
echo "voz skill installed to $DEST"

# Optional always-on wiring.
if [ "$ALWAYS_ON" = "1" ]; then
  if command -v python3 >/dev/null 2>&1; then PY=python3
  elif command -v python >/dev/null 2>&1; then PY=python
  else PY=""; fi
  if [ -z "$PY" ]; then
    echo "python not found on PATH; skipping always-on wiring. Install Python, then re-run with --always-on." >&2
  else
    "$PY" "$DEST/scripts/wire_settings.py" --python "$PY"
  fi
fi

[ -n "$CLONED" ] && rm -rf "$CLONED"
echo "Done. Reload VSCode (Developer: Reload Window) or start a new Claude Code session."
