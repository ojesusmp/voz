#!/usr/bin/env python3
"""voz SessionStart hook.

Prints a short reminder that makes Claude write like a human by default. It runs
every session and stays lightweight on purpose: the full skill (the tell catalog
and the nine register profiles) loads on demand from ~/.claude/skills/voz/SKILL.md
only when there is real writing to do, so this does not tax pure-code sessions.
"""
import json

CONTEXT = (
    "[VOZ ACTIVE - write like a human] Default voice for ALL prose (docs, READMEs, "
    "emails, chat, copy, commit messages): empathetic, plain, confident, specific, "
    "varied rhythm. Kill AI-writing tells - avoid the word-cluster (delve, tapestry, "
    "underscore, boasts, robust, seamless, leverage, showcase, crucial), the "
    "rule-of-three, not-X-but-Y negative parallelism, inflated serves-as-a copulas, "
    "bold-label bullet spam, emoji headers, and em dashes (use commas/colons/parentheses). "
    "Probabilities not laws - judge the cluster, keep a word when it is genuinely most "
    "precise. Switch register only on request: salesman, corporate, lawyer, journalist, "
    "marketing, technical, teacher, motivational. Full skill plus 9 register profiles plus "
    "sourced tell catalog at ~/.claude/skills/voz/SKILL.md - load before substantial "
    "writing. Not a detector; never used to accuse text."
)

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": CONTEXT,
    }
}))
