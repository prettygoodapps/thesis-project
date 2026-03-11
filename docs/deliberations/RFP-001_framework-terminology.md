---
title: "RFP-001: Canonical Framework Terminology"
ai_generated: true
model: "Claude Sonnet 4.6"
model_id: "claude-sonnet-4-6"
platform: "Claude Code (Anthropic) — doc-librarian agent"
date: 2026-03-10
session: "First formal deliberation — framework terminology resolution"
human: "PAS"
task: "Issue a formal RFP for canonical thesis framework terminology under the MADP protocol"
status: open
doctype: deliberation
rfp_number: "RFP-001"
deliberation_topic: "Canonical framework name and core terminology"
arbitrator: "Human (PAS) with optional GPT-4o/o1 synthesis"
proposals_due: "Open until two proposals received"
tags: [librarian, deliberation, rfp, terminology, thesis]
---

> [!important] Librarian-Issued RFP
> **Issued by:** doc-librarian (Claude Sonnet 4.6) · **Date:** 2026-03-10 · **Status:** 🟠 Open
> **To:** All participating models (Claude, Gemini, and any designated arbitrator)
> *Each model must submit an independent proposal before synthesis begins. Do not read other proposals before writing your own.*

---

# RFP-001: Canonical Framework Terminology

**Issued by:** doc-librarian
**Protocol:** Model-Agnostic Deliberation Protocol (MADP) — ref. `docs/20260310_multi_planning_deliberation-protocol.md`
**Deliverable:** One proposal per model → one TDR synthesized by arbitrator

---

## 1. Background

This thesis has been developed concurrently across multiple AI-assisted sessions. As a result, two coherent but competing frameworks have independently emerged:

**Position A — Proposed by Claude (this session):**
- Framework name: **Operational Veracity Framework (OVF)**
- Core concept: "Veracity" — truthfulness and accuracy of AI outputs relative to operational reality
- Emphasis: enterprise-level, practitioner-facing, extending existing IVVT standards
- Coined term: "Veritiology" (proposed as a named framework, not a new discipline)

**Position B — Proposed by Gemini (parallel session):**
- Framework name: **Operational Integrity Framework (OIF)**
- Core concept: "Integrity" — reliability and grounding of AI reasoning over time
- Metric system: **AI Reliability Levels (ARL 1-4)**, adapted from SIL/IEC 61508
- Emphasis: formal engineering, quantitative metrics, standards alignment
- Supporting artifacts: 4-page proposal draft, two vetted research sources

**Original source document:**
- Working concept: "Veritiology" — "assessing for truthiness and accuracy within non-deterministic integrated systems"
- Original metric: Truth Integrity Level (TIL 1-4)

All three positions address the same research gap. The terminology has not been unified.

---

## 2. The Deliberation Question

> **What should the canonical name and core terminology of this thesis framework be, and why?**

This decision affects every subsequent document, the sponsor proposal, the academic framing, and the research sources. It must be resolved before the project can proceed coherently.

---

## 3. Evaluation Criteria

Proposals will be evaluated against the following criteria. Address each explicitly.

| Criterion | Description |
|---|---|
| **Academic defensibility** | Can the terminology withstand academic peer review? Does it avoid overreach for a Masters-level thesis? |
| **Industry legibility** | Will a non-academic industrial sponsor immediately understand what the framework does? |
| **Differentiation** | Does the name clearly distinguish this framework from existing standards (SIL, FMEA, ISO 42001, NIST AI RMF)? |
| **Scope accuracy** | Does the name accurately reflect what the framework actually covers — no more, no less? |
| **Longevity** | Is the terminology stable enough to survive the full thesis lifecycle without needing to be redefined? |

---

## 4. Required Proposal Format

Each model must submit a proposal as a new file:

**Filename:** `docs/deliberations/YYYYMMDD_[model]_proposal_RFP-001.md`

**Required sections:**

```
## 1. Recommended Terminology
State your proposed canonical framework name, acronym, and any subsidiary terms
(metric system name, maturity model name, etc.)

## 2. Rationale
Why this terminology best satisfies the evaluation criteria. Be specific.

## 3. Assessment of Competing Position(s)
Honest strengths and weaknesses of the other proposed terminology.
Do not simply argue against the other — acknowledge what it does well.

## 4. Proposed Concessions
What elements from the competing position(s) could or should be incorporated
into your recommendation, even if your core term is adopted?

## 5. Open Questions
What aspects of the terminology remain unresolved that the arbitrator
or human sponsor should decide?
```

---

## 5. Arbitration

Once both proposals are submitted, the arbitrator will read both and produce:

**Filename:** `docs/deliberations/YYYYMMDD_[model]_tdr_RFP-001.md`

The TDR must follow the format defined in `docs/20260310_multi_planning_deliberation-protocol.md`:
- Title, Status, Context, Options Considered, Decision & Rationale, Consequences

The arbitrator for RFP-001 is: **Human (PAS)**, with the option to delegate synthesis to GPT-4o or o1 if desired.

---

## 6. Ground Rules

1. **Fresh context.** Each model writes its proposal without reading the other's. The human will distribute this RFP document to each model in a fresh session.
2. **No lobbying.** The proposal must stand on its merits. Do not reference "what the human preferred earlier."
3. **Acknowledge uncertainty.** If a position requires validation (e.g., checking whether a term already exists in a published standard), flag it rather than assert it.
4. **The arbitrator's decision is final.** Once the TDR is issued and marked `Accepted`, all subsequent documents must use the canonical terminology.

---

## 7. After Resolution

Once a TDR is issued and accepted:
- [ ] doc-librarian updates `docs/AI-DOCUMENT-CONVENTIONS.md` with a Terminology Register section
- [ ] All existing docs with non-canonical terminology are flagged for review
- [ ] CLAUDE.md and GEMINI.md are updated with the canonical term
- [ ] Gemini's 4-page proposal draft is updated to reflect the agreed terminology

---

*This RFP was issued by the doc-librarian agent in its capacity as neutral documentation authority for this project.*
