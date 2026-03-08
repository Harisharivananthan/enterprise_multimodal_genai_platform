from app.core.llm import get_llm
from app.core.retriever import retrieve_context
from app.core.prompts import build_prompt
from app.validators.output_validator import validate_output
from app.validators.safety_rules import apply_safety_rules

llm = get_llm()


def run_rag(question):
    context = retrieve_context(question)
    prompt = build_prompt(context, question)

    answer = llm.invoke(prompt).content

    answer = validate_output(answer)
    answer = apply_safety_rules(answer)

    return answer