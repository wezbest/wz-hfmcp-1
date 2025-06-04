# /////////////////////////////////////////
# Tavily testing here
# /////////////////////////////////////////

import os

from dotenv import load_dotenv

from .utz import header1

# Get the envs
load_dotenv()
T_V = os.getenv("TA")

# --- Main entry point of function ---


def main_tv():
    header1("Tavily Testing")
    print(T_V)
