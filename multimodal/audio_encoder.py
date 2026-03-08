import whisper
from app.core.embeddings import embed_texts

model = whisper.load_model("base")

def encode_audio(audio_path):
    result = model.transcribe(audio_path)

    text = result["text"]
    vector = embed_texts([text])[0]

    return text, vector