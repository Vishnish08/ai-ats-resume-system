import os
import json
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def safe_json(text):
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


def call_llm(prompt):
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an AI recruiter assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )
    return res.choices[0].message.content


def parse_resume(text):
    prompt = f"""
Extract resume into JSON only:

{{
  "name": "",
  "skills": [],
  "experience": [],
  "projects": [],
  "education": [],
  "certifications": []
}}

Resume:
{text}
"""
    return safe_json(call_llm(prompt))


def recommend_roles(text):
    prompt = f"""
Return TOP 5 roles as JSON array only.

Resume:
{text}
"""
    return safe_json(call_llm(prompt))


def rewrite_resume(text):
    prompt = f"""
Rewrite resume into ATS STAR bullets.

Resume:
{text}
"""
    return call_llm(prompt)


def skill_gap(role, skills):
    prompt = f"""
Role: {role}
Skills: {skills}

Return JSON:
{{
  "30_days": [],
  "60_days": [],
  "90_days": []
}}
"""
    return safe_json(call_llm(prompt))