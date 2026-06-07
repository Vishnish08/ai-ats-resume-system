from core.embeddings import get_embedding
from sentence_transformers import util


def calculate_similarity(resume_text, jd_text):
    emb1 = get_embedding(resume_text)
    emb2 = get_embedding(jd_text)

    return float(util.cos_sim(emb1, emb2)) * 100


def skill_overlap_score(resume_skills, jd_text):
    jd_text = jd_text.lower()
    match = 0

    for skill in resume_skills:
        if skill.lower() in jd_text:
            match += 1

    if len(resume_skills) == 0:
        return 0

    return (match / len(resume_skills)) * 100


def rank_candidates(candidates, jd_text):
    """
    candidates = [
        {
            "parsed": {...},
            "raw_text": "..."
        }
    ]
    """

    ranked = []

    for c in candidates:
        parsed = c.get("parsed", {})
        resume_text = c.get("raw_text", "")

        semantic_score = calculate_similarity(resume_text, jd_text)

        skills = parsed.get("skills", [])
        skill_score = skill_overlap_score(skills, jd_text)

        experience_score = len(parsed.get("experience", [])) * 10

        final_score = (
            0.6 * semantic_score +
            0.3 * skill_score +
            0.1 * min(experience_score, 100)
        )

        ranked.append({
            "name": parsed.get("name", "Unknown"),
            "score": round(final_score, 2),
            "semantic": round(semantic_score, 2),
            "skill_match": round(skill_score, 2),
            "experience_score": experience_score
        })

    ranked = sorted(ranked, key=lambda x: x["score"], reverse=True)

    return ranked