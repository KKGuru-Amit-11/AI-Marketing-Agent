# Import Require Library
import streamlit as st
from crewai import Crew,Process
from agents import market_reseacher,campaign_creator,LLM_Model
from task import market_reseacher_task,campaign_creator_task

# Creating Web Page header
st.title("Welcome to Analytx4T Lab")
st.subheader("Marketing Team with AI Agents")

# Getting Task From Web
task_for_campaign_creator = st.text_area("What Marketing Campaigns Would you Like me to come up with Today?")

# Creating Crew
crew = Crew(
    agents=[market_reseacher,campaign_creator],
    tasks=[market_reseacher_task,campaign_creator_task],
    manager_llm=LLM_Model,
    process=Process.sequential,
    verbose=True
)

# Creating a Dict Input Variable 
inputs={'input':task_for_campaign_creator}

# Query Answering
if st.button("Generate"):
    with st.spinner("Generate Response..."):
        crew.kickoff(inputs=inputs)
        st.subheader("Here is a Response Agent...")
        st.markdown(crew.kickoff(inputs=inputs))