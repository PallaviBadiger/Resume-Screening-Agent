import os
from groq import Groq
import pdfplumber
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text_from_pdf(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        text = f"Error reading PDF: {e}"
    return text


def evaluate_resume(jd_text, resume_text):
    try:
        prompt = f"""
You are an AI resume evaluator.

Compare the resume with the Job Description and return STRICT JSON only.

Required JSON Structure:
{{
  "score": number (0-100),
  "fit": "High" / "Medium" / "Low",
  "matching_skills": [],
  "missing_skills": [],
  "strengths": "",
  "weaknesses": ""
}}

Now evaluate:

Job Description:
{jd_text}

Resume:
{resume_text}
"""

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI Evaluation Error: {str(e)}"
