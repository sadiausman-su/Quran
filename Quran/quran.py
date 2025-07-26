from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("quran_ayahs.json", encoding="utf-8") as f:
    ayahs = json.load(f)

texts = [a["text"] for a in ayahs]
embeddings = model.encode(texts, convert_to_tensor=True)

def get_relevant_ayah(query):
    query_vec = model.encode(query, convert_to_tensor=True)
    scores = util.cos_sim(query_vec, embeddings)
    best_idx = scores.argmax().item()
    return ayahs[best_idx]
