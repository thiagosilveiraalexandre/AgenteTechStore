# ============================================================
# app.py
# Ponto de entrada da aplicação.
# Cria uma interface gráfica (GUI) com PySimpleGUI para o
# Agente Inteligente TechStore, permitindo conversação com o
# agente e exibição do histórico de mensagens.
# ============================================================

import PySimpleGUI as sg
from agents.sales_agent import SalesAgent

# ============================================================
# 1. CONFIGURAÇÃO DA INTERFACE
# ============================================================

# Define o tema visual da janela (escuro com tons azuis)
sg.theme("DarkBlue3")

# ------------------------------------------------------------
# Layout da janela (organização dos elementos)
# ------------------------------------------------------------
# Cada linha da lista é uma linha horizontal na janela.
# Usamos sg.Push() para centralizar elementos e expand_x/expand_y
# para tornar o layout responsivo ao redimensionamento.
layout = [
    # Linha 0: Título centralizado
    [sg.Push(), sg.Text("🤖 Agente Inteligente TechStore", font=("Helvetica", 16)), sg.Push()],

    # Linha 1: Área de histórico (multiline) – expande em ambas as direções
    [sg.Multiline(
        size=(None, None),          # Tamanho automático, controlado por expand_x/expand_y
        key="-HISTORICO-",          # Chave para acessar este elemento
        autoscroll=True,            # Rolagem automática para novas mensagens
        disabled=True,              # Impede edição pelo usuário
        background_color="#2d2d2d", # Cor de fundo escura
        text_color="white",         # Texto branco para contraste
        expand_x=True,              # Expande horizontalmente com a janela
        expand_y=True               # Expande verticalmente com a janela
    )],

    # Linha 2: Campo de entrada e botões
    [
        sg.Text("Você:", size=(6, 1)),                 # Rótulo fixo
        sg.Input(
            size=(None, 1),          # Largura automática (expansível)
            key="-INPUT-",           # Chave para acessar o input
            focus=True,              # Foco inicial no campo
            expand_x=True            # Expande horizontalmente com a janela
        ),
        sg.Button("Enviar", bind_return_key=True),     # Botão ativado pela tecla Enter
        sg.Button("Sair")                              # Botão para fechar
    ]
]

# ------------------------------------------------------------
# Criação da janela
# ------------------------------------------------------------
# resizable=True permite redimensionar a janela.
# finalize=True permite chamar maximize() após a criação.
# size=(800,600) define o tamanho inicial antes de maximizar.
window = sg.Window("TechStore Agent", layout, resizable=True, finalize=True, size=(800, 600))
window.Maximize()  # Maximiza a janela ao abrir (funciona em todas as versões)

# ============================================================
# 2. INICIALIZAÇÃO DO AGENTE
# ============================================================

agent = SalesAgent()  # Cria a instância do agente (que já carrega LLM, router e retriever)

# ============================================================
# 3. LOOP PRINCIPAL DE EVENTOS
# ============================================================

while True:
    # Aguarda um evento (ação do usuário) e retorna os valores dos campos
    event, values = window.read()

    # Se o usuário fechou a janela ou clicou em "Sair", encerra o loop
    if event in (sg.WIN_CLOSED, "Sair"):
        break

    # Se o evento foi "Enviar" (ou Enter, devido ao bind_return_key)
    if event == "Enviar":
        # Obtém a pergunta do campo de input e remove espaços extras
        pergunta = values["-INPUT-"].strip()

        # Se a pergunta estiver vazia, ignora e espera nova entrada
        if not pergunta:
            continue

        # Exibe a pergunta no histórico (com emoji e cor)
        window["-HISTORICO-"].print(f"🧑 Você: {pergunta}")

        # Limpa o campo de input para a próxima pergunta
        window["-INPUT-"].update("")

        # Tenta obter a resposta do agente
        try:
            resposta = agent.responder(pergunta)
            # Exibe a resposta no histórico (com emoji de IA)
            window["-HISTORICO-"].print(f"🤖 IA: {resposta}\n")
        except Exception as e:
            # Em caso de erro, exibe mensagem de erro no histórico
            window["-HISTORICO-"].print(f"❌ Erro: {e}\n")

# ============================================================
# 4. FINALIZAÇÃO
# ============================================================

# Fecha a janela ao sair do loop
window.close()