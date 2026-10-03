# Repository instructions

Remember the law of diminishing returns to decide if something should fit or not here.

## Writing

### Writing gate

Before drafting, editing, or returning repository prose, invoke
`/humanize-writing`. This includes technical documentation, session kits,
runbooks, Markdown, slide content, and user-facing explanations.

In this repository, use the skill to simplify wording and remove AI-patterns from
technical content. Its general technical-writing exclusion does not apply here.

Use the `clear-thinker` voice unless the user requests another voice.

Before finishing, complete both checks:
1. Apply the prose simplification rules in this file.
2. Apply the `/humanize-writing` AI-pattern dictionary and revise the draft until
   it passes.

### Cross-session implementation links

An implementation guide can link to a sibling session's `implementation/README.md`
with `../../<session-slug>/implementation/README.md`. The site builder turns that
link into the sibling's published guide.

Do not add a Markdown link or documented path variable that points to an artifact
outside the current `implementation/` folder. When a script consumes an earlier
session's artifact, keep that path inside the script or accept it as an explicit
parameter. Run `npm run build:site` after changing implementation content.

### Default writing style

Write like a senior engineer explaining something to another competent engineer.

Prefer:
- short, direct sentences;
- concrete verbs over abstract nouns;
- active voice when the actor matters;
- ordinary words over formal or bureaucratic alternatives;
- one main idea per sentence;
- explicit subjects: say who does what;
- the shortest wording that preserves the technical meaning.

Write technical content clearly. Complexity should come from the subject, not from the prose.

Bad:
"If the earlier controls were implemented outside this series, confirm the required state in the table below."

Better:
"If you already implemented these controls elsewhere, check that they match the requirements below."

Bad:
"Completion of the configuration enables the establishment of the required governance posture."

Better:
"Complete this configuration to apply the required governance controls."

Bad:
"This section provides guidance for the implementation of controls that enable organizations to..."

Better:
"This section shows how to implement controls for..."

### Avoid bureaucratic prose

Do not turn verbs into abstract nouns when a verb works:
- "perform validation of" -> "validate"
- "make a determination" -> "decide"
- "provide configuration of" -> "configure"
- "enable the establishment of" -> "establish"
- "conduct an assessment of" -> "assess"

Avoid vague institutional phrases such as:
- "required state"
- "desired state"
- "in the context of"
- "with respect to"
- "in order to"
- "as part of this exercise"
- "the implementation of"
- "the configuration of"
- "it is important to note"
- "this enables organizations to"
- "the following section provides"
- "where applicable"
- "as appropriate"

Use them only when they carry necessary technical meaning.

### Do not over-explain

State the point, explain why it matters when necessary, and move on.

Do not add:
- introductory sentences that merely announce the next paragraph;
- conclusions that repeat the preceding paragraph;
- obvious explanations for expert readers;
- generic benefits;
- artificial transitions between every section;
- exhaustive qualification of straightforward statements.

Do not make a sentence more formal simply because it is documentation.

> [!IMPORTANT]
> Optimize for sufficient completeness, not maximal completeness. Stop adding detail when the next addition would not materially change the reader's understanding,
> decision, or ability to act, and stop when additional work has low marginal value.
> When writing, you need to consider strong simplification. Simplification is beauty.
> Fix your attitude at overcomplicating things, considering that the greatest and finest minds
> transfer knowledge by being clear and understandable.
> Always consider incremental utility value when trying to add things: if there is not, no need to add text or details.

Add some strategic bold text.

### Final prose pass

After drafting, read every sentence as if you had to say it aloud to a colleague.

For each sentence ask:
1. Could this be shorter without losing meaning?
2. Is there a simpler verb?
3. Is the subject clear?
4. Is an abstract noun hiding a simple action?
5. Would an experienced engineer actually say this?
6. Does the sentence contain information worth keeping?

Rewrite or delete sentences that fail this test.

Then apply the `/humanize-writing` AI-pattern dictionary.

Preserve technical facts, Microsoft product names, dates, citations, and governance terminology exactly.

## Coding

Write code with the same goal as the writing: make the intent obvious and keep only
what earns its place.

- Read the surrounding code before changing it. Follow established names, patterns,
  and boundaries.
- Make the smallest change that solves the actual problem. Do not mix a feature fix
  with unrelated cleanup or a speculative refactor.
- Prefer simple control flow, clear types, and direct data shapes. Extract a helper
  only when it removes real repetition or makes a difficult idea easier to follow.
- Handle expected failures close to their source. Return or surface useful errors;
  do not hide them behind broad catches or success-shaped defaults.
- Keep configuration, permissions, secrets, and customer data out of source control.
  Make security-sensitive behavior explicit.
- Add comments only when they explain a decision, constraint, or surprising trade-off.
  Code should explain routine mechanics on its own.
- Use existing libraries and platform features before adding a dependency. Add one
  only when it solves a real gap and fits the repository.
- Spend code only while the next change improves clarity, correctness, safety, or
  maintainability more than it costs. Stop when added abstraction or handling no
  longer earns its place.

Before finishing, read the changed code as if a teammate must maintain it next week.
Remove duplication, indirection, and branches that do not help them understand or
operate it.

## Testing

Tests are evidence that a change works. Keep them focused on the behavior that
changed.

- Run the smallest existing check that covers the work. Use the project's current
  test, build, lint, or site-validation commands rather than adding a new runner.
- Add or update a test when code changes observable behavior, fixes a regression, or
  protects a meaningful boundary. Check the expected result and the failure that
  matters most.
- Keep test setup short and readable. Prefer real inputs and outputs over mocks that
  duplicate implementation details.
- Avoid tautological tests. A test must be able to fail when the behavior breaks;
  do not assert a constant copied from the code, reimplement the same logic in the
  test, or only verify mock interactions.
- Test edge cases that could change a customer artifact, measurement, permission, or
  published page. Do not add tests that only inflate coverage.
- For documentation or static-site work, validate the generated output, links, and
  existing site build when those checks are available.
- If a relevant check cannot run, say what blocked it and what remains unproven.
- Spend tests only while each one protects a distinct failure that matters. Stop
  when another test repeats the same proof without adding useful confidence.

The test should make the reader more confident about the change, not create another
system to maintain.
