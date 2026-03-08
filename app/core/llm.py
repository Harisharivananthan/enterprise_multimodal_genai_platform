from langchain_openai import ChatOpenAI
from config.settings import settings


def get_llm():
    return ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.2,
        max_completion_tokens=512,
        api_key=settings.OPENAI_API_KEY
    )