# Answer key for test-draft.md

Not shown to the agent under test. Every item was planted deliberately.

## Part 1: patterns the skill MUST catch (28)

| # | Pattern | Planted as |
|---|---|---|
| 1 | Emoji as heading decoration | "# 🚀 Introducing..." |
| 2 | Title Case In Headings | "A Paradigm Shift In Workflow" |
| 3 | Throat-clearing opener | "Here's the thing." |
| 4 | Empty phrase: when it comes to | "When it comes to file sync" |
| 5 | Empty adverb: just | "most teams have just accepted" |
| 6 | Faux-insight setup | "What nobody tells you is" |
| 7 | Binary contrast | "It's not a bandwidth issue. It's an ordering issue." |
| 8 | Empty phrase: the truth is | "The truth is," |
| 9 | Empty phrase: at the end of the day | "at the end of the day" |
| 10 | Banned words cluster | delve, leverage, robust, seamless, ever-evolving, streamline |
| 11 | Rhetorical setup | "What if I told you the fix was 200 lines?" |
| 12 | Colon reveal | "The best part: it learns." |
| 13 | Synonym cycling | agent / assistant / tool for the same thing |
| 14 | Weasel attribution | "Studies show", "industry experts agree" |
| 15 | Empty adverbs | "actually recoverable", "fundamentally the core problem" |
| 16 | Fake-strong verb / inflated copula | "serves as a centralized hub" |
| 17 | Importance puffery | "marking a pivotal moment" |
| 18 | Superficial analysis (-ing tail) | "highlighting our team's commitment to innovation" |
| 19 | Abstraction over a specific fact | "significantly improves engineering productivity" |
| 20 | Interpretive metadiscourse | "That last part matters more than it sounds." |
| 21 | Nominalization | "made a decision", "has the ability to" |
| 22 | Inanimate subject doing a human verb | "The decision emerged" |
| 23 | Negative listing | "Not a rewrite. Not a patch. A rebuild." |
| 24 | Rule of three | "fast, simple, and reliable" |
| 25 | Empty adverbs | "truly straightforward", "literally takes one command" |
| 26 | Empty phrases | "in order to", "Going forward", "Let's dive in" |
| 27 | Dramatic fragmentation | "That's it. That's the whole thing." |
| 28 | Sentence case after a colon | "The result: It Worked." |
| 29 | Summary-recap ending | "In conclusion, ..." |
| 30 | Banned words | multifaceted, underscores |
| 31 | Fake-profound kicker | "The future of sync isn't coming. It's already here." |
| 32 | Portability test failure | "underscores our commitment to reliability" moves to any company unchanged |

## Part 2: things the skill MUST NOT destroy (the over-editing trap)

| # | Must survive | Why |
|---|---|---|
| P1 | "median sync latency from 4.2 seconds to 380 milliseconds across 1,900 workspaces" | A real, specific, load-bearing fact. Smoothing it into "significantly faster" is a failure. |
| P2 | "the old code was a complete disaster and I am not going to pretend otherwise" | The writer's blunt voice and honest admission. Sanitizing it is a failure. |
| P3 | "I think it was probably my fault" | A hedge carrying REAL uncertainty and self-awareness, not padding. Cutting it is a failure. |
| P4 | "though I'd argue the deadline deserves some blame too" | A personal aside with character. |
| P5 | "Ha." | A one-word human beat. Deleting it for tidiness is a failure. |
| P6 | The overall blunt, spoken cadence | The edit must not flatten it into corporate-neutral prose. |

## Scoring
- Detection score: patterns found out of 32. Target: at least 29 (90%).
- Preservation score: items P1 to P6 left intact out of 6. Target: 6 of 6.
- A skill that scores high on detection but destroys P1 to P6 has FAILED. Over-editing is the
  failure mode `no-ai-slop` exists to prevent, so parity means catching the slop AND keeping
  the person.
