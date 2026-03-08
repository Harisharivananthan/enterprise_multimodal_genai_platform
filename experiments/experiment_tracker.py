import json
from datetime import datetime


def log_experiment(config: dict, metrics: dict):

    experiment = {
        "timestamp": str(datetime.utcnow()),
        "config": config,
        "metrics": metrics
    }

    with open("experiments/experiments_log.json", "a") as f:
        f.write(json.dumps(experiment) + "\n")