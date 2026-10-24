# Repository instructions

Keep only work that materially improves the reader's ability to act or the code's
correctness, safety, clarity, or maintainability. Stop when the next addition adds
cost without a meaningful benefit.

## Writing

Apply these rules to technical documentation, session kits, runbooks, Markdown,
slide content, and user-facing explanations.

**Tone of voice:** Before writing or revising prose, including user-facing
replies, invoke the `humanize-content` skill and follow the root
`TONE-OF-VOICE.md`. If it is missing, the skill asks for the voice once and creates
it. Reuse the saved voice on later runs; keep task-only overrides out of the file.
The rules below supplement the saved voice.

### Plain language

Write like a senior engineer explaining something to another competent engineer.
Use ordinary words, concrete verbs, explicit subjects, and one main idea per
sentence. Retain technical terms when they carry necessary meaning.

Prefer "validate" to "perform validation of" and "configure" to "provide
configuration of." For example:

> Complete this configuration to apply the required governance controls.

State the point, then explain why it matters when the reader needs that context.
Use **bold** to highlight key decisions or actions. Keep clear, natural wording;
shorter or more formal wording is not inherently better.

**Completion:** Read every changed sentence as if saying it to a colleague.
Resolve unclear subjects and abstract phrasing; remove filler, repeated points,
generic benefits, and detail that does not help an expert reader act. Preserve
technical facts, Microsoft product names, dates, citations, and governance
terminology exactly.

### Cross-session implementation links

Link to a sibling session's published implementation guide with
`../../<session-slug>/implementation/README.md`; the site builder resolves it.
This guide link is the exception to the artifact boundary below.

Keep Markdown artifact links and documented path variables within the current
`implementation/` folder. When a script consumes an earlier session's artifact,
keep that external path inside the script or accept it as an explicit parameter.

**Completion:** After changing implementation content, run `npm run build:site`
and apply the documentation checks under Testing.

## Coding

Read surrounding code before editing and follow its names, patterns, and
boundaries. Make the smallest change that solves the requested problem; keep
unrelated cleanup and speculative refactors outside its scope.

- Make no mistakes.
- Prefer simple control flow, clear types, and direct data shapes. Extract helpers
  when they remove real repetition or clarify a difficult idea.
- Handle expected failures close to their source and surface useful errors.
  Broad catches and success-shaped fallbacks must not hide failures.
- Keep configuration, permissions, secrets, and customer data out of source
  control. Make security-sensitive behavior explicit.
- Comment decisions, constraints, and surprising trade-offs; let code explain
  routine mechanics.
- Use existing libraries and platform features first. Add a dependency only for a
  real gap and when it fits the repository.

**Completion:** Review every changed code path for a teammate maintaining it next
week. Remove duplication, indirection, and branches that add no useful behavior,
then complete the relevant checks below.

## Testing

Run the smallest existing test, build, lint, or site-validation check covering the
change. Use the project's tooling rather than adding a runner.

Add or update tests for changed observable behavior, regressions, and meaningful
boundaries. Each test must catch a distinct failure and fail when that behavior
breaks. Cover edge cases affecting customer artifacts, measurements, permissions,
or published pages.

Keep setup short and readable. Prefer real inputs and outputs over mocks that
duplicate implementation details. Assertions should check behavior rather than
copied constants, reimplemented logic, or mock interactions alone.

For documentation or static-site changes, validate generated output, links, and
the existing site build when those checks are available.

**Completion:** Relevant checks pass, or the final response identifies each blocked
check, its blocker, and what remains unproven.
