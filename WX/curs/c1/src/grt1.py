# //////////////////////////////////////////////////////////
# GEneral Gradio tests in this section
# //////////////////////////////////////////////////////////

from src.utz import header1
import gradio as gr
import os
from dotenv import load_dotenv

# --- Getting the ENV Variables ---

load_dotenv("./src/.env")
hf_token = os.getenv("HF")

# --- Main Function ---


def grt1_main():
    header1("Gradio General Tests ")

# --- Sub functions ----


def grt1_f1():
