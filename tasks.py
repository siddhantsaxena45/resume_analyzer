from crewai import Task
from agents import resume_reviewer, ats_checker, career_coach


def create_tasks(resume_text):

    roast_task = Task(
        description=f"""
Review this resume and roast it honestly.
Highlight weak bullet points and formatting problems.

Resume:
{resume_text}
""",
        expected_output="A brutally honest review of the resume highlighting weak areas and suggestions.",
        agent=resume_reviewer
    )

    ats_task = Task(
        description=f"""
Analyze this resume for ATS compatibility.

Provide:
- ATS score out of 100
- missing keywords
- improvements

Resume:
{resume_text}
""",
        expected_output="ATS score with explanation, missing keywords and optimization suggestions.",
        agent=ats_checker
    )

    skills_task = Task(
        description=f"""
Identify missing technical skills in this resume.

Suggest improvements for software engineering roles.

Resume:
{resume_text}
""",
        expected_output="List of missing skills and recommendations to improve the resume.",
        agent=career_coach
    )

    return roast_task, ats_task, skills_task