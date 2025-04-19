import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from app.config import INDIC_BERT_MODEL_ID

model = AutoModelForSequenceClassification.from_pretrained(INDIC_BERT_MODEL_ID)
tokenizer = AutoTokenizer.from_pretrained(INDIC_BERT_MODEL_ID)

def process_query(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    outputs = model(**inputs)
    response = torch.argmax(outputs.logits, dim=1).item()
    return f"Predicted class: {response}"
