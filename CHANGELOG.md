# Changelog

## 1.2.0 (2026-10-08)

`voz` learned two dials, the words a visitor reads inside a product, and how to get into claude.ai.

### The gap this closes

Until now `voz` had one default voice and nine registers. A user who wanted the same email
"more casual" or "shorter, and from the company, not from me" had no vocabulary for it, and the
skill had nothing to say about the strings a product shows: a button, an error, an empty state.
Those strings are prose a person reads, often while annoyed, and they were being written on
instinct. This release names the dials and writes the rules.

### Added

- **Tone and mood dials.** Tone is distance: casual, neutral, professional. Mood is what the writer
  leads with: empathic, concise, corporate. Both sit on top of any register. Default is neutral +
  empathic; chat is casual + concise; email to anyone outside the company is professional +
  empathic; product strings are neutral + concise. When a register and a dial conflict, the
  register's structure wins and the skill says which dial it dropped.
- **`references/tone-mood.md`**: the two profile tables, the same declined-payment message written
  nine ways so the reader can see what moves and what does not, a surface-to-default table, and
  the shapes of an email, a chat message, a follow-up, a no, bad news and an apology. Spanish maps
  tone onto tú and usted, with gender-aware forms for both languages.
- **`references/ui-copy.md`**: rules per string type (buttons, labels, errors, empty states,
  destructive dialogs, toasts, loading, tooltips, notifications and system emails, toggles,
  badges), a mechanics table (case, periods, exclamation marks, numerals, dates, please, sorry),
  the verbs that look interchangeable and are not (delete, remove, clear, discard), translation
  and accessibility rules, the developer handoff table, and a nine-line self-check.
- **Changing the tone on request** in edit mode: move the dial, keep their vocabulary, facts and
  order, name the shift in What changed.
- **`scripts/package_claude_ai.py`** builds `dist/voz.zip` in the shape claude.ai accepts: one
  top-level `voz/` folder with `SKILL.md`, `LICENSE` and `references/`. Scripts and tests stay out.
- **`tests/lint-output.py`**: a deterministic audit of text voz produced, in the same
  `pattern | line | fix` shape as audit mode. It reads the kill-list from `SKILL.md` so the two
  cannot drift, and `--ui` adds the string anti-patterns.
- **`tests/fixtures/tone-mood-brief.md`** and its key: one email in a named setting with five
  facts that must survive, and one destructive dialog plus toast as a developer key table.
- The coverage check now counts its own assertions (259, up from 104) and also verifies the
  post-edit checklist numbering, that every reference is pointed at from `SKILL.md`, that the
  frontmatter satisfies the Agent Skills spec, that the Spanish in the catalog carries its accents,
  and that the claude.ai zip builds with the right shape.

### Changed

- The frontmatter description now names the surfaces and the dials so claude.ai triggers the skill
  on an email, a message, a UI string, or a tone request. It no longer mentions `CLAUDE.md`, which
  means nothing in a chat.
- The SessionStart banner and the `CLAUDE.md` pointer describe the dials and the UI copy rules.
- Register 1 is "Empathetic (the default)", not "Empathetic-neutral", so it stops colliding with
  the neutral tone.
- The self-check gained a dials question and a product-strings step.

### Fixed

- The post-edit checks in `references/editing.md` were numbered 1 to 9, then 13, 14, 10, 11, 12,
  15. They now run 1 to 23, and the test enforces it.
- The Spanish section of `references/ai-tells.md` had lost its accents (señalar, también,
  posición, conclusión).
- `tests/fixtures/KEY-fresh.md` called its draft `test-draft-2.md`; the file is `fresh-draft.md`.

### Measured

Fresh-context functional run, 2026-10-08, with the model under test barred from the keys. On
`tone-mood-brief.md`: **8 of 8** on the email, **8 of 8** on the strings, both restraint checks
held, and `lint-output.py --ui` reported zero findings. The audit of `fresh-draft.md` is recorded
alongside it in `tests/runs/2026-10-08-tone-mood-ui.md`.

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
