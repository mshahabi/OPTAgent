from langchain import hub
from langchain.agents import AgentExecutor
from langchain_experimental.tools import PythonREPLTool




from langchain.agents import create_openai_functions_agent
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv, find_dotenv
import os
from pathlib import Path

_ = load_dotenv(find_dotenv())
Key = os.getenv("OPENAI_API_KEY")


# import python tools
tools = [PythonREPLTool()]
instructions = """YYou want to sell a certain number  
  of items in order to maximize your profit. Market research tells you that if you set the price at $1.50, 
  you will be able to sell 5000 items, and for every 10 cents you lower the price below $1.50 you will be able to sell another 1000 items. 
  Suppose that your fixed costs ( “start-up costs” ) total $2000, and the per item cost of production ( “marginal cost” ) is $0.50.
"""
base_prompt = hub.pull("langchain-ai/openai-functions-template")
prompt = base_prompt.partial(instructions=instructions)

agent = create_openai_functions_agent(ChatOpenAI(temperature=0), tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke({"input": "What is the 10th fibonacci number?"})

