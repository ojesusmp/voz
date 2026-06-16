# AI-writing tells: the full catalog

_Last re-dated: 2026-06. This vocabulary list ages on purpose ("delve" spiked in 2023 and faded by 2025), so refresh it roughly twice a year. The patterns outlast any specific word._

The signals that make text read as machine-written. Use this as the deep reference behind the kill-list in `SKILL.md`. Every item here is a *probability*, not a verdict. The diagnostic is density: humans use any one of these occasionally; models stack many of them in one piece.

Provenance: the primary source is the Wikipedia community catalog [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). It is reinforced by three peer-reviewed corpus studies: Kobak et al., *Science Advances* 2025 ([15M+ PubMed abstracts](https://www.science.org/doi/10.1126/sciadv.adt3813)); Yakura et al. ([740K+ hours of speech](https://arxiv.org/abs/2409.01754)); and Zaitsu et al., *PLoS ONE* 2025 ([surface-cue judgment study](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0335369&type=printable)). A ranked phrase list comes from [GPTZero](https://gptzero.me/news/most-common-ai-vocabulary/) (Oct 2024 snapshot).

---

## 1. Word choice (the strongest single category)

The Wikipedia catalog says it plainly: an edit introducing "lots of them, lots of times, is one of the strongest tells for AI use." Kobak et al. confirmed an abrupt post-ChatGPT spike and found that 66% of the excess words were verbs and 14% adjectives. These are *style* words, not topic words, which is what makes them detachable from any subject.

**Era-stamped vocabulary** (the list shifts over time, so date it):

- *2023 to mid-2024:* delve, intricate/intricacies, tapestry, testament, underscore(s), boasts, pivotal, enduring, meticulous, garner, bolster, interplay, realm, multifaceted.
- *Mid-2024 to mid-2025:* align with, enhance, foster/fostering, showcase/showcasing, leverage, seamless, elevate, navigate (figurative), vibrant, robust, nuanced, noteworthy, groundbreaking, transformative.
- *Highest raw volume* (Kobak frequency-gap leaders): potential, findings, crucial.
- *Most ratio-inflated* (appear many times more often in AI text): delves, underscores, showcasing.

**The "anything but plain is/has" pattern.** Models avoid simple copulas. They write "serves as a", "stands as a", "marks", "represents", and they replace "has" with marketing verbs: "boasts", "features", "offers", "maintains". Most of the time the honest word is *is* or *has*.

**Significance and legacy clichés:** "stands as a testament to", "plays a vital role", "underscores its importance", "leaves an indelible mark", "cements its place", "a rich tapestry of", "the ever-evolving landscape of", "deeply rooted in".

**GPTZero's ranked phrase list** (Oct 2024, treat multipliers as illustrative not exact): "play a significant role in shaping", "showcasing", "remarked", "aligns", "aims to explore", "today's fast-paced world", "notable works include", "surpassing", "tragically", "impacting".

**Filler openers:** "It's important to note that", "It's worth mentioning", "Needless to say", "When it comes to", "In the world of", "At the end of the day", "More than just".

---

## 2. Sentence and grammar patterns

**Rule of three.** Models reach for three parallel items to sound comprehensive: "innovative, scalable, and reliable" / "she came, she saw, she conquered" applied to everything. The Wikipedia catalog notes AI "uses this pattern to make superficial analyses seem more thorough." One Fortune-500 analysis found this rising, not fading. Fix: deliberately use one, two, or four items, and vary across a piece.

**Negative parallelism.** Two sub-forms, both flagged:
- "Not just X, but Y" / "Not only X but also Y."
- "It's not X. It's Y." (denies the first thing entirely for drama).

Example tell: "It's not a product launch. It's a paradigm shift." A reader who sees one of these per page notices. They are strong devices used rarely, noise used often.

**Trailing participial significance phrases.** Attaching an "-ing" clause at sentence end that asserts impact without support: "...creating a lively community hub" / "...further enhancing its global significance." Usually unsourced synthesis. Cut the tail or attribute the claim.

**Vague attribution and over-generalization:** "Industry experts agree", "Observers have noted", "Some critics argue", "Studies show" (with nothing cited), "such as" before an exhaustive list. One real source gets inflated into "several scholars".

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

**The "Challenges and Future Prospects" template.** A rigid closing pattern: "Despite its [positives], [subject] faces challenges including... Looking ahead, future initiatives aim to..." Formulaic and content-free.

---

## 5. Structure

- Standalone summary sentences at the end of every section.
- Outline-shaped articles with parallel "Challenges", "Legacy", "Future Prospects" sections full of formulaic language.
- Conclusions that restate the intro with no new information ("In conclusion, X is a multifaceted topic that...").
- Leads that treat a common-noun title as a proper noun: "Catchment Area (Health) refers to..." instead of natural phrasing.

---

## 6. Citation and markup tells (mostly for published/wiki content)

- Broken external links, invalid DOIs or ISBNs, DOIs that resolve to unrelated articles.
- Book citations with no page numbers or URLs.
- Fabricated shortcuts, templates, or policies that do not exist.
- Leftover model artifacts in text: `contentReference`, `oai_citation`, `:::`, `turn0search0`, `utm_source=` tracking tails copied from a browser.
- Markdown mixed into a wiki/HTML context (`**bold**` where the platform uses other markup).

---

## 7. How to use this list

1. **Judge the cluster, not the word.** One flagged word in clean prose is fine. Five is a pattern. Ten is a fingerprint.
2. **Surface cues are what readers actually weigh.** Zaitsu et al. found human judges react to phrasing, word endings, conjunctions, and punctuation, not deep structure. Controlling the surface is most of the battle.
3. **Keep it current.** Re-date this list periodically. When a word becomes a known tell, models and writers both move off it, and a new cluster forms.
4. **Never use it as a detector.** Adversarial paraphrasing defeats every feature set, and detectors produce false positives (one Stanford study found ~61% false-positive rates on non-native English writing). This file is for writing well, not for accusing anyone.
