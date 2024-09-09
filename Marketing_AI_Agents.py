# Import Require Library
import os
from crewai import Agent
import streamlit as st
# from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# load_dotenv()

# Creating LLM Variable
os.environ['GOOGLE_API_KEY']='AIzaSyD5ggkVEWVzFE3NaFa73a0MHuJPmkT3U8M'
LLM_Model=ChatGoogleGenerativeAI(model='gemini-1.5-flash',
                                 google_api_key=os.getenv('GOOGLE_API_KEY'))

# print(LLM_Model)
# Creating a market_reseacher Agent
market_reseacher = Agent(
    role='Senior Market Reseacher of {task_for_market_reseacher}',
    goal='Unccover ground breaking information in {task_for_market_reseacher}',
    backstory='''you are Senior Market Researcher with over a decade of experience, 
    adept at uncovering market insights that drive strategic decisions. Renowned for 
    leading cross-functional teams and delivering actionable data, they have a proven 
    track record of navigating complex markets, identifying trends, and transforming raw 
    data into impactful business strategies.''',
    llm=LLM_Model
)

# Creating a campaign_creator Agent
campaign_creator = Agent(
    role= 'Senior Marketing Campaign Creator of {task_for_campaign_creator}',
    goal='''come up with intersting marketing campaign idea in the {task_for_campaign_creator} 
    on the basis of market research insights''',
    backstory= '''you are Senior Marketing Campaign Creator with a flair for crafting compelling narratives 
    that captivate audiences and drive engagement. With over ten years of experience, they excel in designing 
    innovative, multi-channel campaigns that consistently exceed KPIs. Known for their strategic vision and creative 
    leadership, they transform ideas into powerful marketing success stories.''',
    llm=LLM_Model,
    allow_delegation=False
)

# Creating a digital_marketer_writer Agent
digital_marketer_writer = Agent(
    role='Digital Marketer content Creator of {task_for_digital_marketer}',
    goal='''come up with intersting advertisment ideas for 
    marketing on digital platform sach as youtube,instagram and facebook''',
    backstory='''Digital Marketer and Content Creator with a passion for storytelling 
    and a keen eye for trends. With a strong background in creating engaging content 
    across various digital platforms, they excel at driving brand visibility and audience growth. 
    Their data-driven strategies consistently deliver impactful results, turning concepts into 
    captivating campaigns.''',
    llm=LLM_Model,
    allow_delegation=False
)

import os
os.environ['SERPER_API_KEY']='5e91bacd42a33cdf4299197ce6d7e49aaca23310'
# os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')


from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()

# Import Require Library
from crewai import Task

# Creating Task for Agents
market_reseacher_task = Task(
    description='''Find and summarize the latest and most relevant big trend in {task_for_market_reseacher}, 
    focus on identifying pros and cons and the ovreall narrative. your final report should 
    clearly articulate the key points''',
    expected_output='come up with marketing trend comprehensive 3 paragraph report on the latest trend {task_for_market_reseacher}',
    agent=market_reseacher,
    tools=[tool]
)

campaign_creator_task = Task(
    description='''Create impactful marketing campaigns on {task_for_campaign_creator} effortlessly with our tool. Design, plan, 
    and execute strategies tailored to your audience. Boost engagement, track performance, and 
    achieve your marketing goals seamlessly.''',
    expected_output='Generate effective marketing campaigns on {task_for_campaign_creator} for each marketing research trends',
    agent=campaign_creator,
    tools=[tool]
)

digital_marketer_task = Task(
    description='''compose an insightful content on {task_for_digital_marketer} for each market champaign focus on latest trends and
    how it's impacting the industry. this content should be essy to understand, engaging and positive''',
    expected_output='''write the intersting advertisment content on {task_for_digital_marketer}
    for digital platform sach as youtube,instagram and facebook''',
    agent=digital_marketer_writer,
    tools=[tool]
)

# Import Require Library
from crewai import Crew,Process

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
