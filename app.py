import streamlit as st

from resume_module import analyze_resume
from ats_engine import jd_match, ats_score
from llm_engine import recommend_roles, rewrite_resume, skill_gap
from vector.faiss_store import add_candidate, search_candidates


st.set_page_config(page_title="AI Recruiter System", layout="wide")

st.title("AI Recruiter System (Resume Intelligence Engine)")


# ---------------- INPUTS ----------------
file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
jd = st.text_area("Paste Job Description (optional)")
query = st.text_input("Search Candidates (FAISS)")


# ---------------- MAIN PIPELINE ----------------
if file:

    with st.spinner("Parsing resume..."):
        result = analyze_resume(file)

    parsed = result["parsed"]
    raw_text = result["raw_text"]

    # ---------------- OUTPUT ----------------
    st.subheader("📄 Parsed Resume")
    st.json(parsed)

    st.metric("ATS Score", f"{ats_score(parsed)}/100")

    if jd:
        st.metric("JD Match", f"{jd_match(raw_text, jd)}%")

    # ---------------- LLM FEATURES ----------------
    st.subheader("🎯 Role Recommendations")
    try:
        roles = recommend_roles(raw_text)
        st.json(roles)
    except Exception as e:
        st.error(f"Role recommendation failed: {e}")

    st.subheader("✍️ STAR Resume Rewrite")
    try:
        st.write(rewrite_resume(raw_text))
    except Exception as e:
        st.error(f"Rewrite failed: {e}")

    # ---------------- VECTOR STORE ----------------
    try:
        add_candidate(raw_text, parsed)
    except Exception as e:
        st.warning(f"Vector DB insert failed: {e}")


# ---------------- SEARCH ----------------
if query:
    st.subheader("🔎 Candidate Search Results")
    try:
        results = search_candidates(query)
        st.json(results)
    except Exception as e:
        st.error(f"Search failed: {e}")