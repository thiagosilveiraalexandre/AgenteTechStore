import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

import warnings
warnings.filterwarnings("ignore")

# Também silencia logs do LangChain (se houver)
import logging
logging.getLogger("langchain").setLevel(logging.ERROR)
# ============================================================
# teste_oci.py
# Script para testar o agente em ambientes sem interface gráfica
# (ex: Oracle Cloud Infrastructure - OCI).
# 
# Funciona em loop até o usuário digitar "sair".
# Uso: python teste_oci.py
# ============================================================

from agents.sales_agent import SalesAgent

def main():
    print("=" * 50)
    print("Agente Inteligente TechStore - Modo Terminal")
    print("Digite 'sair' para encerrar.")
    print("=" * 50)

    # Cria uma instância do agente (já carrega LLM, router e retriever)
    agent = SalesAgent()

    while True:
        # Lê a pergunta do usuário
        pergunta = input("\nVoce: ")

        # Verifica se o usuário quer sair
        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o agente. Ate logo!")
            break

        # Obtém a resposta do agente
        try:
            resposta = agent.responder(pergunta)
            print(f"IA: {resposta}")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()