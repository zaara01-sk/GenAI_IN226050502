# prompts/skill_extraction_prompt.py
# Prompt template for extracting structured information from a resume

from langchain.prompts import PromptTemplate

# This prompt tells the LLM exactly what to extract and how to format it.
# I'm keeping it strict to avoid hallucination — the model should ONLY extract
# what is explicitly mentioned in the resume text.

SKILL_EXTRACTION_TEMPLATE = """
You are a precise resume parser. Your job is to extract structured information 
from the resume text below.

IMPORTANT RULES:
- Only extract skills, tools, and experience that are EXPLICITLY stated in the resume.
- Do NOT infer or assume anything not written in the resume.
- If a field has no data, return "Not mentioned".

Resume Text:
{resume_text}

Extract and return the following in this exact format:

SKILLS: [comma-separated list of technical skills]
TOOLS: [comma-separated list of tools/technologies/frameworks]
EXPERIENCE: [brief summary of total experience and roles held]
EDUCATION: [highest qualification and institution if mentioned]
PROJECTS: [comma-separated list of notable project names or "Not mentioned"]
CERTIFICATIONS: [comma-separated list or "Not mentioned"]
"""

skill_extraction_prompt = PromptTemplate(
    input_variables=["resume_text"],
    template=SKILL_EXTRACTION_TEMPLATE
)
