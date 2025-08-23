from app.config import settings

def get_retriever(vectorstore):
    return vectorstore.as_retriever(search_kwargs={"k": settings.top_k})