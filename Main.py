from langchain import hub
from langchain.agents import AgentExecutor
from langchain_experimental.tools import PythonREPLTool


# import python tools
tools = [PythonREPLTool()]


from langchain.agents import create_openai_functions_agent
from langchain_openai import ChatOpenAI

instructions = """YYou want to sell a certain number  
  of items in order to maximize your profit. Market research tells you that if you set the price at $1.50, 
  you will be able to sell 5000 items, and for every 10 cents you lower the price below $1.50 you will be able to sell another 1000 items. 
  Suppose that your fixed costs ( “start-up costs” ) total $2000, and the per item cost of production ( “marginal cost” ) is $0.50.
"""
base_prompt = hub.pull("langchain-ai/openai-functions-template")
prompt = base_prompt.partial(instructions=instructions)