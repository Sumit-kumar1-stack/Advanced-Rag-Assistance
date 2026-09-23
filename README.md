# 📚 Advanced RAG Assistant

> A lightweight Retrieval-Augmented Generation (RAG) backend for document ingestion, semantic retrieval, and LLM-assisted question answering.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-REST%20API-000000?logo=flask&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-Vector%20DB-DC244C)
![Hugging%20Face](https://img.shields.io/badge/Hugging%20Face-Embeddings-FFD21E?logo=huggingface&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)

## Overview

This project demonstrates a compact RAG pipeline built with **Flask**, **Qdrant**, and **Hugging Face sentence-transformer embeddings**. Documents can be ingested from Google Drive, indexed as vectors, retrieved through semantic similarity, and passed to an LLM to generate context-aware answers.

## ✨ Features

- Google Drive document ingestion
- Embedding generation with Sentence Transformers
- Qdrant vector storage and semantic retrieval
- Configurable top-k retrieval
- LLM-assisted contextual answers
- REST endpoints for ingestion, health checks, and question answering
- Docker-based local setup

## 🧰 Tech Stack

| Area | Technology |
|---|---|
| API | Flask, Gunicorn |
| Vector database | Qdrant |
| Embeddings | Hugging Face Sentence Transformers |
| LLM layer | OpenAI / Transformers-compatible integration |
| Cloud connector | Google Drive API |
| Local infrastructure | Docker Compose |

## 🏗️ Architecture

```text
Google Drive / Documents
        │
        ▼
   Ingestion Layer
        │
        ▼
Sentence-Transformer Embeddings
        │
        ▼
      Qdrant
        │
        ▼
 Semantic Retrieval
        │
        ▼
   Relevant Context
        │
        ▼
       LLM
        │
        ▼
 Context-aware Answer
```

## 📂 Project Structure

```text
.
├── app.py
├── config.py
├── connectors/
├── rag/
│   ├── ingest.py
│   ├── retriever.py
│   └── llm.py
├── docker-compose.yml
├── requirements.txt
└── .env
```

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Sumit-kumar1-stack/Advanced-Rag-Assistance.git
cd Advanced-Rag-Assistance
```

### 2. Create a virtual environment

**Windows**

```bat
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

**macOS / Linux**

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file using values appropriate for your environment:

```env
QDRANT_URL=http://qdrant:6333
QDRANT_COLLECTION=rag_mini
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
TOP_K=5
OPENAI_API_KEY=your_openai_api_key
GOOGLE_SA_PATH=./service_account.json
DRIVE_FOLDER_ID=your_google_drive_folder_id
```

> Never commit real API keys, service-account credentials, or private document identifiers.

### 4. Start the services

```bash
docker compose up
```

## 🔌 Example API Usage

Health check:

```bash
curl http://localhost:8000/health
```

Ingest a Google Drive folder:

```bash
curl -X POST http://localhost:8000/ingest \
  -H "Content-Type: application/json" \
  -d '{"folder_id":"your_google_drive_folder_id"}'
```

Ask a question:

```bash
curl "http://localhost:8000/ask?query=What%20is%20inside%20the%20documents%3F"
```

## 💡 What This Project Demonstrates

- Retrieval-Augmented Generation fundamentals
- Vector-database integration
- Semantic search
- External document ingestion
- LLM orchestration behind an API
- Environment-based configuration
- Containerized local development

## 🤝 Contributing

Issues and pull requests are welcome. If you want to extend the project, useful areas include document parsing, metadata-aware retrieval, evaluation, reranking, caching, observability, and additional data-source connectors.

## ⚠️ Notes

RAG quality depends on document quality, chunking, embeddings, retrieval configuration, and the selected LLM. Validate answers against source material before using the system for high-stakes decisions.
