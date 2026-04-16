# chains/matching_chain.py
# Defines the LangChain LCEL chain for Steps 2, 3, 4: Matching + Scoring + Explanation
# This is the core evaluation chain of the pipeline.

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompts.matching_prompt import matching_scoring_prompt

def build_matching_chain(llm):
    """
    Builds and returns the matching + scoring + explanation chain using LCEL.
    
    Args:
        llm: An instantiated LangChain LLM object (e.g., ChatOpenAI)
    
    Returns:
        A runnable LCEL chain: prompt | llm
    """
    # LCEL pipe syntax: matching prompt → LLM
    matching_chain = matching_scoring_prompt | llm
    return matching_chain
