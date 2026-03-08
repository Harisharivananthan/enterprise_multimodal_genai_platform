import json


def load_eval_dataset(path: str):
    with open(path, "r") as f:
        data = json.load(f)

    return data