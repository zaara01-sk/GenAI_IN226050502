🤖 AI Resume Screening System with LangSmith TracingAn advanced, production-grade AI recruitment tool developed during my GenAI Internship at Innomatics Research Labs. This system leverages Large Language Models (LLMs) to automate the screening process by extracting structured data from resumes and evaluating candidate fit with explainable scoring.📌 Project OverviewThe AI Resume Screening System moves beyond simple keyword matching by using contextual understanding to evaluate how a candidate's experience aligns with a specific job description.Core Pipeline ArchitectureThe system implements a modular 4-step pipeline using LangChain Expression Language (LCEL):Skill Extraction: Parses raw resume text into structured fields (Skills, Tools, Experience, Education).Matching Logic: Contextual comparison between the extracted profile and Job Description.Fit Scoring: Assigns a deterministic score (0-100) using few-shot calibration.Explainability: Generates a 2-4 sentence justification for the recruiter.🛠️ Tech Stack & ToolsLLM: llama-3.3-70b-versatile via Groq for high-speed, high-accuracy inference.Orchestration: LangChain (PromptTemplates, LCEL, RunnableLambdas).Monitoring: LangSmith for end-to-end tracing and debugging.Environment: Python 3.11+, python-dotenv for secure API management.📁 Project StructureThe repository follows a clean, modular design to ensure maintainability:PlaintextGenAI_Project_Final/
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
🔍 Features & Engineering DecisionsAnti-Hallucination Guardrails: Prompts include strict instructions to only extract explicitly stated information, preventing the LLM from "assuming" candidate skills.Few-Shot Prompting: The evaluation prompt is anchored with three candidate archetypes (Strong, Average, Weak) to ensure scoring consistency.Structured JSON Output: Final results are parsed into JSON for seamless integration with HR databases.Observability: Integrated @traceable decorators allow for deep inspection of prompt inputs and LLM outputs in real-time.📈 Performance & Tracing ProofThe system was validated with four distinct runs to verify accuracy and handle edge cases:Candidate TypeExpected FitKey Characteristics DetectedStrong80-95%IIT Bombay, NLP, AWS, 3yr ExpAverage45-65%Python/SQL skills but lacking Deep LearningWeak5-25%Basic IT skills (HTML/Excel) with no ML expDebug0-20%Intentional vague input to test system robustnessNote: Screenshots of these traces are available in the /screenshots directory.🚀 Setup & InstallationClone the Repo:Bashgit clone https://github.com/zaara01-sk/GenAI_IN226050502.git
cd GenAI_Project_Final
Install Dependencies:Bashpip install -r requirements.txt
Configure Environment: Create a .env file in the root directory:Code snippetGROQ_API_KEY=your_groq_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_PROJECT=AI-Resume-Screening-System
Run the System:Bashpython main.py
🎓 Key LearningsModular Design: Learned to separate extraction from evaluation logic to improve model performance and reliability.LCEL Proficiency: Gained hands-on experience using LangChain's pipe operator (|) to create readable, production-grade pipelines.The Value of Tracing: Used LangSmith to identify where the model was making assumptions, allowing for prompt refinements that eliminated hallucinations.Submitted for Innomatics Research Labs Data Science Internship | February 2026.
