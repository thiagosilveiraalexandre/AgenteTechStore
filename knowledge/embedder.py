# ============================================================
# knowledge/embedder.py
# Responsável por criar o modelo de embeddings (vetores) para o RAG.
# Os embeddings transformam texto em representações numéricas,
# permitindo a busca semântica nos documentos.
# 
# Utiliza FastEmbed, que carrega modelos localmente sem avisos
# de autenticação (HF_TOKEN) e sem dependência do huggingface_hub.
# ============================================================

from fastembed import TextEmbedding


class FastEmbedWrapper:
    """
    Wrapper para compatibilidade com o LangChain/Chroma.
    O Chroma espera métodos embed_documents() e embed_query().
    """
    def __init__(self, model_name: str):
        """
        Inicializa o modelo FastEmbed.

        Parâmetros:
            model_name (str): Nome do modelo no formato HuggingFace.
                              Padrão: 'sentence-transformers/all-MiniLM-L6-v2'.
        """
        self.model = TextEmbedding(model_name=model_name)

    def embed_documents(self, texts):
        """
        Gera embeddings para uma lista de textos (documentos).

        Parâmetros:
            texts (list): Lista de strings.

        Retorna:
            list: Lista de vetores (listas de floats).
        """
        return [list(emb) for emb in self.model.embed(texts)]

    def embed_query(self, text):
        """
        Gera embedding para uma única consulta (pergunta do usuário).

        Parâmetros:
            text (str): Texto da consulta.

        Retorna:
            list: Vetor (lista de floats).
        """
        return list(self.model.embed([text]))[0]


def criar_embedder(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    """
    Cria e retorna um modelo de embeddings local usando FastEmbed.

    Parâmetros:
        model_name (str): Nome do modelo no HuggingFace Hub.
                          O valor padrão 'all-MiniLM-L6-v2' é um modelo leve,
                          rápido e com boa qualidade para busca semântica.

    Retorna:
        FastEmbedWrapper: Instância do wrapper que oferece os métodos
                          embed_documents() e embed_query().

    Como funciona:
        - O modelo converte frases/documentos em vetores de 384 dimensões.
        - Esses vetores são usados pelo Chroma para calcular similaridade
          entre a pergunta do usuário e os trechos dos PDFs.
        - O modelo é baixado localmente na primeira execução (~80 MB).
        - Funciona 100% offline após o download, sem custos de API.
        - Não gera avisos sobre HF_TOKEN, pois o FastEmbed não exige
          autenticação para modelos públicos.
    """
    return FastEmbedWrapper(model_name)