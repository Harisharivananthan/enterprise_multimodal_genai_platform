from vector_store.faiss_store import faiss_store
from app.core.embeddings import embed_texts

def retrieve_context(query: str, top_k: int = 4) -> str:
    query_vec = embed_texts([query])[0]
    docs = faiss_store.search(query_vec, top_k)
    return "\n".join(docs)