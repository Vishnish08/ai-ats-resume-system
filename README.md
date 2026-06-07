# 🔥 AI ATS Resume Intelligence System

An AI-powered **Resume Screening + ATS Scoring + Candidate Ranking System** built using **Streamlit, Groq LLM, Sentence Transformers, and FAISS vector search**.

This project simulates a real-world **AI recruiter pipeline** that parses resumes, scores candidates, recommends roles, rewrites resumes, and performs semantic search over candidates.

---

## 🚀 Features

### 📄 Resume Intelligence
- Upload PDF/DOCX resumes
- Automatic parsing into structured JSON
- Extracts:
  - Skills
  - Experience
  - Projects
  - Education
  - Certifications

---

### 📊 ATS Scoring Engine
- Rule-based ATS score (0–100)
- Evaluates:
  - Skills presence
  - Experience quality
  - Projects
  - Education completeness

---

### 🎯 Job Description Matching
- Semantic similarity using **Sentence Transformers**
- Compares resume vs job description
- Returns match percentage

---

### 🤖 AI Role Recommendation (Groq LLM)
- Suggests top 5 job roles
- Includes:
  - Match score
  - Missing skills
  - Reasoning

---

### ✍️ Resume Enhancement
- STAR-format resume rewriting
- ATS-optimized bullet points
- Action-oriented improvements

---

### 🔍 AI Candidate Search (FAISS)
- Vector-based semantic search
- Find similar candidates instantly
- Scalable retrieval system

---

## 🧠 Tech Stack

- **Frontend:** Streamlit
- **LLM:** Groq API (LLaMA 3 / Mixtral models)
- **Embeddings:** SentenceTransformers (MiniLM)
- **Vector DB:** FAISS
- **Backend:** Python
- **Parsing:** PyPDF2 / docx2txt

---

## 📁 Project Structure
AI_CAREER/
│
├── app.py                  # Streamlit frontend UI
├── resume_module.py        # Resume parsing + orchestration layer
├── llm_engine.py           # Groq LLM-based intelligence layer
├── ats_engine.py           # ATS scoring + matching logic
├── faiss_store.py          # Vector DB (FAISS) for candidate search
│
├── vector_store/           # Embedding + retrieval utilities
├── engine/                 # Core processing modules
├── data/                   # Stored embeddings & metadata
│
├── .env                    # API keys (not pushed to GitHub)
└── requirements.txt

---

## ⚙️ Installation

### 1️⃣ Clone repo
```bash
git clone https://github.com/YOUR_USERNAME/ai-ats-resume-system.git
cd ai-ats-resume-system
```

### 2️⃣ Create virtual environment (Python 3.11 recommended)
python -m venv .venv
.venv\Scripts\activate

### 3️⃣ Install dependencies
pip install -r requirements.txt
📦 Requirements

If you don't have requirements.txt,

use:
streamlit
python-dotenv
groq
sentence-transformers
faiss-cpu
numpy
pandas
scikit-learn
docx2txt
PyPDF2


###🔑 Environment Variables

Create a .env file:
GROQ_API_KEY=your_api_key_here

### ▶️ Run Project
streamlit run app.py

## 📊 System Flow
Resume Upload
      ↓
Text Extraction
      ↓
LLM Parsing (Groq)
      ↓
ATS Scoring Engine
      ↓
Embedding Generation
      ↓
FAISS Vector Storage
      ↓
Role Recommendation + Search
