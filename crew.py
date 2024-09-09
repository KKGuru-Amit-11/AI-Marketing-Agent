# Import Require Library
import streamlit as st
from crewai import Crew,Process
from agents import market_reseacher,campaign_creator,digital_marketer_writer,LLM_Model
from task import market_reseacher_task,campaign_creator_task,digital_marketer_task

# Creating Web Page header
st.title("Welcome to Analytx4T Lab")
st.subheader("Marketing Team with AI Agents")

# Getting Task From Web
task_for_market_reseacher = st.text_area("What Market Researcher Task Would You Like me to do Today?")
task_for_campaign_creator = st.text_area("What Marketing Campaigns Would you Like me to come up with Today?")
task_for_digital_marketer = st.text_area("What Digital Marketing Content Would You Like me to Generate Today?")


# Creating Crew
crew = Crew(
    agents=[market_reseacher,campaign_creator,digital_marketer_writer],
    tasks=[market_reseacher_task,campaign_creator_task,digital_marketer_task],
    manager_llm=LLM_Model,
    process=Process.sequential,
    verbose=True
)

# Creating a Dict Input Variable 
inputs={
    "task_for_market_reseacher":task_for_market_reseacher,
    "task_for_campaign_creator":task_for_campaign_creator,
    "task_for_digital_marketer":task_for_digital_marketer
}

# Query Answering
if st.button("Generate"):
    with st.spinner("Generate Response..."):
        crew.kickoff(inputs=inputs)
        st.subheader("Here is a Response of Market Rreseacher...")
        st.markdown(market_reseacher_task.output)
        st.subheader("Here is a Response of Campaign Creator...")
        st.markdown(campaign_creator_task.output)
        st.subheader("Here is a Response of Digital Marketer...")
        st.markdown(digital_marketer_task.output)