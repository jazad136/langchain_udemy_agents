from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
#from langchain_openai import ChatOpenAI
from langchain_ibm import WatsonxLLM
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile

import os

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
    
    # information = """
    #     Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect, and former chairman of Tesla, Inc.; owner, executive chairman, and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is one of the wealthiest people in the world; as of April 2024, Forbes estimates his net worth to be $193 billion.[4]

    # A member of the wealthy South African Musk family, Musk was born in Pretoria and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University at Kingston in Canada. Musk later transferred to the University of Pennsylvania and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University, but dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999. That same year, Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal. In October 2002, eBay acquired PayPal for $1.5 billion. Using $100 million of the money he made from the sale of PayPal, Musk founded SpaceX, a spaceflight services company, in 2002.

    # """
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    # llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    
    parameters = {
    "decoding_method": "sample",
    "max_new_tokens": 100,
    "min_new_tokens": 1,
    "temperature": 0.5,
    "top_k": 50,
    "top_p": 1,
    }
    llm = WatsonxLLM(
        # temperature=0, model_name='gpt-3.5-turbo'
        model_id="ibm/granite-13b-instruct-v2",
        url="https://us-south.ml.cloud.ibm.com",
        project_id="6541694d69045f5c3af05498",
        params=parameters,
    )
    
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/jonathan-a-saddler")
    res = chain.invoke(input={"information": linkedin_data})
    
    print(res)