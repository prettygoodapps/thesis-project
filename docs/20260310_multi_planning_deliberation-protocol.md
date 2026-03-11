---
title: "Model-Agnostic Deliberation Protocol (MADP) - Parallel Edition"
ai_generated: true
model: "Gemini CLI"
model_id: "gemini-cli-v1"
platform: "Gemini CLI (Google)"
date: 2026-03-10
session: "Expanding MADP to support parallel proposals and cross-model synthesis"
human: "PAS"
task: "Update deliberation protocol to support multiple parallel proposals"
status: draft
doctype: planning
tags: [ai-generated, multi, planning, deliberation, parallel-proposals, consensus]
---

> [!info] AI-Generated Document
> **Model:** Gemini CLI (`gemini-cli-v1`) · **Platform:** Gemini CLI (Google) · **Date:** 2026-03-10
> **Task:** Update MADP for parallel proposals · **Status:** 🟡 Draft
> *Review and validate before formal use.*

# Model-Agnostic Deliberation Protocol: Parallel Edition

This protocol is designed to leverage the unique strengths of multiple AI models by allowing for **Parallel Proposals** and **Cross-Model Synthesis**.

## 1. Functional Roles (Updated)

*   **The Proposer(s):** Multiple models act in this role simultaneously. Each generates an independent solution or response based on the same **Context Manifest**.
*   **The Reviewer (Optional):** A model (or human) that performs a comparative analysis of all submitted Proposals.
*   **The Arbitrator (The Synthesizer):** A model tasked with reading all Proposals and Reviews to generate a formal **TDR (Technical Decision Record)**. This model is responsible for "Semantic Blending"—taking the best technical aspects from each variant.

## 2. Parallel Workflow Structure

### Phase 1: Parallel Proposals (`PROPOSAL`)
The orchestrator (`scripts/deliberate.py`) triggers $N$ proposals.
- `YYYYMMDD_gemini_proposal_[topic]_v1.md`
- `YYYYMMDD_claude_proposal_[topic]_v2.md`

### Phase 2: Cross-Review or Synthesis (`SYNTHESIS`)
Instead of a simple "yes/no" review, the **Arbitrator** is given all variants.
- **Task:** *"Compare all proposals. Identify the most rigorous arguments, resolve contradictions, and synthesize them into a formal Technical Decision Record (TDR)."*

### Phase 3: The TDR Artifact (`TDR`)
The final output is a standardized **Technical Decision Record** (Industry Standard, e.g., AWS/Google style):
- `YYYYMMDD_[model]_tdr_[topic].md`

#### TDR Template Requirements:
1.  **Title:** TDR-{Number}: {Decision}
2.  **Status:** Proposed | Accepted | Superseded
3.  **Context:** The technical problem and research forces at play.
4.  **Options Considered:** Summary of the parallel model proposals and their trade-offs.
5.  **Decision & Rationale:** The synthesized "Consensus" and the engineering logic behind it.
6.  **Consequences:** The positive and negative impacts on the overall thesis architecture.

## 3. Benefits of the Parallel Approach
1.  **Bias Mitigation:** Prevents a single model's "favorite" approach from dominating the thesis.
2.  **Creative Friction:** Different models often interpret the same "Context Manifest" in unique ways, surfacing edge cases that a single model might miss.
3.  **Context Hygiene:** By forcing each model to generate a proposal in a **Fresh Session**, we ensure that their specific "personality" or previous conversation history does not contaminate the joint consensus.

## 4. Implementation in `scripts/deliberate.py`
The tool will support a `multi-propose` flag:
`python scripts/deliberate.py multi-propose --topic "ARL-Definitions" --models "gemini,claude,gpt"`
- This will generate the necessary file placeholders and context manifests for each model to ensure a clean start.
