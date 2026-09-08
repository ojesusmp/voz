# Changelog

## 1.1.0 (2026-09-08)

`voz` learned to edit somebody else's writing without turning it into `voz`.

### The gap this closes

Until now `voz` only governed prose it was writing itself. Handed a draft from another person it
would have applied the house voice to them: cut every "I think", deleted the personal aside as
throat-clearing, sanded off the bluntness, and said nothing about what it had changed. Clean
prose, wrong person. That is the failure this release exists to prevent.

### Added

- **Edit mode.** When someone hands over a draft, their voice wins. Inventory what makes it sound
  like them, make the smallest effective edit, leave strong sentences alone, keep their structure,
  and return the full draft plus a "What changed" note that opens by naming the voice you kept.
- **Audit mode.** Flag without fixing: `pattern | quoted line | short fix`, then stop. No rewrite,
  no score out of ten, and never a claim about who or what wrote the text. A detector guesses; a
  named pattern is evidence a reader can check.
- **`references/editing.md`**, a new reference that loads only when a draft exists. The keep-list
  (bluntness, profanity, humor, self-interruptions, honest admissions, real hedges), the
  never-invent rule, a never-alter list for quotations, code, names, citations and legal terms of
  art, the output contract, and 23 post-edit checks.
- **Nine patterns** that were not named anywhere before: faux-insight setups, rhetorical setups,
  colon reveals, interpretive metadiscourse, fake-profound kickers, negative listing, stacked
  fragments, synonym cycling, and weasel attribution with the fix it was missing.
- **The portability test.** If a sentence could move unchanged to another person, company, country
  or product, it is filler.
- **Protect the specific fact.** A real number in a draft survives the edit. Losing one is a worse
  failure than leaving a flagged word in.
- **Often-empty adverbs** as a category, with a cut-or-keep rule: just, literally, honestly,
  simply, actually, truly, fundamentally, importantly, crucially, inherently, inevitably.
- **Human subjects and direct verbs.** "The team shipped it Tuesday", not "the decision emerged".
- Around 25 more words and phrases, a working cluster threshold, and the carve-out that a word
  quoted as an example is not a tell.
- **A Spanish section** in `references/ai-tells.md`, marked (editorial, unverified) because every
  cited source studied English. It notes the one thing that does not transfer: the raya is standard
  Spanish punctuation, so a Spanish writer's em dash is evidence of nothing.
- **`tests/`**: a 104-assertion parity check with no model in the loop, two planted fixtures with
  their keys, a worked example of an edited draft, and the measured baseline kept as evidence.

### Changed

- The em dash rule got stricter, not looser: zero in short copy, in long drafts, and in a draft you
  are editing for somebody else. It is the only punctuation `voz` overrides on principle.
- The rhythm rule now covers repeated sentence shapes and identically built paragraphs, not only
  sentence length.
- `references/registers.md` gained one table of the shapes a register may use on purpose. Em dashes
  and invented facts are permanently off it.
- The SessionStart banner and the `CLAUDE.md` pointer now describe all three modes.
- Both installers ship `tests/`, so an install can check its own parity.

### Fixed

- `references/registers.md` claimed all nine registers keep the kill-list "no AI tells, ever, in
  any voice" while the motivational profile prescribed tricolon, anaphora and one-word fragments.
  The exception table resolves it.
- One threshold for negative parallelism instead of three different ones across three files.
- `SKILL.md` used a rule of three in the paragraph telling you to vary it, and `human-prose.md` ran
  three consecutive sentences on an identical shape. A writing skill that breaks its own rules
  teaches the model the rule is optional.

### Measured

Same planted draft, same blind method: **22 problems found before this release, 46 after**, with
every preservation trap intact. On a second draft whose wording appears nowhere in the skill,
**19 of 19 pattern classes**, ten of them recognised from the rule rather than a printed phrase,
and the resulting edit cut an unsourced claim rather than inventing a source. `tests/runs/` holds
the baseline. Re-run `python tests/coverage-check.py` to confirm nothing has been lost since.

## 1.0.0 (2026-06-16)

First release. Default human voice, the sourced tell catalog, nine register profiles, the
20-second self-check, and a cross-platform installer with optional always-on wiring.
