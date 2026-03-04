import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

import streamlit as st
from pypdf import PdfReader
from crew_setup import run_resume_agents

st.set_page_config(
    page_title="AI Resume Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Reviewer Agent")
st.markdown("Upload your resume and let **AI agents review it like a real recruiter team**.")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type="pdf"
)


def extract_text(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    return text


if uploaded_file:

    resume_text = extract_text(uploaded_file)

    st.success("Resume uploaded successfully ✅")

    if st.button("🚀 Run AI Resume Agents"):

        with st.spinner("AI agents analyzing your resume..."):

            result = run_resume_agents(resume_text)

        st.success("Analysis Complete 🎉")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("🔥 Recruiter Roast")
            st.write(result.tasks_output[0].raw)

        with col2:
            st.subheader("📊 ATS Analysis")
            st.write(result.tasks_output[1].raw)

        with col3:
            st.subheader("🧠 Career Coach Advice")
            st.write(result.tasks_output[2].raw)

        st.balloons()