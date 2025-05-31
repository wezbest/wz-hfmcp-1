# //////////////////////////////////////////////////
# Testing of chatbot behavior in this
# //////////////////////////////////////////////////

import os

import gradio as gr
import sambanova_gradio as sg
from dotenv import load_dotenv

from .utz import header1

# -- Get tokens ---
load_dotenv("./src/.env")
hf_token = os.getenv("HF")
sn_token = os.getenv("SN")

# --- Main Function caller ---


def ch1_mf():
    chatbot1_sambanova()


# -- Chatbt test 1

def chatbot1_sambanova():

    header1("Chatbot 1 - Llama-4-Maverick-17B-128E-Instruct")

    def main_chat_fn():
        gr.load("Llama-4-Maverick-17B-128E-Instruct",
                src=sg.registry,
                accept_token=True,
                multimodal=True,
                token=sn_token,
                ).launch()
