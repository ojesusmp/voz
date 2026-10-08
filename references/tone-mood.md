# Tone and mood: the two dials

Register (in `registers.md`) is the job a piece of writing does: sell, bind, instruct, report. Tone and mood are two dials laid on top of whatever register is in play. They change how close the writer stands to the reader and what the writer leads with. They do not change the facts, the structure the register demands, or any rule in the kill-list.

Set them when the user names them ("casual", "keep it professional", "the short version", "make it sound like it came from the company"). Infer them from the surface when the user does not. When nothing points either way, the default is **neutral tone, empathic mood**, which is the house voice described in `SKILL.md`.

## Tone: how far the writer stands from the reader

| | Casual | Neutral (default) | Professional |
|---|---|---|---|
| Who it fits | Teammates, friends, consumer apps, texts | Most email, docs, product copy, support | Clients, executives, external partners, anything that may be forwarded |
| Address | First name, "hey", "you" freely | First name, "hi", "you" | Full name, or name and title, until they drop it; "hello" or no greeting |
| Contractions | Always | Yes | Sparingly, and never in a sentence that carries a commitment or a refusal |
| Sentence length | Short, spoken | Mixed | Mixed, leaning complete |
| Humor and asides | Welcome if they are yours | A light one, rarely | None |
| Exclamation marks | One per message at most | Rare | None |
| Emoji | If the channel already uses them | No | No |
| Sign-off | "thanks", first name, or nothing | "Thanks," and your name | "Regards," or "Best regards," with full name and role |

Casual is not sloppy, vague, or padded with "lol" and "haha". A casual message still says the specific thing, with the date and the number. Professional is not stiff, Latinate, or hedged into mush. "Use" still beats "utilize" in a letter to a CEO. The kill-list applies at every setting.

## Mood: what the writer leads with

| | Empathic (default) | Concise | Corporate |
|---|---|---|---|
| Opening move | One clause that meets the reader where they are, then the help | The answer or the ask, in the first words | The headline fact, dated and owned |
| Pronouns | "you", and "I" or "we" as fits | "you", with the fewest words around it | "we" for the organisation; no "I" |
| Acknowledgment | Once, specific to their situation | Only if the reader is upset or lost something | As fact, not feeling: "The outage affected 1,200 accounts" |
| Hedging | Once, if the claim needs it | None, unless the uncertainty is the point | Calibrated: "we expect", "the data suggests" |
| Length | As long as the help needs | The shortest useful version | Short paragraphs, one idea each |
| Close | Next step, offered | Next step, stated | The ask, or "no action needed" |

Concise is not curt. It still frames causes rather than faults, and it still gives the next step. It cuts the greeting ceremony, the acknowledgment the reader did not need, and every sentence that repeats another one.

Corporate is a mood, not the Corporate register. The register is a whole document shape (board update, investor note, all-hands) with its own structure in `registers.md`. The mood is the institutional stance on its own, and it fits a two-line Slack announcement or a status page entry as well as a memo. Use it when the words come from the company rather than from a person. Do not use it when a person is owed a personal answer.

Empathic is never announced. "I completely understand how frustrating this must be" is the AI tell for empathy. Show it by naming their actual situation and getting to the help fast.

## The same message, nine ways

A customer's card was declined. They have until Friday to update it or the account pauses.

- **Casual + empathic.** "Hey Dana, your card got declined on last night's charge. That's usually the bank flagging it, not anything on your end. Update it when you get a sec, ideally before Friday so nothing pauses."
- **Casual + concise.** "Hey Dana, your card was declined. Update it before Friday or the account pauses: [link]."
- **Casual + corporate.** Rarely coherent. If the channel is casual and the voice is the company's, write neutral + corporate and say so.
- **Neutral + empathic.** "Hi Dana, last night's payment didn't go through. That usually means the bank declined the charge, not that anything is wrong with your details. Update the card before Friday and the account stays active: [link]."
- **Neutral + concise.** "Hi Dana, your payment on 6 October was declined. Update your card by Friday 10 October to keep the account active: [link]."
- **Neutral + corporate.** "Payment for account 4471 was declined on 6 October. The account remains active until Friday 10 October. Updating the card before then keeps service uninterrupted: [link]."
- **Professional + empathic.** "Hello Dana, the payment for your account was declined on 6 October. This is usually a bank-side check rather than an error in your details. Updating the card before Friday 10 October keeps the account active, and I am glad to help if the bank needs anything from us."
- **Professional + concise.** "Hello Dana, the payment on 6 October was declined. Please update the card by Friday 10 October to keep the account active: [link]."
- **Professional + corporate.** "Dear Dana Whitfield, the payment for account 4471 was declined on 6 October 2026. Service continues until Friday 10 October 2026. To avoid interruption, update the payment method before that date. Our billing team can be reached at billing@example.com."

What stays the same in all nine: the date, the deadline, the consequence, the link or contact, and the absence of blame. Only the distance and the lead change.

## Picking the dials when nobody says

| Surface | Default setting |
|---|---|
| Text message, team chat, Slack or Teams DM | Casual + concise |
| Internal email, support reply, documentation | Neutral + empathic |
| Email to a client, a partner, an executive, or anyone outside the company | Professional + empathic |
| Incident update, status page, release note, changelog | Neutral + concise |
| Announcement in the company's name, policy change, compliance notice | Neutral + corporate |
| Product strings: buttons, errors, empty states, toasts | Neutral + concise (see `ui-copy.md`) |
| Anything a lawyer will read | Professional, in the Lawyer register |

If the user's own message is casual, match it one step more carefully than they wrote, not two. Someone who writes "yo can u fix the invoice email" wants casual output, not a formal letter, and not a copy of their typos.

When a register and a dial conflict (a casual demand letter, a corporate bedtime explanation), the register's structure wins. Say which dial you dropped, in one line.

## Message shapes

Tone and mood decide the words. These decide the order, and they hold at any setting.

**Email.**
- The subject line is the news or the ask, with the date if there is one: "Invoice 2231: payment due 15 October". Not "Quick question", not "Following up".
- The first sentence is the point. The reader decides from it whether to read on.
- One ask per email. A second ask gets its own email, or a numbered list with an owner and a date on each line.
- Say what you need, from whom, and by when, in one line the reader can paste into a to-do.
- Context goes after the ask. The reader who already knows it skips it; the one who does not reads down.
- Close with the next step and a sign-off that matches the tone. No "I hope this email finds you well", no "please do not hesitate to reach out".
- Replying in a thread: answer first, quote only the line you are answering, do not restate the thread.

**Chat message.** One message, not five in a row. Lead with the ask or the answer. "Hi" alone, then a pause, then the question, tells the reader you had not decided what you wanted. Put the question in the first message. Anything longer than three lines goes in a thread or a doc.

**Follow-up.** The original ask and its date, what has happened since, and the new date. No "just checking in", no "bumping this", no apology for following up.

**Saying no.** The answer in the first sentence, the reason in one, the alternative if there is one. No cushion paragraph before the no. Thanking someone for their patience is not an answer.

**Bad news.** What happened, who it affects, what has been done, what happens next, when they will hear more. Each as a plain sentence. "Mistakes were made" hides the actor; "we deployed the wrong config at 14:10" does not.

**Apology.** One "sorry", tied to the specific thing, from the party at fault. Then the fix and the prevention. A second sorry weakens the first.

## Spanish

Tone maps onto the form of address. Casual is "tú", "hola", first names. Neutral is "tú" in consumer products and in most internal writing, "usted" where the reader, the region, or the company convention expects it; when unsure, write around the choice for a line or two with impersonal forms ("se puede", "hay que") rather than mixing. Professional is "usted", with the full name on first address. Never mix "tú" and "usted" inside one message.

Gender: prefer forms that do not force one when you do not know the reader. "Te damos la bienvenida" instead of "Bienvenido/a", "Hola, equipo" instead of "Hola a todos", "las personas usuarias" when "los usuarios" would read as exclusive in a formal context. Do not invent spellings ("todxs", "tod@s") unless the house style already uses them.

Mood translates directly. Concise Spanish still runs a little longer than concise English; tangle is the problem, not length.

## Gender awareness in English

Use the reader's name or role. "They" for anyone whose pronouns you do not know. No "guys", no "ladies and gentlemen", no "Dear Sir or Madam", no "Dear Sirs". A group is "everyone", "team", or "all". Job titles are neutral by default (chair, firefighter, salesperson). This holds at every tone, and in casual writing most of all, because that is where "hey guys" slips in.

## What never changes

Whatever the setting: the kill-list, zero em dashes, no invented facts or sources, the specific number and date survive, sentence case, one word per concept, and the reader is never blamed for what the system did.
