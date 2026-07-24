from langchain_community.vectorstores import Chroma
from .embedder import criar_embedder
from .loader import carregar_pdfs
from .splitter import dividir_documentos

PERSIST_DIR = "./chroma_db"

def construir_indice():
    docs = carregar_pdfs()
    if not docs:
        raise ValueError("Nenhum PDF encontrado em knowledge/data/")
    chunks = dividir_documentos(docs)
    embedder = criar_embedder()
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedder,
        persist_directory=PERSIST_DIR
    )
    vectorstore.persist()
    return vectorstore

def obter_retriever(k=3):
    embedder = criar_embedder()
    vectorstore = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embedder
    )
    return vectorstore.as_retriever(search_kwargs={"k": k})