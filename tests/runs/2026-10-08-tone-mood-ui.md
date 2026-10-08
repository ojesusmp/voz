# Run 2026-10-08: tone and mood dials, UI copy, and the fresh-draft regression

Method: two fresh-context sessions, each given `SKILL.md` and the seven reference files, barred
from the keys, `tests/runs/` and `tests/README.md`. Scored by hand against `KEY-fresh.md` and
`KEY-tone-mood.md`. `tests/lint-output.py --ui` run on the tone/mood output.

## Scores

### fresh-draft.md audit (regression; baseline was 19 of 19, 5 of 5)

| Class | Found | Note |
|---|---|---|
| 1 Title Case heading | yes | |
| 2 Throat-clearing opener | yes | |
| 3 Faux-insight setup | yes | |
| 4 Binary contrast | yes | counted against the one-per-piece bound |
| 5 Rhetorical setup, self-answered | yes | |
| 6 Stock closer | yes | recognised as "That's the whole thing" in a new coat |
| 7 Banned words | yes | all eight |
| 8 Colon reveal | yes | rule application; wording not printed in voz |
| 9 Synonym cycling (ambiguous by design) | hedged | flagged as borderline repeated shape, three real actors, lean leave. No rewrite prescribed, which the key scores as correct. It did not name the alternative reading (one role, three words). |
| 10 Weasel attribution | yes | both, with "do not supply one" |
| 11 Importance puffery | yes | |
| 12 Significance tail | yes | |
| 13 Weak verb phrase | yes | |
| 14 Empty adverbs | yes | "genuinely" and "inevitably" cut; "actually" kept on purpose as contrast, a defensible cut-or-keep call |
| 15 Abstraction, no specific | yes | "across the board" |
| 16 Portability failure | yes | |
| 17 Metadiscourse | yes | fresh phrasing, rule application |
| 18 Recap ending | yes | |
| 19 Fake-profound kicker | yes | "delete, do not rewrite into a better metaphor" |
| 20 Second negative parallelism | yes | threshold applied |

**20 of 20** classes (item 9 by hedging). Of the 13 classes with no canonical overlap, **13 of 13**
found. Preservation **P1 to P5: 5 of 5** intact, each named in the Preservation section with a
reason; the numbers paragraph marked "not one character changes". Audit shape held: pattern | line
| fix, disclaimer present, no score, no authorship claim, offer to edit afterwards.

The agent's own recognition split: about two thirds phrase recognition, one third rule
application (colon reveal, metadiscourse, "genuinely", "reflect" as inflated copula, "across the
board", the self-answered question, the two threshold counts, and overriding the adverb list to
keep "Honestly?").

### tone-mood-brief.md (new in 1.2.0)

| Row | Result |
|---|---|
| E1 facts survive | pass: 4471, 6 October 2026, Friday 10 October 2026, both addresses, unchanged |
| E2 subject is the news | pass: "Card ending 4471 declined: update it by Friday 10 October" |
| E3 point in sentence one | pass |
| E4 professional distance | pass: "Hello Priya Nair", no jokes, no exclamation marks, "Regards" with name and role |
| E5 concise | pass: four sentences, one ask |
| E6 blame-free | pass: the payment is the actor |
| E7 no announced empathy | pass |
| E8 nothing invented | pass |
| U1 title names the object | pass: "Delete '{project_name}'?" with a note on the render; key updated to accept a named placeholder |
| U2 consequence and reversibility | pass: {count} other people with ICU plural, Trash for 30 days |
| U3 confirm repeats the verb | pass: "Delete project", marked not the default focus |
| U4 cancel | pass |
| U5 toast with undo | pass, no "successfully", no "!" |
| U6 mechanics | pass |
| U7 handoff shape | pass: key, string, where, limit; keys screen.moment.part |
| U8 nothing invented | pass: developer notes only |
| P1 no question asked | pass |
| P2 setting stated once | pass, one line |

**8 of 8, 8 of 8, 2 of 2.** `lint-output.py --ui`: 0 findings.

## Raw output: fresh-draft audit

# Audit: "Notes On Our Q3 Hiring Process Changes"

Request as received: "Is this slop? Flag it, don't rewrite it." Audit mode, so: pattern name | quoted line | fix in a few words. No rewrite, no score.

Core point of the draft, as I read it: the hiring bottleneck was scheduling, not sourcing; one shared calendar fixed it; time-to-schedule fell from 11 days to 1.4 and offer acceptance rose from 58% to 71%.

## Findings

Title Case in heading | "Notes On Our Q3 Hiring Process Changes" | sentence case: "Notes on our Q3 hiring process changes"

Throat-clearing opener | "Let me be clear." | cut it; "Recruiting has been rough this year." is the real first line

Faux-insight setup | "The part everyone misses is that the bottleneck was never the top of the funnel." | cut the setup, keep the claim: the bottleneck was never the top of the funnel

Negative parallelism (1 of 2) | "It's not a sourcing problem. It's a scheduling problem." | one plain statement: it was a scheduling problem

Rhetorical setup | "Think about it: how many good engineers have you lost to a two-week gap between screens?" | drop "Think about it:"; state the two-week gap as a fact

Self-answered question + stacked fragments | "...between screens? Too many. That's the whole story." | cut both fragments; "That's the whole story" is the stock "That's it. That's the whole thing." closer in a new coat

Kill-list cluster (4 in one paragraph) | "embark on a rebuild of the coordinator flow and harness a paradigm shift in how we book panels. Cutting-edge stuff." | embark, harness, paradigm shift, cutting-edge: say "we rebuilt the coordinator flow" and cut "Cutting-edge stuff."

Weak verb phrase | "decided to embark on a rebuild" | "rebuilt"

Colon reveal | "The thing that actually fixed it: one shared calendar." | plain sentence: "One shared calendar fixed it." ("actually" carries contrast against the hype line before it, so it can stay)

Weasel attribution (x2) | "Many argue that automation is paramount here, and industry reports suggest that companies who empower their talent teams see better outcomes" | name the source or cut the sentence; do not supply one

Kill-list words | "paramount", "empower" (same sentence) | cut with the sentence

Significance tail + importance puffery | "...solidifying their position as employers of choice." | cut the tail; the numbers two paragraphs down are the consequence

Portability | whole "Many argue..." sentence | it fits any company; replace with nothing, the next two paragraphs already carry the point

Weak verb phrase | "gives our team the ability to book a panel in under a day" | "lets our team book a panel in under a day" (keep "under a day")

Empty adverb + portable claim | "It has genuinely improved candidate experience across the board." | cut "genuinely"; "across the board" says nothing, and the 58% to 71% line already proves it. Consider cutting the sentence

Interpretive metadiscourse | "Worth sitting with that for a second." | delete; if the point is clear the aside is noise, and the numbers follow anyway

Empty adverb | "The rollout was inevitably a bit messy." | cut "inevitably"

Recap ending | "Overall, this quarter's changes reflect a multifaceted commitment to hiring excellence..." | delete the sentence; end on "We fixed it." or on the numbers

Kill-list words | "multifaceted", "underscoring" (closing paragraph) | cut with the sentence

Inflated copula + significance tail + portability | "reflect a multifaceted commitment to hiring excellence, underscoring the value we place on every candidate" | "reflect a commitment" is "is"; the "-ing" tail asserts importance nothing earned; the whole line would survive in any company's memo

Fake-profound kicker + negative parallelism (2 of 2) | "Hiring isn't a funnel. It's a conversation." | delete, do not rewrite into a better metaphor; the piece exceeds the one-per-piece bound on "It's not X. It's Y."

Borderline, lean leave | "Our recruiter drops the request. The coordinator picks a slot. The scheduler sends the invite." | three identically shaped sentences, but they describe three real steps by three real actors. Leave unless the writer agrees it reads as a drumbeat

Checked and clean: no em dashes anywhere in the draft; no emoji; no bold scattered on ordinary words; no inline-header bullet lists.

Density note: the two heavy paragraphs are "So we decided to embark..." (four kill-list words plus a colon reveal) and the last one (two kill-list words, a recap, a tail, a kicker). The rest of the draft is mostly clean; the tells sit in clusters, which is what makes them fixable without touching the writer's voice.

These are patterns in the text, not a verdict on its author.

Happy to edit it afterwards if you want the fixes applied. The edit would be small: most of the slop is in two paragraphs and the four setup lines, and the middle of the piece holds up.

## Recognition basis

### (a) Recognised from wording printed verbatim or near-verbatim in the skill's files

- "Let me be clear." Listed word for word in SKILL.md's phrases to drop and in ai-tells.md under throat-clearing openers.
- "The part everyone misses". Word for word in SKILL.md's faux-insight bullet and in ai-tells.md.
- "It's not a sourcing problem. It's a scheduling problem." The "It's not X. It's Y." template is printed in both SKILL.md and ai-tells.md; only the nouns are new.
- "Think about it:". Word for word in ai-tells.md's rhetorical setups.
- "That's the whole story." Near-verbatim of the stock closer "That's it. That's the whole thing." quoted in SKILL.md, ai-tells.md and human-prose.md.
- embark, harness, paradigm shift, cutting-edge, paramount, empower, multifaceted, underscoring. All eight are on the printed kill-list.
- "Many argue", "industry reports suggest". Both appear word for word in the weasel attribution lists in SKILL.md and ai-tells.md.
- "solidifying their position as". SKILL.md prints "solidifies its position" under importance puffery.
- "Overall," as a closing move. Named explicitly in SKILL.md's kickers-and-recaps bullet and ai-tells.md section 5.
- "inevitably". On the often-empty adverbs list verbatim.
- "gives our team the ability to". Near-verbatim of the "has the ability to" to "can" example in ai-tells.md and human-prose.md.
- Title Case in the heading. The formatting rule is printed, and the heading is a textbook instance.
- "Hiring isn't a funnel. It's a conversation." The wording is new, but the shape is the printed example "The future isn't coming. It's already here." with the nouns swapped, so I count it as template recognition rather than rule application.

### (b) Applied a pattern rule to wording I had not seen in the skill

- "The thing that actually fixed it: one shared calendar." Colon reveal. The skill's examples are "The best part: it learns" and "The detail that makes it work: ..."; this phrasing is not printed. I also had to judge whether "actually" was empty and decided it carries contrast.
- "Worth sitting with that for a second." Interpretive metadiscourse. The printed examples are "That last part matters more than it sounds", "The key point is", "As you can see". This is a different sentence doing the same job.
- "It has genuinely improved candidate experience across the board." "genuinely" is not on the adverb list; I treated it as the same class (a sincerity marker carrying nothing). "across the board" flagged by the portability test, not by any listed phrase.
- "reflect a multifaceted commitment to hiring excellence". "reflect" is not in the printed inflated-copula list (serves as, stands as, represents, boasts, features); I applied the "anything but plain is/has" rule. "hiring excellence" and "employers of choice" flagged by portability, not by a list.
- "...underscoring the value we place on every candidate." The word is on the list, but reading the clause as a significance tail is a rule application: the printed examples are "highlighting the team's commitment to innovation" and "creating a lively community hub".
- "see better outcomes". Vague claim adjacent to real numbers; portability test, no listed phrase.
- "Too many." Self-answered question. The skill names the "Question? Answer." pair as a pattern without a printed example matching this.
- Counting two negative parallelisms against the "at most one in a piece" bound. Threshold applied, not phrase recognition.
- Counting four kill-list words in one paragraph against the "two in a paragraph is a cluster" threshold.
- The borderline three-sentence process description. Repeated-sentence-shape rule weighed against the "genuinely parallel items" exemption; I chose to leave it.
- Checking for em dashes, emoji, bold, and inline-header bullets and finding none. Rule applied, nothing found.
- Keeping "Honestly?" on purpose. Judgment call using the keep-rule for real hedges and spoken rhythm; "honestly" is on the empty-adverb list, so this is the list overridden by the rule rather than followed.

Honest summary of the split: roughly two thirds of the findings were phrase recognition. The audit would have caught the heavy paragraphs from the kill-list alone. The findings that needed a rule rather than a lookup were the colon reveal, the metadiscourse aside, "genuinely", "reflect", "across the board", the self-answered question, and the two threshold counts.

## Preservation

Lines I would leave untouched if asked to edit, and why.

- "Recruiting has been rough this year." Blunt, plain, the writer's cadence. Becomes the opening line once "Let me be clear." goes.
- "We had plenty of candidates. We could not get them in front of anyone." Two short sentences stating the problem in the writer's words. No tells.
- "a two-week gap between screens". A specific fact sitting inside a flagged setup; the setup goes, the fact stays.
- "one shared calendar". The core fact of the piece. The colon reveal around it is the problem, not the phrase.
- "Our recruiter drops the request. The coordinator picks a slot. The scheduler sends the invite." Three real steps, three real actors, plain verbs. The only thing against it is the identical shape, and the exemption for genuinely parallel items covers it.
- "book a panel in under a day". The specific claim; only the verb phrase around it changes.
- "Time-to-schedule dropped from 11 days to 1.4 days over 63 open roles between July and September. Offer acceptance went from 58% to 71%." The two best sentences in the draft. Four numbers, a date range, a sample size. Not one character changes, and nothing in an edit may smooth them into "significantly faster".
- "Honestly? I pushed back on this project for two months because I thought it was busywork, and I was flat wrong about that. Rachel called it before any of us did. Credit where it's due." Honest admission, a named person, spoken rhythm, a fragment that lands. "Honestly" stays as the writer's real hedge and is named as kept. This is the paragraph the writer would most recognise as theirs.
- "Two panels got double-booked in week one. We fixed it." Specific failure, blunt fix. "We fixed it." is the strongest candidate for the final line once the recap and kicker are gone.
- The order of the piece: problem, cause, fix, process, results, admission, rollout. It already runs the way a reader needs it, so no reordering.
- The absence of em dashes, emoji, bold, and bullet lists. Nothing to override.


## Raw output: tone-mood brief

# Run: tone and mood brief

Settings used: task 1 is professional tone, concise mood; task 2 is the product default, neutral tone, concise mood.

## Task 1: email to Priya Nair

**Subject:** Card ending 4471 declined: update it by Friday 10 October

Hello Priya Nair,

The payment on your card ending 4471 was declined on 6 October 2026. Please update the card by Friday 10 October 2026 at lumenbooks.example/billing to keep your account active. After that date the account pauses.

You can reach billing at billing@lumenbooks.example.

Regards,
Orlando
Billing lead, Lumen Books

## Task 2: delete dialog and toast

| Key | String | Where | Limit |
|---|---|---|---|
| project.delete_dialog.title | Delete '{project_name}'? | Dialog title | 40 chars |
| project.delete_dialog.body | This removes the project for you and {count} other people in this workspace. You can restore it from Trash for 30 days. | Dialog body | 2 lines |
| project.delete_dialog.confirm | Delete project | Dialog confirm button, not the default focus | 2 words |
| project.delete_dialog.cancel | Cancel | Dialog cancel button, default focus | 1 word |
| project.deleted_toast.body | '{project_name}' deleted. You can restore it from Trash for 30 days. | Toast after deletion | 1 line |
| project.deleted_toast.undo | Undo | Toast action button | 1 word |

Notes for the developer:

- `{project_name}` is user supplied; keep the single straight quotes around it in the string, matching the product's quote style.
- `{count}` takes ICU plural forms: `{count, plural, one {# other person} other {# other people}}`. With this project the body renders as "This removes the project for you and 4 other people in this workspace."
- The toast is informational and dismissible. Undo restores the project directly; after the toast closes, Trash is the path back.
