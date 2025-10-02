from dotenv import load_dotenv
load_dotenv()
from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent

from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
import os

tools = [TavilySearch()]

# 2. Set the LLM to your local Ollama model
llm = ChatOllama(model="gemma:2b")

react_promt = hub.pull("hwchase17/react")
agent = create_react_agent(
    llm = llm,
    tools = tools,
    prompt = react_promt,
)
agent_executer = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)
chain = agent_executer

def main():
    result = chain.invoke(
        input={
            "input": "what are the latest job postings on linkedin for an ai engineer in the bay area?",
        }
    )
    print(result)

if __name__ == "__main__":
    main()