# ///////////////////////////////////
# Testing Gradio chat interface with apis from their manual
# ///////////////////////////////////

# --- imports ---

import os

from dotenv import load_dotenv

from .utz import header1

# --- Getting th api keys ---
load_dotenv("./src/.env")
hf_token = os.getenv("HF")

# --- Main Entry Function


def gra2_main():
    header1("Testing HF Chat UI based on docs")

# //// Sun Functions /////


def gra2_chat1():
    header1("Testing HF API and Models")

    client = OpenAI(
        base_url="https://api.hyperbolic.xyz/v1/",
        api_key=api_key,
    )


def predict(message, history):
    history.append({"role": "user", "content": message})
    stream = client.chat.completions.create(
        messages=history, model="gpt-4o-mini", stream=True)
    chunks = []
    for chunk in stream:
        chunks.append(chunk.choices[0].delta.content or "")
        yield "".join(chunks)

    demo = gr.ChatInterface(predict, type="messages")

    demo.launch()
