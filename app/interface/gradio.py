import gradio as gr
from app.core.pipeline import multimodal_pipeline

def launch_gradio():
    iface = gr.Interface(
        fn=multimodal_pipeline,
        inputs=gr.Audio(type="filepath", label="🎤 Record or Upload Audio"),
        outputs=[
            gr.Textbox(label="📝 Transcribed Text"),
            gr.Textbox(label="🤖 LLM Response"),
            gr.Audio(label="🔊 Generated Audio Response")
        ],
        title="🗣️ Speech to Speech Multilanguage System",
        description=(
            "Upload or record an audio query in Hindi (or other supported languages). "
            "The system will transcribe the speech, understand the query using IndicBERT, "
            "and generate a spoken response using Parler TTS."
        ),
        allow_flagging="never",
    )
    iface.launch()

if __name__ == "__main__":
    launch_gradio()
