import streamlit as st
from matcher import match_analyzer

st.title('Job Resume Matcher')

resume_input = st.text_area("Enter the resume content here:")
jobdesc_input = st.text_area("Enter job description here:")

# rewriting this part to tackle error handling
# if st.button("Analyze"):
#     result = match_analyzer(resume_input, jobdesc_input)
    
#     st.metric("Match Score", f"{result['match_score']}/100")
    
#     st.subheader("Matching Skills")
#     for skill in result['matching_skills']:
#         st.write(f"- {skill}")
    
#     st.subheader("Missing Skills")
#     for skill in result['missing_skills']:
#         st.write(f"- {skill}")
    
#     st.subheader("Suggestions")
#     for suggestion in result['suggestions']:
#         st.write(f"- {suggestion}")
if st.button("Analyze"):
    result = match_analyzer(resume_input, jobdesc_input)
    
    st.metric("Match Score", f"{result['match_score']}/100")
    
    st.subheader("Matching Skills")
    for skill in result['matching_skills']:
        st.write(f"- {skill}")
    
    st.subheader("Missing Skills")
    for skill in result['missing_skills']:
        st.write(f"- {skill}")
    
    st.subheader("Suggestions")
    for suggestion in result['suggestions']:
        st.write(f"- {suggestion}")