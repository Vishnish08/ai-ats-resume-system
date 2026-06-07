import json
import re
from core.llm_engine import ask_llm


def safe_json_load(text: str):
    """
    Robust JSON extractor (handles messy LLM output)
    """
    try:
        return json.loads(text)
    except:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except:
                return {}
        return {}


def parse_resume(text: str):
    prompt = f"""
You are an expert resume parser.

Extract structured JSON from resume.

Return ONLY valid JSON:

{{
  "name": "",
  "email": "",
  "skills": [],
  "experience": [
    {{
      "company": "",
      "role": "",
      "duration": "",
      "description": ""
    }}
  ],
  "projects": [
    {{
      "name": "",
      "description": ""
    }}
  ],
  "education": [],
  "certifications": []
}}

RULES:
- Return ONLY JSON
- No explanation
- No markdown
- If missing, use empty values

Resume:
{text}
"""

    response = ask_llm(prompt)
    return safe_json_load(response)