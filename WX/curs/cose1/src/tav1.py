# /////////////////////////////////////////
# Tavily testing here
# /////////////////////////////////////////

import os

from dotenv import load_dotenv
from tavily import TavilyClient

from .utz import header1

# Get the envs
load_dotenv()
T_V = os.getenv("TA")

# --- Main entry point of function ---


def main_tv():
    header1("Tavily Testing")
    print(T_V)


# -- Testing functions below ---

def tv_search_1():

    tavily_client = TavilyClient(api_key=TV)
    response = tavily_client.search("Who is Leo Messi?")

    print(response)
