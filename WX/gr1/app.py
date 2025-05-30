import gradio as gr


def greet(name, intensity):
    return "Fuckoff " + name + "! Intensity: " + str(intensity)


with gr.Blocks(title="Greeting App") as demo:
    with gr.Tabs():
        with gr.Tab("Intro"):
            gr.Markdown("# 👋 Welcome to the Greeting App!")
            gr.Markdown("""
            This app generates a humorous greeting with your name and a chosen intensity.

            - Use the **Greeting** tab to input your name.
            - Slide the intensity meter to dial up or down the 'energy'.
            - It's all in good fun — enjoy!
            """)

        with gr.Tab("Greeting"):
            gr.Markdown("## Customize Your Greeting")
            name = gr.Textbox(label="Name", placeholder="Enter your name")
            intensity = gr.Slider(value=2, minimum=0,
                                  maximum=100, label="Intensity", step=1)
            output = gr.Textbox(label="Greeting", lines=3)
            greet_btn = gr.Button("Greet")
            greet_btn.click(fn=greet, inputs=[name, intensity], outputs=output)

            gr.Examples(
                examples=[["Alice", 10], ["Bob", 20], ["Charlie", 30]],
                inputs=[name, intensity],
            )

if __name__ == "__main__":
    demo.launch()
