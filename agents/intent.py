from enum import Enum


class Intent(Enum):
    """
    Enum com todas as intenções possíveis do agente.
    """

    PRODUTO = "PRODUTO"
    PEDIDO = "PEDIDO"
    CLIENTE = "CLIENTE"
    POLITICA = "POLITICA"
    CONVERSA = "CONVERSA"
    FORA_DO_ESCOPO = "FORA_DO_ESCOPO"