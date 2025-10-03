from dotenv import load_dotenv

load_dotenv()
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_google_vertexai import ChatVertexAI
from langchain_tavily import TavilySearch
import os
import json  # <-- Add this new import


tools = [TavilySearch()]

llm = ChatVertexAI(
    model="gemini-2.5-flash",
    location="us-central1"
)

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)


def main():
    print("Agent is ready! Invoking...")
    query = """
    Search for three distinct AI Engineer job postings in the Bay Area on LinkedIn.
    For each of the three jobs, extract the following details:
    - Job Title
    - Company Name
    - A direct URL to the job posting
    List them clearly.
    """
    result = agent_executor.invoke(
        input={"input": query}
    )

    print("--- FINAL RESULT ---")

    # The agent's output is a string that contains a JSON code block
    output_string = result['output']

    # Clean up the string to get pure JSON
    # It removes the markdown ```json ... ``` wrapper
    try:
        json_part = output_string.split("```json")[1].split("```")[0]
        data = json.loads(json_part)
        # Print just the 'answer' field, which has the newlines
        print(data['answer'])
    except (IndexError, json.JSONDecodeError):
        # If parsing fails, just print the raw output
        print(output_string)


if __name__ == "__main__":
    main()