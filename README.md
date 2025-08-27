# Speech-to-Speech-Multi-Launguage-System

A multilingual Speech-to-Speech AI Assistant that takes audio input in Hindi (or other supported languages), transcribes it using Whisper, classifies the query using IndicBERT, and responds back in audio using Indic Parler TTS.

This project demonstrates a multimodal pipeline integrating:
- 🎙️ Whisper (ASR - Speech to Text)
- 🧠 IndicBERT (Text classification)
- 🔊 Parler-TTS (Text to Speech) 

---

## 🚀 Features

- 🔄 End-to-end speech-to-speech communication
- 🎯 Accurate Hindi transcription using Whisper (extendable to multilingual)
- 💡 Smart classification using IndicBERT
- 🗨️ Natural voice response with Indic Parler TTS
- 🌐 Multilingual support setup ready for expansion
- 🧪 Simple interactive Gradio interface

---

## 🧾 Project Structure

```
speech-to-speech-multilanguage/
│
├── app/
│   ├── __init__.py
│   ├── stt.py                  # Whisper-based speech-to-text
│   ├── nlp.py                  # IndicBERT classification logic
│   ├── tts.py                  # Parler TTS text-to-speech conversion
│   └── pipeline.py             # Complete multimodal pipeline
│
├── interface/
│   └── gradio_ui.py            # Gradio interface definition
│
├── models/
│   └── (optional for downloaded models or cache)
│
├── .env                        # Device, sampling rate, and config vars
├── requirements.txt
├── main.py                     # Entry point for the app
└── README.md
```

---

## 📦 Installation

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/speech-to-speech-multilanguage.git
cd speech-to-speech-multilanguage
```

2. **Create virtual environment (optional)**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup `.env`**
Create a `.env` file in the root directory:
```env
DEVICE=cuda:0
SAMPLING_RATE=16000
WHISPER_MODEL=yash072/Whisper_Smal_FineTuned_Hindi
```

---

## 🌍 Multilingual Support

To switch or add support for other languages:

### Step 1: Choose correct Whisper model
Use multilingual fine-tuned models from HuggingFace, such as:
- `openai/whisper-small`
- `openai/whisper-medium`
- Or any fine-tuned model for your target language.

Update `.env`:
```env
WHISPER_MODEL=openai/whisper-small
```

### Step 2: Update `transcribe_speech()` in `stt.py`:
```python
output = pipe(
    filepath,
    max_new_tokens=256,
    generate_kwargs={"task": "transcribe", "language": "<target_language_code>"},
    chunk_length_s=30,
    batch_size=8,
)
```

| Language        | Code |
|-----------------|------|
| Hindi           | `hi` |
| Marathi         | `mr` |
| Tamil           | `ta` |
| Bengali         | `bn` |
| Gujarati        | `gu` |
| Kannada         | `kn` |

> For full language codes, check [Whisper documentation](https://github.com/openai/whisper#available-models-and-languages).

---

## ▶️ How to Run

```bash
python main.py
```

It will open a Gradio web interface in your browser where you can:
- Record or upload audio
- See the transcription
- View classified response
- Hear the generated speech output

---

## 🔮 Future Improvements

- 🌐 Add multilingual conversational support
- 🧠 Integrate an LLM for more detailed response generation
- 📱 Deploy as mobile app or web API

---

## 🤝 Credits

- [OpenAI Whisper](https://github.com/openai/whisper)
- [AI4Bharat](https://ai4bharat.org/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)

---

