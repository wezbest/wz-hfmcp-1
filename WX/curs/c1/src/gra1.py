# /////////////////////////////////////
# Gradio Interface tests
# /////////////////////////////////////

# --- Imports ---

import os
import time

import gradio as gr
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from src.utz import header1

# -- Get the HF Token ---

load_dotenv("./src/.env")
hf_token = os.getenv("HF")

# --- Main chat function ---


def gra1_main():
    # gra1_chat1()
    # gra1_chat2()
    gra1_chat3()


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


# --- Getting the HF Api responses in gradio chat interface

def gra1_chat3():
    header1("Chat Interface Two - Streaming Chatbot interface")

    # Main Function in the chat interface

    def apichat(message, history):
        client = InferenceClient(
            provider="hf-inference",
            api_key=hf_token,
        )

        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[
                {"role": "user", "content": "Sing and dance for me "}
            ],
        )

        return completion.choices[0].message["content"]

    demo = gr.ChatInterface(
        apichat,
        title="BootySmell",
        type="messages",
        flagging_mode="manual",
        examples=["Smell Pussy", "Lick Ass", "Smell Fart"],
        flagging_options=["Like", "Spam", "Inappropriate", "Other"],
        save_history=True,
    )

    demo.launch()
