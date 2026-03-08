from app.reasoning.reasoning_pipeline import run_reasoning_pipeline

def run_agent_system(question: str) -> str:
    """
    Entry point for the agentic AI system.
    """
    return run_reasoning_pipeline(question)