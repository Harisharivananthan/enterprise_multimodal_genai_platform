SYSTEM_PROMPTS = """
You are a helpful assistant.
Answer ONLY using the provided context.
If the answer is not found,say "Information not available"
"""
def build_prompt(context:str,question:str) -> str:
    return f"""
{SYSTEM_PROMPTS}

Context:
{context}

Question:
{question}
"""