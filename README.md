# HireMate
# 📘 HireMate – AI Hiring Assistant

**Holboxathon 2025 Submission**

---

## 📌 Table of Contents

1. Overview
2. Problem Statement
3. Solution Summary
4. System Architecture Diagram
5. Models / Logic Used
6. Technologies Used
7. Installation Instructions
8. How to Use the App
9. Screenshots
10. Future Improvements
11. Contributors

---

## 🧠 Overview

**HireMate** is an intelligent, lightweight, no-paid-AI hiring assistant. It helps recruiters simplify the hiring process by enabling:

* Resume upload and parsing
* Rule-based candidate-to-job matching
* Candidate scoring and ranking
* Interview email auto-generation
* A clean and demo-ready Streamlit interface

Built for teams that need smart hiring without the cost of commercial AI.

---

## ❓ Problem Statement

Recruiters face repetitive tasks like:

* Reading dozens of resumes
* Matching them manually to job descriptions
* Following up with emails
* Scheduling interviews

This causes delays, inconsistent screening, and poor candidate experience — especially in small or mid-sized companies that can't afford full-fledged paid AI tools.

---

## 💡 Solution Summary

**HireMate** uses only free tools to:

* Automatically extract and summarize resume content
* Compare it to job descriptions via a rule-based engine
* Score and rank candidates using keyword matching
* Send a professional interview invitation (via dynamic template)

No OpenAI, GPT, or cloud AI needed.

---

## 🧱 System Architecture Diagram

```
                +--------------------+
                |   Resume (PDF)     |
                +--------------------+
                          |
                          ▼
         +-------------------------------+
         |   Resume Parser (PyMuPDF)     |
         +-------------------------------+
                          |
                          ▼
        +-----------------------------------+
        |  Rule-Based Matcher & Scorer     |
        |  - Keyword Match                 |
        |  - Experience Check (if any)     |
        +-----------------------------------+
                          |
           +-----------------------------+
           |  Streamlit Interface        |
           |  (View summary, match, etc) |
           +-----------------------------+
                          |
                          ▼
               +------------------------+
               | Email Generator (opt.) |
               +------------------------+
```

---

## 🧠 Models / Logic Used

### 1. Resume Parser (Model: PyMuPDF)

* Extracts clean text from uploaded `.pdf` resumes
* Strips whitespace, combines all pages

### 2. Job Matching Logic

* Compares extracted resume text to job description keywords
* Uses:

  * Keyword overlap (skill match)
  * Minimum experience years (if extractable)
  * Bonus keywords for ranking

### 3. Scoring System

* Score = Total matches × weight
* Bonus for strong matches like frameworks/tools
* Penalty if key skills missing

### 4. Email Generator

* Uses Python string templates with dynamic name/role

---

## ⚙️ Technologies Used

| Tool          | Purpose                        |
| ------------- | ------------------------------ |
| Python 3.x    | Core programming language      |
| Streamlit     | Web UI with no frontend coding |
| PyMuPDF       | PDF parsing                    |
| JSON          | Simple data storage            |
| smtplib (opt) | Email sending                  |
| VS Code       | Code editor                    |
| GitHub        | Code hosting                   |

---

## 💻 Installation Instructions

### 1. Install Python

* Download Python from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* Check “Add Python to PATH” during installation

### 2. Install Required Packages

```bash
pip install streamlit pymupdf
```

---

## ▶️ How to Use the App

1. Save your main file as `hiring_assistant.py`
2. Run it using:

```bash
streamlit run hiring_assistant.py
```

3. Upload a resume (PDF)
4. Choose a job title (preloaded or manual)
5. Get summary, match score, and email invite

---

## 🖼 Screenshots

(You can add these in your submission)
![Screenshot 2025-05-26 083229](https://github.com/user-attachments/assets/b369ac3c-d38b-4e20-a586-cc0d3b8b352e)
![Screenshot 2025-05-26 083319](https://github.com/user-attachments/assets/64e78371-d538-497e-b712-9c64088f57f7)


---

## 🔮 Future Improvements

* Support `.docx` resumes
* Add resume summary visualization (bar chart, keywords)
* Store candidate history in a database (SQLite)
* Add admin login to review applicants
* Schedule interviews via Google Calendar API (free)

---

## 👥 Contributors

* Kalpesh Gangani
* Prince Gambhava
* Vedant Changela
