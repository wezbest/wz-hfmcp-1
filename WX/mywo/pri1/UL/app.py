# ///////////////////////////
# Testing gradio private spaces and functions
# ///////////////////////////

import gradio as gr

from funcz import intro_tab, name_func

# Theming variables

themes = [
    gr.themes.Ocean(),
    gr.themes.Monochrome(),
    gr.themes.Citrus(),
    gr.themes.Glass(),
    gr.themes.Default(),
    gr.themes.Soft()
]
choose_theme = themes[5]

# This is the actual name function


with gr.Blocks(theme=choose_theme) as demo:

    with gr.Tab("Intro"):
        intro_tab()

    with gr.Tab("Name Function"):
        name_func()


if __name__ == "__main__":
    demo.launch()
