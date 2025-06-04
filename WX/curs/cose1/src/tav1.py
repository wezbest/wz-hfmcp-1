# /////////////////////////////////////////
# Tavily testing here
# /////////////////////////////////////////

import os

from dotenv import load_dotenv
from rich import print as rprint
from tavily import TavilyClient

from .utz import header1

# Get the envs
load_dotenv()
T_V = os.getenv("TA")

# --- Main entry point of function ---


def main_tv():
    header1("Tavily Testing")
    tv_search_1()


# -- Testing functions below ---

def tv_search_1():

    header1("Tavily Testing 1 ")

    search_query = "What is cosmology"

    try:
        tavily_client = TavilyClient(api_key=T_V)
        response = tavily_client.search(search_query)
        rprint(response)
    except Exception as e:
        rprint(f"[bold red]Error:[/bold red] {e}")
