---
name: AI Dev Skills
description: An Agent Plugins bundle of on-demand skills for development reviews, documentation, content editing, and workflows.
---

# AI Dev Skills

On-demand skills for code reviews, testing, documentation, and workflows.
Use them with any technology stack.

## Install

### This repository's skills

**GitHub Copilot CLI:** install the whole [Agent Plugins](https://agent-plugins.org/) bundle.
Requires a current CLI with plugin support.

```bash
copilot plugin install olivomarco/ai-dev-skills
```

Start a new Copilot session after installation. No marketplace registration is needed.

**Individual skills or other agents:** use the [`skills` CLI](https://github.com/vercel-labs/skills)
for Claude Code, Codex, Cursor, OpenCode, and other supported agents.

```bash
# Choose skills and target agents interactively
npx skills add olivomarco/ai-dev-skills
# Install one skill
npx skills add olivomarco/ai-dev-skills --skill humanize-content
# List available skills
npx skills add olivomarco/ai-dev-skills --list
# Install all skills to Claude Code without prompts
npx skills add olivomarco/ai-dev-skills --all -a claude-code -y
```

Choose one installation method per agent to avoid loading duplicate copies of
the same skills.

### Optional third-party skills

Install these separately; **they are not included in this repository's plugin**.
Choose the ones you need.

```bash
# Content humanization alternatives
npx skills add lguz/humanize-writing-skill
npx skills add cursor/plugins --skill unslop --full-depth
npx skills add blader/humanizer

# Coding
npx skills add mattpocock/skills
npx skills add humanlayer/skills --skill show-me
npx skills add anthropics/skills --skill skill-creator

# Drawings and diagrams
npx skills add coleam00/excalidraw-diagram-skill
npx skills add Agents365-ai/drawio-skill
npx skills add claude-office-skills/skills --skill diagram-creator
npx skills add jimliu/baoyu-skills --skill baoyu-infographic
npx skills add cathrynlavery/diagram-design

# Documents, PDFs, spreadsheets, and slides
npx skills add anthropics/skills --skill docx pdf xlsx pptx

# Graphics and animations
npx impeccable install
npx skills add emilkowalski/skills
```

### Manage the Copilot plugin

```bash
copilot plugin list
copilot plugin update ai-dev-skills
```

## Skills

### Code Quality & Testing

| Skill | What it does | Changes code? |
| --- | --- | --- |
| [`dry-consolidation`](skills/dry-consolidation/SKILL.md) | Finds duplication/inconsistency and proposes shared building blocks | No (reports) |
| [`unit-test-coverage`](skills/unit-test-coverage/SKILL.md) | Audits coverage gaps and writes new unit tests | Yes (adds tests) |
| [`stale-code-check`](skills/stale-code-check/SKILL.md) | Detects dead/obsolete code, deps, config, and assets | No (reports) |
| [`ai-slop-detector`](skills/ai-slop-detector/SKILL.md) | Detects, prevents, and remediates low-quality AI-generated code | No (reports) |

### Product & Documentation

| Skill | What it does | Changes code? |
| --- | --- | --- |
| [`next-feature-opportunities`](skills/next-feature-opportunities/SKILL.md) | Recommends the most impactful next features to build | No (recommends) |
| [`align-documentation`](skills/align-documentation/SKILL.md) | Updates existing docs in place to match the codebase | Yes (edits docs) |
| [`humanize-content`](skills/humanize-content/SKILL.md) | Humanizes prose with scope confirmation every run, four voice presets, and a meaning-preservation check | No code; optionally edits prose files |

### Workflow & Productivity

| Skill | What it does | Changes code? |
| --- | --- | --- |
| [`youtube-transcript`](skills/youtube-transcript/SKILL.md) | Deterministically downloads transcripts from a YouTube video or playlist (via `yt-dlp`) and produces a detailed summary | No (writes transcripts) |

## Repository instructions template

Use the reusable [sample `AGENTS.md`](sample-AGENTS.md) as a starting point for
your repository instructions. It is not applied automatically by the plugin.

```bash
curl -o AGENTS.md https://raw.githubusercontent.com/olivomarco/ai-dev-skills/main/sample-AGENTS.md
```
