# /////////////////////////////////////
# Gradio Interface tests
# /////////////////////////////////////

# --- Imports ---

import time

import gradio as gr

from src.utz import header1

# --- Main chat function ---


def gra1_main():
    # gra1_chat1()
    gra1_chat2()


# -- Sub functions call ---

# Examples from the official documentation
def gra1_chat1():
    header1("Chat Interface One")

    def echo(message, history):
        return message

    demo = gr.ChatInterface(fn=echo, type="messages", examples=[
                            "hello", "hola", "merhaba"], title="SellPanty")
    demo.launch()

# Streaming echo chat test


def gra1_chat2():
    header1("Chat Interface Two - Streaming Chatbot interface")

    # Main Function in the chat interface
    def slow_echo(message, history):
        for i in range(len(message)):
            time.sleep(0.05)
            yield "You Fucked " + message[: i + 1]

    demo = gr.ChatInterface(
        slow_echo,
        title="BootySmell",
        type="messages",
        flagging_mode="manual",
        examples=["Smell Pussy", "Lick Ass", "Smell Fart"],
        flagging_options=["Like", "Spam", "Inappropriate", "Other"],
        save_history=True,
    )

    demo.launch()
