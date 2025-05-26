import streamlit as st
import fitz  # PyMuPDF
import requests

# ✅ Your Gemini API key from Google AI Studio (Makersuite)
GEMINI_API_KEY = "AIzaSyBk1kawlnU7fR7Fj_2JEov-EYkFH9HzYAA" # Replace with your actual key

# ✅ Corrected Endpoint for Gemini Pro
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def summarize_resume(resume_text):
    prompt = f"Summarize this resume in simple terms:\n\n{resume_text}"
    
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(GEMINI_ENDPOINT, headers=headers, json=data)

    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "⚠️ Gemini responded, but content couldn't be extracted."
    else:
        return f"⚠️ API Error: {response.status_code} - {response.text}"

# Streamlit UI
st.title("🧠 AI Hiring Assistant (Gemini API v1beta)")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.subheader("📄 Extracted Resume Text")
    st.text_area("Resume Text", resume_text, height=300)

    if st.button("Summarize Resume"):
        with st.spinner("Summarizing with Gemini..."):
            summary = summarize_resume(resume_text)
            st.success("✅ AI Summary")
            st.write(summary)