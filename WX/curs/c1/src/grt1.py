# //////////////////////////////////////////////////////////
# GEneral Gradio tests in this section
# //////////////////////////////////////////////////////////

import os

import gradio as gr
from dotenv import load_dotenv

from src.utz import header1

# --- Getting the ENV Variables ---

load_dotenv("./src/.env")
hf_token = os.getenv("HF")

# --- Main Function ---


def grt1_main():
    grt1_f1()

# --- Sub functions ----

# Trying to understand basic input and ouput here


def grt1_f1():
    header1("Gradio General Tests ")

    def greet(name):
        return name + "SmellFarts"

    def tab1():
        with gr.Tab("Smell Panty"):
            gr.Image("../../../wo/085.jpg")
            gr.Markdown("# Woman Si ltink Sniff")

    with gr.Blocks() as demo:
        tab1()
        tab1()
        tab1()

    demo.launch()
