# 🤖 AI Resume Screening System with LangSmith Tracing

[![LangChain](https://img.shields.io/badge/Framework-LangChain-blue)](https://python.langchain.com/)
[![LLM](https://img.shields.io/badge/LLM-Groq_Llama--3.3--70b-orange)](https://groq.com/)
[![Observability](https://img.shields.io/badge/Tracing-LangSmith-green)](https://smith.langchain.com/)

An advanced, production-grade AI recruitment tool developed during my GenAI Internship at **Innomatics Research Labs**. [cite_start]This system leverages Large Language Models (LLMs) to automate the screening process by extracting structured data from resumes and evaluating candidate fit with explainable scoring[cite: 141, 142].

---

## 📌 Project Overview
[cite_start]The **AI Resume Screening System** moves beyond simple keyword matching by using contextual understanding to evaluate how a candidate's experience aligns with a specific job description[cite: 145].

### Core Pipeline Architecture
[cite_start]The system implements a modular 4-step pipeline using **LangChain Expression Language (LCEL)**[cite: 151]:
1. [cite_start]**Skill Extraction:** Parses raw resume text into structured fields (Skills, Tools, Experience, Education)[cite: 151].
2. [cite_start]**Matching Logic:** Contextual comparison between the extracted profile and Job Description[cite: 151].
3. [cite_start]**Fit Scoring:** Assigns a deterministic score (0-100) using few-shot calibration[cite: 151, 180].
4. [cite_start]**Explainability:** Generates a 2-4 sentence justification for the recruiter[cite: 151].

---

## 🛠️ Tech Stack & Tools
* **LLM:** `llama-3.3-70b-versatile` via **Groq** for high-speed, high-accuracy inference.
* [cite_start]**Orchestration:** **LangChain** (PromptTemplates, LCEL, RunnableLambdas)[cite: 143, 160].
* [cite_start]**Monitoring:** **LangSmith** for end-to-end tracing and debugging[cite: 143, 182].
* [cite_start]**Environment:** Python 3.11+, `python-dotenv` for secure API management[cite: 143, 233].

---

## 📁 Project Structure
[cite_start]The repository follows a clean, modular design to ensure maintainability[cite: 155]:

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
