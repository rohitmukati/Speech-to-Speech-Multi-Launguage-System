from app.whisper_asr import transcribe_speech
from app.text_processor import process_query
from app.tts_generator import text_to_speech

def multimodal_pipeline(audio_input):
    text_query = transcribe_speech(audio_input)
    response_text = process_query(text_query)
    audio_response_path = text_to_speech(response_text)
    return text_query, response_text, audio_response_path
