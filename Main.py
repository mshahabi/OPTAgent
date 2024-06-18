from langchain import hub
from langchain.agents import AgentExecutor
from langchain_experimental.tools import PythonREPLTool




from langchain.agents import create_openai_functions_agent
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv, find_dotenv
import os
from pathlib import Path

_ = load_dotenv(find_dotenv())
key = os.getenv("OPENAI_API_KEY")


# import python tools
tools = [PythonREPLTool()]

instructions = """use git clone https://github.com/Pyomo/pyomo, use cvxopt solver"""

base_prompt = hub.pull("langchain-ai/openai-functions-template")

prompt = base_prompt.partial(instructions=instructions)
print(prompt)
agent = create_openai_functions_agent(ChatOpenAI(temperature=0.5), tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke({"input": "Find the price to set per item and the number of items sold in order to maximize profit, and also determine the maximum profit you can get?"})

