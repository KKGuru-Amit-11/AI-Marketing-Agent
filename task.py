# Import Require Library
from crewai import Task
# from tools import tool
from agents import market_reseacher,campaign_creator

# Creating Task for Agents
market_reseacher_task = Task(
    description='''Find and summarize the latest and most relevant big trend in {input}, 
    focus on identifying pros and cons and the ovreall narrative. your final report should 
    clearly articulate the key points''',
    expected_output='come up with marketing trend comprehensive 3 paragraph report on the latest trend {input}',
    # tools=[tool],
    agent=market_reseacher
)

campaign_creator_task = Task(
    description='''Create impactful marketing campaigns on {input} effortlessly with our tool. Design, plan, 
    and execute strategies tailored to your audience. Boost engagement, track performance, and 
    achieve your marketing goals seamlessly.''',
    expected_output='Generate effective and intersting marketing campaigns on {input} for each marketing research trends',
    agent=campaign_creator,
    # tools=[tool],
    # output_file='marketing campaigns.txt'
)

# digital_marketer_task = Task(
#     description='''compose an insightful content on {input} for each market champaign focus on latest trends and
#     how it's impacting the industry. this content should be essy to understand, engaging and positive''',
#     expected_output='''write the intersting advertisment content on {input}
#     for digital platform sach as youtube,instagram and facebook''',
#     agent=digital_marketer_writer,
#     output_file='advertisment-content.txt'
# )
