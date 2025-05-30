import gradio as gr


# Main greeter function
def greet(name, intensity):
    return "Fuckoff " + name + "! Intensity: " + str(intensity)


# Setting up the Gradio interface with blocks and tabs
with gr.Blocks(title="Greeting App") as demo:
    with gr.Tabs():

        # Intro tab with a welcome message
        with gr.Tab("Intro"):
            gr.Markdown("# 👋 Welcome to the Greeting App!")
            gr.Markdown("""
            This app generates a humorous greeting with your name and a chosen intensity.

            - Use the **Greeting** tab to input your name.
            - Slide the intensity meter to dial up or down the 'energy'.
            - It's all in good fun — enjoy!
            """)

        # Greeting tab with input fields and a button


if __name__ == "__main__":
    demo.launch()
