from app.config import settings

def get_chat_llm():
    prov = settings.llm_provider.lower()
    if prov == "openai":
        from langchain_openai import ChatOpenAI
        if not settings.openai_api_key:
            raise ValueError("OPENAI_API_KEY is required for OpenAI LLM.")
        return ChatOpenAI(model=settings.llm_model, temperature=0, api_key=settings.openai_api_key)
    elif prov == "ollama":
        from langchain_community.chat_models import ChatOllama
        return ChatOllama(model=settings.ollama_model, temperature=0)
    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {prov}")

def get_embeddings():
    if settings.embeddings_provider.lower() == "openai":
        from langchain_openai import OpenAIEmbeddings
        if not settings.openai_api_key:
            raise ValueError("OPENAI_API_KEY is required for OpenAI embeddings.")
        return OpenAIEmbeddings(model=settings.openai_embeddings_model, api_key=settings.openai_api_key)
    else:
        from langchain_community.embeddings import HuggingFaceEmbeddings
        return HuggingFaceEmbeddings(model_name=settings.hf_embeddings_model)