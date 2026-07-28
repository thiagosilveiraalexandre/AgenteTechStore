from enum import Enum

class Intent(Enum):
    """
    Enum com todas as intenções possíveis do agente.
    Usado para classificar a pergunta do usuário e direcionar para a lógica correta.
    """
    PRODUTO = "PRODUTO"          # Dúvidas sobre produtos, preços, estoque
    PEDIDO = "PEDIDO"            # Acompanhamento, cancelamento, rastreio
    CLIENTE = "CLIENTE"          # Cadastro, dados pessoais, login
    POLITICA = "POLITICA"        # Garantia, troca, devolução, prazos
    CONVERSA = "CONVERSA"        # Saudação, agradecimento, conversa fiada
    RELATORIO = "RELATORIO"      
    FORA_DO_ESCOPO = "FORA_DO_ESCOPO"  # Assuntos não relacionados