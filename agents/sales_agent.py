# ============================================================
# agents/sales_agent.py
# Agente principal da TechStore.
# Orquestra a classificação de intenção, a busca RAG e a geração
# de respostas usando a LLM.
# ============================================================

# Importa a função que cria o modelo de linguagem (LLM)
from llm.provider import get_llm

# Importa o roteador que classifica a pergunta do usuário
from agents.intent_router import IntentRouter

# Importa o Enum com todas as intenções possíveis
from agents.intent import Intent

# Importa a função que obtém o retriever (busca no índice vetorial)
from knowledge.vector_store import obter_retriever


class SalesAgent:
    """
    Agente de vendas da TechStore.

    Responsabilidades:
        - Classificar a intenção da pergunta do usuário.
        - Para perguntas sobre produtos e políticas, usar RAG (busca em PDFs).
        - Para outros assuntos, usar respostas fixas ou genéricas.
        - Gerar respostas contextualizadas e amigáveis.
    """

    def __init__(self):
        """
        Inicializa o agente com:
            - LLM: modelo de linguagem para gerar respostas.
            - Router: classificador de intenções.
            - Retriever: ferramenta de busca semântica (RAG) que retorna os
              trechos mais relevantes dos PDFs indexados.
        """
        self.llm = get_llm()
        self.router = IntentRouter()
        # k=3 significa que o retriever vai devolver os 3 trechos mais similares
        self.retriever = obter_retriever(k=3)

    def responder(self, pergunta: str) -> str:
        """
        Processa a pergunta do usuário e retorna uma resposta.

        Etapas:
            1. Classifica a intenção usando o router.
            2. Roteia para a lógica específica de cada intenção.
            3. Para PRODUTO e POLITICA, busca contexto no índice e usa a LLM.
            4. Para RELATORIO, usa RAG também (perguntas sobre dados do catálogo).
            5. Para CONVERSA, PEDIDO, CLIENTE e FORA_DO_ESCOPO, usa respostas fixas.

        Parâmetro:
            pergunta (str): A mensagem digitada pelo usuário.

        Retorno:
            str: A resposta gerada pelo agente.
        """

        # -- 1. Classificação da intenção --
        intencao = self.router.classificar(pergunta)

        # -- 2. Roteamento por intenção --

        # --- CASO CONVERSA: saudação / boas-vindas ---
        if intencao == Intent.CONVERSA:
            return (
        "Olá! 😊 Seja bem-vindo à TechStore.\n\n"
        "Posso ajudá-lo com:\n"
        "• Produtos\n"
        "• Preços\n"
        "• Pedidos\n"
        "• Entregas\n"
        "• Pagamentos\n"
        "• Garantias\n"
        "• Relatórios\n\n"  # <--- NOVO
        "Como posso ajudar?"
    )

        # --- CASO PRODUTO: usa RAG para buscar no PDF ---
        elif intencao == Intent.PRODUTO:
            # Busca os 3 trechos mais relevantes para a pergunta
            docs = self.retriever.invoke(pergunta)

            # Se não encontrar nada, avisa o usuário
            if not docs:
                return "Desculpe, não encontrei informações sobre esse produto no nosso catálogo."

            # Junta os trechos em um único bloco de contexto
            contexto = "\n\n".join([doc.page_content for doc in docs])

            # Monta o prompt com instruções claras para a LLM
            prompt = f"""
Você é um assistente de vendas da TechStore.
Responda de forma amigável e direta, usando APENAS as informações do contexto abaixo.

Contexto:
{contexto}

Pergunta do cliente: {pergunta}
Resposta:"""

            # Gera a resposta com a LLM e retorna o conteúdo
            resposta = self.llm.invoke(prompt)
            return resposta.content

        # --- CASO PEDIDO: funcionalidade futura (sem RAG) ---
        elif intencao == Intent.PEDIDO:
            return (
                "Em breve consultarei seus pedidos diretamente "
                "em nosso banco de dados."
            )

        # --- CASO CLIENTE: funcionalidade futura (sem RAG) ---
        elif intencao == Intent.CLIENTE:
            return (
                "Em breve poderei consultar seus dados "
                "de cadastro."
            )

        # --- CASO POLITICA: usa RAG para buscar no PDF ---
        elif intencao == Intent.POLITICA:
            docs = self.retriever.invoke(pergunta)
            if not docs:
                return "Desculpe, não encontrei essa política em nossos documentos."

            contexto = "\n\n".join([doc.page_content for doc in docs])

            prompt = f"""
Você é um assistente de vendas da TechStore.
Responda de forma clara e objetiva, usando APENAS as informações do contexto abaixo.

Contexto:
{contexto}

Pergunta do cliente: {pergunta}
Resposta:"""

            resposta = self.llm.invoke(prompt)
            return resposta.content

        # --- CASO RELATORIO: usa RAG para responder perguntas sobre dados do catálogo ---
        elif intencao == Intent.RELATORIO:
            # Exemplos: "qual o produto mais caro?", "quantos produtos temos?"
            docs = self.retriever.invoke(pergunta)
            if not docs:
                return "Desculpe, não encontrei informações suficientes no catálogo para responder."

            contexto = "\n\n".join([doc.page_content for doc in docs])

            prompt = f"""
Você é um assistente de vendas da TechStore.
Responda à pergunta sobre relatório ou análise usando APENAS os dados do contexto abaixo.
Seja direto e numérico quando possível.

Contexto:
{contexto}

Pergunta: {pergunta}
Resposta:"""

            resposta = self.llm.invoke(prompt)
            return resposta.content

        # --- CASO FORA_DO_ESCOPO (fallback) ---
        else:
            return (
                "Posso ajudá-lo apenas com assuntos relacionados "
                "à TechStore, como produtos, pedidos, pagamentos, "
                "entregas e políticas da empresa."
            )