# AI Document Conventions — Thesis Project

This file defines the authorship header and file naming conventions for all AI-generated
planning, analysis, research, and draft documents in this project. These rules apply
regardless of which AI model or platform produced the document.

Documents are stored in `docs/` and symlinked into the Obsidian vault via `as-link thesis-project docs`.

---

## File Naming Convention

All AI-generated documents must follow this pattern:

```
YYYYMMDD_[model]_[doctype]_[slug].md
```

| Field | Description | Examples |
|---|---|---|
| `YYYYMMDD` | ISO date the document was created | `20260310` |
| `[model]` | Short model/platform identifier (see table below) | `claude`, `gemini`, `perplexity` |
| `[doctype]` | Document type (see table below) | `analysis`, `planning`, `draft` |
| `[slug]` | Kebab-case description of the content | `thesis-gap-analysis`, `ivvt-framework-outline` |

### Model Identifiers

| Platform / Model | Identifier |
|---|---|
| Claude (any version, Anthropic) | `claude` |
| Gemini (any version, Google) | `gemini` |
| Perplexity (any model) | `perplexity` |
| ChatGPT / GPT-4o (OpenAI) | `gpt` |
| Copilot (Microsoft) | `copilot` |
| Human-authored | `human` |
| Multiple models / collaborative | `multi` |

### Document Type Identifiers

| Type | Use for |
|---|---|
| `analysis` | Gap analysis, assessments, evaluations |
| `planning` | Research plans, project plans, roadmaps |
| `draft` | Early-stage document drafts (thesis sections, proposals) |
| `research` | Literature surveys, source summaries, reference notes |
| `summary` | Condensed summaries of sessions or documents |
| `review` | Review or critique of existing work |
| `notes` | Informal session notes, brainstorming |
| `deliberation` | MADP protocol documents: RFPs, proposals, and TDRs |

### Examples

```
20260310_claude_analysis_thesis-concept-refinement.md
20260311_gemini_research_ivvt-standards-survey.md
20260312_perplexity_research_eu-ai-act-overview.md
20260315_multi_planning_research-methodology.md
20260320_human_draft_thesis-proposal-v1.md
```

---

## Required Document Header

Every AI-generated document must begin with two components: a **YAML frontmatter block**
followed immediately by a **visible callout block**. Together these serve machine indexing
(Obsidian Properties, Dataview) and human readability in rendered view.

### Part 1 — YAML Frontmatter

Must be the very first thing in the file (line 1). Fill in all fields.

```yaml
---
title: "[Descriptive title of the document]"
ai_generated: true
model: "[Full model name, e.g. Claude Sonnet 4.6]"
model_id: "[Model ID, e.g. claude-sonnet-4-6]"
platform: "[Platform, e.g. Claude Code (Anthropic)]"
date: YYYY-MM-DD
session: "[Brief description of the conversation or task context]"
human: "[Initials or name of the person who prompted this]"
task: "[One-line description of what was requested]"
status: draft
doctype: [analysis|planning|draft|research|summary|review|notes]
tags: [ai-generated, [model], [doctype], thesis]
---
```

### Part 2 — Visible Callout Block

Immediately after the frontmatter, before any document content. This is visible in
Obsidian reading view and any Markdown renderer.

```markdown
> [!info] AI-Generated Document
> **Model:** [Full model name] (`[model_id]`) · **Platform:** [Platform] · **Date:** YYYY-MM-DD
> **Task:** [One-line task description] · **Status:** 🟡 Draft
> *Review and validate before formal use.*
```

Update the status emoji as the document progresses:
- 🟡 Draft
- 🔵 Review
- 🟢 Approved

---

### Completed Example

```markdown
---
title: "Thesis Concept Refinement Analysis"
ai_generated: true
model: "Claude Sonnet 4.6"
model_id: "claude-sonnet-4-6"
platform: "Claude Code (Anthropic)"
date: 2026-03-10
session: "Thesis concept refinement from IVVT rough draft"
human: "PAS"
task: "Analyze rough draft and propose refined thesis arc"
status: draft
doctype: analysis
tags: [ai-generated, claude, analysis, thesis]
---

> [!info] AI-Generated Document
> **Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`) · **Platform:** Claude Code (Anthropic) · **Date:** 2026-03-10
> **Task:** Analyze rough draft and propose refined thesis arc · **Status:** 🟡 Draft
> *Review and validate before formal use.*

# Thesis Concept Refinement Analysis

[Document content begins here...]
```

---

## Dataview Query Examples

With this convention in place, the Obsidian Dataview plugin can index all AI documents.

List all drafts needing review:
````
```dataview
TABLE model, task, date
WHERE ai_generated = true AND status = "draft"
SORT date DESC
```
````

List all documents by model:
````
```dataview
TABLE title, doctype, status, date
WHERE ai_generated = true
SORT model ASC, date DESC
```
````

---

## Research & Source Vetting Standards

All research documents and any document that cites external sources must follow these standards to maintain academic rigor.

### Rules

- **One source, one file.** Every cited source must have a corresponding analysis file in `docs/research/` before it may be cited in any thesis document. Use the standard naming convention: `YYYYMMDD_[model]_research_[author-slug-keyword].md`
- **Methodology critique required.** Each source analysis must include an assessment of the source's methodology and an active search for disconfirming evidence or counter-arguments.
- **Bibliography is the index.** `docs/research/BIBLIOGRAPHY.md` is the single, authoritative index of all vetted sources. It must be updated whenever a new source analysis file is created.
- **No citation without vetting.** Draft documents must not cite sources that do not yet have a corresponding entry in `docs/research/` and `BIBLIOGRAPHY.md`.

### Source Analysis File Structure

Use the template at `docs/research/SOURCE-ANALYSIS-TEMPLATE.md` for all new source analysis files.

Key sections required in every source analysis:
1. **Citation** — full bibliographic reference in APA 7th edition
2. **Summary** — what the source claims and its relevance to the thesis
3. **Methodology Assessment** — how the source's conclusions were reached; strengths and weaknesses
4. **Disconfirming Evidence** — counter-arguments, contradicting sources, or limitations
5. **Thesis Relevance** — specific claim(s) in the thesis this source supports or informs

---

## Platform Domain Boundaries

AI agents must not edit instructive or configuration documents that belong to another platform's domain. Domain ownership is determined by the file's primary audience:

| File | Owner | May also be edited by |
|---|---|---|
| `CLAUDE.md` (any level) | Claude / Claude Code | doc-librarian agent only |
| `GEMINI.md` (any level) | Gemini | doc-librarian agent only |
| `AGENTS.md`, `Copilot instructions`, etc. | Respective platform | doc-librarian agent only |
| `docs/AI-DOCUMENT-CONVENTIONS.md` | doc-librarian (canonical) | Any agent, read-only — edits via librarian |
| Research, draft, analysis docs in `docs/` | Any agent (with proper header) | — |

**The doc-librarian agent is the sole exception** — it has cross-domain authority by design and is the designated agent for any change that must be applied consistently across multiple platform config files.

**Automated sync via `scripts/sync_md.py`** — this project includes a filesystem watcher that propagates shared sections between CLAUDE.md and GEMINI.md automatically. This is the correct mechanism for keeping shared content in sync; it does not violate the domain boundary rule because it is not an AI agent making editorial decisions. See the sync tool notes in the doc-librarian agent definition for known limitations.

---

## Terminology Register (Canonical)

The following terminology has been finalized via **TDR-001** and must be used in all formal documentation.

| Concept | Canonical Term | Definition |
|---|---|---|
| **Framework Name** | **Operational Integrity Framework (OIF)** | A methodology for verifying AI reasoning and outputs against operational reality. |
| **Core Metric** | **AI Reliability Levels (ARL 1-4)** | Quantitative grades of AI dependability based on input entropy and output non-determinism. |
| **Subset Metric** | **Operational Veracity** | The specific measure of an AI's semantic truthfulness and grounding in facts. |
| **Architecture** | **Verification-as-a-Service (VaaS)** | The real-time verification stack supporting the OIF. |
| **Protocol** | **Verifiable State Handshake (VSH)** | The cross-agent protocol for maintaining state integrity. |

---

## Rules Summary

1. **Always apply both header components.** Frontmatter + callout block, in that order, before any content.
2. **Always use the naming convention.** Human-authored files use `human` as the model identifier.
3. **Status field is mandatory.** Keep it updated: `draft` → `review` → `approved` (in frontmatter); update the callout emoji to match.
4. **Collaborative documents** use `multi` as the model identifier and list contributors in the `session` field.
5. **Do not rename files** after creation in a way that removes the date or model prefix — this breaks indexing.
6. **Web-based AI tools** (Perplexity, ChatGPT web, etc.) cannot write frontmatter automatically — paste the template manually before saving the output.
7. **Respect platform domain boundaries.** Do not edit another platform's config files. Route cross-platform changes through the doc-librarian agent.
