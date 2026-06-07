from sentence_transformers import SentenceTransformer
import numpy as np

# lightweight model (fast + free)
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text: str):
    if not text:
        return np.zeros(384, dtype="float32")
    
    return model.encode(text, normalize_embeddings=True).astype("float32")


# -----------------------------
# ATS SCORING
# -----------------------------
def ats_score(parsed: dict):
    score = 0

    if parsed.get("skills"):
        score += 30
    if parsed.get("experience"):
        score += 30
    if parsed.get("projects"):
        score += 25
    if parsed.get("education"):
        score += 15

    return min(score, 100)


# -----------------------------
# JD MATCHING
# -----------------------------
def jd_match(resume_text: str, jd_text: str):
    emb1 = model.encode(resume_text, normalize_embeddings=True)
    emb2 = model.encode(jd_text, normalize_embeddings=True)

    similarity = float(np.dot(emb1, emb2))  # cosine since normalized
    return round(similarity * 100, 2)