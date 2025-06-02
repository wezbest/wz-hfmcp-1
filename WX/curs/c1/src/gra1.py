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


# --- Getting the HF Api responses in gradio chat interface This method works ---

def gra1_chat3():
    header1("Chat Interface Two - Streaming Chatbot interface")

    # Main Function in the chat interface

    modelz = [
        "mistralai/Mistral-7B-Instruct-v0.3",
        "meta-llama/Llama-3.3-70B-Instruct"
    ]

    def apichat(message, history):
        client = InferenceClient(
            provider="hf-inference",
            api_key=hf_token,
        )

        completion = client.chat.completions.create(
            model=modelz[0],
            messages=[
                {"role": "user", "content": message}
            ],
        )

        return completion.choices[0].message["content"]

    demo = gr.ChatInterface(
        apichat,
        title=modelz[0],
        description="Chat with " + modelz[0],
        flagging_mode="manual",
        examples=["Smell Pussy", "Lick Ass", "Smell Fart"],
        flagging_options=["Like", "Spam", "Inappropriate", "Other"],
        save_history=True,
    )

    demo.launch()


# --- hf Chat with streaming and best practices
def gra1_chat3():
    modelz = [
        "mistralai/Mistral-7B-Instruct-v0.3",
        "meta-llama/Llama-3.3-70B-Instruct"
    ]

    def apichat(message, history):
        messages = []
        for user_msg, bot_reply in history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": bot_reply})

        messages.append({"role": "user", "content": message})

        client = InferenceClient(
            provider="hf-inference",
            api_key=hf_token,
        )

        # Enable streaming
        response_stream = client.chat.completions.create(
            model=modelz[0],
            messages=messages,
            stream=True
        )

        reply = ""
        for chunk in response_stream:
            delta = chunk.choices[0].delta.get("content", "")
            reply += delta
            yield reply  # This enables token streaming in ChatInterface

    with gr.Blocks() as demo:
        gr.Markdown(f"# Chat Interface - {modelz[0]}")
        gr.ChatInterface(
            fn=apichat,
            title=f"{modelz[0]}",
            description=f"Chat with the {modelz[0]} model",
            examples=["Tell me a joke",
                      "How do I learn Python?", "Explain gravity"],
            flagging_mode="manual",
            flagging_options=["Helpful", "Spam", "Inappropriate", "Other"],
            save_history=True,
            streaming=True  # Enable streaming in the UI
        )

    demo.launch()
