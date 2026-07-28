# ============================================================
# knowledge/vector_store.py
# Responsável por criar e gerenciar o índice vetorial (vector store)
# usando Chroma. Permite construir o índice a partir de PDFs e
# obter um retriever para busca semântica.
# ============================================================

from langchain_chroma import Chroma
from .embedder import criar_embedder
from .loader import carregar_pdfs
from .splitter import dividir_documentos

# Diretório onde o índice vetorial será persistido em disco.
PERSIST_DIR = "./chroma_db"


def construir_indice():
    """
    Constrói o índice vetorial a partir dos PDFs encontrados em knowledge/data/.
    """
    docs = carregar_pdfs()
    if not docs:
        raise ValueError("Nenhum PDF encontrado em knowledge/data/")

    chunks = dividir_documentos(docs)
    embedder = criar_embedder()

    # Cria o vector store (o Chroma já persiste automaticamente)
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedder,
        persist_directory=PERSIST_DIR
    )

    # O método .persist() não é mais necessário em versões recentes
    # Seu índice já está salvo em PERSIST_DIR

    return vectorstore


def obter_retriever(k: int = 3):
    """
    Obtém um retriever para busca semântica a partir do índice persistido.
    """
    embedder = criar_embedder()
    vectorstore = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embedder
    )
    return vectorstore.as_retriever(search_kwargs={"k": k})