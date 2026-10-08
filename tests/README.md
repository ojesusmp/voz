# voz tests

Inert at runtime. Claude Code loads `SKILL.md` and the files in `references/`; nothing here is
read unless you run it on purpose.

## `coverage-check.py`

The regression check. It asserts that every pattern, word class, mode, register, dial and
discipline voz claims to cover is still present somewhere in it, that the zero em dash house rule
has not been weakened into an allowance, that the "probabilities, not laws" posture survived, that
the post-edit checklist is numbered in order, that every reference file is pointed at from
`SKILL.md`, that the frontmatter satisfies the Agent Skills spec claude.ai and Claude Code share,
and that `scripts/package_claude_ai.py` builds a zip with the shape claude.ai accepts.

```sh
python tests/coverage-check.py
```

It prints how many checks it ran (268 at 1.2.0). Exit 0 means nothing was lost. Run it after
editing voz, and after the twice-yearly refresh of the word list in `references/ai-tells.md`. No
model in the loop, so the answer is the same every time.

## `lint-output.py`

The other direction: a deterministic check on text voz produced. Give it an email, a message, or
a file of UI strings and it reports the mechanical half of the kill-list in audit shape
(`pattern | line | fix`), reading the word and phrase lists straight out of `SKILL.md` so the two
cannot drift. `--ui` adds the string rules (Oops, Are you sure?, successfully, generic buttons,
exclamation marks, positional placeholders).

```sh
python tests/lint-output.py draft.md
python tests/lint-output.py --ui strings.md
```

Exit 1 means it found something. It catches what a regex can catch and nothing else: a rule of
three, a kicker, or a portability failure still need a reader. Do not run it on voz's own files,
which quote every word they ban.

## `fixtures/`

- `slop-draft.md` is a short draft with one instance of each of 32 named patterns, plus six
  deliberate traps a good editor must NOT touch: a real number, a blunt admission, a genuine
  "I think", a personal aside, a one-word beat, and the spoken cadence overall.
- `KEY.md` is the answer key and the scoring rule. Do not show it to the model under test.

The functional test: hand a fresh session `SKILL.md` plus the reference files and the draft, ask
it to audit without rewriting, and score its findings against the key.

**Over-editing counts as failure.** A pass needs at least 29 of 32 patterns found AND all six
traps left intact. Catching every tell while flattening the writer is not a better edit, it is
a different failure.

## The two fixtures, and why there are two

`slop-draft.md` shares some example strings with voz's own files, because both drew on the same
pattern list. A high score there partly measures string matching. `fresh-draft.md` was written
afterwards for exactly that reason: same pattern classes, different subject, different voice,
wording that appears nowhere in voz. When you re-test, run both, and treat the fresh draft as the
real result. Ask the model under test to separate findings it made by recognising a printed
phrase from findings it made by applying a pattern to wording it had not seen. That second number
is the one that matters.

`fresh-draft.md` also plants one deliberately ambiguous line (three role words that might be
three real roles). Hedging on it is correct. Confidently rewriting it is not.

## `fixtures/tone-mood-brief.md` and `KEY-tone-mood.md`

The 1.2.0 functional test. The brief asks for one email in a named setting (professional +
concise) with five facts that must survive, and one destructive dialog plus its toast delivered as
a developer key table at the product default. The key is mechanical where it can be: run
`lint-output.py --ui` on the output first, then score the 16 rows and the 2 restraint checks.

## `fixtures/slop-draft.edited.md`

A worked example of the output contract: the edited draft plus its What changed note. The rules
describe that shape in prose, and a model copies an example far more reliably than it follows a
description. It is a target, not the only correct edit.

## Runs

`2026-09-08-baseline.md` is the full pre-parity run. `2026-10-08-tone-mood-ui.md` records the
1.2.0 functional test: a fresh-context audit of `fresh-draft.md` against `KEY-fresh.md`, and the
tone/mood brief against `KEY-tone-mood.md`.

## Baseline

Measured 2026-09-08, before the parity work, on `slop-draft.md`: **22** patterns found, no edit
mode, no audit mode. After: **32 of 32** found, 6 of 6 preservation traps intact. On
`fresh-draft.md`, which did not exist before the work: **19 of 19** valid classes found, 5 of 5
traps intact, with nine of them identified from the pattern description rather than a printed
phrase. Those are the numbers any future change should stay above.
