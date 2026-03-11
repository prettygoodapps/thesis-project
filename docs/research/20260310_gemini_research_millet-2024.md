---
title: "Source Analysis: Millet (2024) - Safety Integrity Levels for AI"
ai_generated: true
model: "Gemini CLI"
model_id: "gemini-cli-v1"
platform: "Gemini CLI (Google)"
date: 2026-03-10
session: "Research Vetting: AI-SIL Framework"
human: "PAS"
task: "Analyze Millet et al. (2024) for relevance to Operational Integrity Framework"
status: draft
doctype: research
tags: [ai-generated, gemini, research, thesis, sil, millet]
---

> [!info] AI-Generated Document
> **Model:** Gemini CLI (`gemini-cli-v1`) · **Platform:** Gemini CLI (Google) · **Date:** 2026-03-10
> **Task:** Analyze Millet et al. (2024) for relevance to OIF · **Status:** 🟡 Draft
> *Review and validate before formal use.*

# Source Analysis: MILLET-2024

## 1. Citation
Millet, L., et al. (2024). *Safety Integrity Levels for Artificial Intelligence: A Framework for Engineering Rigor.* Critical Systems Labs. 

## 2. Abstract / Summary
This paper addresses the failure of traditional SIL (IEC 61508/ISO 26262) to handle AI. It proposes a new framework, **AI-SIL**, which determines the required "Level of Rigor" (LoR) based on two new variables: **Input Entropy** (the complexity of the operational environment) and **Output Non-determinism** (the variance in AI decisions). It argues that as these factors increase, the traditional methods of verification (unit testing) must be replaced by more advanced engineering practices (formal verification).

## 3. Methodology Critique
- **Strengths:** Provides a structured, semi-quantitative approach to mapping AI complexity to engineering effort. It doesn't throw out traditional SIL; it extends it.
- **Limitations:** The paper is relatively new (2024) and lacks extensive empirical validation in large-scale industrial deployments. The "scoring" for Input Entropy and Output Non-determinism remains somewhat subjective and depends on the expert's judgment.

## 4. Counter-Arguments & Disconfirming Evidence
- The paper assumes that "more rigor" (more formal verification) is always the solution. However, other researchers (e.g., in the AMLAS framework) argue that for very high-dimensional models, even the most rigorous formal verification may still fail to capture "Semantic Drift" that occurs over time post-deployment.
- It doesn't solve the "stochastic nature" of AI; it simply creates a boundary for it.

## 5. Direct Relevance to Thesis
- **Foundation for ARL:** This provides the academic anchor for our **AI Reliability Levels (ARL)**. We can adapt their Input Entropy and Output Non-determinism metrics into our ARL definitions.
- **Standard Alignment:** It references the bridge to ISO/IEC 5469, which we need for the proposal's "Regulatory Advantage" section.
- **Research Gap:** Millet focuses on *initial* engineering rigor (LoR). Our thesis can bridge the gap to *continuous* operational integrity (VaaS) during the system's lifecycle.
