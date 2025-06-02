# /////////////////////////////////////
# Gradio Interface tests
# /////////////////////////////////////

# --- Imports ---

import gradio as gr

from src.utz import header1

# --- Main chat function ---


def gra1_main():
    gra1_chat1()


# -- Sub functions call ---

# Examples from the official documentation
def gra1_chat1():
    header1("Chat Interface One")

    def echo(message, history):
        return message

    demo = gr.ChatInterface(fn=echo, type="messages", examples=[
                            "hello", "hola", "merhaba"], title="Echo Bot")
    demo.launch()
