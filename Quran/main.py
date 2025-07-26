from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel
from quran import get_relevant_ayah
from emotion import detect_emotion
from comfort import generate_comfort

app = FastAPI()

class JournalRequest(BaseModel):
    text: str
    emotion_before: str

@app.post("/journal")
def journal_entry(entry: JournalRequest):
    emotion_after = detect_emotion(entry.text)
    ayah = get_relevant_ayah(entry.text)
    comfort = generate_comfort(entry.text, emotion_after)

    return {
        "emotion_before": entry.emotion_before,
        "emotion_after": emotion_after,
        "ayah": ayah,
        "comfort": comfort
    }
