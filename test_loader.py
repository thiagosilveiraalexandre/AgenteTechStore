from knowledge.loader import carregar_pdfs
docs = carregar_pdfs()
print(f"Número de documentos carregados: {len(docs)}")
if docs:
    print("Primeiro documento:", docs[0].page_content[:100])