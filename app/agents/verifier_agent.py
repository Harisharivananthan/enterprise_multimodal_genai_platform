from app.validators.output_validator import validate_output
from app.validators.safety_rules import apply_safety_rules

def verify_answer(answer: str) -> str:
    """
    Applies validation and safety checks.
    """
    answer = validate_output(answer)
    answer = apply_safety_rules(answer)
    return answer