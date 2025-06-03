# ///////////////////////////////////
# Testing Gradio chat interface with apis from their manual
# ///////////////////////////////////

# --- imports ---

import os

from dotenv import load_dotenv

from .utz import header1

# --- Getting th api keys ---
load_dotenv("./src/.env")
hf_token = os.getenv("HF")

# --- Main Entry Function


def gra2_main():
    header1("Testing HF Chat UI based on docs")

# //// Sun Functions /////


def gra2_chat1():
    header1("Testing HF API and Models")
