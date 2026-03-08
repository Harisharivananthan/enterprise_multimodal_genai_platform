from app.tools.generation_tool import generation_tool

def generate_answer(question: str, context: str) -> str:
    """
    Agent responsible for generating an answer using retrieved context.
    """
    return generation_tool(question, context)