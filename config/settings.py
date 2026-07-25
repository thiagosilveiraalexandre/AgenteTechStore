# ============================================================
# config/settings.py
# Centraliza todas as configurações do projeto.
# ============================================================

import os
from dotenv import load_dotenv

# ------------------------------------------------------------
# 1. CARREGAR VARIÁVEIS DE AMBIENTE
# ------------------------------------------------------------
# O arquivo .env contém credenciais e configurações sensíveis
# que NÃO devem ser versionadas no GitHub.
load_dotenv()  # Procura por um arquivo .env na raiz do projeto


# ------------------------------------------------------------
# 2. CONFIGURAÇÕES DA LLM (OpenRouter)
# ------------------------------------------------------------

# Chave de API para autenticação no OpenRouter (obtida do .env)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Nome do modelo de linguagem utilizado.
# "inclusionai/ling-3.0-flash:free" é um modelo gratuito disponível no OpenRouter.
# Pode ser alterado para outros modelos pagos ou mais especializados.
MODEL_NAME = "inclusionai/ling-3.0-flash:free"

# Temperatura controla a criatividade das respostas.
# 0 = respostas mais determinísticas e objetivas (recomendado para chatbot de vendas).
# Valores mais altos (0.7~1.0) geram respostas mais criativas, mas menos precisas.
TEMPERATURE = 0

# URL base da API do OpenRouter (não alterar a menos que mude de provedor).
BASE_URL = "https://openrouter.ai/api/v1"


# ------------------------------------------------------------
# 3. CAMINHOS DE DIRETÓRIOS E ARQUIVOS DO PROJETO
# ------------------------------------------------------------

# Diretório base do projeto (onde este arquivo está, subindo dois níveis)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho para a pasta docs/ (onde fica o README.md e requirements.txt)
DOCS_PATH = os.path.join(BASE_DIR, "docs")

# Caminho para a pasta vectorstore/ (onde será salvo o índice vetorial do RAG)
VECTORSTORE_PATH = os.path.join(BASE_DIR, "vectorstore")

