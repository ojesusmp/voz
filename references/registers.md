# The nine registers

Each register changes diction, rhythm, and rhetorical stance to fit a reader and a purpose. All nine keep the kill-list rules from `ai-tells.md`: no AI tells, ever, in any voice. What changes is everything else.

Foundational principle (Halliday's register theory, and [OpenOregon Technical Writing 2e §8.4](https://openoregon.pressbooks.pub/techwriting2e/chapter/8-4-tone/)): the writer's stance should match the audience and the purpose. Consistent, not identical. Pick the register from the artifact and the reader, then commit to it.

---

## 1. Empathetic-neutral (the default)

**Purpose.** Inform and help without friction. The reader is busy, possibly stressed, and wants to be treated as capable. This is the house voice for docs, support replies, chat, and anything with no reason to be otherwise.

**Diction.** Plain and common. Use/before/help, not utilize/prior to/facilitate. Warm but not chummy.

**Structure.** Varied sentence length. Lead with the answer, then the why. Impersonal cause-and-effect instead of second-person blame.

**Signature moves.**
- Replace fault framing with situation framing: "The system shuts down if an install error occurs" (not "You didn't install it correctly, so it shut down"). Example pair from OpenOregon §8.4.
- Acknowledge the reader's position in one clause, then get to the help.
- Hedge at most once, then state the thing.

**Sample opening.** "If the upload keeps failing, it is almost always the file size. Here is how to check and fix it in under a minute."

**Avoid.** Accusatory "you", cheerfulness that ignores the reader's problem, and the AI-tell habit of announcing empathy ("I completely understand how frustrating this must be!") instead of just being useful.

**When.** Default. Most writing and all normal conversation.

---

## 2. Salesman / closer

**Purpose.** Move one identified person toward a yes. One-to-one selling, proposals, objection handling, follow-ups. ([Persuasive business writing](https://www.instructionalsolutions.com/blog/types-of-business-writing); [sales closing technique](https://www.outreach.ai/resources/blog/sales-closing-techniques).)

**Diction.** Outcome words: results, save, faster, covered, guaranteed, worth. The buyer's language, not your product's.

**Structure.** Short and forward-moving. One idea per line. Questions that get a yes. End on the ask.

**Signature moves.**
- Lead with the buyer's outcome, not the feature. "You stop losing leads overnight" before "the system has 24/7 routing."
- Name the objection before they do, and answer it.
- Honest urgency: a real deadline, a real cost of waiting. Never manufactured scarcity.
- Assume the close: "Want me to set it up for Monday or Wednesday?"

**Sample opening.** "You told me the after-hours calls are the ones that hurt. That is exactly the gap this closes. Here is what it would cost you to keep losing them, and what it costs to stop."

**Avoid.** Hype, pressure that reads as desperation, feature dumps, and the rule-of-three benefit list ("powerful, flexible, and affordable"). Specifics close; adjectives do not.

**When.** A named prospect is deciding. Not for broadcast copy (that is Marketing).

---

## 3. Corporate professional

**Purpose.** Inform and align a mixed senior audience (leadership, the board, investors) and move them to a decision without surprises. Signals institutional competence and candor, not personal voice. ([HBR on business writing](https://hbr.org/2021/07/the-science-of-strong-business-writing).)

**Diction.** stakeholders, alignment, headwinds/tailwinds, cross-functional, deliverables, trajectory, run rate, risk mitigation, accountability, cadence, governance, north star, escalation path. Use them only where they carry precise meaning.

**Structure.** Sentences of 15 to 25 words, active voice, calibrated hedging ("we expect", "the data suggests"). Short paragraphs, one idea each, the load-bearing sentence first.

**Signature moves.**
- Headline first. State the decision or result in sentence one. ("Postponing the message to the middle" is the classic business-writing failure.)
- Frame bad news as context, then impact, then plan.
- "We" framing for shared ownership of results.
- Anchor every claim to a metric, a date, or a named owner.
- Close with a clear ask or an explicit "no action needed."

**Sample opening.** "Q3 revenue came in at $12.4M, 8% under target, driven by one delayed enterprise contract and softer SMB volume. This note covers what happened, what we are doing, and what to expect in Q4."

**Avoid.** Empty corporate-speak: synergy, circle back, boil the ocean, move the needle, low-hanging fruit, leverage (as a verb), think outside the box. The test: if the phrase fits any company on any topic, it is doing no work.

**When.** Board materials, all-hands from leadership, investor notes, official statements, decision escalations. Not casual team chat.

---

## 4. Lawyer / legal

**Purpose.** Precision that leaves no interpretive gap, enforceability, allocation of risk, preservation of rights. Dual audience: the other party who must act, and a court that may read it years later. (Bryan Garner, [*Legal Writing in Plain English*](https://press.uchicago.edu/ucp/books/book/chicago/L/bo199200593.html); [IRAC method](https://www.quimbee.com/resources/how-the-irac-method-can-improve-your-legal-writing).) *Style guidance only, not legal advice.*

**Diction, two kinds.**
- *Legalese to cut* (Garner): hereinafter, witnesseth, said (as "the"), pursuant to, provided that, in the event that, and/or, inter alia, prior to, notwithstanding-anything-to-the-contrary when sloppy.
- *Terms of art to keep*: indemnify, representations and warranties, covenant, force majeure, liquidated damages, estoppel, negligence. Courts have built meaning around these; plain synonyms lose the doctrine.

**Structure.** Define a term once in parentheses ("the 'Company'"), then use it identically every time. Numbered sections and lettered subsections for exact cross-reference. "Must" for obligation, "may" for permission, "will" for a future act (not the slippery "shall"). Conditions as explicit if/then.

**Signature moves.** Define then use; enumerate to remove ambiguity ("any claim, demand, action, or proceeding"); state the rule then apply it (IRAC); carve out exceptions precisely; qualify representations by knowledge or materiality to limit exposure.

**Sample openings.**
- Plain-drafting recital: "The parties enter this Agreement on [Date]. [Company] engages [Contractor] to perform the services in Exhibit A. The parties agree as follows:"
- Demand letter: "This firm represents [Client]. On [Date], your client breached Section 4.1 by failing to pay the $50,000 invoice. Unless paid in full by [Deadline], we will file suit without further notice."

**Avoid.** Ceremonial deadwood (know all men by these presents, comes now), and the opposite error: stripping a genuine term of art for a plain word that loses its settled meaning. Ask: does a court already know what this word means? If yes, keep it.

**When.** Contracts, NDAs, terms of service, demand and cease-and-desist letters, legal memos and briefs, compliance notices. Not for client-friendly explanations of those documents (use Empathetic or Teacher for that).

---

## 5. Journalist / plain-news

**Purpose.** Inform fast and neutrally. Most important fact first; a reader can stop anywhere and still have the story. Transmission, not persuasion. ([Inverted pyramid](https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism)); [Reuters Handbook](https://www.mediareform.org.uk/wp-content/uploads/2015/12/Reuters_Handbook_of_Journalism.pdf).)

**Diction and rules.** The 5 Ws and H. "Said" as the default attribution verb (neutral, invisible); "according to" for documents. Avoid loaded verbs (claimed, admitted, revealed, warned). "Alleged" for unproven accusations. Plain Anglo-Saxon words: fire not conflagration, buy not purchase. AP number rule (spell out one to nine, numerals for 10+). Full name and title on first reference, last name after.

**Structure.** A lede of 25 to 30 words answering the most important Ws, in one or two sentences. Then a nut graf (why it matters now). Then descending importance, each paragraph one to two sentences, self-contained so an editor can cut from the bottom. Active voice.

**Signature moves.** Inverted pyramid; attribute every claim to a named source; lead with the news not the background; show the fact instead of characterizing it; neutral framing without false balance.

**Sample opening.** "A $95 billion foreign-aid package passed the U.S. Senate on Wednesday, sending the measure to the president after weeks of stalled border-security negotiations."

**Avoid.** Editorializing adjectives (landmark, devastating, much-needed), opinion-smuggling adverbs (surprisingly, alarmingly), burying the lede, passive evasion ("mistakes were made"), unattributed assertion, and throat-clearing openers ("In a development that underscores growing tensions...").

**When.** Announcements, news, briefs, stripping spin out of a press release. The reader's first question is "what happened?" not "what does it mean?"

---

## 6. Marketing / copywriter

**Purpose.** Win attention and a click from a broad audience, fast. One-to-many. Landing pages, ads, headlines, email campaigns, social. ([Literary devices in copywriting](https://techhelp.ca/literary-devices-in-copywriting/); [rhetorical devices in copy](https://jotjotboom.com/blog/using-rhetorical-devices-in-copywriting).)

**Diction.** Concrete, sensory, benefit-led. "You" and "your". Verbs that move (get, build, ship, stop, skip). Specific nouns over category words.

**Structure.** Hook in the first line or you have lost them. Short. Rhythm and sound matter (alliteration, a deliberate fragment, a turn). One big idea, not five. One clear call to action.

**Signature moves.** Lead with the single strongest benefit; one concrete image beats a list of claims; a headline that promises something specific; social proof shown not asserted; close with one action ("Start free", "See it in 2 minutes").

**Sample opening.** "Your invoices are sitting in three different apps. This puts them in one, and tells you who hasn't paid before you have to ask."

**Avoid.** The everything-bagel of benefits, the rule-of-three slogan ("Fast. Simple. Powerful."), superlatives with no proof (revolutionary, world-class, cutting-edge), and clever that hides what the thing is. Distinct from Salesman: marketing is one-to-many and earns a click; salesman is one-to-one and earns a yes.

**When.** Public-facing copy meant to convert a stranger. Not for a 1:1 deal in motion.

---

## 7. Technical / engineer

**Purpose.** Let a competent reader do a task or understand a system correctly. Precision and completeness over personality. Specs, API docs, runbooks, architecture notes. ([Imperative-mood instructions](https://pressbooks.bccampus.ca/technicalwriting/); instructional writing principles.)

**Diction.** Exact and consistent. The same term for the same thing every time (no elegant variation: pick "request" or "call", not both). Defined acronyms on first use. Numbers, types, limits, units.

**Structure.** Short declarative sentences. Imperative mood for steps ("Run the migration", "Set `TIMEOUT` to 30"). Code and examples over adjectives. Tables and lists where data is genuinely tabular. Passive voice is acceptable when the actor is the system or irrelevant.

**Signature moves.** State preconditions before steps; one action per step, in order; show the exact command or payload; document the failure mode and the error, not just the happy path; cross-reference precisely.

**Sample opening.** "This endpoint returns a paginated list of orders. It requires a bearer token with the `orders:read` scope. Rate limit: 100 requests per minute."

**Avoid.** Marketing adjectives in technical text (powerful, seamless, robust), vague quantities ("large files", "a while"), undefined pronouns ("it returns this"), and decoration. If a sentence does not help the reader do the task, cut it.

**When.** Any artifact a developer or operator acts on. Distinct from Teacher: technical assumes competence and optimizes for reference; teacher builds understanding from less.

---

## 8. Teacher / explainer

**Purpose.** Build understanding in someone who does not have it yet. Guides, onboarding, tutorials, conceptual explainers. Accounts for the reader's current knowledge level. ([Instructional writing](https://www.instructionalsolutions.com/blog/types-of-business-writing).)

**Diction.** Plain, concrete, friendly. Define a term the first time you need it, in the flow. Analogies to things the reader already knows.

**Structure.** One idea at a time, in the order a learner needs them, not the order an expert would list them. Short paragraphs. A worked example after each concept. Frequent "here is why this matters" before "here is the detail".

**Signature moves.** Start from the reader's existing knowledge; introduce one new thing per step; analogy then literal; show a concrete example immediately; check understanding ("If that worked, you should see X"); anticipate the predictable confusion and address it.

**Sample opening.** "A webhook is just a phone number you give another service so it can call you when something happens, instead of you calling it over and over to check. Here is how to set one up."

**Avoid.** Assuming knowledge the reader lacks, dumping all the detail at once, jargon before it is defined, and the false-friendly AI tic of "Let's dive in!" or "Great, now let's explore...". Be genuinely clear instead of performing friendliness.

**When.** The reader is learning. If they already know the domain and want reference, use Technical.

---

## 9. Motivational speaker

**Purpose.** Move an audience from doubt to belief to action. Performs a transformation, not an argument. Pathos leads. ([Rhetorical triangle](https://fords.org/resource/rhetorical-triangle/); [future-pacing](https://magneticspeaking.com/future-pacing-simple-teahnique-big-impact-persuasion/).)

**Diction.** "You" and "your" above all. imagine, today, right now, decide, choice, become, rise, ready, enough, possible. Present and future tense. Concrete sensory verbs (feel the weight, hear your own voice, walk through that door).

**Structure.** Contrast short and long. A short line lands like a fist. Then a long, building, cumulative sentence that stacks clauses until the audience feels the momentum. Then a fragment. "Now." Cadence and the pause do real work; in writing, a one-line paragraph is the pause.

**Signature moves.** Anaphora (repeat the opening of successive lines to build, not pad); tricolon used on purpose; future-pacing ("imagine waking up a year from now, and today's fear is just the memory of what made you move"); a specific personal failure that turns into a universal lesson; the problem-then-turn ("And yet."); direct address to one imagined listener; a concrete call to action (a verb, not a vibe).

**Sample opening.** "You have been waiting for someone to give you permission. I am not going to do that. You already have it."

**Avoid.** This is the most cliché-prone register, so guard it hardest: believe in yourself, the sky's the limit, hustle harder, everything happens for a reason, you've got this. And avoid toxic positivity: name the real obstacle specifically before reaching for the resolution, or the uplift reads as dismissive. Specificity is the antidote.

**When.** A real transition point, used once, with genuine stakes. Do not use it when the reader needs to think clearly, is grieving or in crisis, or needs credibility with skeptics. It degrades analytical writing. Overused across a body of work it becomes noise and signals performed inspiration rather than the real thing.
