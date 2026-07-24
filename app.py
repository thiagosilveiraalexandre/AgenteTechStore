import PySimpleGUI as sg
from agents.sales_agent import SalesAgent

sg.theme("DarkBlue3")

# Layout responsivo
layout = [
    [sg.Push(), sg.Text("🤖 Agente Inteligente TechStore", font=("Helvetica", 16)), sg.Push()],
    [sg.Multiline(
        size=(None, None),
        key="-HISTORICO-",
        autoscroll=True,
        disabled=True,
        background_color="#2d2d2d",
        text_color="white",
        expand_x=True,
        expand_y=True
    )],
    [sg.Text("Você:", size=(6,1)),
     sg.Input(size=(None, 1), key="-INPUT-", focus=True, expand_x=True),
     sg.Button("Enviar", bind_return_key=True),
     sg.Button("Sair")]
]

window = sg.Window("TechStore Agent", layout, resizable=True, finalize=True, size=(800, 600))
window.Maximize()  # Atenção: 'M' maiúsculo (funciona em todas as versões)

agent = SalesAgent()

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Sair"):
        break
    if event == "Enviar":
        pergunta = values["-INPUT-"].strip()
        if not pergunta:
            continue
        window["-HISTORICO-"].print(f"🧑 Você: {pergunta}")
        window["-INPUT-"].update("")
        try:
            resposta = agent.responder(pergunta)
            window["-HISTORICO-"].print(f"🤖 IA: {resposta}\n")
        except Exception as e:
            window["-HISTORICO-"].print(f"❌ Erro: {e}\n")

window.close()