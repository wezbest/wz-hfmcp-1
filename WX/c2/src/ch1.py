# //////////////////////////////////////////////////
# Testing of chatbot behavior in this
# //////////////////////////////////////////////////

import gradio as gr
import sambanova_gradio as sg

from .utz import header1


# --- Main Function caller ---
def ch1_mf():
    chatbot1_sambanova()


# -- Chatbt test 1

def chatbot1_sambanova():

    header1("Chatbot 1 - Llama-4-Maverick-17B-128E-Instruct")

    gr.load("Llama-4-Maverick-17B-128E-Instruct", src=sg.registry,
            accept_token=True, multi_model=True).launch()
