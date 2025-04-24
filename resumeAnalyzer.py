import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_text_from_pdf(uploaded_file):
    pdf = PdfReader(uploaded_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
    return text

def calculate_similarity(resume_text, job_desc_text):
    texts = [resume_text, job_desc_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    # Proper 2D slice-based similarity
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    return similarity_score[0][0]

st.set_page_config(page_title="Resume Analyzer", layout="centered")
st.title("📄 Resume Analyzer for Job Descriptions")
st.markdown("Upload your resume and a job description to get a matching score!")
url = "https://cdn.enhancv.com/images/1496/i/L19uZXh0L3N0YXRpYy9pbWFnZXMvcmVzdW1lLWNoZWNrZXItbW9iaWxlLTg5M2U1NDFiM2QzM2Y0NzEwZWNhZTRiMDliZTI3OGE3LndlYnA~.webp"
response = requests.get(url)
img = Image.open(BytesIO(response.content)).convert("RGB")
st.image(img, use_container_width=True)

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jobdesc_file = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])

if resume_file and jobdesc_file:
    with st.spinner("Processing files..."):
        resume_text = preprocess_text(extract_text_from_pdf(resume_file))
        jd_text = preprocess_text(extract_text_from_pdf(jobdesc_file))
        score = calculate_similarity(resume_text, jd_text)
    
    st.success("Analysis Complete!")
    st.metric(label="📊 Similarity Score", value=f"{score*100:.2f}%")

    if score > 0.75:
        st.info("✅ Great Match! Your resume aligns well with the job description.")
    elif score > 0.5:
        st.warning("🧐 Decent Match. Consider tailoring your resume to match more keywords.")
    else:
        st.error("❌ Low Match. Try customizing your resume to better align with the job.")