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
    # chatbot1_sambanova()
    chatbot2_sambanova()


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

# --- Chat Modal Test with tabs


def chatbot2_sambanova():
    header1("Chatbot 1 - Llama-4-Maverick-17B-128E-Instruct")

    def main_chat_fn():
        # Create description tab first
        with gr.Blocks() as desc_tab:
            gr.Markdown("### Model Documentation...")

        # Load the chat interface
        chat_interface = gr.load(
            "Llama-4-Maverick-17B-128E-Instruct",
            src=sg.registry,
            accept_token=True,
            multimodal=True,
            token=sn_token
        )

        # Combine them
        gr.TabbedInterface(
            [chat_interface, desc_tab],
            ["Chat", "Info"]
        ).launch()
