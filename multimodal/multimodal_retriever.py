from app.core.retriever import retrieve_context


def multimodal_retrieve(query):
    text_context = retrieve_context(query)

    multimodal_context = ""

    context = f"""
TEXT CONTEXT:
{text_context}

MULTIMODAL CONTEXT:
{multimodal_context}
"""

    return context