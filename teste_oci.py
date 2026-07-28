# ============================================================
# teste_oci.py
# Script para testar o agente em ambientes sem interface gráfica
# (ex: Oracle Cloud Infrastructure - OCI).
# 
# Funciona em loop contínuo, simulando um chat no terminal.
# Digite "sair" para encerrar.
# Uso: python teste_oci.py
# ============================================================

import os
import warnings

# --- SUPRIME O AVISO DO HF_TOKEN ---
os.environ["HF_TOKEN"] = "dummy"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# Suprime avisos de depreciação (LangChain, etc.)
warnings.filterwarnings("ignore")
# Suprime avisos específicos do HuggingFace
warnings.filterwarnings("ignore", message=".*unauthenticated.*")
warnings.filterwarnings("ignore", message=".*HF_TOKEN.*")

import logging
logging.getLogger("langchain").setLevel(logging.ERROR)  # Remove logs verbosos do LangChain
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)  # Remove logs do HuggingFace

# Importa o agente principal (já carrega LLM, router e retriever)
from agents.sales_agent import SalesAgent


def main():
    """
    Função principal do script de teste.
    Cria o agente e inicia um loop de conversação via terminal.
    """
    print("=" * 50)
    print("Agente Inteligente TechStore - Modo Terminal")
    print("Digite 'sair' para encerrar.")
    print("=" * 50)

    # Cria uma instância do agente (já carrega LLM, router e retriever)
    agent = SalesAgent()

    # Loop principal – mantém a conversa até o usuário digitar "sair"
    while True:
        # Lê a pergunta do usuário (entrada pelo terminal)
        pergunta = input("\nVoce: ")

        # Verifica se o usuário quer encerrar (suporta várias variações)
        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o agente. Ate logo!")
            break

        # Tenta obter a resposta do agente
        try:
            resposta = agent.responder(pergunta)
            print(f"IA: {resposta}")
        except Exception as e:
            # Em caso de erro, exibe a mensagem sem interromper o programa
            print(f"Erro: {e}")


# Ponto de entrada do script
if __name__ == "__main__":
    main()