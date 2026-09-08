# Answer key for test-draft-2.md (the generalization test)

Built AFTER the first test revealed a weakness: draft 1 shared several example strings with
voz's own files, so a high score there partly measured string matching. Draft 2 plants the same
pattern classes using **different words, different subject, different voice**. Items marked
(near-canonical) still share a phrase with voz's lists; everything else is fresh.

## Patterns planted (20 classes)

| # | Pattern class | Planted as | Canonical overlap |
|---|---|---|---|
| 1 | Title Case heading | "Notes On Our Q3 Hiring Process Changes" | none |
| 2 | Throat-clearing opener | "Let me be clear." | listed phrase |
| 3 | Faux-insight setup | "The part everyone misses is that the bottleneck..." | (near-canonical) |
| 4 | Binary contrast | "It's not a sourcing problem. It's a scheduling problem." | fresh instance |
| 5 | Rhetorical setup, self-answered | "Think about it: how many good engineers have you lost...? Too many." | fresh instance |
| 6 | Stock closer / dramatic fragmentation | "That's the whole story." | (near-canonical variant) |
| 7 | Banned words | embark, harness, paradigm shift, cutting-edge, empower, paramount, multifaceted | listed words |
| 8 | Colon reveal | "The thing that actually fixed it: one shared calendar." | fresh instance |
| 9 | Synonym cycling | recruiter / coordinator / scheduler for one role | fresh, and deliberately ambiguous: these could be three real roles, so flagging it as *possible* cycling is the right answer, and confidently rewriting it would be wrong |
| 10 | Weasel attribution | "Many argue", "industry reports suggest" | listed phrases |
| 11 | Importance puffery | "solidifying their position as employers of choice" | fresh instance |
| 12 | Significance tail | "underscoring the value we place on every candidate" | fresh instance |
| 13 | Weak verb phrase | "gives our team the ability to book a panel" | fresh instance |
| 14 | Empty adverbs | "genuinely improved", "inevitably a bit messy", "actually fixed it" | fresh instances |
| 15 | Abstraction, no specific | "improved candidate experience across the board" | fresh instance |
| 16 | Portability failure | "a multifaceted commitment to hiring excellence" | fresh instance |
| 17 | Metadiscourse | "Worth sitting with that for a second." | fresh phrasing, not on any voz list |
| 18 | Recap ending | "Overall, this quarter's changes reflect..." | listed word |
| 19 | Fake-profound kicker | "Hiring isn't a funnel. It's a conversation." | fresh instance |
| 20 | Negative parallelism, second use | items 4 and 19 are both this shape in one short piece | fresh |

## Must NOT be destroyed (5)

| # | Must survive | Why |
|---|---|---|
| P1 | "from 11 days to 1.4 days over 63 open roles between July and September" and "58% to 71%" | Real, load-bearing numbers. |
| P2 | "Honestly? I pushed back on this project for two months because I thought it was busywork, and I was flat wrong about that." | Blunt self-criticism. "Honestly" here carries real sincerity, and "I thought" is a real hedge. The empty-adverb rule must not eat it. |
| P3 | "Rachel called it before any of us did. Credit where it's due." | A named person and a generous aside. Character. |
| P4 | "Two panels got double-booked in week one. We fixed it." | Specific, plain, honest. Two short sentences that are rhythm, not stacked fragments. |
| P5 | "We had plenty of candidates. We could not get them in front of anyone." | Already clean and human. Any "improvement" here is over-editing. |

## Scoring
- Detection: pattern classes found out of 20. Target at least 17.
- The honest sub-score: of the classes with **no canonical overlap** (4, 5, 8, 9, 11, 12, 13, 14,
  15, 16, 17, 19, 20 = 13 classes), how many were found? That number is the real generalization
  result, because none of them can be matched against a string in voz's own files.
- Preservation: P1 to P5 intact out of 5. Target 5 of 5.
- Item 9 is scored correct if flagged with hedged wording; scored WRONG if it is confidently
  called synonym cycling and a rewrite is prescribed, because the draft does not settle whether
  those are three roles or one.
