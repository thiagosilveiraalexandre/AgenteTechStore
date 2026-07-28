# ============================================================
# knowledge/embedder.py
# Responsável por criar o modelo de embeddings (vetores) para o RAG.
# Utiliza FastEmbed (leve, local, sem avisos de autenticação).
# ============================================================

from fastembed import TextEmbedding

class FastEmbedWrapper:
    """
    Wrapper para compatibilidade com o Chroma.
    O Chroma espera métodos embed_documents() e embed_query().
    """
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = TextEmbedding(model_name)

    def embed_documents(self, texts):
        """Gera embeddings para uma lista de textos."""
        # O FastEmbed retorna um gerador, convertemos para lista de listas
        return [list(embedding) for embedding in self.model.embed(texts)]

    def embed_query(self, text):
        """Gera embedding para uma única consulta."""
        return list(next(self.model.embed([text])))

def criar_embedder(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    return FastEmbedWrapper(model_name)