#!/usr/bin/env python3
"""Deterministic lint for text that voz produced (an email, a message, a batch of UI strings).

It reports the mechanical half of the kill-list in audit-mode shape:

    pattern | the offending line | the fix in a few words

and exits 1 if anything was found. No model in the loop. It reads the kill-list words and
phrases from SKILL.md so this file cannot drift from the skill.

    python tests/lint-output.py draft.md [more files]
    python tests/lint-output.py --ui strings.md     # also apply the UI-string rules
    python tests/lint-output.py --es-pr correo.md   # also flag Spanish that is not Puerto Rican

Do not run it on voz's own files: they quote every word they ban, and quoting is not using.
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = (ROOT / 'SKILL.md').read_text(encoding='utf-8')


def kill_words():
    m = re.search(r'(?s)not measured\.\s*(delve,.*?)The tell is density', SKILL)
    words = []
    for w in re.split(r',\s*', m.group(1)):
        w = re.sub(r'\(.*?\)', '', w).strip(' .:*"“”').lower()
        if len(w) > 3:
            words.append(w)
    return words


def kill_phrases():
    m = re.search(r'(?s)\*\*Phrases to drop:\*\*(.*?)\n\n', SKILL)
    return [p.lower() for p in re.findall(r'"([^"]+)"', m.group(1))]


PROSE_PATTERNS = [
    ('em dash', re.compile('—'), 'comma, colon, parentheses, or two sentences'),
    ('negative parallelism', re.compile(r"(?i)\b(it'?s|this is|that'?s) not (just |only |about )?[^.]{1,60}[.,;] (it'?s|this is|that'?s)\b"), 'say the second half'),
    ('not just X but Y', re.compile(r'(?i)\bnot (just|only|merely) \b[^.]{1,60}\bbut (also )?\b'), 'state Y'),
    ('recap ending', re.compile(r'(?im)^\s*(in conclusion|ultimately|overall|in summary|to sum up)\b'), 'end on the last concrete point'),
    ('self-narration', re.compile(r'(?i)\b(certainly!|great question|i hope this helps|let me break this down|happy to help!)'), 'delete'),
    ('announced empathy', re.compile(r"(?i)\bi (completely|totally|fully) understand\b"), 'name their situation instead'),
    ('weasel attribution', re.compile(r'(?i)\b(experts agree|studies show|many argue|widely regarded|industry reports suggest)\b'), 'name the source or cut'),
    ('throat-clearing opener', re.compile(r"(?i)\b(i hope this (email )?finds you well|please do not hesitate|just checking in|bumping this)\b"), 'cut; lead with the point'),
    ('title case heading', re.compile(r'(?m)^#{1,6} +\S.* (On|Of|The|And|In|For|To|With|A|An|Our|Your|Is|Are|At|By|From) [A-Z]'), 'sentence case'),
    ('emoji as structure', re.compile(r'(?m)^\s*(?:[-*]\s*)?[\U0001F300-\U0001FAFF✅⭐✨]'), 'plain bullet or heading'),
    ('inflated copula', re.compile(r'(?i)\b(serves as a|stands as a|boasts|represents a (significant|major|key))\b'), '"is" or "has"'),
]

UI_PATTERNS = [
    ('oops', re.compile(r'(?i)\b(oops|whoops|uh[- ]oh)\b'), 'say what happened and the fix'),
    ('vague failure', re.compile(r'(?i)\bsomething went wrong\b'), 'name what failed and what to do'),
    ('are you sure', re.compile(r'(?i)\bare you sure\b'), 'ask about the specific object: "Delete X?"'),
    ('invalid', re.compile(r'(?i)\binvalid\b'), 'say what a valid value looks like'),
    ('successfully', re.compile(r'(?i)\bsuccessfully\b'), 'the past-tense verb already says it'),
    ('please wait', re.compile(r'(?i)\bplease wait\b'), 'say what is happening'),
    ('click here', re.compile(r'(?i)\b(click|tap) here\b'), 'link text names the destination'),
    ('generic button', re.compile(r'(?m)^\s*(?:[-*]\s*|\|\s*)?(OK|Okay|Yes|No|Submit)\s*(\||$)'), 'verb plus object'),
    ('exclamation', re.compile(r'!'), 'none by default; one earned celebration at most'),
    ('(s) plural', re.compile(r'\w\(s\)'), 'handle plurals in code'),
    ('spelled-out count', re.compile(r'(?i)\b(one|two|three|four|five|six|seven|eight|nine|ten) (files?|items?|comments?|members?|messages?|results?|minutes?|days?)\b'), 'numerals'),
    ('positional placeholder', re.compile(r'%[sd]|\{\d\}'), 'named placeholder: {count}'),
]


ES_PR_PATTERNS = [
    ('peninsular word', re.compile(r'(?i)\b(ordenador(es)?|m\u00f3vil(es)?|coche|aparca\w*|fichero|rat\u00f3n|v\u00eddeo|zumo|patata|vosotr[oa]s|vuestr[oa]s?)\b'), 'see the Puerto Rico table in ai-tells.md section 7'),
    ('peninsular verb', re.compile(r'(?i)\b(puls[ae]|pulsar|pinch[ae]|pinchar)\b'), 'oprime, haz clic, presiona'),
    ('peninsular filler', re.compile(r'(?i)\b(vale|guay|t\u00edo)\b[,.!?]'), 'est\u00e1 bien, dale, ch\u00e9vere (casual only)'),
    ('ahorita', re.compile(r'(?i)\bahorita\b'), 'in Puerto Rico this means "in a while"; use "ahora mismo"'),
    ('slash gender form', re.compile(r'(?i)\b\w+[oa]/a\b|\b\w+@s\b|\b\w+xs\b|\btodes\b'), 'a form that does not force a gender'),
    ('Srta.', re.compile(r'Srta\.'), 'Sra. only if the reader uses it, else the full name'),
    ('numeric short date', re.compile(r'\b(0?[1-9]|[12]\d|3[01])/(0?[1-9]|1[0-2])/\d{2,4}\b'), 'ambiguous between day-first and month-first; write the month out: "6 de octubre de 2026"'),
    ('tu/usted mix', re.compile(r'(?i)\busted(es)?\b'), 'check: this message also uses t\u00fa forms (flagged only when both appear)'),
]


def mixes_tu_usted(text: str) -> bool:
    has_usted = re.search(r'(?i)\busted\b', text) is not None
    has_tu = re.search(r'(?i)\b(tu|tus|te|t\u00fa|contigo)\b', text) is not None
    return has_usted and has_tu


def lint(path: pathlib.Path, ui: bool, es_pr: bool = False):
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    findings = []
    words = kill_words()
    phrases = kill_phrases()
    for i, line in enumerate(lines, 1):
        low = line.lower()
        for w in words:
            if re.search(r'\b%s\b' % re.escape(w), low):
                findings.append(('kill-list word "%s"' % w, i, line.strip(), 'plain word, or keep on purpose'))
        for ph in phrases:
            if ph in low:
                findings.append(('stock phrase "%s"' % ph, i, line.strip(), 'cut'))
        for name, rx, fix in PROSE_PATTERNS + (UI_PATTERNS if ui else []):
            if rx.search(line):
                findings.append((name, i, line.strip(), fix))
        if es_pr:
            for name, rx, fix in ES_PR_PATTERNS:
                if name == 'tu/usted mix' and not mixes_tu_usted(text):
                    continue
                if rx.search(line):
                    findings.append((name, i, line.strip(), fix))
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('files', nargs='+')
    ap.add_argument('--ui', action='store_true', help='also apply the UI-string rules')
    ap.add_argument('--es-pr', action='store_true', help='also apply the Puerto Rican Spanish rules')
    args = ap.parse_args()
    total = 0
    for f in args.files:
        p = pathlib.Path(f)
        found = lint(p, args.ui, args.es_pr)
        total += len(found)
        print("%s: %d finding(s)" % (p, len(found)))
        for name, ln, line, fix in found:
            print("  %s | line %d: %s | %s" % (name, ln, line[:90], fix))
    print("\nthese are patterns in the text, not a verdict on its author.")
    return 1 if total else 0


if __name__ == '__main__':
    sys.exit(main())
