# voz

A Claude Code skill that makes writing read like a person wrote it, and lets you switch voice to fit the reader.

This is writing guidance, not an AI detector. The goal is clear, honest prose. It is never a tool for labeling, scoring, or accusing anyone's text, and it should not be used that way.

`voz` ("voice" in Spanish) does two things:

1. **Kills AI-writing tells.** The overused words (delve, tapestry, underscore, boasts, robust, seamless), the rule-of-three, the "it's not X, it's Y" pattern, the inflated "serves as a" instead of "is", and the formatting overkill (bold-label bullet lists, em dashes, emoji headers, Title Case Headings). Strip those and text stops sounding machine-made.
2. **Switches register on demand.** One warm, plain, confident default voice, plus eight professional registers you can call by name.

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

## What's in here

```
SKILL.md                  the spine: default voice, kill-list, register table, self-check
references/
  ai-tells.md             full tell catalog, with sources and dates
  registers.md            all nine register profiles (diction, moves, sample openings)
  human-prose.md          the positive craft: specificity, rhythm, restraint
  self-check.md           a 20-second pass to run before you deliver
```

## Install

Clone into your Claude Code skills directory:

```sh
git clone https://github.com/ojesusmp/voz.git ~/.claude/skills/voz
```

Claude Code picks it up on the next session. To verify, ask Claude to "write a short product description and avoid AI tells", or name a register: "rewrite this in the journalist register."

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

## License

MIT. See [LICENSE](LICENSE).
