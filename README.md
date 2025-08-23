# Advanced RAG Assistant (Module 1+)

A production-ready RAG starter featuring:
- TXT/PDF ingestion
- FAISS or Chroma vector store (configurable)
- HuggingFace or OpenAI embeddings
- Multi-query retrieval (RAG-Fusion style)
- Guardrails: confidence threshold → “I don’t know”
- Streamlit chat UI + FastAPI server
- Dockerfile + docker-compose
- Simple retrieval evaluation

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env (choose LLM/embeddings, add OPENAI_API_KEY if needed)

# Add your docs
mkdir -p data/raw
# (place .txt/.pdf here)

# Ingest
python -m scripts.ingest

# CLI
python -m scripts.chat_cli

# Streamlit UI
streamlit run ui/streamlit_app.py

# FastAPI
uvicorn app.server.api:app --reload
```

### Docker
```bash
docker build -t rag-assistant .
docker run --env-file .env -p 8501:8501 -p 8000:8000 -v $(pwd)/data:/app/data -v $(pwd)/vectorstore:/app/vectorstore rag-assistant
# or with compose
docker-compose up --build
```

## Structure
```text
app/
  config.py          # settings + factories
  llm/factory.py     # OpenAI or Ollama chat
  vectorstores/factory.py  # FAISS or Chroma
  retrievers/simple.py     # basic retriever
  retrievers/fusion.py     # multi-query RAG-fusion retriever
  chains/qa.py        # QA chain w/ guardrails
  indexers/build_index.py  # ingestion orchestration
  server/api.py       # FastAPI routes
  utils/eval.py       # tiny retrieval eval
ui/
  streamlit_app.py    # minimal chat UI w/ history + sources
scripts/
  ingest.py           # CLI wrapper to ingest
  chat_cli.py         # CLI chat with sources
  eval_retrieval.py   # runs the simple eval
data/raw/             # your docs
data/eval/qas.jsonl   # sample eval set
```