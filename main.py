# main.py
# AI Resume Screening System — Main Pipeline
# Innomatics Data Science Internship Assignment | February 2026
# 
# Pipeline: Resume → Skill Extraction → Matching → Scoring → Explanation → Tracing
#
# This script runs the full evaluation pipeline for 3 candidates 
# (Strong, Average, Weak) against a Data Scientist job description.
# LangSmith tracing is enabled via environment variables.

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda
from langsmith import traceable

# Load environment variables from .env file
load_dotenv()

# ─────────────────────────────────────────────
# LangSmith Tracing Setup (Mandatory)
# ─────────────────────────────────────────────
# These env variables are set in the .env file.
# LANGCHAIN_TRACING_V2=true enables automatic tracing of all LangChain runs.
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "AI-Resume-Screening-System"  # Project name in LangSmith

# ─────────────────────────────────────────────
# Import our modular chains
# ─────────────────────────────────────────────
from chains.extraction_chain import build_extraction_chain
from chains.matching_chain import build_matching_chain

# ─────────────────────────────────────────────
# Sample Data: Job Description
# ─────────────────────────────────────────────
JOB_DESCRIPTION = """
Position: Data Scientist
Company: TechCorp Analytics

Required Skills:
- Python (pandas, numpy, scikit-learn)
- Machine Learning (supervised and unsupervised)
- Deep Learning (TensorFlow or PyTorch)
- SQL and database querying
- Data visualization (matplotlib, seaborn, or Tableau)
- Feature engineering and model evaluation

Nice to Have:
- Experience with cloud platforms (AWS / GCP / Azure)
- NLP or computer vision experience
- MLOps / model deployment experience

Experience Required: 2+ years in a data science or ML role
Education: Bachelor's or Master's in Computer Science, Statistics, or related field
"""

# ─────────────────────────────────────────────
# Sample Data: 3 Resumes
# ─────────────────────────────────────────────

# Resume 1 — Strong Candidate
RESUME_STRONG = """
Name: Ananya Sharma
Email: ananya.sharma@email.com

Summary:
Data Scientist with 3 years of experience building ML models and deploying them at scale.

Skills:
Python, pandas, numpy, scikit-learn, TensorFlow, PyTorch, SQL, matplotlib, seaborn, Tableau,
feature engineering, model evaluation, A/B testing, NLP, AWS SageMaker, MLflow

Experience:
- Data Scientist at Flipkart Analytics (2022–Present, 2 years)
  Built recommendation engine using collaborative filtering, improved CTR by 18%.
  Deployed ML models on AWS SageMaker with MLflow tracking.
  
- Junior Data Scientist at InfoEdge (2021–2022, 1 year)
  Worked on churn prediction using Random Forest and XGBoost.
  Wrote SQL queries for large-scale data extraction.

Education:
M.Tech in Data Science — IIT Bombay, 2021

Certifications:
IBM Data Science Professional Certificate, AWS Certified Machine Learning Specialty

Projects:
- NLP Sentiment Analysis Pipeline (BERT-based)
- Customer Churn Prediction Dashboard
- Image Classification using CNN (PyTorch)
"""

# Resume 2 — Average Candidate
RESUME_AVERAGE = """
Name: Ravi Mehta
Email: ravi.mehta@email.com

Summary:
Aspiring data scientist with 1 year of internship experience and strong academic background.

Skills:
Python, pandas, numpy, scikit-learn, SQL, matplotlib

Experience:
- Data Science Intern at Infosys (2023–2024, 10 months)
  Worked on regression models for sales forecasting.
  Used Python and pandas for data cleaning and EDA.
  Created visualizations using matplotlib.

Education:
B.E. in Computer Science — Pune University, 2023

Projects:
- House Price Prediction using Linear Regression
- COVID-19 Data Analysis (Exploratory)
"""

# Resume 3 — Weak Candidate
RESUME_WEAK = """
Name: Karan Patil
Email: karan.patil@email.com

Summary:
Fresh graduate looking for entry level opportunities in IT.

Skills:
MS Excel, PowerPoint, basic Python (loops, functions), HTML, CSS

Experience:
No professional work experience.

Education:
BCA — Nagpur University, 2024

Projects:
- College website using HTML and CSS
- Excel-based attendance tracker
"""

# ─────────────────────────────────────────────
# Initialize LLM
# ─────────────────────────────────────────────
def get_llm():
    """Initialize the OpenAI LLM with GPT-4o-mini for cost efficiency."""
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,           # Temperature 0 = deterministic, no hallucinations
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

# ─────────────────────────────────────────────
# Core Pipeline Function
# ─────────────────────────────────────────────
@traceable(name="resume_screening_pipeline")  # LangSmith trace decorator
def run_screening_pipeline(candidate_name: str, resume_text: str, job_description: str, llm):
    """
    Runs the full 4-step pipeline for a single resume:
    Step 1: Extract skills/experience from resume
    Step 2+3+4: Match against JD, score, and explain
    
    Args:
        candidate_name: Label for this candidate (e.g., "Strong Candidate")
        resume_text: Raw resume text
        job_description: Job description text
        llm: Instantiated LangChain LLM
    
    Returns:
        dict with extracted_profile, score_result, and parsed score
    """
    print(f"\n{'='*60}")
    print(f"Processing: {candidate_name}")
    print(f"{'='*60}")
    
    # Build chains
    extraction_chain = build_extraction_chain(llm)
    matching_chain = build_matching_chain(llm)
    
    # ── Step 1: Skill Extraction ──────────────────────────────
    print("\n[Step 1] Extracting skills and experience...")
    extraction_result = extraction_chain.invoke({"resume_text": resume_text})
    extracted_profile = extraction_result.content
    print(extracted_profile)
    
    # ── Step 2 + 3 + 4: Match → Score → Explain ──────────────
    print("\n[Step 2/3/4] Matching, scoring, and explaining...")
    scoring_result = matching_chain.invoke({
        "job_description": job_description,
        "extracted_profile": extracted_profile
    })
    score_output = scoring_result.content
    print(score_output)
    
    # ── Parse score for summary ───────────────────────────────
    fit_score = None
    for line in score_output.split("\n"):
        if line.startswith("FIT_SCORE:"):
            try:
                fit_score = int(line.replace("FIT_SCORE:", "").strip())
            except ValueError:
                fit_score = "N/A"
            break
    
    return {
        "candidate": candidate_name,
        "extracted_profile": extracted_profile,
        "score_result": score_output,
        "fit_score": fit_score
    }

# ─────────────────────────────────────────────
# Main Execution
# ─────────────────────────────────────────────
def main():
    llm = get_llm()
    
    # Define the 3 candidates to screen
    candidates = [
        ("Strong Candidate — Ananya Sharma", RESUME_STRONG),
        ("Average Candidate — Ravi Mehta",   RESUME_AVERAGE),
        ("Weak Candidate — Karan Patil",     RESUME_WEAK),
    ]
    
    results = []
    for name, resume in candidates:
        result = run_screening_pipeline(
            candidate_name=name,
            resume_text=resume,
            job_description=JOB_DESCRIPTION,
            llm=llm
        )
        results.append(result)
    
    # ── Final Summary ─────────────────────────────────────────
    print("\n\n" + "="*60)
    print("SCREENING SUMMARY")
    print("="*60)
    print(f"{'Candidate':<40} {'Fit Score':>10}")
    print("-"*60)
    for r in results:
        print(f"{r['candidate']:<40} {str(r['fit_score']):>10}")
    
    return results

if __name__ == "__main__":
    main()
