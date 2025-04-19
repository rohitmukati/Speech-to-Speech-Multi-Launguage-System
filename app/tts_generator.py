import torch
import soundfile as sf
from transformers import AutoTokenizer
from parler_tts import ParlerTTSForConditionalGeneration
from app.config import INDIC_PARLER_TTS_ID, DEVICE

tts_model = ParlerTTSForConditionalGeneration.from_pretrained(INDIC_PARLER_TTS_ID).to(DEVICE)
text_tokenizer = AutoTokenizer.from_pretrained(INDIC_PARLER_TTS_ID)
desc_tokenizer = AutoTokenizer.from_pretrained(tts_model.config.text_encoder._name_or_path)

def text_to_speech(response_text):
    prompt = response_text
    description = "A female speaker delivers a clear, natural tone in moderate speed and pitch."
    description_ids = desc_tokenizer(description, return_tensors="pt").to(DEVICE)
    prompt_ids = text_tokenizer(prompt, return_tensors="pt").to(DEVICE)

    generation = tts_model.generate(
        input_ids=description_ids.input_ids,
        attention_mask=description_ids.attention_mask,
        prompt_input_ids=prompt_ids.input_ids,
        prompt_attention_mask=prompt_ids.attention_mask
    )
    audio_arr = generation.cpu().numpy().squeeze()
    output_file = "tts_output.wav"
    sf.write(output_file, audio_arr, tts_model.config.sampling_rate)
    return output_file
