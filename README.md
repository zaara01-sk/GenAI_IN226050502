# 🤖 AI Resume Screening System with LangSmith Tracing

[![LangChain](https://img.shields.io/badge/Framework-LangChain-blue)](https://python.langchain.com/)
[![LLM](https://img.shields.io/badge/LLM-Groq_Llama--3.3--70b-orange)](https://groq.com/)
[![Observability](https://img.shields.io/badge/Tracing-LangSmith-green)](https://smith.langchain.com/)

An advanced, production-grade AI recruitment tool developed during my GenAI Internship at **Innomatics Research Labs**. This system leverages Large Language Models (LLMs) to automate the screening process by extracting structured data from resumes and evaluating candidate fit with explainable scoring.

---

## 📌 Project Overview
The **AI Resume Screening System** moves beyond simple keyword matching by using contextual understanding to evaluate how a candidate's experience aligns with a specific job description.

### Core Pipeline Architecture
The system implements a modular 4-step pipeline using **LangChain Expression Language (LCEL)**:
1. **Skill Extraction:** Parses raw resume text into structured fields (Skills, Tools, Experience, Education).
2. **Matching Logic:** Contextual comparison between the extracted profile and Job Description.
3. **Fit Scoring:** Assigns a deterministic score (0-100) using few-shot calibration.
4. **Explainability:** Generates a 2-4 sentence justification for the recruiter.

---

## 🛠️ Tech Stack & Tools
* **LLM:** `llama-3.3-70b-versatile` via **Groq** for high-speed, high-accuracy inference.
* **Orchestration:** **LangChain** (PromptTemplates, LCEL, RunnableLambdas).
* **Monitoring:** **LangSmith** for end-to-end tracing and debugging.
* **Environment:** Python 3.11+, `python-dotenv` for secure API management.

---

## 📁 Project Structure
The repository follows a clean, modular design to ensure maintainability:

```text
GenAI_Project_Final/
├── prompts/
│   ├── skill_extraction_prompt.py   # System prompts for Step 1
│   └── matching_prompt.py           # Evaluation logic for Steps 2-4
├── chains/
│   ├── extraction_chain.py          # LCEL chain for data extraction
│   └── matching_chain.py            # LCEL chain for matching/scoring
├── screenshots/                     # Proof of LangSmith Tracing
├── main.py                          # CLI runner for the pipeline
├── AI_Resume_Screening_System.ipynb # Interactive development notebook
├── requirements.txt                 # Dependencies
└── .env                             # Environment variables (Git-ignored)
