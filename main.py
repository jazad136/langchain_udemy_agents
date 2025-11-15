from dotenv import load_dotenv

load_dotenv()

# from langchain import hub
# from langchain.agents import AgentExecutor
# from langchain.agents.react.agent import create_react_agent
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

tools = TavilySearch()
# '''A search engine optimized for comprehensive, accurate, and 
# trusted results. Useful for when you need 
# to answer questions about current events. 
# It not only retrieves URLs and snippets, 
# but offers advanced search depths, domain management,
# time range filters, and image search, this tool 
# delivers real-time, accurate, and citation-backed 
# results.Input should be a search query.'''
def main():
    print("Hello from langchain-course!")
# tools.query
# '''
# {'description': 'Search query to look up', 
# 'title': 'Query', 
# 'type': 'string'}
# '''

if __name__ == "__main__":
    main()
