# LangChain ReAct Search Agent 🚀

A powerful, autonomous AI agent built with Python and LangChain. This agent leverages large language models (LLMs) to understand complex queries, use external tools to search the internet for real-time information, and provide structured, actionable answers.

## Description

This project demonstrates the **ReAct (Reason + Act)** framework, where an LLM is used as a reasoning engine to delegate tasks to a set of tools. The agent is configured by default to run with local LLMs via **Ollama**, ensuring 100% privacy and no API costs, but it can be easily configured to use powerful cloud APIs like Google Vertex AI or OpenAI.

## How It Works

The agent operates on a loop until it can answer the user's question:

1.  **Thought**: The LLM first thinks about the user's query and decides on a plan.
2.  **Action**: It chooses a tool to execute (e.g., `tavily_search`) and determines the input for that tool.
3.  **Observation**: The agent receives the output from the tool (e.g., the search results).
4.  **Repeat**: The agent takes the new information from the observation and goes back to the "Thought" step. This loop continues until the agent believes it has enough information.
5.  **Final Answer**: The agent synthesizes all the information it has gathered and provides a final, comprehensive answer.

## Tech Stack

* **Python 3.10+**
* **LangChain**: The core framework for composing the agent.
* **Ollama**: For running local LLMs like Llama 3.1 and Gemma.
* **Tavily Search API**: For real-time, AI-optimized web search.
* **Google Vertex AI / OpenAI**: (Optional) For scalable, cloud-based LLMs.

---

## 🚀 Getting Started

Follow these steps to get the project running on your local machine.

#### 1. Clone the Repository

```bash
git clone [https://github.com/Divyanshu9382/langchain-search-agent.git](https://github.com/Divyanshu9382/langchain-search-agent.git)
cd langchain-search-agent
```
#### 2. Create and Activate a Virtual Environment



This project uses uv for fast environment and package management.

Bash

# Create the virtual environment
uv venv

# Activate the environment (for Windows PowerShell)
.venv\Scripts\activate

#### 3. Install Dependencies


Install all the necessary packages from the requirements.txt file.

Bash

uv pip install -r requirements.txt
(If you don't have a requirements.txt file, you can create one by running uv pip freeze > requirements.txt after installing the required packages.)

⚙️ Configuration
## 1. Local LLM Setup (Default)


This agent is configured to use a local LLM with Ollama.

Install Ollama from ollama.com.

Download a model for the agent to use:



ollama pull llama3.1:latest

Ensure the Ollama application is running in the background before starting the script.

## 2. API Keys


The agent's search tool requires an API key.

Create a file named .env in the root of the project folder.

Get a free API key from the Tavily AI website.

Add your key to the .env file:

TAVILY_API_KEY="tvly-YourTavilyApiKeyGoesHere"

## 3. Alternative Configuration (Cloud APIs)


You can easily switch to a cloud-based model by modifying main.py.

For Google Vertex AI: Install langchain-google-vertexai, uncomment the relevant code block in main.py, and ensure you have authenticated with gcloud.

For OpenAI: Install langchain-openai, uncomment an OpenAI code block in main.py, and add your OPENAI_API_KEY="sk-..." to the .env file.

 Usage
Make sure the Ollama application is running.

Activate your virtual environment: .venv\Scripts\activate.

Run the script:

Bash

python main.py
You can change the query inside the main.py file to ask the agent different questions.
