import PySimpleGUI as sg
from agents.sales_agent import SalesAgent

# Tema (opcional, mas bonito)
sg.theme("DarkBlue3")

# Layout da janela
layout = [
    [sg.Text("🤖 Agente Inteligente TechStore", font=("Helvetica", 16))],
    [sg.Multiline(
        size=(60, 15),
        key="-HISTORICO-",
        autoscroll=True,
        disabled=True,
        background_color="#2d2d2d",
        text_color="white"
    )],
    [sg.Text("Você:"), sg.Input(size=(50, 1), key="-INPUT-", focus=True)],
    [sg.Button("Enviar", bind_return_key=True), sg.Button("Sair")]
]

window = sg.Window("TechStore Agent", layout, resizable=True, finalize=True)
window.maximize()  # <--- Essa linha faz a mágica

# Cria o agente
agent = SalesAgent()

# Loop principal da interface
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Sair"):
        break

    if event == "Enviar":
        pergunta = values["-INPUT-"].strip()
        if not pergunta:
            continue

        # Exibe a pergunta no histórico
        window["-HISTORICO-"].print(f"🧑 Você: {pergunta}")
        window["-INPUT-"].update("")  # Limpa o campo

        # Obtém a resposta do agente
        try:
            resposta = agent.responder(pergunta)
            window["-HISTORICO-"].print(f"🤖 IA: {resposta}\n")
        except Exception as e:
            window["-HISTORICO-"].print(f"❌ Erro: {e}\n")

window.close()