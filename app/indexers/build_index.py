from tqdm import tqdm
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config import settings
from app.loaders import load_documents_from_dir
from app.vectorstores.factory import build_from_documents, save_vectorstore

def build_index():
    print(f"[ingest] Loading from: {settings.data_dir}")
    docs = load_documents_from_dir(settings.data_dir)
    if not docs:
        print("[ingest] No documents found. Put files into data/raw and re-run.")
        return False
    print(f"[ingest] Loaded {len(docs)} docs. Splitting...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=80)
    chunks = splitter.split_documents(docs)
    print(f"[ingest] {len(chunks)} chunks. Building vector store...")
    vs = build_from_documents(chunks)
    print("[ingest] Saving vector store...")
    save_vectorstore(vs)
    print("[ingest] Done.")
    return True