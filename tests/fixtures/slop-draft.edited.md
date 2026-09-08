# A worked example: `slop-draft.md`, edited

This is what the output contract in `references/editing.md` looks like when it is actually
followed. A description of a format is easy to misread; an example is not. Use it as the target
shape, not as the only correct edit. Someone else could make different calls on the same draft
and still be right.

Note what is NOT here. The numbers survived. The swearing survived. The "I think" survived. The
one-word "Ha." survived. That is the point of the exercise, and it is the part most edits get
wrong.

---

## The edited draft

# Introducing our new sync engine

Most teams have accepted that file sync breaks. The breakage is almost always a queue problem
rather than a network one: an ordering issue, not a bandwidth issue.

So we rebuilt the ordering layer. The fix was 200 lines.

The engine learns. Our agent watches your folder, notices a conflict, and resolves it before you
see a spinner. Most sync failures are recoverable, and ordering was the thing that kept ours from
recovering.

The new engine resolves conflicts in one place. It is the first release where a shared folder
survives two people editing at once.

We decided to rebuild rather than patch, because the old design could handle only one writer at a
time. We decided that after three months of incident reports.

Honestly, the old code was a complete disaster and I am not going to pretend otherwise. I think
it was probably my fault for shipping it in the first place, though I'd argue the deadline
deserves some blame too. It was fast and it was simple, right up until it wasn't. Ha.

The rollout takes one command. The migration runs in a fixed order to preserve your history.
We will be shipping weekly from here.

We cut median sync latency from 4.2 seconds to 380 milliseconds across 1,900 workspaces.

---

## What changed

**Voice kept:** blunt, first person, self-deprecating, one-word beats.

- **Kill-list words (7):** delve, leverage, robust, seamless, ever-evolving, streamline,
  multifaceted. Each replaced with what the thing actually does, or cut.
- **Empty adverbs (6):** just, actually, fundamentally, truly, literally, and "simply has the
  ability to". Kept "Honestly" in the admission paragraph, where it carries real sincerity.
- **Empty phrases (5):** "when it comes to", "the truth is", "at the end of the day", "in order
  to", "going forward", "let's dive in".
- **Openers and setups (4):** "Here's the thing", "What nobody tells you is", "What if I told
  you", and the colon reveal "The best part: it learns."
- **Weasel attribution (2):** "Studies show" and "industry experts agree" had no source, so the
  claims were narrowed to what your own incident data supports. Nothing was invented to replace
  them. If you do have a study, put it back with the citation.
- **Puffery and tails (3):** "serves as a centralized hub", "marking a pivotal moment",
  "highlighting our team's commitment to innovation". Replaced with the concrete outcome.
- **Portability (2):** "significantly improves engineering productivity" and "underscores our
  commitment to reliability" would both fit any company on earth. Cut. Your latency numbers were
  already doing that work better.
- **Synonym cycling (1):** agent / assistant / tool were the same program. Now it is "our agent"
  throughout.
- **Endings (3):** "That's it. That's the whole thing.", the "In conclusion" recap, and the
  kicker "The future of sync isn't coming. It's already here." All cut. The piece now ends on the
  latency numbers, which is the strongest sentence in it.
- **Formatting (4):** rocket emoji in the heading, Title Case heading, mid-sentence bold on
  "complete disaster", and "The result: It Worked." Sentence case throughout.
- **Rule of three (1):** "fast, simple, and reliable" became two. The undercutting clause after
  it was doing the work anyway.
- **Structure:** the latency numbers moved to the end, because everything before them is setup
  and they are the proof. Say the word and I will put them back where they were.

**Left alone on purpose:** the 4.2s to 380ms figures and the 1,900 workspaces, the admission that
the old code was a disaster, "I think it was probably my fault", the deadline aside, and "Ha."
