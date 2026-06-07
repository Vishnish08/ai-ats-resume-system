from core.llm_engine import ask_llm
import json

def recommend_roles(resume_text):
    prompt = f"""
You are a senior recruiter.

Give TOP 5 job roles.

Return ONLY JSON array:
[
  {{
    "role": "",
    "match": 0,
    "missing_skills": [],
    "reason": ""
  }}
]

Resume:
{resume_text}
"""
    return ask_llm(prompt)