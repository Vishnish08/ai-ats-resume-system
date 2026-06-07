# test.py (final, flexible version)
import io, json
from pathlib import Path
from resume_module import analyze_resume, extract_text_from_file
from ats_scoring import ats_score_no_jd

# ---------- CONFIG ----------
RESUME_PATH = "temp_resume.pdf"          # Change to your resume file
JOB_KEYWORDS = ["Python", "Machine Learning", "Deep Learning",
                "Data Analysis", "SQL", "Docker"]  # Optional for fit score

# Load skill database
skill_db = json.loads(Path("skills_db.json").read_text(encoding="utf8"))

# ---------- LOAD RESUME ----------
with open(RESUME_PATH, "rb") as f:
    uploaded_file = io.BytesIO(f.read())
    uploaded_file.name = RESUME_PATH  # Required for type detection

# Quick extraction check
text = extract_text_from_file(uploaded_file)
used_ocr = "OCR" if not text.strip() else "Standard"

# ---------- FULL ANALYSIS ----------
uploaded_file.seek(0)
result = analyze_resume(uploaded_file, JOB_KEYWORDS)

# JD-free ATS score
jd_free_ats = ats_score_no_jd(text, skill_db)

# ---------- OUTPUT REPORT ----------
print("\n" + "="*80)
print("🌈  RESUME ANALYSIS REPORT")
print("="*80)
print(f"Extraction method : {used_ocr}")
print(f"JD-free ATS score : {jd_free_ats:.1f}%")
print(f"Keyword fit score : {result.get('fit_score',0):.1f}%")
print("-"*80)

# Candidate Information
ci = result.get("candidate_information", {})
if ci:
    print("\n👤  CANDIDATE INFORMATION")
    print(f"Name  : {ci.get('name','N/A')}")
    print(f"Email : {ci.get('email','N/A')}")
    print(f"Phone : {ci.get('phone','N/A')}")
    for key, link in ci.get("social_links", {}).items():
        print(f"{key.title():<8}: {link}")

# Skills
skills = result.get("resume_skills", [])
missing = result.get("missing_skills", [])
print(f"\n✅  EXTRACTED SKILLS ({len(skills)})")
for s in skills:
    print(f"   {s}")

if missing:
    print(f"\n❌  MISSING KEYWORDS ({len(missing)})")
    for m in missing:
        print(f"   {m}")

# Projects
projects = result.get("projects", [])
if projects:
    print(f"\n📂  PROJECTS ({len(projects)})")
    for p in projects:
        title, link = p.get("title"), p.get("link")
        print(f" - {title}" + (f" ({link})" if link else ""))

# Certifications
certs = result.get("certifications", [])
if certs:
    print(f"\n📜  CERTIFICATIONS ({len(certs)})")
    for c in certs:
        title, link = c.get("title"), c.get("link")
        print(f" - {title}" + (f" ({link})" if link else ""))

# Education
education = result.get("education_found", [])
if education:
    print(f"\n🎓  EDUCATION ({len(education)})")
    for e in education:
        print(f" - {e}")

# Top Recommended Roles
top_roles = result.get("recommended_roles", [])
if top_roles:
    print(f"\n🏆  TOP 5 RECOMMENDED JOB ROLES")
    for role in top_roles:
        print(f" - {role}")

# Suggestions
suggestions = result.get("suggestions", [])
if suggestions:
    print(f"\n💡  CAREER IMPROVEMENT SUGGESTIONS")
    for s in suggestions:
        print(f" - {s}")

print("\n" + "="*80)
print("End of Report")