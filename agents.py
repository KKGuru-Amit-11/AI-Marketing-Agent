# Import Require Library
import os
from crewai import Agent
import streamlit as st
# from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

# Creating LLM Variable
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
