# Resume Job description Matching tool
AI-powered resume and job description matcher using Gemini API and Streamlit

# Resume ↔ Job Description Matcher

An AI-powered tool that compares a resume against a job description and returns a match score, matching/missing skills, and actionable suggestions to improve fit.

## What it does
- Takes a resume and a job description as input
- Uses Google's Gemini API to analyze alignment between the two
- Returns:
  - A match score (0-100)
  - Skills that match the job requirements
  - Skills missing from the resume
  - Specific suggestions to improve the resume for that role

## Tech Stack
- Python
- Streamlit (UI)
- Google Gemini API (LLM analysis)
- python-dotenv (environment variable management)

## How it works
The app sends the resume and job description to Gemini with a structured prompt instructing it to return analysis as JSON. The app then parses this JSON and displays it in a simple, readable interface.

## Running locally
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Gemini API key to a `.env` file:
  GEMINI_API_KEY= your_api_key
4. Run: `streamlit run app.py`

## Live demo
https://7bhhhvg9uwi8h6hnfd5cwb.streamlit.app

## Future improvements
- PDF resume upload support
- Support for comparing against multiple job descriptions at once
- Improved prompt tuning for more nuanced scoring
