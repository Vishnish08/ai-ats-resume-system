import io
import pdfplumber
import docx2txt
from llm_engine import parse_resume, recommend_roles, rewrite_resume, skill_gap


def extract_text(file):
    name = file.name.lower()

    if name.endswith(".pdf"):
        with pdfplumber.open(io.BytesIO(file.read())) as pdf:
            return "\n".join([p.extract_text() or "" for p in pdf.pages])

    elif name.endswith(".docx"):
        return docx2txt.process(file)

    return file.read().decode("utf-8", errors="ignore")


def analyze_resume(file):
    text = extract_text(file)

    parsed = parse_resume(text)

    return {
        "raw_text": text,
        "parsed": parsed
    }