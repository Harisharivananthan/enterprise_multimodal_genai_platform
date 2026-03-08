from app.core.llm import get_llm


class ModelServer:

    def __init__(self):
        self.llm = get_llm()

    def generate(self, prompt: str):
        response = self.llm.invoke(prompt)
        return response.content


model_server = ModelServer()