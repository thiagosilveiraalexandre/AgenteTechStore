from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

def carregar_pdfs(pasta: str = "knowledge/data"):
    arquivos = Path(pasta).glob("*.pdf")
    docs = []
    for arquivo in arquivos:
        loader = PyPDFLoader(str(arquivo))
        docs.extend(loader.load())
    return docs