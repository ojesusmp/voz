# Answer key for tone-mood-brief.md

Mechanical where possible. Run `python tests/lint-output.py --ui` on the output first; any
finding there is a failure on its own. Then score the rows below.

## Task 1: the email (professional + concise)

| # | Check | Pass when |
|---|---|---|
| E1 | Facts survive | 4471, 6 October 2026, Friday 10 October 2026, lumenbooks.example/billing, billing@lumenbooks.example all present and unchanged |
| E2 | Subject line is the news | Subject names the declined payment or the deadline. Not "Quick question", "Following up", "Important". |
| E3 | Point in the first sentence | The first sentence of the body says the card was declined. No "I hope this finds you well". |
| E4 | Professional distance | Greeting uses "Priya Nair" or "Priya" (not "Hey", not "Ms Nair", not "Dear Madam"); no jokes; no exclamation marks; sign-off is "Regards" or "Best regards" with full name and role |
| E5 | Concise | Six sentences or fewer in the body. No acknowledgment paragraph, no restating the thread, one ask. |
| E6 | Blame-free | The sentence that reports the decline has the bank or the payment as the actor, not "you". |
| E7 | No announced empathy | No "I understand how frustrating". |
| E8 | Nothing invented | No reason for the decline the brief did not give, no discount, no "many customers". |

Target 8 of 8. E1 or E8 failing fails the task on its own.

## Task 2: the dialog and toast (product default: neutral + concise)

| # | Check | Pass when |
|---|---|---|
| U1 | Title names the object | Title contains "Q3 budget", or a named placeholder such as {project_name} that renders to it, and a question mark. Not "Are you sure?". |
| U2 | Body states consequence and reversibility | Mentions the 4 other people (or "everyone in the workspace") and the 30-day Trash restore. |
| U3 | Confirm button repeats the verb | "Delete project" or "Delete 'Q3 budget'". Not "OK", "Yes", "Confirm". |
| U4 | Cancel is "Cancel" | Exactly. |
| U5 | Toast confirms the specific thing with undo | Names "Q3 budget" (literally, by placeholder, or as "project"), says it was deleted or moved to Trash, and has "Undo". No "successfully", no "!" |
| U6 | Mechanics | Sentence case throughout; no period on buttons; period on full sentences |
| U7 | Handoff shape | A table (or JSON) with a key per string and a where/limit column; keys name screen.moment.part |
| U8 | Nothing invented | No extra strings about billing, no marketing, no second confirmation step |

Target 8 of 8.

## Task 3: the Spanish email (Puerto Rico, neutral + empathic)

Run `python tests/lint-output.py --es-pr` on it first; any finding is a failure.

| # | Check | Pass when |
|---|---|---|
| S1 | Facts survive | 4471, 6 de octubre de 2026, viernes 10 de octubre de 2026, lumenbooks.example/billing, billing@lumenbooks.example |
| S2 | tú throughout | Second-person singular informal everywhere (actualiza, tu tarjeta, puedes). No "usted", no "vosotros". |
| S3 | Puerto Rican vocabulary | No ordenador, móvil, pulsar, pinchar, vídeo, vale, coche. "Rechazada" or "declinada" both pass. |
| S4 | Opener and closer | Opens with "Hola" or "Saludos" (or "Buenos días"); closes with "Saludos", "Cordialmente", or the team's name. No "Estimado/a", no "Bienvenido/a". |
| S5 | Date written out | "6 de octubre de 2026" with a lowercase month. No numeric 6/10 or 10/6. |
| S6 | Empathic, not announced | One clause naming her situation; no "Entendemos lo frustrante que". |
| S7 | Blame-free | The payment or the bank is the actor ("el pago no se procesó", "la tarjeta fue rechazada"), not "no pagaste". |
| S8 | Nothing invented | No cause beyond the decline itself, no discount, no "muchos clientes". Signed by the team, not by a named person. |

Target 8 of 8.

## Preservation and restraint

| # | Must hold |
|---|---|
| P1 | The model did not ask a question before delivering; the brief gives enough. |
| P2 | The model stated its setting only once, or not at all. No lecture about tone theory. |
