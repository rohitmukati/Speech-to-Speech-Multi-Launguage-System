import gradio as gr
from app.pipeline import multimodal_pipeline

iface = gr.Interface(
    fn=multimodal_pipeline,
    inputs=gr.Audio(type="filepath", label="Record or Upload Audio"),
    outputs=[
        gr.Textbox(label="Transcribed Text"),
        gr.Textbox(label="LLM Response"),
        gr.Audio(label="Generated Audio Response")
    ],
    title="E-commerce Query Solution",
    description="Upload or record an audio query in Hindi to get a spoken response."
)

if __name__ == "__main__":
    iface.launch()
