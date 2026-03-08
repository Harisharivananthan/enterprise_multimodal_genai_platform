from ingestion.loader import load_document
from ingestion.cleaner import clean_text
from ingestion.chunker import chunk_text
from app.core.embeddings import embed_texts
from vector_store.faiss_store import faiss_store

def ingest_document(path: str):
    raw_text = load_document(path)
    clean = clean_text(raw_text)
    chunks = chunk_text(clean)
    vectors = embed_texts(chunks)
    faiss_store.add(chunks, vectors)