# Importa a função que cria/fornece o modelo de linguagem (LLM)
from llm.provider import get_llm
# Importa o Enum Intent, que define as intenções possíveis
from agents.intent import Intent


class IntentRouter:
    """
    Classe responsável por classificar a intenção da pergunta do usuário.
    Utiliza a LLM para interpretar o texto e retornar uma das intenções definidas no Enum Intent.
    """

    def __init__(self):
        """
        Inicializa o roteador obtendo a instância da LLM (via get_llm).
        A LLM será usada para fazer a classificação.
        """
        self.llm = get_llm()

    def classificar(self, pergunta: str) -> Intent:
        """
        Classifica a intenção da mensagem do usuário.

        Parâmetros:
            pergunta (str): A mensagem/frase digitada pelo usuário.

        Retorna:
            Intent: Um valor do Enum Intent indicando a intenção detectada.

        O método constrói um prompt com exemplos (few-shot) e instruções rígidas
        para que a LLM retorne APENAS uma palavra dentre as opções do Enum.
        Se a resposta não for válida, retorna FORA_DO_ESCOPO como fallback.
        """

        # --- Construção do prompt para a LLM ---
        # O prompt define o papel do sistema (classificador), dá regras claras
        # e fornece exemplos de perguntas e respostas esperadas (few-shot).
        prompt = f"""
Você é um classificador de intenções da TechStore.

Sua única função é classificar a intenção da pergunta.

Nunca explique.
Nunca converse.
Nunca responda a pergunta.

Responda SOMENTE com uma destas palavras:

PRODUTO
PEDIDO
CLIENTE
POLITICA
CONVERSA
FORA_DO_ESCOPO

Exemplos:

Usuário: Oi
Resposta: CONVERSA

Usuário: Bom dia
Resposta: CONVERSA

Usuário: Quero comprar um notebook
Resposta: PRODUTO

Usuário: Quanto custa um celular?
Resposta: PRODUTO

Usuário: Onde está meu pedido?
Resposta: PEDIDO

Usuário: Quero acompanhar meu pedido
Resposta: PEDIDO

Usuário: Quero alterar meu cadastro
Resposta: CLIENTE

Usuário: Como funciona a garantia?
Resposta: POLITICA

Usuário: Como funciona a troca?
Resposta: POLITICA

Usuário: Quem descobriu o Brasil?
Resposta: FORA_DO_ESCOPO

Agora classifique:

Usuário: {pergunta}

Resposta:
"""

        # --- Chamada à LLM ---
        # Envia o prompt para a LLM e obtém a resposta (objeto com atributo .content)
        resposta = self.llm.invoke(prompt)

        # --- Processamento da resposta ---
        # Remove espaços extras e converte para maiúsculas para padronizar
        texto = resposta.content.strip().upper()

        try:
            # Tenta converter a string recebida para um valor do Enum Intent
            # Se a string não corresponder a nenhum membro do Enum, levanta ValueError
            return Intent(texto)
        except ValueError:
            # Fallback: se a LLM retornar algo inesperado, assume que é fora do escopo
            return Intent.FORA_DO_ESCOPO