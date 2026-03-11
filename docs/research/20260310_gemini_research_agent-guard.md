---
title: "Source Analysis: AgentGuard (2025) - Runtime Verification for Agentic Workflows"
ai_generated: true
model: "Gemini CLI"
model_id: "gemini-cli-v1"
platform: "Gemini CLI (Google)"
date: 2026-03-10
session: "Research Vetting: AgentGuard Framework"
human: "PAS"
task: "Analyze AgentGuard (2025) for relevance to Operational Integrity Framework"
status: draft
doctype: research
tags: [ai-generated, gemini, research, thesis, agent-guard, runtime-verification]
---

> [!info] AI-Generated Document
> **Model:** Gemini CLI (`gemini-cli-v1`) · **Platform:** Gemini CLI (Google) · **Date:** 2026-03-10
> **Task:** Analyze AgentGuard (2025) for relevance to OIF · **Status:** 🟡 Draft
> *Review and validate before formal use.*

# Source Analysis: AGENT-GUARD

## 1. Citation
TBD. (2025). *AgentGuard: Runtime Verification for Agentic Workflows via Probabilistic Model Checking.* (Pre-print/Arxiv).

## 2. Abstract / Summary
AgentGuard addresses the challenge of verifying non-deterministic AI agent behavior in production environments. It abstracts an agent's interactions into formal events and uses online learning to build a **Markov Decision Process (MDP)** model of the agent's behavior. It then performs **Probabilistic Model Checking** in real-time to predict the likelihood of a safety or policy violation within a given time horizon (e.g., the next 10 steps).

## 3. Methodology Critique
- **Strengths:** It moves beyond "static" testing (IVVT) into **Runtime Verification (RV)**, which is crucial for systems that evolve (Semantic Drift). The use of MDPs and probabilistic model checking is a mathematically sound approach for non-deterministic systems.
- **Limitations:** The computational overhead of real-time model checking for complex, multi-agent workflows may be significant. Its effectiveness depends heavily on the accuracy of the abstraction layer (how well the "formal events" represent the agent's real-world actions).

## 4. Counter-Arguments & Disconfirming Evidence
- Critics argue that MDPs are still a simplification of the "black box" LLM reasoning. If the agent's behavior is too chaotic or high-dimensional, the MDP might fail to capture critical edge cases.
- It relies on a "known" set of policies. It cannot easily verify "unknown unknowns" that were not pre-defined in the model checker.

## 5. Direct Relevance to Thesis
- **Technical Basis for VaaS:** This is the primary inspiration for our **Verification-as-a-Service (VaaS)** stack. We can leverage their MDP approach as a core component of our continuous verification layer.
- **Support for Industry ROI:** It provides a technical proof-of-concept for "Real-time Monitoring" that can be used to convince industrial sponsors that AI risk *can* be quantified and managed in production.
- **Handshake Protocol:** The "formal event" abstraction can be integrated into our **Verifiable State Handshake** protocol to ensure that the metadata exchanged between agents is mathematically auditable.
