from multimodal.multimodal_retriever import multimodal_retrieve

def retrieval_tool(query: str):
    return multimodal_retrieve(query)