from agents.sales_agent import SalesAgent


def main():
    print("=" * 50)
    print("🤖 Agente Inteligente TechStore")
    print("Digite 'sair' para encerrar.")
    print("=" * 50)

    # Cria o agente de vendas
    agent = SalesAgent()

    while True:
        pergunta = input("\nVocê: ")

        if pergunta.lower() == "sair":
            print("Até logo!")
            break

        try:
            resposta = agent.responder(pergunta)
            print(f"\nIA: {resposta}")

        except Exception as erro:
            print(f"\nErro: {erro}")


if __name__ == "__main__":
    main()