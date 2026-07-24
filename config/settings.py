import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# ============================
# CONFIGURAÇÕES DA LLM
# ============================

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL_NAME = "inclusionai/ling-3.0-flash:free"

TEMPERATURE = 0

# URL da API do OpenRouter
BASE_URL = "https://openrouter.ai/api/v1"

# ============================
# CAMINHOS DO PROJETO
# ============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOCS_PATH = os.path.join(BASE_DIR, "docs")
VECTORSTORE_PATH = os.path.join(BASE_DIR, "vectorstore")
DATABASE_PATH = os.path.join(BASE_DIR, "database", "loja.db")