# 🤖 AI Resume Screening System with LangSmith Tracing

[![LangChain](https://img.shields.io/badge/Framework-LangChain-blue)](https://python.langchain.com/)
[![LLM](https://img.shields.io/badge/LLM-Groq_Llama--3.3--70b-orange)](https://groq.com/)
[![Observability](https://img.shields.io/badge/Tracing-LangSmith-green)](https://smith.langchain.com/)

An advanced, production-grade AI recruitment tool developed during my GenAI Internship at **Innomatics Research Labs**. This system leverages Large Language Models (LLMs) to automate the screening process by extracting structured data from resumes and evaluating candidate fit with explainable scoring.

---

## 📌 Project Overview
The **AI Resume Screening System** moves beyond keyword matching by using contextual understanding to evaluate how a candidate's experience aligns with a specific job description.

### Core Pipeline Architecture:
The system implements a modular 4-step pipeline using **LangChain Expression Language (LCEL)**:
1.  [cite_start]**Skill Extraction:** Parses raw resume text into structured fields (Skills, Tools, Experience, Education)[cite: 60, 151].
2.  [cite_start]**Matching Logic:** Contextual comparison between the extracted profile and Job Description[cite: 65, 151].
3.  [cite_start]**Fit Scoring:** Assigns a deterministic score (0-100) using few-shot calibration[cite: 151, 180].
4.  [cite_start]**Explainability:** Generates a 2-4 sentence justification for the recruiter[cite: 151, 196].

---

## 🛠️ Tech Stack & Tools
- **LLM:** `llama-3.3-70b-versatile` via **Groq** for high-speed, high-accuracy inference.
- [cite_start]**Orchestration:** **LangChain** (PromptTemplates, LCEL, RunnableLambdas)[cite: 81, 83, 163, 169].
- [cite_start]**Monitoring:** **LangSmith** for end-to-end tracing and debugging[cite: 84, 182].
- [cite_start]**Environment:** Python 3.11+, `python-dotenv` for secure API management[cite: 233].

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
```

---

## 🔍 Features & Engineering Decisions
- [cite_start]**Anti-Hallucination Guardrails:** Prompts include strict instructions to only extract explicitly stated information, preventing the LLM from "assuming" candidate skills[cite: 99, 132, 196].
- [cite_start]**Few-Shot Prompting:** The evaluation prompt is anchored with three candidate archetypes (Strong, Average, Weak) to ensure scoring consistency[cite: 102, 180, 218].
- [cite_start]**Structured JSON Output:** Final results are parsed into JSON for seamless integration with HR databases[cite: 104, 219].
- [cite_start]**Observability:** Integrated `@traceable` decorators allow for deep inspection of prompt inputs and LLM outputs in real-time[cite: 185, 187].

---

## 📈 Performance & Tracing Proof
[cite_start]As per the assignment requirements, the system was validated with four distinct runs[cite: 189, 190]:

| Candidate Type | Expected Fit | Key Characteristics Detected |
| :--- | :--- | :--- |
| **Strong** | 80-95% | [cite_start]IIT Bombay, NLP, AWS, 3yr Exp [cite: 189, 204] |
| **Average** | 45-65% | [cite_start]Python/SQL skills but lacking Deep Learning [cite: 189, 204] |
| **Weak** | 5-25% | [cite_start]Basic IT skills (HTML/Excel) with no ML exp [cite: 190, 204] |
| **Debug** | 0-20% | [cite_start]Intentional vague input to test system robustness [cite: 190, 191] |

*Note: Screenshots of these traces are available in the `/screenshots` directory.*

---

## 🚀 Setup & Installation
1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/zaara01-sk/GenAI_IN226050502.git](https://github.com/zaara01-sk/GenAI_IN226050502.git)
    cd GenAI_Project_Final
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Environment:** Create a `.env` file with:
    ```env
    GROQ_API_KEY=your_groq_key
    LANGCHAIN_TRACING_V2=true
    LANGCHAIN_API_KEY=your_langsmith_key
    LANGCHAIN_PROJECT=AI-Resume-Screening-System
    ```
4.  **Run the System:**
    ```bash
    python main.py
    ```

---

## 🎓 Key Learnings
This project provided deep insights into building production-level LLM applications:
- [cite_start]**LCEL vs. Traditional Chains:** Moving from prompt-usage to building composable pipelines using the pipe operator (`|`) significantly improves code readability[cite: 224, 225].
- **Tracing is Non-Negotiable:** Debugging LLMs without tracing is guesswork. [cite_start]LangSmith provided the transparency needed to catch model drift and refine prompts[cite: 226].

---
**Submitted for Innomatics Research Labs Data Science Internship | [cite_start]February 2026**[cite: 142].
```

