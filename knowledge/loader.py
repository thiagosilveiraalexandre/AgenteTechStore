# ============================================================
# knowledge/loader.py
# Responsável por carregar documentos PDF da pasta especificada.
# Utiliza o PyPDFLoader do LangChain para extrair texto de cada PDF.
# ============================================================

from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path


def carregar_pdfs(pasta: str = "knowledge/data"):
    """
    Carrega todos os arquivos PDF encontrados em uma pasta.

    Parâmetros:
        pasta (str): Caminho para a pasta onde os PDFs estão armazenados.
                     O valor padrão é "knowledge/data".

    Retorna:
        list: Uma lista de objetos Document do LangChain, onde cada objeto
              contém o texto extraído e metadados (como nome do arquivo, página, etc.).

    Como funciona:
        1. Usa pathlib.Path para localizar todos os arquivos com extensão .pdf.
        2. Para cada arquivo, instancia um PyPDFLoader e carrega o conteúdo.
        3. O método loader.load() extrai texto de todas as páginas e retorna
           uma lista de Document (um por página).
        4. Todos os documentos são acumulados em uma única lista.

    Observação:
        - O PyPDFLoader é adequado para PDFs com texto extraível (não scaneados).
        - Se um PDF estiver corrompido ou vazio, pode lançar exceção.
        - A pasta padrão "knowledge/data" está no .gitignore, então os PDFs
          não serão versionados no GitHub (evita arquivos grandes).
    """
    # Cria um objeto Path para a pasta especificada e busca todos os arquivos .pdf
    arquivos = Path(pasta).glob("*.pdf")
    docs = []

    # Itera sobre cada arquivo PDF encontrado
    for arquivo in arquivos:
        # Instancia o loader para o arquivo atual
        loader = PyPDFLoader(str(arquivo))
        # Carrega o conteúdo do PDF (retorna lista de Document)
        docs.extend(loader.load())

    return docs