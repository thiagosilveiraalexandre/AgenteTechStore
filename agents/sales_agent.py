from llm.provider import get_llm
from agents.intent_router import IntentRouter
from agents.intent import Intent


class SalesAgent:

    def __init__(self):
        self.llm = get_llm()
        self.router = IntentRouter()

    def responder(self, pergunta: str) -> str:
        """
        Processa a pergunta do usuário e retorna a resposta.
        """

        # Descobre a intenção da pergunta
        intencao = self.router.classificar(pergunta)

        # Conversa inicial
        if intencao == Intent.CONVERSA:

            return (
                "Olá! 😊 Seja bem-vindo à TechStore.\n\n"
                "Posso ajudá-lo com:\n"
                "• Produtos\n"
                "• Preços\n"
                "• Pedidos\n"
                "• Entregas\n"
                "• Pagamentos\n"
                "• Garantias\n\n"
                "Como posso ajudar?"
            )

        # Produto (por enquanto usa a LLM)
        elif intencao == Intent.PRODUTO:

            resposta = self.llm.invoke(pergunta)
            return resposta.content

        # Pedido
        elif intencao == Intent.PEDIDO:

            return (
                "Em breve consultarei seus pedidos diretamente "
                "em nosso banco de dados."
            )

        # Cliente
        elif intencao == Intent.CLIENTE:

            return (
                "Em breve poderei consultar seus dados "
                "de cadastro."
            )

        # Políticas
        elif intencao == Intent.POLITICA:

            return (
                "Em breve consultarei nossa documentação "
                "utilizando RAG."
            )

        # Fora do escopo
        else:

            return (
                "Posso ajudá-lo apenas com assuntos relacionados "
                "à TechStore, como produtos, pedidos, pagamentos, "
                "entregas e políticas da empresa."
            )