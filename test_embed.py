from knowledge.embedder import criar_embedder
embedder = criar_embedder()
print(embedder.embed_documents(["teste"])[0][:5])  # Deve mostrar os primeiros números