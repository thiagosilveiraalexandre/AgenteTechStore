from knowledge.loader import carregar_pdfs
from knowledge.splitter import dividir_documentos
docs = carregar_pdfs()
if docs:
    chunks = dividir_documentos(docs)
    print(f"Chunks gerados: {len(chunks)}")
    if chunks:
        print("Primeiro chunk:", chunks[0].page_content[:100])
else:
    print("Nenhum documento carregado.")