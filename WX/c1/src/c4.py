# ///////////////////////////////////////////////////////////////
# c4.py - Truying to write a streaming chatbot from scratch with Hugging Face API
#
# ////////////////////////////////////////////////////////////////

import time

import gradio as gr

from .utz import header1  # Assuming this exists and prints a heading


def chat_c4():
    header1("Streaming Chatbot Tests")

    intro_message = """
# 🤖 Streaming Chatbot Example
This is a simple test using streaming responses inside a tabbed interface.
"""

    # Define chatbot function
    def slow_echo(message, history):
        for i in range(len(message)):
            time.sleep(0.05)
            yield "You typed: " + message[: i + 1]

    with gr.Blocks() as demo:
        with gr.Tabs():
            with gr.Tab("Intro"):
                gr.Markdown(intro_message)

            with gr.Tab("Chat"):
                gr.ChatInterface(
                    fn=slow_echo,
                    chatbot=gr.Chatbot(type="messages"),
                    textbox=gr.Textbox(placeholder="Type something..."),
                    type="generator",
                    retry_btn=None,
                    undo_btn=None,
                    clear_btn="Clear",
                    submit_btn="Send",
                )

    demo.launch()
