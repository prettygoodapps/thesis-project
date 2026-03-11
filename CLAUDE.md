# CLAUDE.md — Thesis Project

Project-specific instructions for Claude Code. Global workstation conventions are in `/home/pas/projects/CLAUDE.md`.

## Project Overview

This directory serves as the research and development hub for a Master's degree thesis in **AI and ML Engineering**. The primary objective is to manage the end-to-end lifecycle of the thesis, from proposal formalization to technical implementation and final documentation.

**Current Phase:** Proposal Phase — focusing on creating a four-page summary to solicit industry sponsorship for research.

## AI Document Conventions

**All AI-generated documents in this project must follow the conventions defined in:**
`docs/AI-DOCUMENT-CONVENTIONS.md`

### Research & Source Vetting Standards

To maintain academic rigor and avoid "source chasing":
- **Evidence-Based:** Every cited source must have a corresponding analysis file in `docs/research/`.
- **Methodology Critique:** Analysis must include a critique of the source's methodology and a search for disconfirming evidence.
- **Bibliography:** Maintain `docs/research/BIBLIOGRAPHY.md` as the central index of vetted sources.

Summary of the rules:

### File Naming
```
YYYYMMDD_[model]_[doctype]_[slug].md
```
- `[model]`: `claude`, `gemini`, `perplexity`, `gpt`, `human`, `multi`
- `[doctype]`: `analysis`, `planning`, `draft`, `research`, `summary`, `review`, `notes`
- Example: `20260310_claude_analysis_thesis-concept-refinement.md`

### Required Header (two parts, in this order)

**Part 1 — YAML frontmatter** (line 1 of the file):
```yaml
---
title: "[Document title]"
ai_generated: true
model: "[Full model name]"
model_id: "[model_id]"
platform: "[Platform]"
date: YYYY-MM-DD
session: "[Session description]"
human: "[Initials]"
task: "[One-line task description]"
status: draft
doctype: [analysis|planning|draft|research|summary|review|notes]
tags: [ai-generated, claude, [doctype], thesis]
---
```

**Part 2 — Visible callout** (immediately after frontmatter):
```markdown
> [!info] AI-Generated Document
> **Model:** [name] (`[id]`) · **Platform:** [platform] · **Date:** YYYY-MM-DD
> **Task:** [task] · **Status:** 🟡 Draft
> *Review and validate before formal use.*
```

Status emoji: 🟡 Draft · 🔵 Review · 🟢 Approved

See `docs/AI-DOCUMENT-CONVENTIONS.md` for the full spec, completed example, and Dataview query templates.

## Platform Domain Boundaries

Claude and Claude Code must **not** edit `GEMINI.md` or any other platform's configuration files. These are outside Claude's domain.

- **Claude's domain:** `CLAUDE.md` files, research/analysis/draft docs in `docs/`
- **Off-limits:** `GEMINI.md`, `AGENTS.md`, or any other platform config
- **Exception:** The `doc-librarian` agent has explicit cross-domain authority and is the correct agent to invoke for changes that must be applied to multiple platform configs simultaneously

Cross-platform sync of shared sections is handled automatically by `scripts/sync_md.py` — do not manually replicate changes into other platform files.

## Technical Conventions

- **Committing:** Use `as-push` for commits. Follow conventional commits (`feat:`, `docs:`, `chore:`, etc.).
- **Python:** Use `uv` for all environment and dependency management.
- **Markdown:** All research and reports must follow the AI Document Conventions above and be linked to the vault via `as-link thesis-project docs`.

## Usage

1. **Drafting the Thesis Proposal:** Collaborative drafting of the four-page industry-facing summary.
2. **Research Organization:** Storing notes and references for AI/ML engineering topics.
3. **Sponsorship Solicitation:** Generating documentation for the professor to use with industry partners.

---

*Note: This file provides project-specific context. For global workstation guidelines, see `/home/pas/projects/CLAUDE.md`.*
