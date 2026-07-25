# ============================================================
# knowledge/vector_store.py
# Responsável por criar e gerenciar o índice vetorial (vector store)
# usando Chroma. Permite construir o índice a partir de PDFs e
# obter um retriever para busca semântica.
# ============================================================

from langchain_community.vectorstores import Chroma
from .embedder import criar_embedder
from .loader import carregar_pdfs
from .splitter import dividir_documentos

# Diretório onde o índice vetorial será persistido em disco.
# O Chroma salva os embeddings e metadados localmente, permitindo
# reutilizar o índice sem precisar reprocessar os PDFs a cada execução.
PERSIST_DIR = "./chroma_db"


def construir_indice():
    """
    Constrói o índice vetorial a partir dos PDFs encontrados em knowledge/data/.

    Fluxo:
        1. Carrega todos os PDFs da pasta usando carregar_pdfs().
        2. Divide os documentos em chunks usando dividir_documentos().
        3. Cria um embedder (modelo de embeddings).
        4. Cria um índice Chroma a partir dos chunks e embeddings.
        5. Persiste o índice no diretório PERSIST_DIR para reuso.

    Retorna:
        Chroma: O objeto vectorstore criado.

    Levanta:
        ValueError: Se nenhum PDF for encontrado na pasta.

    Observações:
        - Este processo pode levar alguns segundos/minutos dependendo da
          quantidade de PDFs e do tamanho dos documentos.
        - O modelo de embeddings é baixado na primeira execução (~80MB).
        - Após a criação, o índice fica salvo em ./chroma_db, acelerando
          futuras execuções do programa.
    """
    # 1. Carrega os PDFs
    docs = carregar_pdfs()
    if not docs:
        raise ValueError("Nenhum PDF encontrado em knowledge/data/")

    # 2. Divide em chunks
    chunks = dividir_documentos(docs)

    # 3. Cria o embedder
    embedder = criar_embedder()

    # 4. Cria o vector store (índice) a partir dos chunks
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedder,
        persist_directory=PERSIST_DIR
    )

    # 5. Persiste o índice em disco para reuso
    vectorstore.persist()

    return vectorstore


def obter_retriever(k: int = 3):
    """
    Obtém um retriever para busca semântica a partir do índice persistido.

    Parâmetros:
        k (int): Número de chunks mais relevantes a serem retornados.
                 O valor padrão é 3, equilibrando precisão e velocidade.

    Retorna:
        Retriever: Um objeto que pode ser usado para buscar documentos
                   relevantes com base na similaridade semântica.

    Como funciona:
        1. Carrega o embedder (mesmo modelo usado na criação).
        2. Conecta ao índice Chroma existente no diretório PERSIST_DIR.
        3. Retorna um retriever configurado para buscar os k chunks mais similares.

    Observações:
        - Este método assume que o índice já foi construído (construir_indice()
          já foi executado pelo menos uma vez).
        - Se o índice não existir, o Chroma criará um vazio, mas a busca
          não retornará resultados. Por isso, é importante construir o
          índice antes de usar o agente.
        - O retriever é usado no SalesAgent para buscar contexto relevante
          para cada pergunta do usuário.
    """
    # Cria o embedder (necessário para converter a pergunta em vetor)
    embedder = criar_embedder()

    # Conecta ao índice existente
    vectorstore = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embedder
    )

    # Configura o retriever para retornar os k melhores resultados
    return vectorstore.as_retriever(search_kwargs={"k": k})