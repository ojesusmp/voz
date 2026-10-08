# UI copy: the words a visitor reads inside a product

Load this when the output is a string a product will show: a button, a label, a placeholder, an error, an empty state, a confirmation dialog, a toast, a tooltip, a notification, an onboarding step, a 404 page, or an email the system sends on its own. The reader is in the middle of a task. They read the string once, at a glance, often on a phone, often slightly annoyed. Nothing here is read for pleasure.

Everything in `SKILL.md` still applies. This file adds the rules that prose does not need. The default dials for product strings are neutral tone and concise mood (`tone-mood.md`).

## Four rules that cover most strings

1. **One job per string.** What happened, or what to do. Both when both matter. The reason only when it changes what the reader does next.
2. **Name the next action.** Every string that reports a problem ends in something the reader can do, or says plainly that there is nothing to do and who is on it.
3. **The system is the actor and the reader is never the fault.** "The file is larger than 25 MB", not "You uploaded a file that is too large". "Enter a password of at least 12 characters", not "Invalid password".
4. **Say it the way the interface says it everywhere else.** One word per concept across the whole product. If the sidebar says "Workspace", no dialog says "team" or "org". If the button says "Sign in", nothing says "Log in".

## By string type

### Buttons and actions
- Verb plus object: "Save changes", "Delete 3 files", "Send invite", "Create project". Not "OK", "Yes", "Submit", or "Continue" where a real verb exists.
- The confirm button repeats the verb from the dialog title. Title "Delete this project?" leads to the buttons "Delete project" and "Cancel".
- A destructive action is never the default focused button, and never green.
- Two or three words. If a button needs a sentence, the sentence belongs above it.
- No trailing period. Sentence case: "Save changes", not "Save Changes".

### Labels and placeholders
- A label names the field and stays visible after the user types: "Work email".
- A placeholder is an example of a valid value, not the label, and never an instruction the user needs later: "name@company.com". It disappears on focus, so anything the user must remember cannot live there.
- Help text under the field says what the field is for or what format is accepted, in one line: "We only use this to send receipts."

### Error messages
State what happened, then what to do. Place it next to where it happened. Keep the user's input on screen.
- Field error: "Enter a date after today", "This username is taken. Try dana_w or dana.whitfield". Never "Invalid", "Error", "Incorrect value", or "Required" on its own.
- Form error: list the fields that need attention and move focus to the first one.
- System error: what failed, what is safe, what to do. "We couldn't save your changes. Your draft is still here. Try again, or copy your text before leaving the page." Never "Something went wrong" by itself, never an error code without a sentence, never "Oops" or "Whoops".
- Network: "You're offline. Changes will sync when you're back." Say whether work is lost.
- Permission: "You need an admin role to change billing. Ask your workspace admin or request access." Say who can help.
- Not found: "That page doesn't exist or has moved. Search, or go to the dashboard." A joke on the 404 page is optional and is never the only thing on it.
- No humor in any error that cost the user time, money, or data.

### Empty states
What this screen is for, and the one action that fills it. "No invoices yet. Create your first invoice to start tracking payments." Not "Nothing here!" and not a paragraph of marketing. If the emptiness comes from a filter, say so and offer to clear it: "No results for 'refund' in March. Clear filters".

### Confirmations and destructive dialogs
- The title asks about the specific object: "Delete 'Q3 budget'?", not "Are you sure?".
- The body states the consequence and whether it can be undone: "This removes the file for everyone in the workspace. You can restore it from Trash for 30 days." Or: "This can't be undone."
- Buttons: the verb, and "Cancel". Never "Yes" and "No", never "OK".
- Make the user type the name only when the loss is severe and irreversible.
- No confirmshaming. The decline option is a plain "No thanks" or "Not now", never "No, I don't want to save money".

### Success messages and toasts
Confirm the specific thing in one line, then offer the next step or the undo. "Invoice sent to dana@acme.com. Undo". Not "Success!", not "Your invoice has been successfully sent" (a past-tense verb already says it worked, so "successfully" adds nothing). A toast disappears, so it never carries anything the user must act on later.

### Loading and progress
Say what is happening, not that something is happening. "Importing 240 contacts..." beats "Loading...". If it may take more than a few seconds, say so and say whether the user can leave. Never "Please wait" alone.

### Tooltips and help text
One sentence that adds information the label could not carry. If the tooltip repeats the label, delete the tooltip. Never hide required information in a tooltip.

### Notifications and system emails
- The subject or title carries the whole message for someone who reads nothing else: "Your password was changed", "Payment of $120 received", "Dana commented on 'Roadmap'".
- Body: what happened, when, what to do if it was not you or not expected, and where to change the setting that sent this.
- Verification and reset emails: the single action, the expiry, and "if you didn't ask for this, you can ignore this email" in plain words. No marketing in a security email.
- Receipts: amount, what for, date, how to get help. Nothing else.

### Settings and toggles
Label the state, not the question. "Email me when someone comments" (on or off), not "Do you want to disable comment emails?". No double negatives, and never a toggle that turns something off when switched on.

### Status and badges
One or two words that describe a state, used identically everywhere: "Paid", "Overdue", "Draft". Not "Completed successfully".

## Mechanics

| Element | Rule |
|---|---|
| Capitalization | Sentence case everywhere: headings, buttons, labels, menu items. Proper nouns and product names keep their own. |
| Periods | Full sentences get one. Buttons, labels, menu items, titles, and single fragments do not. |
| Exclamation marks | None by default. One, in a celebration the user chose ("Project published!"), is the ceiling. Never in an error. |
| Numbers | Numerals always: "3 files", "1 comment", not "three files". Plurals are handled in code, never with "(s)". |
| Dates and times | Relative for the recent ("2 min ago", "Yesterday"), absolute beyond a week ("3 Oct 2026, 14:10"). Both when the reader may act on it. |
| Ellipsis | Only on an action in progress ("Saving..."). Never for drama. |
| "Please" | Once, when asking the user to do work they did not plan to do. Not on every button and error. |
| "Sorry" | Once, when the product is at fault and the user lost something. Not for a validation error. |
| Quotes | Around user-supplied names inside a sentence: Delete 'Q3 budget'? Use the product's one quote style, straight or curly, never both. |

## Vocabulary

Verbs that look interchangeable and are not. Pick once, write the choice in the glossary, repeat it.

- **Delete** destroys. **Remove** detaches without destroying (remove a member from a team). **Clear** empties a field or a list. **Discard** throws away unsaved changes.
- **Cancel** stops an action in progress. **Close** dismisses a panel with nothing pending. **Back** returns to the previous step.
- **Sign in / Sign out / Sign up**, or **Log in / Log out / Register**. One family, never mixed.
- **Save** keeps changes and stays. **Done** keeps changes and leaves. **Apply** keeps changes to a preview.
- **Edit** opens something for change. **Update** commits a change already made. **Change** is the plain user-facing verb when neither distinction is needed.
- **You** is the user. **We** is the company, used sparingly and never to dodge ("we couldn't process the payment" is fine; "we are experiencing issues" is a dodge). The product never says **I**.

## Tone and mood dials in a product

The defaults are neutral tone and concise mood. Move them on purpose:

- Casual for a consumer app whose brand already talks that way: "You're all set." Not for a bank's message about a failed transfer.
- Professional for B2B, finance, health, government, and anything legal: "Your changes were saved." No jokes, no "Yay".
- Empathic mood where the user lost something or is about to: failed payment, lost work, locked account, deleted data. One sentence that names the situation, then the way out.
- Corporate mood for compliance notices, terms updates, and security disclosures: dated, owned, no personal voice.

## Writing for translation

- No idioms, puns, or cultural references. "Hit the ground running" does not exist in most languages.
- Never build a sentence from fragments in code. `"You have " + count + " items"` breaks in every language with cases or gender. Use one string with named placeholders, "You have {count} items", and let the string file carry the ICU plural forms.
- Leave room: translations run up to 30 percent longer than English. Buttons and table headers feel this first.
- Dates, numbers, currency, and sort order come from the locale, never from the string.
- Spanish strings are Puerto Rican Spanish. "Tú" is the default even for banks and B2B; "usted" only for government, legal, and health products whose readers expect it, and never both in one product. Buttons take the infinitive ("Guardar cambios", "Eliminar archivo"), which also sidesteps gendered agreement; instructions say "oprime" or "haz clic", not "pulsa" or "pincha". Vocabulary follows the table in `ai-tells.md` section 7: computadora, celular, archivo, mouse, video, estacionamiento. "Papelera" for Trash, "Iniciar sesión" and "Cerrar sesión" for sign in and out, "correo electrónico" in the interface even though people say "email". Prefer forms that do not force a gender: "Te damos la bienvenida", "Hola, equipo", "la persona invitada". The es-PR locale formats numbers US-style (1,200.50), dates month/day/year, and times on a 12-hour clock ("2:10 p.m."); let the locale do it and never hard-code "6/10" into a string.
- Give translators context on every string: where it shows, what it refers to, the maximum length.

## Accessibility

- Link text says where it goes: "View invoice 2231", not "click here" or "here".
- An icon-only button has a text label for screen readers, and it is the same verb a visible button would carry.
- Errors are announced in words, not only by a red border, and they say which field.
- Do not say "above", "below", or "on the right"; layouts reflow. Name the thing.
- Do not rely on the reader seeing a colour. "Overdue" is a status; a red dot is not.

## Delivering strings to a developer

When the user is building, hand over strings as data, not prose: a table or JSON with a key, the string, where it shows, and the limit, in the order the user meets them.

| Key | String | Where | Limit |
|---|---|---|---|
| billing.card_declined.title | Payment declined | Banner on billing page | 30 chars |
| billing.card_declined.body | Your card was declined on {date}. Update it by {deadline} to keep your account active. | Banner body | 2 lines |
| billing.card_declined.cta | Update card | Banner button | 2 words |

Keys name the screen, the moment, and the part. Placeholders are named, never positional. Any string with a plural gets its ICU forms. If a string departs from the product's default tone or mood, say so in a note so the next writer keeps it consistent.

## Self-check for a batch of strings

1. Every error names the fix or says who is on it.
2. Every button is a verb plus an object, and the confirm button repeats the title's verb.
3. None of these appear: "Oops", "Whoops", "Something went wrong" alone, "Are you sure?", "Invalid", "successfully", "Please wait", "click here".
4. No exclamation marks except one earned celebration. No em dashes anywhere.
5. Sentence case throughout. Periods only on full sentences.
6. One word per concept, checked against the rest of the product.
7. Numerals for numbers, named placeholders, no concatenation, no idioms.
8. Nothing blames the user for what the system did.
9. The tone and mood match the product's default or a stated exception.
