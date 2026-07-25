# ============================================================
# teste_oci.py
# Script para testar o agente em ambientes sem interface gráfica
# (ex: Oracle Cloud Infrastructure - OCI).
# 
# Uso: python teste_oci.py
# ============================================================

from agents.sales_agent import SalesAgent

def main():
    """
    Função principal que cria o agente, solicita uma pergunta ao usuário
    via terminal e exibe a resposta gerada.
    """
    # Cria uma instância do agente (já carrega LLM, router e retriever)
    print("Inicializando o agente...")
    agent = SalesAgent()
    print("Agente pronto! Digite sua pergunta:")

    # Lê a pergunta do usuário (entrada pelo terminal)
    pergunta = input("Digite sua pergunta: ")

    # Obtém a resposta do agente
    resposta = agent.responder(pergunta)

    # Exibe a resposta no terminal
    print(f"\nResposta: {resposta}")

if __name__ == "__main__":
    main()