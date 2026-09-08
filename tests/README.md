# voz tests

Inert at runtime. Claude Code loads `SKILL.md` and the files in `references/`; nothing here is
read unless you run it on purpose.

## `coverage-check.py`

The parity regression check. It asserts that every pattern, word class, mode and discipline the
`no-ai-slop` skill covers is still present somewhere in voz, that the zero em dash house rule
has not been weakened into an allowance, and that the "probabilities, not laws" posture survived
the merge.

```sh
python tests/coverage-check.py
```

Exit 0 means parity holds. Run it after editing voz, and after the twice-yearly refresh of the
word list in `references/ai-tells.md`. No model in the loop, so the answer is the same every time.

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

## `fixtures/slop-draft.edited.md`

A worked example of the output contract: the edited draft plus its What changed note. The rules
describe that shape in prose, and a model copies an example far more reliably than it follows a
description. It is a target, not the only correct edit.

## `runs/`

The evidence behind the numbers below. `2026-09-08-baseline.md` is the full pre-parity run.

## Baseline

Measured 2026-09-08, before the parity work, on `slop-draft.md`: **22** patterns found, no edit
mode, no audit mode. After: **32 of 32** found, 6 of 6 preservation traps intact. On
`fresh-draft.md`, which did not exist before the work: **19 of 19** valid classes found, 5 of 5
traps intact, with nine of them identified from the pattern description rather than a printed
phrase. Those are the numbers any future change should stay above.
