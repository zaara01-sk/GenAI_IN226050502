# chains/extraction_chain.py
# Defines the LangChain LCEL chain for Step 1: Skill Extraction
# Uses the pipe (|) operator from LangChain Expression Language (LCEL)

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompts.skill_extraction_prompt import skill_extraction_prompt

def build_extraction_chain(llm):
    """
    Builds and returns the skill extraction chain using LCEL.
    
    Args:
        llm: An instantiated LangChain LLM object (e.g., ChatOpenAI)
    
    Returns:
        A runnable LCEL chain: prompt | llm
    """
    # LCEL pipe syntax: prompt template → LLM
    extraction_chain = skill_extraction_prompt | llm
    return extraction_chain
