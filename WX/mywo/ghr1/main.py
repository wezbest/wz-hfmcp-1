import gradio as gr

with gr.Blocks() as demo:

    with gr.Tab("Intro"):
        gr.Markdown("# Booty Dance")

    with gr.Tab("Tab 1"):
        gr.Markdown("# Greetings from Gradio!")
        inp = gr.Textbox(placeholder="What is your name Bastard Raper?")
        out = gr.Textbox()

        inp.change(fn=lambda x: f"Welcome, {x}!",
                   inputs=inp,
                   outputs=out)

if __name__ == "__main__":
    demo.launch()
