from inference.model_server import model_server


def route_inference(task_type: str, prompt: str):
    """
    Route request to correct model.
    """

    if task_type == "text_generation":
        return model_server.generate(prompt)

    raise ValueError("Unknown task type")