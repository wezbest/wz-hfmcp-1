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
    # gra1_chat3()
    gra1_chat4()


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
def gra1_chat4():
    modelz = [
        "mistralai/Mistral-7B-Instruct-v0.3",
        "meta-llama/Llama-3.3-70B-Instruct"
    ]

    def apichat(message, history):
        # Build messages in OpenAI format
        messages = []
        for user, assistant in history:
            messages.append({"role": "user", "content": user})
            messages.append({"role": "assistant", "content": assistant})
        messages.append({"role": "user", "content": message})

        client = InferenceClient(
            provider="hf-inference",
            api_key=hf_token,
        )

        # Generate streamed response
        stream = client.chat.completions.create(
            model=modelz[0],
            messages=messages,
            stream=True
        )

        partial_message = ""
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                partial_message += token
                yield partial_message  # Yield accumulated message

    with gr.Blocks() as demo:
        gr.Markdown(f"# Chat Interface - {modelz[0]}")
        gr.ChatInterface(
            apichat,
            title=modelz[0],
            description=f"Chat with {modelz[0]}",
            examples=["Tell me a joke",
                      "How do I learn Python?",
                      "Explain gravity"],
            flagging_mode="manual",
            flagging_options=["Helpful", "Spam", "Inappropriate", "Other"]
        )

    demo.launch()
