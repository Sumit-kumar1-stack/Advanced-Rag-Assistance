# 📚 RAG-MINI: Retrieval-Augmented Generation Assistant

A lightweight Retrieval-Augmented Generation (RAG) system built with **Flask**, **Qdrant**, and **Hugging Face** to enable document ingestion, semantic search, and LLM-powered question answering.  

---

## 🚀 Features
- 🔹 Ingest documents from **Google Drive** (PDFs, text, etc.)
- 🔹 Store and manage embeddings in **Qdrant vector database**
- 🔹 Perform **semantic search** to retrieve relevant context
- 🔹 Use **LLMs (OpenAI / Hugging Face)** to generate contextual answers
- 🔹 Simple REST API endpoints for integration

---

## 🛠️ Tech Stack
- **Backend:** Flask + Gunicorn  
- **Vector Database:** Qdrant  
- **ML/Embeddings:** Hugging Face Sentence Transformers  
- **LLM:** OpenAI GPT / Transformers  
- **Cloud Connector:** Google Drive API  

---

## 📂 Project Structure
rag-mini/
│── app.py # Flask app with REST endpoints
│── config.py # Configuration and environment variables
│── connectors/ # Google Drive connector
│── rag/
│ ├── ingest.py # Document ingestion pipeline
│ ├── retriever.py # Semantic search
│ └── llm.py # Answer generation with LLM
│── docker-compose.yml # Qdrant + App services
│── requirements.txt # Dependencies
│── .env # API keys & configs


---

## ⚡ Quick Start

### 1️⃣ Clone the repo
bash
git clone https://github.com/your-username/rag-mini.git
cd rag-mini

Setup environment
python -m venv env
source env/bin/activate   # On Windows: .\env\Scripts\activate
pip install -r requirements.txt

3️⃣ Start with Docker
docker-compose up

4️⃣ Test API

Health check:

curl http://localhost:8000/health


Ingest Google Drive folder:

curl -X POST http://localhost:8000/ingest \
     -H "Content-Type: application/json" \
     -d '{"folder_id":"your_google_drive_folder_id"}'


Ask a question:

curl "http://localhost:8000/ask?query=What is inside the documents?"

🔑 Environment Variables (.env)
QDRANT_URL=http://qdrant:6333
QDRANT_COLLECTION=rag_mini
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
TOP_K=5
OPENAI_API_KEY=your_openai_api_key
GOOGLE_SA_PATH=./service_account.json
DRIVE_FOLDER_ID=your_google_drive_folder_id

