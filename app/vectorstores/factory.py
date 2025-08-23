import os
from typing import Optional
from app.config import settings
from app.llm.factory import get_embeddings

def build_from_documents(documents):
    backend = settings.vectorstore_backend.lower()
    embeddings = get_embeddings()
    if backend == "faiss":
        from langchain_community.vectorstores import FAISS
        return FAISS.from_documents(documents, embeddings)
    elif backend == "chroma":
        from langchain_community.vectorstores import Chroma
        return Chroma.from_documents(documents, embeddings)
    else:
        raise ValueError(f"Unsupported VECTORSTORE_BACKEND: {backend}")

def save_vectorstore(vs):
    backend = settings.vectorstore_backend.lower()
    os.makedirs(settings.vectorstore_dir, exist_ok=True)
    if backend == "faiss":
        vs.save_local(settings.vectorstore_dir)
    elif backend == "chroma":
        # Chroma persists automatically if persist_directory is set on creation;
        # for simplicity we rebuild when loading.
        pass

def load_vectorstore() -> Optional[object]:
    backend = settings.vectorstore_backend.lower()
    embeddings = get_embeddings()
    if backend == "faiss":
        from langchain_community.vectorstores import FAISS
        if not os.path.isdir(settings.vectorstore_dir):
            return None
        return FAISS.load_local(settings.vectorstore_dir, embeddings, allow_dangerous_deserialization=True)
    elif backend == "chroma":
        from langchain_community.vectorstores import Chroma
        # If directory empty, return None
        if not os.path.isdir(settings.vectorstore_dir):
            return None
        return Chroma(persist_directory=settings.vectorstore_dir, embedding_function=embeddings)
    else:
        raise ValueError(f"Unsupported VECTORSTORE_BACKEND: {backend}")