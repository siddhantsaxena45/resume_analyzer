import os
from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

resume_reviewer = Agent(
    role="Senior Tech Recruiter",
    goal="Give brutally honest resume feedback",
    backstory="You are a FAANG recruiter reviewing resumes.",
    llm=llm,
    verbose=True
)

ats_checker = Agent(
    role="ATS Expert",
    goal="Analyze ATS compatibility",
    backstory="You understand how ATS systems filter resumes.",
    llm=llm,
    verbose=True
)

career_coach = Agent(
    role="Career Coach",
    goal="Suggest improvements and missing skills",
    backstory="You help engineers improve resumes.",
    llm=llm,
    verbose=True
)