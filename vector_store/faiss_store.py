import faiss
import numpy as np


class FAISSStore:
    def __init__(self, dim=384):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, texts, vectors):
        vectors = np.array(vectors, dtype="float32")
        self.index.add(vectors)
        self.texts.extend(texts)

    def search(self, query_vector, top_k=5):
        query = np.array([query_vector], dtype="float32")
        _, ids = self.index.search(query, top_k)
        return [self.texts[i] for i in ids[0]]


faiss_store = FAISSStore()