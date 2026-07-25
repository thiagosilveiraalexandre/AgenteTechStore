# ============================================================
# knowledge/splitter.py
# Responsável por dividir documentos longos em pedaços menores (chunks).
# Isso é essencial para o RAG, pois permite buscar apenas os trechos
# mais relevantes de um PDF, sem sobrecarregar a LLM com texto desnecessário.
# ============================================================

from langchain.text_splitter import RecursiveCharacterTextSplitter


def dividir_documentos(docs, chunk_size=500, overlap=50):
    """
    Divide uma lista de documentos em chunks menores para indexação vetorial.

    Parâmetros:
        docs (list): Lista de objetos Document (geralmente vindos do loader).
        chunk_size (int): Número máximo de caracteres por chunk.
                          Valor padrão: 500 caracteres.
        overlap (int): Número de caracteres que se sobrepõem entre chunks consecutivos.
                       Valor padrão: 50 caracteres.

    Retorna:
        list: Uma lista de Document divididos em chunks menores.

    Como funciona:
        1. O RecursiveCharacterTextSplitter tenta primeiro dividir o texto
           por parágrafos, depois por frases e, por último, por palavras.
           Isso preserva o máximo possível o significado semântico.
        2. O overlap (sobreposição) garante que informações importantes
           no limite entre dois chunks não sejam perdidas.
        3. Textos menores que chunk_size não são divididos.

    Por que esses valores?
        - chunk_size=500: Tamanho ideal para embeddings como o all-MiniLM,
          que tem limite de 512 tokens. 500 caracteres equivale a ~100-150 tokens.
        - overlap=50: Mantém contexto entre chunks, evitando perda de informações
          quando uma frase importante está "cortada" entre dois chunks.
    """
    # Cria o splitter com as configurações definidas
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    # Aplica a divisão a todos os documentos e retorna os chunks
    return splitter.split_documents(docs)