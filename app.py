import os
import json
import streamlit as st
from dotenv import load_dotenv
from utils import extract_text_from_pdf, evaluate_resume

# Load environment variables
load_dotenv()

st.title("🧠 AI Resume Screening Agent (GROQ Version)")

# Upload Job Description PDF
jd_file = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])

# Upload multiple resumes
resume_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

if st.button("Analyze Resumes"):
    # Check API Key
    if not os.getenv("GROQ_API_KEY"):
        st.error("❌ GROQ_API_KEY not found. Add it inside a .env file.")
        st.stop()

    if jd_file and resume_files:
        jd_text = extract_text_from_pdf(jd_file)
        results = []

        for file in resume_files:
            resume_text = extract_text_from_pdf(file)
            raw_output = evaluate_resume(jd_text, resume_text)

            # Try to parse JSON
            try:
                ai_output = json.loads(raw_output)
            except:
                ai_output = {
                    "score": 0,
                    "fit": "Unknown",
                    "matching_skills": [],
                    "missing_skills": [],
                    "strengths": "",
                    "weaknesses": "",
                    "raw_output": raw_output,
                }

            ai_output["resume_name"] = file.name
            results.append(ai_output)

        # Sort by score
        results = sorted(results, key=lambda x: float(x.get("score", 0)), reverse=True)

        st.subheader("📊 Resume Ranking")
        for r in results:
            st.write(f"### {r['resume_name']}")
            st.write(f"Score: **{r['score']}**")
            st.write(f"Fit: **{r['fit']}**")
            st.write(f"**Matching Skills:** {r['matching_skills']}")
            st.write(f"**Missing Skills:** {r['missing_skills']}")
            st.write(f"**Strengths:** {r['strengths']}")
            st.write(f"**Weaknesses:** {r['weaknesses']}")

            if "raw_output" in r:
                with st.expander("Raw AI Output (debugging)"):
                    st.code(r["raw_output"], language="json")

            st.write("---")
