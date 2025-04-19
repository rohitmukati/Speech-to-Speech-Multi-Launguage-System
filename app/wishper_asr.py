from transformers import pipeline
from app.config import WHISPER_MODEL_ID

pipe = pipeline("automatic-speech-recognition", model=WHISPER_MODEL_ID)

def transcribe_speech(filepath):
    output = pipe(filepath, max_new_tokens=256, generate_kwargs={"task": "transcribe", "language": "hi"}, chunk_length_s=30, batch_size=8)
    return output["text"]
