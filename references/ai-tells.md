# AI-writing tells: the full catalog

_Last re-dated: 2026-09. This vocabulary list ages on purpose ("delve" spiked in 2023 and faded by 2025), so refresh it roughly twice a year. The patterns outlast any specific word._

The signals that make text read as machine-written. Use this as the deep reference behind the kill-list in `SKILL.md`. Every item here is a *probability*, not a verdict. The diagnostic is density: humans use any one of these occasionally; models stack many of them in one piece.

Provenance: the primary source is the Wikipedia community catalog [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). It is reinforced by three peer-reviewed corpus studies: Kobak et al., *Science Advances* 2025 ([15M+ PubMed abstracts](https://www.science.org/doi/10.1126/sciadv.adt3813)); Yakura et al. ([740K+ hours of speech](https://arxiv.org/abs/2409.01754)); and Zaitsu et al., *PLoS ONE* 2025 ([surface-cue judgment study](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0335369&type=printable)). A ranked phrase list comes from [GPTZero](https://gptzero.me/news/most-common-ai-vocabulary/) (Oct 2024 snapshot). Items marked **(editorial)** come from editorial practice rather than a corpus study: widely observed, not measured.

---

## 1. Word choice (the strongest single category)

The Wikipedia catalog says it plainly: an edit introducing "lots of them, lots of times, is one of the strongest tells for AI use." Kobak et al. confirmed an abrupt post-ChatGPT spike and found that 66% of the excess words were verbs and 14% adjectives. These are *style* words, not topic words, which is what makes them detachable from any subject.

**Era-stamped vocabulary** (the list shifts over time, so date it):

- *2023 to mid-2024:* delve, intricate/intricacies, tapestry, testament, underscore(s), boasts, pivotal, enduring, meticulous, garner, bolster, interplay, realm, multifaceted.
- *Mid-2024 to mid-2025:* align with, enhance, foster/fostering, showcase/showcasing, leverage, seamless, elevate, navigate (figurative), vibrant, robust, nuanced, noteworthy, groundbreaking, transformative.
- *Highest raw volume* (Kobak frequency-gap leaders): potential, findings, crucial.
- *Most ratio-inflated* (appear many times more often in AI text): delves, underscores, showcasing.
- *2025 to 2026 (editorial):* utilize, facilitate, empower, streamline, harness, embark, paramount, cutting-edge, game changer, paradigm shift, ever-evolving, beacon, supercharge, "this is huge", "this changes everything".

**Often-empty adverbs (editorial).** just, literally, honestly, simply, actually, truly, fundamentally, importantly, crucially, inherently, inevitably. These are intensifiers and sincerity markers that usually add nothing to the claim. The rule is cut-or-keep, not ban: cut when the sentence means the same without it, keep when it carries emphasis, contrast, real uncertainty, or the writer's spoken rhythm. "It literally takes one command" is padding. "I literally could not open the file" is a person talking.

**Weak verb phrases (editorial).** A verb turned into a noun and propped up with a helper. Put the verb back: "made a decision" to "decided", "has the ability to" to "can", "is able to provide" to "provides", "conducted an analysis of" to "analysed", "gave consideration to" to "considered". This is one of the few tells you can fix mechanically without reading for meaning.

**The "anything but plain is/has" pattern.** Models avoid simple copulas. They write "serves as a", "stands as a", "marks", "represents", and they replace "has" with marketing verbs: "boasts", "features", "offers", "maintains". Most of the time the honest word is *is* or *has*.

**Significance and legacy clichés:** "stands as a testament to", "plays a vital role", "underscores its importance", "leaves an indelible mark", "cements its place", "a rich tapestry of", "the ever-evolving landscape of", "deeply rooted in".

**GPTZero's ranked phrase list** (Oct 2024, treat multipliers as illustrative not exact): "play a significant role in shaping", "showcasing", "remarked", "aligns", "aims to explore", "in today's fast-paced world", "notable works include", "surpassing", "tragically", "impacting".

**Filler openers:** "It's important to note that", "It's worth mentioning", "Needless to say", "When it comes to", "In the world of", "At the end of the day", "More than just", "At its core", "In the age of", "The reality is", "The truth is", "In terms of", "With regard to", "In order to", "Going forward", "In this article", "Let's dive in".

---

## 2. Sentence and grammar patterns

**Rule of three.** Models reach for three parallel items to sound comprehensive: "innovative, scalable, and reliable" / "she came, she saw, she conquered" applied to everything. The Wikipedia catalog notes AI "uses this pattern to make superficial analyses seem more thorough." One Fortune-500 analysis found this rising, not fading. Fix: deliberately use one, two, or four items, and vary across a piece.

**Negative parallelism.** Two sub-forms, both flagged:
- "Not just X, but Y" / "Not only X but also Y."
- "It's not X. It's Y." (denies the first thing entirely for drama).

Example tell: "It's not a product launch. It's a paradigm shift." A reader who sees one of these per page notices. They are strong devices used rarely, noise used often.

**Trailing participial significance phrases.** Attaching an "-ing" clause at sentence end that asserts impact without support: "...creating a lively community hub" / "...further enhancing its global significance." Usually unsourced synthesis. Cut the tail or attribute the claim.

**Vague attribution and over-generalization:** "Industry experts agree", "Observers have noted", "Some critics argue", "Studies show" (with nothing cited), "industry reports suggest", "many argue", "widely regarded as", "such as" before an exhaustive list. One real source gets inflated into "several scholars". The fix has a hard edge: name the source or cut the claim. If you are editing and the writer has no source, ask them or flag it. Never supply a source yourself, and never invent a plausible-sounding one.

**Throat-clearing openers (editorial).** "Here's the thing", "Here's what I mean", "Let me be clear", "I'll be honest", "The uncomfortable truth is". A sentence that only announces the sentence after it. Cut it and state the point.

**Faux-insight setups (editorial).** "This is the part most people skip", "What most people get wrong", "Here's what nobody tells you", "The part everyone misses". They flatter the writer as the lone expert who sees what others cannot, and they delay the claim. Cut the setup and let the claim carry itself. "The part everyone misses: distribution is the real moat" becomes "Distribution is the moat."

**Rhetorical setups (editorial).** "What if I told you...", "Think about it:", "Plot twist:", and the self-answered "Question? Answer." pair. Drop the setup and make the point.

**Colon reveals (editorial).** A noun phrase, a colon, then a short dramatic reveal: "The detail that makes it work: a separate agent grades it." "The best part: it learns." Rewrite as a plain sentence. Colons are for lists, labels, and quotes, not for drama. Related: use sentence case after a colon unless grammar, a proper noun, a title, or code requires otherwise. Note the trap in this house: voz tells you to replace em dashes with colons, and a careless swap turns an em dash into a colon reveal.

**Negative listing (editorial).** "Not a X. Not a Y. A Z." A cousin of negative parallelism that stacks the denials for rhythm. Say Z.

**Dramatic fragmentation (editorial).** "X. And Y. And Z." or "That's it. That's the whole thing." This is the one place voz needs a bound rather than a ban, because voz permits fragments on purpose. A fragment after a long sentence is a beat and it is good. Three in a row is a drum solo, and the stock closer "That's it. That's the whole thing." is a cliche whatever the rhythm around it. If you have three fragments in a row, two of them are decoration.

**Synonym cycling (editorial).** Rotating words for one thing so as not to repeat yourself: "The agent reviews the draft. The assistant scores the piece. The tool suggests fixes." All three are the same program, and the reader now wonders whether they are three things. If the clear word is right, repeat it. (Note this is the general rule; `registers.md` already required it for technical writing.)

**Abstractions doing human verbs (editorial).** "The decision emerged." "The data suggests we should feel." "The landscape demands." An abstract noun performing a human action hides who acted. The boundary matters: "the cron job corrupts the file" is fine, because a cron job is a real actor doing a real thing. The tell is the abstraction standing in for a person.

---

## 3. Punctuation and formatting

**Title Case In Headings.** Models capitalize all main words in section headings. Standard human and house style is sentence case ("Section heading", not "Section Heading").

**Mechanical boldface.** Bolding ordinary words for emphasis, or bolding every instance of a chosen term. Reads as a slide deck, not prose.

**Inline-header bullet lists.** The "`- **Term:** description`" pattern repeated down a vertical list, where a paragraph or a simple list would serve. Use lists for genuinely parallel, scannable items, not to shred prose into fragments.

**Numbered lists replacing sentences.** Turning a two-step explanation into "1. ... 2. ..." when a sentence carries it fine.

**Emoji as structure.** Emoji as section headers or bullet markers (✅, 🚀, 🔑). Almost always a tell outside casual social posts.

**Em dashes: the honest version.** The popular "em dash = AI" claim is *overstated*. Deep research did not support the idea that the em dash is the most recognizable AI tell. Models do overuse em dashes, but a single em dash proves nothing, and plenty of human writers love them. For `voz`, the operative rule is a house preference: **zero em dashes.** Replace with a comma, a colon, parentheses, or split into two sentences. Do not treat other people's em dashes as proof of anything.

---

## 4. Tone and stance

**Forced significance on trivial things.** Even mundane subjects get a hedged importance statement. Etymology sections get "reflecting broader cultural trends." Population data gets "underscoring the region's dynamic growth."

**Promotional drift.** Travel-brochure and press-release tone: "nestled in the heart of", "renowned for its", "a diverse array of", "boasting natural beauty". Wikipedia flags this as advertisement tone.

**Over-hedged courtesy and self-narration.** "Certainly! Here's...", "I hope this helps!", "Great question!", "Let me break this down for you." Stock framing that surrounds the actual answer.

**False balance.** Presenting a fringe claim as equal to documented consensus to seem even-handed.

**Interpretive metadiscourse (editorial).** Lines that step outside the subject to tell the reader what to notice or how much weight to give it: "That last part matters more than it sounds", "The key point is", "As you can see", "This distinction matters", and a redundant "In other words". The test is simple. If the point is already clear, the aside is noise and you delete it. If the point is not clear, the aside does not fix it; add the missing fact instead.

**Fake-profound kickers (editorial).** The final "deep" line that turns the point into a metaphor, an aphorism, or a mic-drop: "The future isn't coming. It's already here." Delete it. Do not rewrite it into a better metaphor, and do not preserve its rhythm with something else; the impulse to land a closing beat is the problem. End on the clearest concrete sentence already in the piece. If the ending needs closure, use a plain takeaway or the next action.

**The "Challenges and Future Prospects" template.** A rigid closing pattern: "Despite its [positives], [subject] faces challenges including... Looking ahead, future initiatives aim to..." Formulaic and content-free.

---

## 5. Structure

- Standalone summary sentences at the end of every section.
- Outline-shaped articles with parallel "Challenges", "Legacy", "Future Prospects" sections full of formulaic language.
- Conclusions that restate the intro with no new information ("In conclusion, X is a multifaceted topic that..."). Also "Ultimately", "Overall", and any final paragraph that summarises what the reader just read. End on the last concrete point, takeaway, or next action instead.
- A heading over a section of two sentences. Headings promise structure; use one when there is structure.
- Leads that treat a common-noun title as a proper noun: "Catchment Area (Health) refers to..." instead of natural phrasing.

---

## 6. Citation and markup tells (mostly for published/wiki content)

- Broken external links, invalid DOIs or ISBNs, DOIs that resolve to unrelated articles.
- Book citations with no page numbers or URLs.
- Fabricated shortcuts, templates, or policies that do not exist.
- Leftover model artifacts in text: `contentReference`, `oai_citation`, `:::`, `turn0search0`, `utm_source=` tracking tails copied from a browser.
- Markdown mixed into a wiki/HTML context (`**bold**` where the platform uses other markup).

---

## 7. Spanish (editorial, unverified)

`voz` is named in Spanish and gets used on Spanish copy, but every source cited above studied
English. This section is working knowledge, **not** backed by a corpus study or a catalog, and it
carries no dates because nobody has measured when these rose. Treat it as a starting list to
check against real Spanish drafts, not as evidence, and verify before relying on it for anything
client-facing.

**Stock phrases:** "en el mundo actual", "en la era digital", "cabe destacar", "cabe mencionar",
"es importante destacar/mencionar/senalar", "sin lugar a dudas", "sin duda alguna", "en
definitiva", "en resumen", "un abanico de", "una amplia gama de", "el mundo de", "a la hora de",
"no solo X, sino tambien Y" (the Spanish negative parallelism), "sumergirse en" (the local
"delve"), "desbloquear el potencial", "llevar al siguiente nivel", "marcar la diferencia".

**Shapes:** the same rule of three, the same "-ando/-iendo" significance tail
("consolidando su posicion como", "reflejando su compromiso con"), and the same closing
"En conclusion" recap. Spanish tolerates longer sentences than English, so length alone is a
weaker signal there; tangle still is not.

**One thing that does not transfer:** the em dash. The raya is standard Spanish punctuation for
dialogue and parenthetical asides, so its presence carries no signal at all in Spanish prose. The
house rule of zero still applies to what `voz` writes, because it is a house preference rather
than a tell, but never read a Spanish writer's raya as evidence of anything.

---

## 8. How to use this list

1. **Judge the cluster, not the word.** One flagged word in clean prose is fine. Five is a pattern. Ten is a fingerprint. A working threshold, offered as a house heuristic and not as a research finding: two flagged items in one paragraph is a cluster, so fix the paragraph; one every few hundred words is ordinary English, so leave it alone.
2. **A word quoted as an example is not a tell.** This file is full of flagged words. So is any audit report. Only count a word the text is using, not one it is naming.
3. **Surface cues are what readers actually weigh.** Zaitsu et al. found human judges react to phrasing, word endings, conjunctions, and punctuation, not deep structure. Controlling the surface is most of the battle.
4. **Keep it current.** Re-date this list periodically. When a word becomes a known tell, models and writers both move off it, and a new cluster forms.
5. **Never use it as a detector.** Adversarial paraphrasing defeats every feature set, and detectors produce false positives (one Stanford study found ~61% false-positive rates on non-native English writing). This file is for writing well, not for accusing anyone.
