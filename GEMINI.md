# GEMINI.md — Thesis Project Context

Project-specific instructions for Gemini. Global workstation conventions are in `[PROJECT_ROOT]/GEMINI.md`.

## Project Overview

This directory serves as the research and development hub for a Master's degree thesis in **AI and ML Engineering**. The primary objective is to develop the **Operational Integrity Framework (OIF)** for Industry 5.0—a methodology for bridging the "Integrity Gap" between probabilistic AI agents and deterministic industrial systems using **AI Reliability Levels (ARL 1-4)**.

**Current Phase:** Proposal Phase — finalizing the OIF sponsorship summary for industry partners.

## Ecosystem Context

This project is part of a Linux workstation ecosystem located at `[PROJECT_ROOT]/`.
- Global conventions are defined in `[PROJECT_ROOT]/GEMINI.md`.
- **Knowledge Base:** Use the Obsidian vault at `[PROJECT_ROOT]/agent-workspace/vault/` for session logs and research.
- **Project Linkage:** Run `as-link thesis-project docs` to symlink documentation into the vault.

## Directory Structure

- `docs/`: Research papers, proposal drafts, literature reviews, and the final thesis document.
- `src/`: Technical implementation, experiments, and model development.
- `tests/`: Code validation and model testing.

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
- `[model]`: `gemini`, `claude`, `perplexity`, `gpt`, `human`, `multi`
- `[doctype]`: `analysis`, `planning`, `draft`, `research`, `summary`, `review`, `notes`
- Example: `20260310_gemini_analysis_thesis-concept-refinement.md`

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
tags: [ai-generated, gemini, [doctype], thesis]
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

Gemini must **not** edit `CLAUDE.md` or any other platform's configuration files. These are outside Gemini's domain.

- **Gemini's domain:** `GEMINI.md` files, research/analysis/draft docs in `docs/`
- **Off-limits:** `CLAUDE.md`, `AGENTS.md`, or any other platform config
- **Exception:** The `doc-librarian` agent has explicit cross-domain authority and is the correct agent to invoke for changes that must be applied to multiple platform configs simultaneously

Cross-platform sync of shared sections is handled automatically by `scripts/sync_md.py` — do not manually replicate changes into other platform files.

## Multi-Agent Deliberation Protocol (MADP)

This project utilizes a **Parallel-to-Consensus** workflow to ensure academic rigor and minimize model bias.

### 1. The Deliberation Orchestrator Role
When requested (e.g., "Issue an RFP for..."), the active agent acts as the **Orchestrator**:
- **Context Harvesting:** Identify relevant research from `docs/research/` and current drafts.
- **RFP Generation:** Create a `docs/deliberation/<topic>/RFP.md` file defining the task and context.
- **Clean Slate Protocol:** Provide the human with a "Context Block" for a **Fresh Session** in parallel models.

### 2. The TDR Artifact (Technical Decision Record)
The final output of any deliberation is a formal **TDR** (Industry Standard):
- **Title:** TDR-{ID}: {Decision}
- **Status:** Proposed | Accepted | Superseded
- **Options Considered:** Summary of parallel model proposals.
- **Rationale & Consequences:** The engineering logic and impact on the thesis.

## Security Enforcement

This project maintains a **Zero-Tolerance Security Policy**. All files must be audited for sensitive data (e.g., absolute paths, secrets, `.env` files) before being pushed to a remote repository.

- **Mandatory Agent:** The `security-lint` agent MUST be invoked before any `git push`, `gh repo create`, or `as-push` operation.
- **Strict Guardrail:** If the security linting fails, all pushing operations MUST be aborted until the identified issues are resolved.
- **Auditor Role:** Gemini acts as the **Security Auditor** in this project, proactively identifying and correcting security risks before they leave the workstation environment.

## Technical Conventions

- **Committing:** Use `as-push` for commits. Follow conventional commits (`feat:`, `docs:`, `chore:`, etc.).
- **Python:** Use `uv` for all environment and dependency management.
- **Markdown:** All research and reports must follow the AI Document Conventions above and be linked to the vault via `as-link thesis-project docs`.

## Usage

1. **Drafting the Thesis Proposal:** Collaborative drafting of the four-page industry-facing summary.
2. **Research Organization:** Storing notes and references for AI/ML engineering topics.
3. **Sponsorship Solicitation:** Generating documentation for the professor to use with industry partners.

---

*Note: This file provides project-specific context. For global workstation guidelines, see `[PROJECT_ROOT]/GEMINI.md`.*
