import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash")
def match_analyzer(resume, jobdesc):
    prompt= f""" You are an ATS resume screening assistant. Compare the following resume with the job description.
    Resume: {resume}
    Job description: {jobdesc}

    Return ONLY valid JSON, no other text, with these exact keys: 
    match_score (integer 0-100), matching_skills (list of strings), 
    missing_skills (list of strings), suggestions (list of strings, 2-3 actionable suggestions)."""
    
    response = model.generate_content(prompt)
    raw_text = response.text.strip()

    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1]
        raw_text = raw_text.replace("json", "", 1).strip()

    result = json.loads(raw_text)
    return result