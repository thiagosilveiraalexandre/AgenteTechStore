from llm.provider import get_llm
from agents.intent_router import IntentRouter
from agents.intent import Intent
from knowledge.vector_store import obter_retriever  # <--- NOVO


class SalesAgent:

    def __init__(self):
        self.llm = get_llm()
        self.router = IntentRouter()
        self.retriever = obter_retriever(k=3)  # <--- NOVO (busca 3 chunks)

    def responder(self, pergunta: str) -> str:
        """
        Processa a pergunta do usuário e retorna a resposta.
        """

        intencao = self.router.classificar(pergunta)

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

        elif intencao == Intent.PRODUTO:
            # --- USANDO RAG PARA PRODUTOS ---
            docs = self.retriever.invoke(pergunta)
            if not docs:
                return "Desculpe, não encontrei informações sobre esse produto no nosso catálogo."
            contexto = "\n\n".join([doc.page_content for doc in docs])
            prompt = f"""
Você é um assistente de vendas da TechStore. Responda de forma amigável e direta, usando APENAS as informações do contexto abaixo.

Contexto:
{contexto}

Pergunta do cliente: {pergunta}
Resposta:"""
            resposta = self.llm.invoke(prompt)
            return resposta.content

        elif intencao == Intent.PEDIDO:
            return (
                "Em breve consultarei seus pedidos diretamente "
                "em nosso banco de dados."
            )

        elif intencao == Intent.CLIENTE:
            return (
                "Em breve poderei consultar seus dados "
                "de cadastro."
            )

        elif intencao == Intent.POLITICA:
            # --- USANDO RAG PARA POLÍTICAS ---
            docs = self.retriever.invoke(pergunta)
            if not docs:
                return "Desculpe, não encontrei essa política em nossos documentos."
            contexto = "\n\n".join([doc.page_content for doc in docs])
            prompt = f"""
Você é um assistente de vendas da TechStore. Responda de forma clara e objetiva, usando APENAS as informações do contexto abaixo.

Contexto:
{contexto}

Pergunta do cliente: {pergunta}
Resposta:"""
            resposta = self.llm.invoke(prompt)
            return resposta.content

        else:  # FORA_DO_ESCOPO
            return (
                "Posso ajudá-lo apenas com assuntos relacionados "
                "à TechStore, como produtos, pedidos, pagamentos, "
                "entregas e políticas da empresa."
            )