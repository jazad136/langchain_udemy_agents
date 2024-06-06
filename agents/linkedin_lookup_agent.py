import os
from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool

from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub

def lookup(name: str) -> str: 
    # return "https://www.linkedin.com/in/eden-marco"
    llm = ChatOpenAI(
        temperature = 0,
        model_name="gpt-3.5-turbo",
    )
    template = """given the full name {name_of_person} I want you to get me a link to their Linkedin profile page.
    Your answer should contain only a URL"""
    
    prompt_template = PromptTemplate(
        template = template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func="?",
            description="useful for when you need get the Linkedin Page URL",
        )
    ]
    
    react_prompt = hub.pull('hwchase17/react')
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    # agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, 
                                   verbose=True, return_intermediate_steps = True,
                                   handle_parsing_errors=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    # return result
    linkedin_profile_url = result["output"]
    return linkedin_profile_url
if __name__ == '__main__':
    linkedin_url = lookup(name="Eden Marco")
    print(linkedin_url)