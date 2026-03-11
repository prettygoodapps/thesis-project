# Operational Integrity Framework (OIF) — Thesis Project

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Phase: Proposal](https://img.shields.io/badge/Phase-Proposal-orange.svg)]()

This repository hosts the research and development lifecycle for a Master's degree thesis in **AI and ML Engineering**. The primary objective is to develop the **Operational Integrity Framework (OIF)** for Industry 5.0—bridging the "Integrity Gap" between probabilistic AI agents and deterministic industrial requirements.

---

## 🚀 Core Concept

The **Operational Integrity Framework (OIF)** is a formal engineering methodology designed to verify AI reasoning and outputs against operational reality. It addresses the unique failure modes of autonomous agents, such as **Contextual Divergence** and **Operational Veracity Decay**.

### Key Metrics: AI Reliability Levels (ARL 1-4)
Adapted from traditional Safety Integrity Levels (SIL/IEC 61508), ARL provides quantitative grades of AI dependability based on **Input Entropy** and **Output Non-determinism**:

- **ARL-1 (Assisted):** Human-in-the-Loop verification.
- **ARL-2 (Monitored):** Passive automated auditing.
- **ARL-3 (Collaborative):** Active **Runtime Verification (RV)** protocols.
- **ARL-4 (Autonomous):** Formal mathematical grounding with immutable integrity certificates.

## 🌍 Strategic Alignment

This project is aligned with the global transition toward **Industry 5.0** and **Society 5.0**, as emphasized in the **2022 UN Commission on Science and Technology for Development (CSTD)** updates:

- **Human-Centricity:** OIF formalizes human-machine collaboration (ARL 1-2).
- **Resilience:** Addressing **SDG 9** (Industry, Innovation, and Infrastructure) through formal AI grounding and verification.
- **SDG Protection:** Mitigating the 59 SDG targets potentially inhibited by unaligned AI systems through real-time verification of operational integrity.

---

## 📂 Project Structure

- `docs/`: Research papers, OIF proposal drafts, and literature reviews.
- `scripts/`: Supporting tools for multi-agent deliberation and configuration sync.
- `src/`: Technical implementation and OIF prototype (Phase III).
- `tests/`: Validation suites for both code and model reasoning.

---

## 🛠 Multi-Agent Deliberation Protocol (MADP)

This project utilizes a **Parallel-to-Consensus** workflow to ensure academic rigor and minimize model bias. All major architectural decisions (e.g., terminology, framework scope) are resolved via formal **RFPs (Requests for Proposals)** and **TDRs (Technical Decision Records)** involving multiple AI models (Gemini, Claude).

- **Active Decision Records:** See `docs/deliberations/` for the decision history.

---

## 🛡 Security & Ethics

This project enforces a **Zero-Tolerance Security Policy**. All files are audited via a custom **`security-lint` agent** to prevent the exposure of sensitive local paths or credentials.

- **Pre-Push Check:** Every push is preceded by a mandatory security audit.
- **AI-Document-Conventions:** All AI-generated content follows strict authorship and vetting standards (ref: `docs/AI-DOCUMENT-CONVENTIONS.md`).

---

## 📋 Research Basis

Our research is grounded in foundational industry standards and peer-reviewed literature:
- **[AMLAS (2022)](https://www.york.ac.uk/assuring-autonomy/guidance/amlas/amlas-pdf/):** Assurance of ML for Autonomous Systems.
- **[NIST AI RMF 1.0 (2023)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf):** AI Risk Management Framework.
- **[ISO/IEC TR 5469:2024](https://www.iso.org/standard/83610.html):** Functional Safety and AI Systems.
- **[Millet et al. (2024)](https://doi.org/10.1007/978-3-031-40953-0_29):** Safety Integrity Levels for AI.

---

## 🤝 Sponsorship & Inquiries

We are currently in the **Proposal Phase** and actively seeking industrial partners for pilot implementation and empirical validation.

- **Draft Proposal:** See `docs/20260310_gemini_draft_thesis-proposal-summary.md` for the full 4-page summary.
- **Contact:** Please contact the Graduate Research Office at your affiliated University.

---

*Note: This repository is managed using the [Gemini CLI](https://github.com/google/gemini-cli) agent system.*
