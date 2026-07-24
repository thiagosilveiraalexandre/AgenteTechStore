from langchain_openai import ChatOpenAI

from config.settings import (
    OPENROUTER_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    BASE_URL
)


def get_llm():
    """
    Cria e retorna a LLM configurada.
    """

    return ChatOpenAI(
        model=MODEL_NAME,
        api_key=OPENROUTER_API_KEY,
        base_url=BASE_URL,
        temperature=TEMPERATURE
    )