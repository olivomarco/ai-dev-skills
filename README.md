---
name: AI Dev Skills
description: A collection of on-demand, technology-agnostic skills for AI-assisted development reviews and audits.
---

# AI Dev Skills

A collection of **technology-agnostic** [Agent Skills](https://skills.sh) for AI-assisted software development. Each skill is a self-contained review/audit you run **manually, whenever you want**, against any codebase. They produce reports and plans (and, where noted, make changes) without being tied to a particular language or framework.

## Skills

| Skill | What it does | Changes code? |
| --- | --- | --- |
| [`security-review`](skills/security-review/SKILL.md) | OWASP-aligned security audit with a prioritized remediation plan | No (reports) |
| [`functional-review`](skills/functional-review/SKILL.md) | Reviews existing functionality for correctness, broken flows, and missing states | No (reports) |
| [`dry-consolidation`](skills/dry-consolidation/SKILL.md) | Finds duplication/inconsistency and proposes shared building blocks | No (reports) |
| [`refactoring-opportunities`](skills/refactoring-opportunities/SKILL.md) | Identifies code smells and tech debt with a prioritized refactor plan | No (reports) |
| [`unit-test-coverage`](skills/unit-test-coverage/SKILL.md) | Audits coverage gaps and writes new unit tests | Yes (adds tests) |
| [`stale-code-check`](skills/stale-code-check/SKILL.md) | Detects dead/obsolete code, deps, config, and assets | No (reports) |
| [`next-feature-opportunities`](skills/next-feature-opportunities/SKILL.md) | Recommends the most impactful next features to build | No (recommends) |
| [`align-documentation`](skills/align-documentation/SKILL.md) | Updates existing docs in place to match the codebase | Yes (edits docs) |

## Install

These skills are installed with the [`skills`](https://www.npmjs.com/package/skills) CLI, which supports Claude Code, Codex, Cursor, OpenCode, and many more agents.

```bash
# List the skills in this repo
npx skills add olivomarco/ai-dev-skills --list

# Install all skills (interactive agent/scope selection)
npx skills add olivomarco/ai-dev-skills

# Install a specific skill
npx skills add olivomarco/ai-dev-skills --skill security-review

# Install everything to a specific agent, non-interactively
npx skills add olivomarco/ai-dev-skills --all -a claude-code -y
```

> Replace `olivomarco/ai-dev-skills` with the actual `owner/repo` if you fork or rename it.

Use a skill once without installing:

```bash
npx skills use olivomarco/ai-dev-skills --skill refactoring-opportunities --agent claude-code
```

## How to run a skill

Once installed, just ask your agent in natural language, e.g.:

- "Run a security review on `src/api`."
- "Find refactoring opportunities in this repo."
- "Improve unit-test coverage for the payments module."
- "Align the docs with the current codebase."

Each skill's `description` lists the trigger phrases that activate it.

## Repository layout

```
ai-dev-skills/
├── README.md
├── skills.sh.json          # optional grouping metadata for skills.sh
└── skills/
    └── <skill-name>/
        └── SKILL.md         # one skill per directory
```

## Authoring conventions

Each skill is a directory under `skills/` containing a `SKILL.md` with YAML frontmatter:

```yaml
---
name: skill-name            # lowercase, hyphenated, matches the directory
description: One sentence on what it does + the trigger phrases that activate it.
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <optional-argument-shape>
---
```

The body is Markdown instructions: a **Mission**, **Scope & Preconditions**, a **Workflow**, **Output Expectations**, and **Quality Assurance**. Skills here are written to be technology-agnostic — they detect the stack first and adapt their checks to whatever language/framework is in use.

To scaffold a new skill: `npx skills init skills/<new-skill-name>`.
