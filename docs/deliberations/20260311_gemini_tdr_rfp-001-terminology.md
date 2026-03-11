---
title: "TDR-001: Canonical Thesis Framework Terminology"
ai_generated: true
model: "Gemini 2.0 Flash"
model_id: "gemini-2.0-flash"
platform: "Gemini CLI"
date: 2026-03-11
session: "Librarian agent resolving RFP-001 terminology via MADP protocol"
human: "PAS"
task: "Synthesize RFP-001 proposals into a formal Technical Decision Record (TDR)"
status: proposed
doctype: deliberation
tags: [ai-generated, gemini, deliberation, tdr, terminology, thesis, oif]
---

> [!info] AI-Generated Document (TDR)
> **Model:** Gemini 2.0 Flash (`gemini-2.0-flash`) · **Platform:** Gemini CLI · **Date:** 2026-03-11
> **Task:** Synthesize RFP-001 proposals into TDR · **Status:** 🟡 Proposed
> *Review and approve to finalize canonical terminology.*

# TDR-001: Canonical Thesis Framework Terminology

**Status:** 🟢 Accepted
**Related RFP:** [RFP-001: Canonical Framework Terminology](RFP-001_framework-terminology.md)

---

## 1. Context
The project entered the proposal phase with two competing terminological sets: the **Operational Veracity Framework (OVF)** (proposed by Claude) and the **Operational Integrity Framework (OIF)** (proposed by Gemini). A formal resolution is required to ensure consistency across the industry sponsorship proposal, academic drafts, and research documentation.

## 2. Options Considered

### Option A: Operational Veracity Framework (OVF)
- **Strengths:** Precise focus on "truthfulness" vs. "hallucination"; clear differentiation from traditional safety standards; aligns with "Data Veracity" in information science.
- **Weaknesses:** "Veracity" is perceived as a "softer" or more linguistic term in industrial engineering; lacks the established weight of "Integrity" in safety-critical sectors.

### Option B: Operational Integrity Framework (OIF)
- **Strengths:** Strong alignment with established industrial standards (SIL/ISO 26262/AMLAS); "Integrity" is a core KPI for the target Industry 5.0 audience; provides a robust engineering lineage.
- **Weaknesses:** Risks being perceived as a derivative of existing safety standards; "Integrity" is a broad term that may require specific qualification for AI contexts.

## 3. Decision & Rationale

**Decision:** Adopt **Operational Integrity Framework (OIF)** as the canonical name.

### Rationale:
1.  **Industrial Alignment:** Research benchmarking (ref: [Terminology Addendum](20260311_gemini_analysis_rfp-001-terminology-addendum.md)) confirms that **AMLAS (University of York)** and **ISO/IEC TR 5469:2024** explicitly use "Operational Integrity" and "Safety Integrity" to describe the assurance of AI systems.
2.  **Engineering Legibility:** For industrial sponsors, "Integrity" is an actionable engineering property. "Veracity" remains a critical *metric* (a subset of Integrity) focusing on semantic correctness and grounding.
3.  **Synthesis of Strengths:** We will adopt the **AI Reliability Levels (ARL 1-4)** metric system as the core quantitative measure, satisfying the requirement for academic rigor and industry familiarity.
4.  **Veritiology:** The term "Veritiology" will be demoted from a formal discipline name to a **marketing/brand descriptor** for the "art and science of assessing AI integrity."

## 4. Canonical Terminology Register

| Concept | Canonical Term | Definition |
|---|---|---|
| **Framework Name** | **Operational Integrity Framework (OIF)** | A methodology for verifying AI reasoning and outputs against operational reality. |
| **Core Metric** | **AI Reliability Levels (ARL 1-4)** | Quantitative grades of AI dependability based on input entropy and output non-determinism. |
| **Subset Metric** | **Operational Veracity** | The specific measure of an AI's semantic truthfulness and grounding in facts. |
| **Architecture** | **Verification-as-a-Service (VaaS)** | The real-time verification stack supporting the OIF. |
| **Protocol** | **Verifiable State Handshake (VSH)** | The cross-agent protocol for maintaining state integrity. |

## 5. Consequences
1.  **Document Updates:** The 4-page industry proposal (`docs/20260310_gemini_draft_thesis-proposal-summary.md`) must be updated to use OIF/ARL exclusively.
2.  **Config Sync:** `GEMINI.md` and `CLAUDE.md` must be updated by the doc-librarian to reflect the canonical terminology.
3.  **Research Integration:** Future research analysis must map findings to the OIF/ARL structure.

---
*Proposed by Gemini 2.0 Flash (Arbitrator) on 2026-03-11.*
