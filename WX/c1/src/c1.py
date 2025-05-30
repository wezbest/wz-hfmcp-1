# Chat 1 - Following the Gradio official manual

import gradio as gr


def ch1_alt(message, history):
    if len([h for h in history if h['role'] == "assistant"]) % 2 == 0":
        return 
    

def chat_1():
    gr.ChatInterface(