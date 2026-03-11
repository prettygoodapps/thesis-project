---
title: "AMLAS: Assurance of Machine Learning for Autonomous Systems"
ai_generated: true
model: "Gemini 2.0 Flash"
model_id: "gemini-2.0-flash"
platform: "Gemini CLI"
date: 2026-03-11
session: "Librarian agent collecting source documentation for thesis proposal"
human: "PAS"
task: "Analyze AMLAS framework for thesis research"
status: draft
doctype: research
tags: [ai-generated, gemini, research, thesis, amlas, safety-assurance]
---

> [!info] AI-Generated Document
> **Model:** Gemini 2.0 Flash (`gemini-2.0-flash`) · **Platform:** Gemini CLI · **Date:** 2026-03-11
> **Task:** Analyze AMLAS framework for thesis research · **Status:** 🟡 Draft
> *Review and validate before formal use.*

# AMLAS Framework Analysis

## 1. Citation
University of York Centre for Assuring Autonomy. (2022). *AMLAS: Assurance of Machine Learning for Autonomous Systems*. University of York. https://www.york.ac.uk/assuring-autonomy/guidance/amlas/

## 2. Summary
AMLAS is a systematic methodology for integrating safety assurance into the development of machine learning (ML) components. It provides a structured process to generate a "safety case" by linking system-level safety requirements to ML-specific evidence across six iterative stages.

### The Six Stages of AMLAS:
1. **ML Safety Assurance Scoping:** Defines boundaries and operational context.
2. **ML Safety Requirements Elicitation:** Translates system safety to ML safety requirements.
3. **Data Management:** Assures data representativeness and accuracy.
4. **Model Learning:** Assures the training process and bias mitigation.
5. **Model Verification:** Evidence of meeting requirements (testing, formal methods).
6. **Model Deployment:** Establishes **operational integrity** via runtime monitoring and integration.

## 3. Methodology Assessment
- **Strengths:** Provides a clear bridge between high-level safety goals and low-level ML metrics. Uses Goal Structuring Notation (GSN) for transparent reasoning. Emphasizes the "Semantic Gap."
- **Weaknesses:** Highly dependent on the quality of the "Operational Design Domain" (ODD) definition. Can be resource-intensive for complex systems.

## 4. Disconfirming Evidence
- Traditional safety standards (like ISO 26262) initially struggled with AMLAS's probabilistic nature, though newer technical reports (ISO/IEC 5469) are aligning with it.
- Criticism exists regarding the difficulty of defining "completeness" in Stage 3 for open-world environments.

## 5. Thesis Relevance
- **Operational Integrity:** AMLAS explicitly uses this term in Stage 6 to describe runtime monitoring and safe performance in deployment.
- **Reliability Levels:** Stage 5 and 6 provide a foundation for defining "Reliability Levels" based on verification evidence and monitoring coverage.
- **VaaS Stack:** The AMLAS "Safety Argument Pattern" can be implemented as part of a Verification-as-a-Service architecture.
