import faiss
import numpy as np
import pickle
import os

# CHANGE THIS IMPORT if needed
from ats_engine import get_embedding  # safer for your project

# -----------------------------
# CONFIG
# -----------------------------
DIMENSION = 384

index = faiss.IndexFlatL2(DIMENSION)
metadata_store = []

INDEX_FILE = "faiss.index"
META_FILE = "metadata.pkl"


# -----------------------------
# LOAD IF EXISTS
# -----------------------------
def load_index():
    global index, metadata_store

    if os.path.exists(INDEX_FILE):
        index = faiss.read_index(INDEX_FILE)

    if os.path.exists(META_FILE):
        with open(META_FILE, "rb") as f:
            metadata_store = pickle.load(f)


# -----------------------------
# SAVE
# -----------------------------
def save_index():
    faiss.write_index(index, INDEX_FILE)

    with open(META_FILE, "wb") as f:
        pickle.dump(metadata_store, f)


# -----------------------------
# ADD CANDIDATE
# -----------------------------
def add_candidate(raw_text: str, parsed: dict):
    embedding = np.array(get_embedding(raw_text), dtype="float32")

    # ensure correct shape for FAISS
    if len(embedding.shape) == 1:
        embedding = np.expand_dims(embedding, axis=0)

    index.add(embedding)

    metadata_store.append({
        "raw_text": raw_text,
        "parsed": parsed
    })

    save_index()


# -----------------------------
# SEARCH
# -----------------------------
def search_candidates(query: str, k: int = 5):
    if len(metadata_store) == 0:
        return []

    query_vec = np.array(get_embedding(query), dtype="float32")

    if len(query_vec.shape) == 1:
        query_vec = np.expand_dims(query_vec, axis=0)

    distances, indices = index.search(query_vec, k)

    results = []
    for i in indices[0]:
        if 0 <= i < len(metadata_store):
            results.append(metadata_store[i])

    return results