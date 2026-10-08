#!/usr/bin/env python3
"""Parity regression check for voz.

Asserts that every pattern, word class, mode, register, dial and discipline voz
claims to cover is still present somewhere in it. Run it after editing voz, and after
the twice-yearly refresh of the word list in references/ai-tells.md.

It checks presence AND consistency: that SKILL.md's kill-list is a subset of the catalog
it points at, and that every pattern the edit checklist demands be removed is one SKILL.md
actually names. Both of those caught real defects the day they were written.

No model in the loop. Pure text matching, so the result is the same every time.

    python tests/coverage-check.py    # exit 0 = nothing lost, 1 = something was lost

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
    'references/tone-mood.md',
    'references/ui-copy.md',
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

    # the two dials (1.2.0)
    'tone dial named': r'(?i)tone[^.\n]{0,40}casual, neutral, professional',
    'mood dial named': r'(?i)mood[^.\n]{0,40}empathic, concise, corporate',
    'default dial setting': r'(?i)neutral tone, empathic mood|neutral \+ empathic',
    'concise is not curt': r'(?i)concise is not curt',
    'corporate mood vs register': r'(?i)corporate is a mood, not the corporate register',
    'empathy never announced': r'(?i)never announced|completely understand how frustrating',
    'register wins over dial': r"(?i)register'?s structure wins|the register wins",
    'surface to default table': r'(?i)Picking the dials when nobody says',
    'email subject is the ask': r'(?i)subject line is the news or the ask',
    'one ask per email': r'(?i)one ask per email',
    'spanish tu/usted': r'(?i)"tú" and "usted"|tú and usted',
    'gender-aware address': r'(?i)"They" for anyone whose pronouns|no "guys"',

    # UI copy (1.2.0)
    'ui copy reference exists': r'(?i)words a visitor reads',
    'button is verb plus object': r'(?i)verb plus (its )?object',
    'confirm button repeats verb': r'(?i)confirm button repeats the verb',
    'error names the fix': r'(?i)Enter a password of at least 12 characters',
    'no are-you-sure': r'(?i)not "Are you sure\?"',
    'no oops': r'(?i)never "Oops"|no "Oops"',
    'successfully banned': r'(?i)"successfully" adds nothing|no "successfully"',
    'empty state rule': r'(?i)No invoices yet',
    'one word per concept': r'(?i)one word per concept',
    'named placeholders': r'(?i)named placeholders',
    'string handoff format': r'(?i)Delivering strings to a developer',
    'string self-check': r'(?i)Self-check for a batch of strings',
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



CHECKS = 0
FAILS = []


def check(ok, msg):
    global CHECKS
    CHECKS += 1
    if not ok:
        FAILS.append(msg)


def main():
    missing_files = [f for f in FILES if not (VOZ / f).is_file()]
    if missing_files:
        print("FAIL  missing files: %s" % ', '.join(missing_files))
        return 1

    blob = '\n'.join((VOZ / f).read_text(encoding='utf-8') for f in FILES)
    low = blob.lower()

    for name, pat in sorted(REQUIRED.items()):
        check(re.search(pat, blob), "concept not covered: %s" % name)
    for w in REQUIRED_WORDS:
        check(w.lower() in low, "kill-list word missing: %s" % w)
    for p in REQUIRED_PHRASES:
        check(p.lower() in low, "kill-list phrase missing: %s" % p)

    # all nine register profiles must survive, by name. Checking only for the word
    # "motivational" let a whole profile be deleted with every check still passing.
    reg = (VOZ / 'references/registers.md').read_text(encoding='utf-8')
    for r in ('Empathetic', 'Salesman', 'Corporate', 'Lawyer', 'Journalist',
              'Marketing', 'Technical', 'Teacher', 'Motivational'):
        check(re.search(r'(?im)^#+ *\d+\. *%s' % r, reg),
              "register profile missing or renamed: %s" % r)
    heads = len(re.findall(r'(?m)^## \d+\.', reg))
    check(heads == 9, "expected 9 numbered register profiles, found %d" % heads)

    adverb_line = re.search(r'(?i)\*\*Often-empty adverbs[^\n]*\n?[^\n]*', blob)
    adv_blob = adverb_line.group(0).lower() if adverb_line else ''
    for a in REQUIRED_ADVERBS:
        check(a in adv_blob, "empty adverb missing from the adverb list: %s" % a)

    # CONSISTENCY, not just presence. SKILL.md calls ai-tells.md the "full catalog",
    # so every word and phrase named in the SKILL.md kill-list has to be in the catalog.
    skill = (VOZ / 'SKILL.md').read_text(encoding='utf-8')
    tells = (VOZ / 'references/ai-tells.md').read_text(encoding='utf-8').lower()
    m = re.search(r'(?s)not measured\.\s*(delve,.*?)The tell is density', skill)
    check(m, 'SKILL.md kill-list paragraph not found (lint-output.py parses it too)')
    if m:
        for w in re.split(r',\s*', m.group(1)):
            w = re.sub(r'\(.*?\)', '', w).strip(' .:*"“”').lower()
            if len(w) > 3:
                check(w in tells, 'SKILL.md kill-list word absent from the "full catalog": %s' % w)
    m = re.search(r'(?s)\*\*Phrases to drop:\*\*(.*?)\n\n', skill)
    check(m, 'SKILL.md "Phrases to drop" paragraph not found')
    if m:
        for ph in re.findall(r'"([^"]+)"', m.group(1)):
            check(ph.lower() in tells, 'SKILL.md kill-list phrase absent from the "full catalog": %s' % ph)

    # Every pattern the edit checklist says must be gone has to be named in SKILL.md,
    # or an editor is told to remove something the writer was never told to avoid.
    editing = (VOZ / 'references/editing.md').read_text(encoding='utf-8').lower()
    sl = skill.lower()
    for concept in ('negative listing', 'throat-clearing', 'faux-insight', 'rhetorical setup',
                    'colon reveal', 'puffery', 'weasel attribution', 'copula',
                    'synonym cycling', 'fragment', 'metadiscourse', 'kicker', 'recap'):
        check(not (concept in editing and concept not in sl),
              'editing.md requires removing "%s" but SKILL.md never names it' % concept)

    # The post-edit checklist is numbered 1..23 in order. It once read 1-9, 13, 14, 10, 11...
    tail = editing.split('## post-edit checks', 1)[-1]
    nums = [int(x) for x in re.findall(r'(?m)^(\d+)\. ', tail)]
    check(nums == list(range(1, 24)), 'editing.md post-edit checks are not numbered 1 to 23 in order: %s' % nums)

    # Every reference SKILL.md points at exists, and every reference file is pointed at.
    for ref in set(re.findall(r'`references/([a-z-]+\.md)`', skill)):
        check((VOZ / 'references' / ref).is_file(), 'SKILL.md points at a missing reference: %s' % ref)
    for f in sorted((VOZ / 'references').glob('*.md')):
        check('references/%s' % f.name in skill, 'reference never mentioned in SKILL.md: %s' % f.name)
        check('references/%s' % f.name in FILES, 'reference not covered by this check: %s' % f.name)

    # Frontmatter has to satisfy the Agent Skills spec that claude.ai and Claude Code share.
    fm = re.search(r'(?s)\A---\n(.*?)\n---', skill)
    check(fm, 'SKILL.md has no YAML frontmatter')
    if fm:
        name = re.search(r'(?m)^name: *(.+)$', fm.group(1))
        desc = re.search(r'(?m)^description: *(.+)$', fm.group(1))
        check(name and re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', name.group(1).strip()) and len(name.group(1).strip()) <= 64,
              'frontmatter name must be 1-64 chars of lowercase letters, digits and hyphens')
        check(name and name.group(1).strip() == VOZ.name or name and name.group(1).strip() == 'voz',
              'frontmatter name must be "voz" so it matches the folder claude.ai unzips')
        check(desc and len(desc.group(1)) <= 1024, 'frontmatter description over 1024 characters')
        check(desc and chr(8212) not in desc.group(1), 'em dash in the frontmatter description')
        check(desc and 'CLAUDE.md' not in desc.group(1), 'description mentions CLAUDE.md, which means nothing in claude.ai')
        for trig in ('email', 'UI strings', 'casual', 'concise', 'audit'):
            check(desc and trig in desc.group(1), 'description does not name the trigger "%s"' % trig)

    # house rules that must never be weakened
    em = blob.count(chr(8212))  # escape, never the literal, or this file trips its own check
    check(em == 0, "em dash present in voz source: %d occurrence(s)" % em)
    ALLOWANCE = (r'(?i)(1[- ]?(to[- ]?)?2|one or two|a couple of|a few|sparing(ly)?|'
                 r'occasional|at most (one|two)|no more than (one|two))[^.\n]{0,40}em[- ]?dash')
    check(not re.search(ALLOWANCE, blob), "the zero em dash house rule was weakened to an allowance")
    check('probabilities, not laws' in blob, "the probabilities-not-laws posture was lost")

    # Spanish in the catalog carries its accents; a skill named in Spanish cannot ship "conclusion".
    for bad in ('senalar', 'tambien', 'en conclusion"', 'posicion'):
        check(bad not in tells, 'unaccented Spanish in ai-tells.md: %s' % bad)

    # The claude.ai zip has the right shape: one top folder, SKILL.md inside it, every reference.
    import tempfile, zipfile, subprocess, sys as _sys
    with tempfile.TemporaryDirectory() as td:
        out = pathlib.Path(td) / 'voz.zip'
        r = subprocess.run([_sys.executable, str(VOZ / 'scripts/package_claude_ai.py'), '--out', str(out)],
                           capture_output=True, text=True)
        check(r.returncode == 0, 'package_claude_ai.py failed: %s' % r.stderr.strip())
        if r.returncode == 0:
            names = zipfile.ZipFile(out).namelist()
            check('voz/SKILL.md' in names, 'zip lacks voz/SKILL.md at the top folder')
            check(all(n.startswith('voz/') for n in names), 'zip has files outside the voz/ folder')
            for f in sorted((VOZ / 'references').glob('*.md')):
                check('voz/references/%s' % f.name in names, 'zip lacks references/%s' % f.name)
            check(not any('scripts/' in n or 'tests/' in n for n in names), 'zip ships scripts or tests')

    # The output linter runs clean on its own worked example and finds the planted tells.
    r = subprocess.run([_sys.executable, str(VOZ / 'tests/lint-output.py'), str(VOZ / 'tests/fixtures/fresh-draft.md')],
                       capture_output=True, text=True)
    check(r.returncode == 1 and 'kill-list word "embark"' in r.stdout and 'recap ending' in r.stdout,
          'lint-output.py did not find the planted tells in fresh-draft.md')

    if FAILS:
        for f in FAILS:
            print("FAIL  %s" % f)
        print("\n%d of %d checks failed." % (len(FAILS), CHECKS))
        return 1

    print("PASS  all %d checks" % CHECKS)
    print("PASS  zero em dashes across %d voz files" % len(FILES))
    print("PASS  probabilities-not-laws posture intact")
    print("PASS  claude.ai zip builds with the right shape")
    return 0


if __name__ == '__main__':
    sys.exit(main())
