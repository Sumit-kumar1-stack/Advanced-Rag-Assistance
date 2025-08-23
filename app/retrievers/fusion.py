from typing import List
from app.config import settings
from app.llm.factory import get_chat_llm

def multi_query_expand(question: str, n: int) -> List[str]:
    """Use the LLM to generate alternative phrasings of the query."""
    prompt = f"""Generate {n} distinct alternative queries that capture different angles of the user's question.
    Original: {question}
    Return as a numbered list without explanations."""
    llm = get_chat_llm()
    resp = llm.invoke(prompt).content
    queries = []
    for line in resp.splitlines():
        line = line.strip()
        if not line: 
            continue
        if line[0].isdigit() and "." in line[:3]:
            line = line.split(".",1)[1].strip()
        queries.append(line)
    if not queries:
        queries = [question]
    return queries[:n]

def rag_fusion_retrieve(vectorstore, question: str):
    """Simple RAG-Fusion: expand query, retrieve for each, then re-rank by frequency/score."""
    queries = [question] + multi_query_expand(question, settings.fusion_queries)
    all_docs = []
    for q in queries:
        all_docs.extend(vectorstore.similarity_search_with_score(q, k=settings.top_k))
    # Deduplicate by page_content
    seen = {}
    for doc, score in all_docs:
        key = doc.page_content[:200]
        if key not in seen or score < seen[key][1]:
            seen[key] = (doc, score)
    # Sort by score (lower is better for distance metrics used by FAISS)
    ranked = sorted(seen.values(), key=lambda x: x[1])
    return [d for d, s in ranked[:settings.top_k]]