from app.core.llm import get_llm

llm = get_llm()

REWRITE_PROMPT = """
Rewrite the user's question to make it more precise for document search.
Return ONLY the improved query.

User question:
{question}
"""

def rewrite_query(question):
    prompt = REWRITE_PROMPT.format(question=question)
    result = llm.invoke(prompt)
    return result.content.strip()