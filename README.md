# 🔥 AI ATS Resume Intelligence System

An AI-powered Resume Screening, ATS Scoring, Role Recommendation, and Candidate Search system built using Streamlit, Groq LLM, Sentence Transformers, and FAISS vector database. This project simulates a real-world AI Recruiter pipeline that extracts resume intelligence, evaluates candidates, and enables semantic search across resumes.

## 🚀 Features

### 📄 Resume Intelligence
- Upload PDF/DOCX resumes
- Extract structured JSON data including name, skills, experience, projects, education, and certifications using LLM-based parsing.

### 📊 ATS Scoring Engine
- Rule-based ATS scoring system (0–100)
- Evaluates skills coverage, experience depth, project quality, and education relevance.

### 🎯 Job Description Matching
- Semantic similarity using Sentence Transformers
- Compare resume vs job description
- Returns match percentage score

### 🤖 AI Role Recommendation (Groq LLM)
- Suggests top 5 job roles based on resume
- Provides match score, missing skills, and reasoning

### ✍️ Resume Enhancement
- STAR-format resume rewriting
- ATS-friendly bullet optimization
- Action-driven improvements

### 🔍 Semantic Candidate Search (FAISS)
- Vector-based similarity search
- Retrieve similar resumes instantly
- Scalable recruiter-style search system

## 🧠 Tech Stack

Streamlit, Python, Groq API (LLaMA 3 / Mixtral), SentenceTransformers (MiniLM), FAISS, PyPDF2, docx2txt, scikit-learn, numpy, pandas

## 📁 Project Structure

AI_CAREER/ ├── app.py ├── resume_module.py ├── llm_engine.py ├── ats_engine.py ├── faiss_store.py ├── vector_store/ ├── engine/ ├── data/ ├── .env └── requirements.txt

## ⚙️ Installation

### 1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/ai-ats-resume-system.git
cd ai-ats-resume-system

### 2️⃣ Create Virtual Environment (Python 3.11 recommended)
python -m venv .venv  
.venv\Scripts\activate   (Windows)

### 3️⃣ Install Dependencies
pip install -r requirements.txt

If requirements.txt missing:
pip install streamlit python-dotenv groq sentence-transformers faiss-cpu numpy pandas scikit-learn docx2txt PyPDF2

## 🔐 Environment Variables

Create a .env file:

GROQ_API_KEY=your_api_key_here

## ▶️ Run Project

streamlit run app.py

## 🔄 System Flow

Resume Upload → Text Extraction → LLM Parsing (Groq) → ATS Scoring Engine → Embedding Generation → FAISS Vector Storage → Role Recommendation + Search

## 📊 Core Modules

Resume Parser: Extracts structured resume JSON using LLM  
ATS Engine: Scores resume based on skills, experience, projects, education  
Role Recommender: Suggests job roles using Groq LLM  
FAISS Engine: Semantic similarity search across resumes  

## ⚠️ Known Issues

- Groq API rate limits may occur
- First run downloads embedding model
- Streamlit reruns on every interaction

## 🚀 Future Improvements

- Multi-user recruiter dashboard
- Cloud vector database integration
- Resume ranking system
- Improved LLM scoring system
- PDF export for rewritten resumes

## 👨‍💻 Author

AI ATS Resume Intelligence System — Built as a GenAI + ML portfolio project

## ⭐ Support

If you like this project, star it on GitHub and share with recruiters
