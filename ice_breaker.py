import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile




if __name__ == '__main__':
    load_dotenv()
    
    print('Hello Langchain')
    # print(os.environ['OPENAI_API_KEY'])
    print(f'Cool API Key {os.environ["COOL_API_KEY"]}')
    
    summary_template = """
    given the information {information} about a person I want you to create: 
    1. A short summary 
    2. two interesting facts about them
    """
    
   
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/jonathan-a-saddler")
    
    res = chain.invoke(input={"information": linkedin_data})
    
    print(res)