import os
from dotenv import load_dotenv

load_dotenv()

WHISPER_MODEL_ID = os.getenv("WHISPER_MODEL_ID")
INDIC_BERT_MODEL_ID = os.getenv("INDIC_BERT_MODEL_ID")
INDIC_PARLER_TTS_ID = os.getenv("INDIC_PARLER_TTS_ID")
DEVICE = os.getenv("DEVICE", "cpu")
