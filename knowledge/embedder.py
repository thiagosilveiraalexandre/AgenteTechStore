# ============================================================
# knowledge/embedder.py
# Responsável por criar o modelo de embeddings (vetores) para o RAG.
# Os embeddings transformam texto em representações numéricas,
# permitindo a busca semântica nos documentos.
#
# Utiliza HuggingFaceEmbeddings com HF_TOKEN configurado no sistema
# para evitar avisos de autenticação.
# ============================================================

from langchain_huggingface import HuggingFaceEmbeddings


def criar_embedder(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    """
    Cria e retorna um modelo de embeddings local da HuggingFace.

    Parâmetros:
        model_name (str): Nome do modelo no HuggingFace Hub.
                          O valor padrão 'all-MiniLM-L6-v2' é um modelo leve,
                          rápido e com boa qualidade para busca semântica.

    Retorna:
        HuggingFaceEmbeddings: Instância do modelo pronta para gerar embeddings
                               a partir de textos.

    Como funciona:
        - O modelo converte frases/documentos em vetores de 384 dimensões.
        - Esses vetores são usados pelo Chroma para calcular similaridade
          entre a pergunta do usuário e os trechos dos PDFs.
        - O modelo é baixado localmente na primeira execução (~80 MB).
        - Funciona 100% offline após o download, sem custos de API.
        - Com HF_TOKEN configurado, não há avisos de autenticação.
    """
    return HuggingFaceEmbeddings(model_name=model_name)