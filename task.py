# Import Require Library
from crewai import Task
from tools import tool
from agents import market_reseacher,campaign_creator,digital_marketer_writer

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