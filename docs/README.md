# Agente Inteligente TechStore

## Sobre o projeto

Este é um agente inteligente para atendimento ao cliente da TechStore, desenvolvido em Python com interface grafica (GUI) utilizando PySimpleGUI.

O agente e capaz de:
- Classificar a intencao da pergunta do usuario (produto, pedido, cliente, politica, conversa ou fora do escopo).
- Responder perguntas sobre produtos e politicas com base em documentos PDF (utilizando RAG - Retrieval-Augmented Generation).
- Fornecer respostas amigaveis e contextuais, utilizando um modelo de linguagem (LLM) via OpenRouter.

tem como você ver ele funcionando em 
https://agente-tech-store--thiagosilveir12.replit.app

<img width="1416" height="511" alt="print funcionando" src="https://github.com/user-attachments/assets/1379b160-434f-40c8-8c74-b8a3960e2728" />

## Tecnologias utilizadas

| Componente | Tecnologia |
| :--- | :--- |
| Linguagem | Python 3.14 |
| Interface grafica | PySimpleGUI |
| Framework RAG | LangChain |
| Vector Store | ChromaDB |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| LLM | OpenRouter (modelo inclusionai/ling-3.0-flash:free) |
| Gerenciamento de dependencias | pip + requirements.txt |
| Versionamento | Git + GitHub |

## Pre-requisitos

Antes de executar o projeto, voce precisara ter instalado:

- Python 3.10+
- Pip (gerenciador de pacotes do Python)
- Uma chave de API do OpenRouter (gratuita). Cadastre-se em openrouter.ai e obtenha sua chave.

## Instalacao e configuracao

### 1. Clone o repositorio

```bash
git clone https://github.com/thiagosilveiraalexandre/AgenteTechStore.git
cd AgenteTechStore

