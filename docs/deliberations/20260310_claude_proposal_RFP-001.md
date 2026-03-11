---
title: "Proposal — RFP-001: Canonical Framework Terminology (Claude)"
ai_generated: true
model: "Claude Sonnet 4.6"
model_id: "claude-sonnet-4-6"
platform: "Claude Code (Anthropic)"
date: 2026-03-10
session: "MADP deliberation — RFP-001 response"
human: "PAS"
task: "Submit Claude's independent proposal on canonical framework terminology per RFP-001"
status: submitted
doctype: deliberation
rfp_ref: "RFP-001"
tags: [claude, deliberation, proposal, terminology, thesis]
---

> [!note] MADP Proposal — Claude
> **Model:** Claude Sonnet 4.6 · **RFP:** RFP-001 · **Date:** 2026-03-10 · **Status:** 🔵 Submitted
> *Independent proposal submitted per Model-Agnostic Deliberation Protocol. See RFP-001 for evaluation criteria.*

---

# Proposal: RFP-001 — Canonical Framework Terminology

---

## 1. Recommended Terminology

**Primary framework name:** Operational Veracity Framework (OVF)

**Subsidiary terms:**

| Concept | Recommended term | Replaces |
|---|---|---|
| Quantitative reliability metric | AI Reliability Levels (ARL 1–4) | Truth Integrity Level (TIL) |
| Maturity assessment model | Veracity Maturity Model (VMM) | Integrity Maturity Model (IMM) |
| Continuous monitoring architecture | Verification-as-a-Service (VaaS) | — (retain as-is) |
| Cross-agent provenance protocol | Verifiable State Handshake (VSH) | — (retain as-is) |
| Coined discipline term (optional) | Veritiology | — (demote to descriptive term, not a discipline) |

**One-line definition for all documents:**
> *The Operational Veracity Framework (OVF) is a structured methodology for verifying and maintaining the accuracy and real-world grounding of AI-augmented systems throughout their operational lifecycle.*

---

## 2. Rationale

### Academic defensibility
"Veracity" has a precise, unambiguous meaning — truthfulness and accuracy of claims relative to reality. It is used in information science, database theory (data veracity as the fourth V of Big Data), and epistemology. It is not a vague or invented word, and it maps directly to the core problem: AI systems producing outputs that are plausible but ungrounded.

"Integrity," by contrast, has significant semantic load in engineering contexts already — *data integrity*, *structural integrity*, *Safety Integrity Levels (SIL)*. Using it as the anchor term risks reviewers conflating OVF with extensions of existing SIL frameworks, which would require the thesis to spend defensive effort clarifying what it is *not* rather than establishing what it *is*.

### Industry legibility
An industrial sponsor reading "Operational Veracity Framework" can immediately parse the question it answers: *"Can we trust what this AI system is telling us during operation?"* That is the precise fear driving AI adoption hesitancy in industrial settings — not a general concern about "integrity," but a specific concern about whether AI outputs are accurate enough to act on.

"Veracity" also connects naturally to the regulatory language emerging in the EU AI Act and NIST AI RMF, both of which use accuracy and reliability framing rather than integrity framing when discussing AI output quality.

### Differentiation
This is where "Veracity" has its clearest advantage. The existing standards landscape is populated with integrity-adjacent language:
- IEC 61508: Safety Integrity Levels (SIL)
- ISO 26262: Functional safety and integrity
- ISO/IEC 5469: Functional safety and AI systems

An "Operational *Integrity* Framework" risks being perceived as a derivative or extension of this family. An "Operational *Veracity* Framework" occupies new semantic ground — it is clearly not a functional safety standard. It is asking a different, more specific question: not *"does the system fail safely?"* but *"does the system remain truthful?"* That distinction is the thesis's core contribution and should be legible in the name.

### Scope accuracy
The framework addresses: AI output accuracy, grounding loss, semantic drift, cross-agent veracity, and lifecycle verification. All of these are about the *truthfulness and real-world alignment* of outputs — not system integrity in the engineering sense. "Veracity" is the more accurate descriptor.

### Longevity
"Veracity" is not a trend term. It does not depend on the currency of any particular AI technology (LLMs, agents, etc.) and would remain meaningful if the technology landscape shifts significantly during the thesis lifecycle or afterward.

---

## 3. Assessment of the Competing Position (OIF)

**Strengths of OIF that must be acknowledged:**

- **The ARL metric system is superior to TIL.** Gemini's ARL 1–4 framework, grounded in the Millet et al. (2024) AI-SIL paper and mapped to Input Entropy / Output Non-determinism, is more academically rigorous than the original TIL concept. It should be adopted regardless of which framework name wins.

- **"Integrity" resonates with industrial engineers.** Professionals already fluent in SIL, FMEA, and ISO safety standards will find "integrity" immediately familiar. This reduces the friction of introducing a new framework to a technical industrial audience.

- **The 4-page proposal draft is well-executed.** The OIF proposal document is coherent, well-structured, and closer to ready for sponsor distribution than anything produced under the OVF label. This is a practical asset that should be preserved and adapted, not discarded.

- **"Operational Integrity" has an intuitive feel for systems thinking.** In a systems engineering context, "integrity" conveys wholeness and coherence across components — which is relevant for multi-agent orchestration scenarios.

**Weaknesses of OIF:**

- The term does not clearly distinguish the framework from existing SIL-based standards, creating an interpretation problem that will require repeated clarification in academic writing.
- "Integrity" does not capture the specific concern about AI truthfulness vs. operational reality. A system can have high integrity (consistent, reliable, fail-safe) while still producing systematically wrong outputs grounded in a corrupted model. Veracity addresses this case directly; integrity does not.
- The IMM (Integrity Maturity Model) name conflicts with the existing CMMI (Capability Maturity Model Integration) family, which could create confusion for readers familiar with process maturity frameworks.

---

## 4. Proposed Concessions

Regardless of which framework name is adopted, this proposal recommends the following elements from the OIF position be incorporated:

1. **Adopt ARL 1–4 as the metric system.** The Millet grounding and the Input Entropy / Output Non-determinism variables make ARL more defensible than TIL. Rename to *Veracity Reliability Levels (VRL)* if OVF is adopted, or retain as ARL under OIF.

2. **Preserve the 4-page proposal structure.** Gemini's draft is the most complete and sponsor-ready document in the project. It should be updated with canonical terminology rather than replaced.

3. **Retain VaaS and VSH as subsidiary terms.** Both are functional, legible, and not in conflict with either framework name. They should be carried forward unchanged.

4. **Retire "Veritiology" as a discipline name.** Both positions implicitly agree that coining a new discipline is out of scope for a Masters thesis. "Veritiology" can be retained as a descriptive or colloquial term if the sponsor finds it memorable, but should not appear in the formal academic framing.

---

## 5. Open Questions

The following remain unresolved and should be decided by the arbitrator or human sponsor:

1. **ARL vs. VRL naming.** If OVF is adopted, should the metric system be renamed Veracity Reliability Levels (VRL) for internal consistency, or is ARL sufficiently distinct from the framework name that it can stand independently? A practitioner argument could be made either way.

2. **"Veritiology" as a marketing term.** The original draft coined this term and the human sponsor found it memorable. Should it be preserved as a colloquial or brand-facing term distinct from the formal academic name, similar to how "DevOps" functions alongside formal SDLC terminology?

3. **AgentGuard citation status.** The OIF proposal cites AgentGuard (2025) as a primary technical basis for VaaS. This citation has no verified authors or DOI. Before either framework's proposal is submitted to a sponsor, this source must be confirmed or replaced. The arbitrator should set a deadline for source verification.

4. **Framework scope boundary.** Both positions leave ambiguous whether the framework applies to: (a) enterprise IT systems specifically, (b) industrial/OT systems specifically, or (c) both. The thesis cannot credibly validate against both in a Masters-level scope. The arbitrator should recommend a primary domain for the case study with the other domain noted as future work.
