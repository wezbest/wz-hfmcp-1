# ////////////////////////////////////////////////////////////////
# Testkng gradio video
# ////////////////////////////////////////////////////////////////
import gradio as gr


with gr.Blocks(theme=choose_theme) as demo:

    with gr.Tab("Intro"):
        intro_tab()

    with gr.Tab("Name Function"):
        name_func()


if __name__ == "__main__":
    demo.launch()


if __name__ == "__main__":
    main()
