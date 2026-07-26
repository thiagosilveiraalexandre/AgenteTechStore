import os
import warnings

# === SILENCIA O AVISO DO HF TOKEN ===
warnings.filterwarnings("ignore", message="You are sending unauthenticated requests")
warnings.filterwarnings("ignore", category=UserWarning, module="huggingface_hub")

# === DEFINE VARIÁVEIS DE AMBIENTE (por segurança) ===
os.environ["HF_TOKEN"] = "dummy"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# === SILENCIA LOGS DAS BIBLIOTECAS ===
import logging
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)
logging.getLogger("langchain").setLevel(logging.ERROR)
logging.getLogger("sentence_transformers").setLevel(logging.ERROR)

# === AGORA IMPORTA O AGENTE ===
from agents.sales_agent import SalesAgent

def main():
    print("=" * 50)
    print("Agente Inteligente TechStore - Modo Terminal")
    print("Digite 'sair' para encerrar.")
    print("=" * 50)

    agent = SalesAgent()

    while True:
        pergunta = input("\nVoce: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o agente. Ate logo!")
            break
        try:
            resposta = agent.responder(pergunta)
            print(f"IA: {resposta}")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()