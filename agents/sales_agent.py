# Importa a função que fornece o modelo de linguagem (LLM)
from llm.provider import get_llm
# Importa o roteador de intenções (classifica a pergunta)
from agents.intent_router import IntentRouter
# Importa o Enum Intent com as intenções possíveis
from agents.intent import Intent
# Importa a função que obtém o retriever para buscar documentos (RAG)
from knowledge.vector_store import obter_retriever


class SalesAgent:
    """
    Agente de vendas da TechStore.
    Responsável por processar perguntas do usuário, classificar a intenção
    e gerar respostas, utilizando RAG para buscar informações em documentos.
    """

    def __init__(self):
        """Inicializa o agente com LLM, roteador e retriever."""
        self.llm = get_llm()  # Modelo de linguagem para gerar respostas
        self.router = IntentRouter()  # Classifica a intenção da pergunta
        self.retriever = obter_retriever(k=3)  # Busca os 3 trechos mais relevantes dos PDFs

    def responder(self, pergunta: str) -> str:
        """
        Processa a pergunta do usuário e retorna uma resposta adequada.

        Parâmetros:
            pergunta (str): Texto digitado pelo usuário.

        Retorna:
            str: Resposta gerada pelo agente.

        O fluxo é:
        1. Classifica a intenção da pergunta.
        2. Com base na intenção, executa a lógica correspondente.
        3. Para PRODUTO e POLITICA, usa RAG para buscar contexto e gerar resposta.
        """

        # 1. Classifica a intenção da pergunta
        intencao = self.router.classificar(pergunta)

        # 2. Lógica por intenção

        # CASO CONVERSA: saudação ou conversa inicial
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

        # CASO PRODUTO: busca informações sobre produtos no índice vetorial (RAG)
        elif intencao == Intent.PRODUTO:
            # Busca trechos relevantes nos PDFs
            docs = self.retriever.invoke(pergunta)
            if not docs:
                return "Desculpe, não encontrei informações sobre esse produto no nosso catálogo."
            # Concatena os trechos para formar o contexto
            contexto = "\n\n".join([doc.page_content for doc in docs])
            # Monta o prompt com contexto e pergunta
            prompt = f"""
Você é um assistente de vendas da TechStore. Responda de forma amigável e direta, usando APENAS as informações do contexto abaixo.

Contexto:
{contexto}

Pergunta do cliente: {pergunta}
Resposta:"""
            # Gera a resposta com a LLM
            resposta = self.llm.invoke(prompt)
            return resposta.content

        # CASO PEDIDO: funcionalidade futura
        elif intencao == Intent.PEDIDO:
            return (
                "Em breve consultarei seus pedidos diretamente "
                "em nosso banco de dados."
            )

        # CASO CLIENTE: funcionalidade futura
        elif intencao == Intent.CLIENTE:
            return (
                "Em breve poderei consultar seus dados "
                "de cadastro."
            )

        # CASO POLITICA: busca informações sobre políticas no índice vetorial (RAG)
        elif intencao == Intent.POLITICA:
            # Busca trechos relevantes nos PDFs
            docs = self.retriever.invoke(pergunta)
            if not docs:
                return "Desculpe, não encontrei essa política em nossos documentos."
            # Concatena os trechos para formar o contexto
            contexto = "\n\n".join([doc.page_content for doc in docs])
            # Monta o prompt com contexto e pergunta
            prompt = f"""
Você é um assistente de vendas da TechStore. Responda de forma clara e objetiva, usando APENAS as informações do contexto abaixo.

Contexto:
{contexto}

Pergunta do cliente: {pergunta}
Resposta:"""
            # Gera a resposta com a LLM
            resposta = self.llm.invoke(prompt)
            return resposta.content

        # CASO FORA_DO_ESCOPO: assunto não relacionado à empresa
        else:
            return (
                "Posso ajudá-lo apenas com assuntos relacionados "
                "à TechStore, como produtos, pedidos, pagamentos, "
                "entregas e políticas da empresa."
            )