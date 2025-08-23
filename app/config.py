import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    llm_provider: str = os.getenv("LLM_PROVIDER", "openai")
    llm_model: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "llama3.1")

    embeddings_provider: str = os.getenv("EMBEDDINGS_PROVIDER", "huggingface")
    hf_embeddings_model: str = os.getenv("HF_EMBEDDINGS_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    openai_embeddings_model: str = os.getenv("OPENAI_EMBEDDINGS_MODEL", "text-embedding-3-small")

    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")

    vectorstore_backend: str = os.getenv("VECTORSTORE_BACKEND", "faiss")
    top_k: int = int(os.getenv("TOP_K", "4"))
    fusion_queries: int = int(os.getenv("FUSION_QUERIES", "3"))
    min_similarity: float = float(os.getenv("MIN_SIMILARITY", "0.25"))

    data_dir: str = os.getenv("DATA_DIR", "data/raw")
    vectorstore_dir: str = os.getenv("VECTORSTORE_DIR", "vectorstore/index")

settings = Settings()