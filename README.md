# voz

A skill for Claude Code and claude.ai that makes writing read like a person wrote it, and lets you switch voice to fit the reader: emails, chat messages, documents, and the strings a product shows its visitors.

This is writing guidance, not an AI detector. The goal is clear, honest prose. It is never a tool for labeling, scoring, or accusing anyone's text, and it should not be used that way.

`voz` ("voice" in Spanish) does three things:

1. **Kills AI-writing tells.** The overused words (delve, tapestry, underscore, boasts, robust, seamless), the rule-of-three, the "it's not X, it's Y" pattern, the inflated "serves as a" instead of "is", and the formatting overkill (bold-label bullet lists, em dashes, emoji headers, Title Case Headings). Strip those and text stops sounding machine-made.
2. **Edits a draft without erasing the writer.** Handed prose someone else wrote, the job inverts: keep their voice, their bluntness, their real hedges and their facts, and remove only the tells. There is an audit mode too, which names each pattern with the offending line and a short fix and rewrites nothing. It never claims a machine wrote anything; it points at patterns a reader can check.
3. **Switches register on demand.** One warm, plain, confident default voice, plus eight professional registers you can call by name.
4. **Sets tone and mood as two dials.** Tone is distance: casual, neutral, professional. Mood is what the writer leads with: empathic, concise, corporate. Say "professional and concise" and the same facts come out at that setting, with the date, the deadline and the blame-free framing intact.
5. **Writes the words a visitor reads.** Buttons, errors, empty states, confirmations, toasts, notifications, system emails. Verb-plus-object buttons, errors that name the fix, no "Oops" or "Are you sure?", one word per concept, strings handed to the developer as a key table.

It is designed to run by default once you wire it into your own Claude Code setup (a pointer in your `CLAUDE.md`, or a SessionStart hook). The repo itself is just the skill; the always-on wiring is yours to add. You should not have to ask for good writing.

## The registers

| Register | For |
|---|---|
| Empathetic (default) | docs, support, chat, most things |
| Salesman / closer | 1:1 selling, proposals, objection handling |
| Corporate | board updates, all-hands, investor notes |
| Lawyer / legal | contracts, demand letters, terms, notices |
| Journalist | announcements, news, press-release rewrites |
| Marketing | landing pages, ads, headlines, email |
| Technical | specs, APIs, runbooks, dev docs |
| Teacher | guides, onboarding, explainers |
| Motivational | pep talks, vision, closers (use sparingly) |

Say the register's name and the writing shifts. Say nothing and you get the default.

## The two dials

| Dial | Settings | Default |
|---|---|---|
| Tone (distance) | casual, neutral, professional | neutral |
| Mood (what it leads with) | empathic, concise, corporate | empathic (concise for product strings) |

The dials sit on top of any register. Chat defaults to casual + concise, an email to someone outside the company to professional + empathic, an announcement in the company's name to neutral + corporate. `references/tone-mood.md` has the same declined-payment message written nine ways, so you can see what moves and what does not.

## What's in here

```
SKILL.md                  the spine: three modes, default voice, kill-list, registers, dials, UI copy, self-check
references/
  editing.md              editing someone else's draft, audit mode, 23 post-edit checks
  ai-tells.md             full tell catalog, with sources and dates
  registers.md            all nine register profiles, and the one table of exceptions
  tone-mood.md            the two dials, the nine-way example, email and chat shapes, Spanish and gender-aware forms
  ui-copy.md              product strings by type, mechanics, vocabulary, translation, accessibility, handoff
  human-prose.md          the positive craft: specificity, the portability test, rhythm
  self-check.md           a 20-second pass to run before you deliver
scripts/
  voz_sessionstart.py     the lightweight reminder the always-on hook prints
  wire_settings.py        idempotent always-on wiring (CLAUDE.md + settings.json)
  package_claude_ai.py    builds dist/voz.zip for upload to claude.ai
tests/
  coverage-check.py       259 assertions that nothing was lost; no model in the loop
  lint-output.py          deterministic audit of text voz produced (emails, messages, UI strings)
  fixtures/               planted drafts, briefs, their keys, and a worked edited example
  runs/                   the measured results, kept as evidence
install.ps1               one-command installer (Windows)
install.sh                one-command installer (macOS/Linux)
```

## Install

### Quick install

Clone the repo and run the installer. It copies the skill into `~/.claude/skills/voz`, which both the Claude Code CLI and the VSCode extension read.

Windows (PowerShell):
```powershell
git clone https://github.com/ojesusmp/voz.git
./voz/install.ps1
```

macOS/Linux (bash):
```bash
git clone https://github.com/ojesusmp/voz.git
bash voz/install.sh
```

### Always-on (optional)

A plain install just adds the skill, so you invoke it when you want it. To make the default voice apply automatically in every session, add the always-on flag. It appends a pointer to your global `~/.claude/CLAUDE.md` and a small SessionStart hook to `~/.claude/settings.json`. Both edits are idempotent and touch nothing else in your config.

```powershell
./voz/install.ps1 -AlwaysOn
```
```bash
bash voz/install.sh --always-on
```

Always-on needs Python on your PATH, since the hook is a short Python script. If Python is missing the installer skips the wiring and tells you, leaving the skill itself installed.

### In claude.ai and the Claude desktop app

Custom skills in claude.ai are a zip with one top-level folder that holds `SKILL.md`. Build it and upload it:

```sh
python scripts/package_claude_ai.py        # writes dist/voz.zip
```

Then in claude.ai: **Settings > Capabilities > Skills > Upload skill**, pick `dist/voz.zip`, and switch it on. The same zip works in the Claude desktop app. Custom skills need a Pro, Max, Team or Enterprise plan with code execution enabled, and they are per user, so each person uploads their own copy. Some accounts label the page **Settings > Features**; it is the same place.

The zip holds only `SKILL.md`, `LICENSE` and `references/`. The scripts and tests are Claude Code mechanics and stay out. Re-run the packager and re-upload after each update; claude.ai does not pull from the repo.

There is no always-on hook in claude.ai. To get the same effect, paste the one-paragraph pointer that `scripts/wire_settings.py` writes into a Project's custom instructions, or into Settings > Profile under "what preferences should Claude consider".

### Manual install

If you would rather not run a script, copy the folder yourself:
```sh
git clone https://github.com/ojesusmp/voz.git ~/.claude/skills/voz
```

### Verify

Reload VSCode (`Developer: Reload Window`) or start a new Claude Code session, then ask Claude to "write a short product description and avoid AI tells", or name a register: "rewrite this in the journalist register." To check the edit mode, paste a rough draft and say "clean this up but keep my voice". To check the audit mode, paste one and ask "is this slop?". To check the dials, ask for "the declined-payment email, professional and concise", then "same thing, casual". To check UI copy, ask for "the strings for a dialog that deletes a project, as a key table".

## Test it

```sh
python tests/coverage-check.py
```

259 assertions, no model in the loop, so the answer is the same every run. It checks that every pattern, word class, mode, register and dial is present, that the SKILL.md kill-list is a subset of the catalog it points at, that every pattern the edit checklist demands be removed is one SKILL.md actually names, that all nine registers survive, that the zero em dash rule has not been softened into an allowance, that the frontmatter is valid for claude.ai, and that the claude.ai zip builds with the right shape. Exit 0 means nothing was lost. Run it after editing the skill and after each refresh of the word list.

```sh
python tests/lint-output.py --ui strings.md
```

The other direction: a deterministic check on something voz wrote. It reports kill-list words, stock phrases, em dashes, negative parallelism, recap endings and (with `--ui`) the string anti-patterns, in the same `pattern | line | fix` shape as audit mode. It reads the word lists from `SKILL.md`, so the two cannot drift.

For a functional check, hand a fresh session the skill files plus `tests/fixtures/fresh-draft.md` and ask for an audit, then score against `tests/fixtures/KEY-fresh.md`; or hand it `tests/fixtures/tone-mood-brief.md` and score against `KEY-tone-mood.md`. `tests/runs/` records the measured results so a later change has a number to beat rather than a feeling.

## How it was built

The avoid-list is grounded in real sources, not vibes:

- [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), the community catalog, as the primary source.
- Kobak et al., *Science Advances* 2025, a [study of 15M+ scientific abstracts](https://www.science.org/doi/10.1126/sciadv.adt3813) showing the post-ChatGPT vocabulary spike.
- Yakura et al., a [study of 740K+ hours of speech](https://arxiv.org/abs/2409.01754) finding the same words leaking into how people talk.
- Zaitsu et al., *PLoS ONE* 2025, on [what surface cues humans actually use](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0335369&type=printable) to judge text as machine-written.

The nine register profiles were each researched against style references (Bryan Garner for legal, AP and Reuters for journalism, HBR for corporate, classical rhetoric for motivational, and more, cited inline in `references/registers.md`).

Two honest caveats, baked into the skill:

- **The word list ages.** "delve" spiked in 2023 and faded by 2025. The list is datable and meant to be refreshed. The patterns outlast the words.
- **No single tell is proof.** One em dash means nothing; the "em dash equals robot" claim is overstated. The skill judges clusters, and it is writing guidance, not a detector. The aim is to write well, not to accuse anyone's text.
- **The Spanish section is unverified.** Every source above studied English. `references/ai-tells.md` carries a Spanish section marked (editorial, unverified) because the skill is named in Spanish and gets used on Spanish copy, but no corpus study backs that list. Check it against real drafts before relying on it. It does record one thing worth knowing: the raya is standard Spanish punctuation, so a Spanish writer's em dash is evidence of nothing at all.

## Changes

See [CHANGELOG.md](CHANGELOG.md). The short version: 1.1.0 taught `voz` to edit somebody else's draft without turning it into `voz`; 1.2.0 added the tone and mood dials, the UI copy rules, and the claude.ai package.

## License

MIT. See [LICENSE](LICENSE).
