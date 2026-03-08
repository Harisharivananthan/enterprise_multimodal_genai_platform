from app.agents.query_rewriter_agent import rewrite_query
from app.tools.retrieval_tool import retrieval_tool
from app.agents.answer_generator_agent import generate_answer
from app.agents.verifier_agent import verify_answer

def run_reasoning_pipeline(question: str) -> str:
    """
    Multi-step reasoning pipeline.
    """

    # Step 1: rewrite query
    improved_query = rewrite_query(question)

    # Step 2: retrieve documents
    context = retrieval_tool(improved_query)

    # Step 3: generate answer
    answer = generate_answer(question, context)

    # Step 4: verify answer
    verified_answer = verify_answer(answer)

    return verified_answer