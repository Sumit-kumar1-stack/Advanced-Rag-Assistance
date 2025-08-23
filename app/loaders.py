import os
from typing import List
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.schema import Document

def load_documents_from_dir(directory: str) -> List[Document]:
    docs: List[Document] = []
    for root, _, files in os.walk(directory):
        for fname in files:
            path = os.path.join(root, fname)
            ext = os.path.splitext(fname)[1].lower()
            if ext in [".txt", ".md"]:
                docs.extend(TextLoader(path, encoding="utf-8").load())
            elif ext == ".pdf":
                docs.extend(PyPDFLoader(path).load())
    for d in docs:
        d.metadata["source"] = d.metadata.get("source") or d.metadata.get("file_path") or d.metadata.get("source", path)
    return docs