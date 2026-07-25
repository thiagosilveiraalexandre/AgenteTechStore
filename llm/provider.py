# ============================================================
# llm/provider.py
# Responsável por criar e configurar a instância da LLM (Modelo de Linguagem)
# utilizada pelo agente. Centraliza a configuração do cliente OpenAI
# para conectar ao OpenRouter (ou qualquer provedor compatível).
# ============================================================

from langchain_openai import ChatOpenAI

# Importa as configurações definidas em config/settings.py
from config.settings import (
    OPENROUTER_API_KEY,   # Chave de API para autenticação
    MODEL_NAME,           # Nome do modelo a ser usado
    TEMPERATURE,          # Controla a criatividade das respostas
    BASE_URL              # URL base da API (OpenRouter)
)


def get_llm():
    """
    Cria e retorna uma instância da LLM configurada para o projeto.

    A função utiliza as configurações centralizadas em settings.py,
    garantindo que todos os parâmetros (modelo, temperatura, API key, base URL)
    estejam consistentes em toda a aplicação.

    Retorna:
        ChatOpenAI: Instância do modelo de linguagem configurada.

    Como funciona:
        1. O LangChain usa a classe ChatOpenAI como interface para modelos
           compatíveis com a API da OpenAI.
        2. Mesmo usando o OpenRouter (que não é a OpenAI oficial), a API
           é compatível com o formato OpenAI, permitindo o uso do ChatOpenAI.
        3. A configuração de BASE_URL redireciona as chamadas para o endpoint
           do OpenRouter, onde múltiplos modelos estão disponíveis.
        4. A chave OPENROUTER_API_KEY é lida do arquivo .env, garantindo
           que credenciais não fiquem expostas no código.

    Observações:
        - Se a chave API estiver ausente ou inválida, a LLM lançará erro.
        - O modelo "inclusionai/ling-3.0-flash:free" é gratuito e funciona
          bem para chatbots de vendas.
        - A temperatura 0 torna as respostas mais determinísticas e precisas.
    """
    return ChatOpenAI(
        model=MODEL_NAME,
        api_key=OPENROUTER_API_KEY,
        base_url=BASE_URL,
        temperature=TEMPERATURE
    )