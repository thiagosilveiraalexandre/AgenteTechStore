# ============================================================
# knowledge/embedder.py
# Responsável por criar o modelo de embeddings (vetores) para o RAG.
# Utiliza SentenceTransformer diretamente (mais confiável).
# ============================================================

from sentence_transformers import SentenceTransformer

class SentenceTransformerWrapper:
    """
    Wrapper para compatibilidade com o Chroma (espera métodos embed_documents e embed_query).
    """
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        """Gera embeddings para uma lista de textos."""
        return self.model.encode(texts, convert_to_numpy=True).tolist()

    def embed_query(self, text):
        """Gera embedding para uma única consulta."""
        return self.model.encode([text], convert_to_numpy=True)[0].tolist()

def criar_embedder(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    """
    Cria e retorna um wrapper para SentenceTransformer.
    """
    return SentenceTransformerWrapper(model_name)