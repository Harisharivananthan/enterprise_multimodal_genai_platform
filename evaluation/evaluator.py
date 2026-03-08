from evaluation.datasets import load_eval_dataset
from app.agents.agent_orchestrator import run_agent_system


def evaluate_system(dataset_path: str):

    dataset = load_eval_dataset(dataset_path)

    results = []

    for item in dataset:

        question = item["question"]
        expected = item["expected_answer"]

        predicted = run_agent_system(question)

        result = {
            "question": question,
            "expected": expected,
            "predicted": predicted
        }

        results.append(result)

    return results