from llm.provider import get_llm
from agents.intent import Intent


class IntentRouter:

    def __init__(self):
        self.llm = get_llm()

    def classificar(self, pergunta: str) -> intent:
        """
        Classifica a intenção da mensagem do usuário.

        Retorna apenas UMA das opções:
        - PRODUTO
        - PEDIDO
        - CLIENTE
        - POLITICA
        - CONVERSA
        - FORA_DO_ESCOPO
        """

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

        resposta = self.llm.invoke(prompt)

        texto = resposta.content.strip().upper()

        try:
            return Intent(texto)

        except ValueError:
            return Intent.FORA_DO_ESCOPO
