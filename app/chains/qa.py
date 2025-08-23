from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from app.config import settings
from app.llm.factory import get_chat_llm

DEFAULT_PROMPT = PromptTemplate.from_template(
    """You are a helpful assistant that answers **only** using the provided context.
    If the answer is not contained in the context, say: "I don't know based on the documents."

    Question: {question}
    Context:
    {context}
    """)

def build_qa_chain(retriever):
    llm = get_chat_llm()
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": DEFAULT_PROMPT},
    )
    return chain

def is_confident(result) -> bool:
    # If your vector store returns similarity scores, you could add them here.
    # For FAISS via RetrievalQA, we'll rely on presence of sources; downstream UIs can set a threshold.
    # This placeholder always returns True; keep MIN_SIMILARITY for custom logic if you attach scores.
    return True