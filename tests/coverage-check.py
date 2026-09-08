#!/usr/bin/env python3
"""Parity regression check for voz.

Asserts that every pattern, word class, mode and discipline that the `no-ai-slop`
skill covers is still present somewhere in voz. Run it after editing voz, and after
the twice-yearly refresh of the word list in references/ai-tells.md.

It checks presence AND consistency: that SKILL.md's kill-list is a subset of the catalog
it points at, and that every pattern the edit checklist demands be removed is one SKILL.md
actually names. Both of those caught real defects the day they were written.

No model in the loop. Pure text matching, so the result is the same every time.

    python coverage-check.py          # exit 0 = parity holds, 1 = something was lost

Baseline: voz reached parity on 2026-09-08. Before that date it covered 22 of the
32 patterns in tests/fixtures/slop-draft.md and had neither an edit nor an audit mode.
"""
import pathlib
import re
import sys

VOZ = pathlib.Path(__file__).resolve().parent.parent

FILES = [
    'SKILL.md',
    'references/ai-tells.md',
    'references/human-prose.md',
    'references/self-check.md',
    'references/editing.md',
    'references/registers.md',
]

# Each entry: concept name -> a regex that must match somewhere in voz.
# Keep these anchored to wording that carries the idea, not to incidental phrasing.
REQUIRED = {
    # modes and disciplines, the structural half
    'edit mode exists': r'(?i)hands you a draft|draft someone else wrote|draft that is not yours',
    'audit mode exists': r'(?i)pattern name \| quoted line|flag, not fix|audit mode',
    'no authorship claim': r'(?i)never a claim about who or what wrote it|no claim about authorship|verdict on its author',
    'preserve the writer voice': r'(?i)the voice is theirs|voice is theirs, not yours|would the writer recognise',
    'minimum effective edit': r'(?i)smallest edit|minimum effective edit',
    'never invent': r'(?i)[Nn]ever (add|invent) a? ?(claim|claims)|never supply one|invent nothing',
    'what changed output': r'(?i)what changed',
    'protect the specific fact': r'(?i)[Pp]rotect the specific fact',
    'post-edit checks': r'(?i)post-edit checks|fix and rerun until',
    'inverse check on own edits': r'(?i)re-scan only the sentences you changed|editors (add|introduce) tells while removing',

    # the named patterns
    'binary contrast': r'(?i)negative parallelism|not just X, but Y|not X\. It.s Y',
    'throat-clearing openers': r'(?i)here.s the thing|throat-clearing',
    'faux-insight setups': r'(?i)what nobody tells you|faux-insight|part everyone misses',
    'rhetorical setups': r'(?i)what if I told you|plot twist',
    'colon reveals': r'(?i)colon reveal|The best part: it learns',
    'superficial -ing analysis': r'(?i)significance tails?|highlighting the team',
    'importance puffery': r'(?i)pivotal moment|importance puffery|plays a vital role',
    'metadiscourse': r'(?i)metadiscourse|the key point is|as you can see',
    'weasel attribution': r'(?i)weasel attribution|studies show|experts agree',
    'fake-strong verbs': r'(?i)inflated copulas?|serves as a',
    'synonym cycling': r'(?i)synonym cycling|rotating .the agent|elegant variation',
    'negative listing': r'(?i)negative listing|Not a rewrite\. Not a patch',
    'dramatic fragmentation': r'(?i)stacked fragments|dramatic fragmentation|that.s the whole thing',
    'robotic rhythm': r'(?i)robotic|uniform sentence length|repeated sentence shapes',
    'fake-profound kickers': r'(?i)kicker|mic-drop',
    'recap endings': r'(?i)[Ii]n conclusion|recap ending|summary-recap',
    'formatting slop': r'(?i)emoji as (structure|section headers)|emoji headers',
    'heading over two sentences': r'(?i)heading over a section of two sentences|headers? over',
    'sentence case after colon': r'(?i)sentence case after a colon',
    'rule of three': r'(?i)rule of three',
    'title case headings': r'(?i)Title Case In Headings',

    # word and phrase classes
    'often-empty adverbs': r'(?i)[Oo]ften-empty adverbs',
    'weak verb phrases': r'(?i)made a decision|has the ability to',
    'human subjects': r'(?i)the decision emerged',
    'portability test': r'(?i)portability test',
    'open it up not dumb it down': r'(?i)do not dumb it down|dumb it down',

    # posture that must survive the merge, not be lost to no-ai-slop absolutism
    'probabilities not laws': r'probabilities, not laws',
    'quoted example carve-out': r'(?i)quoted as an example|word quoted as an example',
    'cluster threshold': r'(?i)two (flagged items )?in (one|a) paragraph is a cluster',
    'not a detector': r'(?i)not detection|never used to accuse|not a detector',

    'register exception table': r'(?i)Shapes a register may use on purpose',
}

# Words that must appear in the kill-list somewhere.
REQUIRED_WORDS = [
    'delve', 'utilize', 'facilitate', 'empower', 'streamline', 'harness', 'embark',
    'paramount', 'cutting-edge', 'game changer', 'ever-evolving', 'robust', 'leverage',
    'paradigm shift', 'beacon', 'supercharge', 'this is huge', 'this changes everything',
    'tapestry', 'realm', 'multifaceted', 'meticulous', 'intricate', 'transformative',
    'elevate', 'foster',
]
REQUIRED_PHRASES = [
    "it's important to note", "at the end of the day", "when it comes to", "at its core",
    "the reality is", "the truth is", "in terms of", "going forward", "in order to",
    "in this article", "let's dive in",
]
REQUIRED_ADVERBS = [
    'just', 'literally', 'honestly', 'simply', 'actually', 'truly', 'fundamentally',
    'importantly', 'crucially', 'inherently', 'inevitably',
]


def main():
    missing_files = [f for f in FILES if not (VOZ / f).is_file()]
    if missing_files:
        print("FAIL  missing files: %s" % ', '.join(missing_files))
        return 1

    blob = '\n'.join((VOZ / f).read_text(encoding='utf-8') for f in FILES)
    low = blob.lower()
    fails = []

    for name, pat in sorted(REQUIRED.items()):
        if not re.search(pat, blob):
            fails.append("concept not covered: %s" % name)

    for w in REQUIRED_WORDS:
        if w.lower() not in low:
            fails.append("kill-list word missing: %s" % w)
    for p in REQUIRED_PHRASES:
        if p.lower() not in low:
            fails.append("kill-list phrase missing: %s" % p)

    # all nine register profiles must survive, by name. Checking only for the word
    # "motivational" let a whole profile be deleted with every check still passing.
    reg = (VOZ / 'references/registers.md').read_text(encoding='utf-8')
    for r in ('Empathetic', 'Salesman', 'Corporate', 'Lawyer', 'Journalist',
              'Marketing', 'Technical', 'Teacher', 'Motivational'):
        if not re.search(r'(?im)^#+ *\d+\. *%s' % r, reg):
            fails.append("register profile missing or renamed: %s" % r)
    heads = len(re.findall(r'(?m)^## \d+\.', reg))
    if heads != 9:
        fails.append("expected 9 numbered register profiles, found %d" % heads)

    adverb_line = re.search(r'(?i)\*\*Often-empty adverbs[^\n]*\n?[^\n]*', blob)
    adv_blob = adverb_line.group(0).lower() if adverb_line else ''
    for a in REQUIRED_ADVERBS:
        if a not in adv_blob:
            fails.append("empty adverb missing from the adverb list: %s" % a)

    # CONSISTENCY, not just presence. SKILL.md calls ai-tells.md the "full catalog",
    # so every word and phrase named in the SKILL.md kill-list has to be in the catalog.
    skill = (VOZ / 'SKILL.md').read_text(encoding='utf-8')
    tells = (VOZ / 'references/ai-tells.md').read_text(encoding='utf-8').lower()
    m = re.search(r'(?s)not measured\.\s*(delve,.*?)The tell is density', skill)
    if m:
        for w in re.split(r',\s*', m.group(1)):
            w = re.sub(r'\(.*?\)', '', w).strip(' .:*"\u201c\u201d').lower()
            if len(w) > 3 and w not in tells:
                fails.append('SKILL.md kill-list word absent from the "full catalog": %s' % w)
    m = re.search(r'(?s)\*\*Phrases to drop:\*\*(.*?)\n\n', skill)
    if m:
        for ph in re.findall(r'"([^"]+)"', m.group(1)):
            if ph.lower() not in tells:
                fails.append('SKILL.md kill-list phrase absent from the "full catalog": %s' % ph)

    # Every pattern the edit checklist says must be gone has to be named in SKILL.md,
    # or an editor is told to remove something the writer was never told to avoid.
    editing = (VOZ / 'references/editing.md').read_text(encoding='utf-8').lower()
    sl = skill.lower()
    for concept in ('negative listing', 'throat-clearing', 'faux-insight', 'rhetorical setup',
                    'colon reveal', 'puffery', 'weasel attribution', 'copula',
                    'synonym cycling', 'fragment', 'metadiscourse', 'kicker', 'recap'):
        if concept in editing and concept not in sl:
            fails.append('editing.md requires removing "%s" but SKILL.md never names it' % concept)

    # house rules that must never be weakened
    em = blob.count(chr(8212))  # escape, never the literal, or this file trips its own check
    if em:
        fails.append("em dash present in voz source: %d occurrence(s)" % em)
    ALLOWANCE = (r'(?i)(1[- ]?(to[- ]?)?2|one or two|a couple of|a few|sparing(ly)?|'
                 r'occasional|at most (one|two)|no more than (one|two))[^.\n]{0,40}em[- ]?dash')
    if re.search(ALLOWANCE, blob):
        fails.append("the zero em dash house rule was weakened to an allowance")
    if 'probabilities, not laws' not in blob:
        fails.append("the probabilities-not-laws posture was lost")

    total = (len(REQUIRED) + len(REQUIRED_WORDS) + len(REQUIRED_PHRASES)
             + len(REQUIRED_ADVERBS) + 3 + 10 + 2)
    if fails:
        for f in fails:
            print("FAIL  %s" % f)
        print("\n%d of %d checks failed. voz has lost parity with no-ai-slop." % (len(fails), total))
        return 1

    print("PASS  all %d parity checks" % total)
    print("PASS  zero em dashes across %d voz files" % len(FILES))
    print("PASS  probabilities-not-laws posture intact")
    print("\nvoz still covers everything no-ai-slop covers.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
