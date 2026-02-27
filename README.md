# 📄 AI Resume Builder & ATS Score Checker

## 📌 Project Overview
Many candidates struggle to present their technical skills and projects in an optimized, professional format. Furthermore, mapping coursework and technical skills to specific job descriptions is inefficient and often leads to low application success rates due to Applicant Tracking System (ATS) filters.

This project is an **AI/ML Capstone Project** that solves this problem by combining Generative AI with traditional Machine Learning. It automatically generates tailored, highly technical resumes from raw student data and calculates a real-time ATS compatibility score against a target job description.

## ✨ Features
* **Generative AI Resume Creation:** Utilizes Google's Gemini 2.5 Flash model to transform basic user inputs (Education, Skills, Projects) into professionally formatted, action-oriented resume bullet points.
* **Applicant Tracking System (ATS) Scoring:** Employs Natural Language Processing (NLP) to calculate how well the generated resume matches a given Job Description.
* **Interactive Web Interface:** Built entirely in Python using Streamlit for a seamless, responsive user experience.
* **One-Click Download:** Users can export their newly generated AI resume directly as a text file.

## 🛠️ Technology Stack & Architecture
* **Frontend & Backend:** [Streamlit](https://streamlit.io/) (Python)
* **Generative AI Engine:** [Google Gemini API](https://ai.google.dev/) (`gemini-2.5-flash`)
* **Machine Learning Pipeline:** [Scikit-Learn](https://scikit-learn.org/)
  * **Text Vectorization:** `TfidfVectorizer` (Term Frequency-Inverse Document Frequency)
  * **Similarity Calculation:** `cosine_similarity` algorithm
* **Environment Management:** `python-dotenv`

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
