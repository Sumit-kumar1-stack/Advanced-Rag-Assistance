from fastapi import FastAPI
from pydantic import BaseModel
from app.vectorstores.factory import load_vectorstore
from app.retrievers.simple import get_retriever
from app.chains.qa import build_qa_chain

app = FastAPI(title="RAG Assistant API")

class Query(BaseModel):
    question: str

vs = load_vectorstore()
if vs:
    qa = build_qa_chain(get_retriever(vs))
else:
    qa = None

@app.get("/health")
def health():
    return {"status": "ok", "vectorstore_loaded": bool(vs)}

@app.post("/ask")
def ask(q: Query):
    if not qa:
        return {"error": "Vector store not loaded. Run ingestion first."}
    res = qa({"query": q.question})
    out = {
        "answer": res.get("result", ""),
        "sources": [d.metadata.get("source","unknown") for d in res.get("source_documents", [])]
    }
    return out