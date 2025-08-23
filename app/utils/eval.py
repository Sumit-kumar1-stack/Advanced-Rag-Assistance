import json, os
from typing import List, Dict
from app.vectorstores.factory import load_vectorstore

# Very small illustrative retrieval eval (recall@k based on naive keyword match)
def evaluate_retrieval(qas_path: str, k: int = 4) -> Dict[str, float]:
    vs = load_vectorstore()
    if not vs:
        raise RuntimeError("Vector store not loaded. Run ingestion first.")
    with open(qas_path, "r", encoding="utf-8") as f:
        lines = [json.loads(x) for x in f if x.strip()]
    ok = 0
    for ex in lines:
        q = ex["question"]
        gold_kw = ex.get("keyword")
        docs = vs.similarity_search(q, k=k)
        retrieved_text = " ".join([d.page_content for d in docs]).lower()
        if gold_kw and gold_kw.lower() in retrieved_text:
            ok += 1
    return {"recall@k": ok/len(lines) if lines else 0.0, "n": len(lines)}