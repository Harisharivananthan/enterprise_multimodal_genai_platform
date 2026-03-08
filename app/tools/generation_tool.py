from app.core.llm import get_llm
from app.core.prompts import build_prompt

llm = get_llm()

def generation_tool(question: str, context: str) -> str:
    """
    Generate an answer grounded in retrieved context.
    """
    prompt = build_prompt(context, question)
    response = llm.invoke(prompt)
    return response.content.strip()