---
title: "Research Methodology and Source Vetting Workflow"
ai_generated: true
model: "Gemini CLI"
model_id: "gemini-cli-v1"
platform: "Gemini CLI (Google)"
date: 2026-03-10
session: "Establishing academic research rigor"
human: "PAS"
task: "Define a formal workflow for capturing and vetting academic/industry research"
status: draft
doctype: planning
tags: [ai-generated, gemini, planning, research, methodology, thesis]
---

> [!info] AI-Generated Document
> **Model:** Gemini CLI (`gemini-cli-v1`) · **Platform:** Gemini CLI (Google) · **Date:** 2026-03-10
> **Task:** Define a formal workflow for capturing and vetting research · **Status:** 🟡 Draft
> *Review and validate before formal use.*

# Research Methodology: Source Vetting and Documentation

To ensure this thesis meets Master's level academic standards, we are moving from concept-driven ideation to **Evidence-Based Research**. This document defines the protocol for finding, analyzing, and citing sources.

## 1. The "Source Analysis" Protocol
Every major paper, standard, or industry report added to this project must be accompanied by a **Source Analysis** file in `docs/research/`.

### File Naming
`YYYYMMDD_[model]_research_[bibtex-key-slug].md`

### Required Content for Research Analysis
Each analysis must include:
1.  **Full Citation:** (APA or IEEE format).
2.  **Abstract/Summary:** A brief overview of the work.
3.  **Methodology Critique:** How did the authors reach their conclusion? Is the sample size/model size sufficient?
4.  **Counter-Arguments:** Does this source present data that contradicts our current "Operational Integrity" direction?
5.  **Direct Relevance:** Specific ways this contributes to the thesis (e.g., "Supports ARL-3 definitions," "Provides a metric for Semantic Drift").

## 2. Avoiding "Source Chasing"
To maintain objectivity, we will actively seek **Disconfirming Evidence**:
- **Search Queries:** We will explicitly search for "Limitations of AI Formal Verification" or "Failures of Continuous Monitoring in ML" to ensure we are not cherry-picking.
- **Peer Review:** When an AI model finds a source, it must play "Devil's Advocate" to find potential flaws in that source's logic.

## 3. Central Bibliography
A `docs/research/BIBLIOGRAPHY.md` file will serve as the central index, categorizing sources into:
- **Foundational Standards:** (ISO, IEC, IEEE, NIST).
- **Academic State-of-the-Art:** (Peer-reviewed papers from NeurIPS, ICML, etc.).
- **Industry Whitepapers:** (Reports from McKinsey, Gartner, or major AI labs).

## 4. Next Actions
1.  **Initialize Bibliography:** Create the central index.
2.  **Initial Search:** Perform targeted searches for existing "Continuous Verification" and "SIL for AI" research.
3.  **Vetting:** Begin the first round of Source Analysis for identified foundational papers.
