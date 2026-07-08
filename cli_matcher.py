import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash")

resume_text=input("Please enter the Resume contents:")
jobdesc_text=input("please enter job description:")

def match_analyzer(resume=resume_text, jobdesc=jobdesc_text):
    prompt= f""" You are an ATS resume screening assistant. Compare the following resume with the job description.
    Resume: {resume}
    Job description: {jobdesc}

    Return ONLY valid JSON, no other text, with these exact keys: 
    match_score (integer 0-100), matching_skills (list of strings), 
    missing_skills (list of strings), suggestions (list of strings, 2-3 actionable suggestions)."""

    response=model.generate_content(prompt)
    # it's still in markdown formatting which we need to remove
    raw_text=response.text.strip()

    # remvoving markdown code fence "  ````  "
    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1]  # grab content between fences
        raw_text = raw_text.replace("json", "", 1).strip()  # remove leading "json" label if present

    result = json.loads(raw_text)
    return result

    # to check if the response is in json
    #  print("Raw response:" , response.text)

    result=json.loads(response.text)
    return result

output = match_analyzer()
print(output)
