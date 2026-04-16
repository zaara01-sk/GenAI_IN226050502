# prompts/matching_prompt.py
# Prompt template for matching extracted resume data against a job description
# and assigning a score with full explanation.

from langchain.prompts import PromptTemplate

MATCHING_SCORING_TEMPLATE = """
You are an expert technical recruiter evaluating candidate fit for a job role.

Job Description:
{job_description}

Candidate Profile (extracted from resume):
{extracted_profile}

Your task:
1. Compare the candidate's skills, tools, and experience with the job requirements.
2. Identify which required skills are PRESENT and which are MISSING.
3. Assign a FIT SCORE between 0 and 100 based on how well the candidate matches.
4. Provide a clear, honest explanation for the score.

Scoring Guide:
- 80-100: Strong match — most required skills present, relevant experience
- 50-79: Average match — some required skills present, partial experience
- 0-49: Weak match — few or no required skills, insufficient experience

IMPORTANT RULES:
- Base your score ONLY on information in the candidate profile above.
- Do NOT assume the candidate has skills not listed in their profile.
- Be honest and direct.

Return your response in this exact format:

MATCHED_SKILLS: [skills present in both resume and job description]
MISSING_SKILLS: [skills required by job but absent in resume]
FIT_SCORE: [integer between 0-100]
SCORE_EXPLANATION: [2-4 sentences explaining why this score was given, referencing specific skills and gaps]
HIRING_RECOMMENDATION: [one of: SHORTLIST / CONSIDER / REJECT]
"""

matching_scoring_prompt = PromptTemplate(
    input_variables=["job_description", "extracted_profile"],
    template=MATCHING_SCORING_TEMPLATE
)
