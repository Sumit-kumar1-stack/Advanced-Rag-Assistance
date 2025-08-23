
import streamlit as st
import time
from app.vectorstores.factory import load_vectorstore
from app.retrievers.simple import get_retriever
from app.retrievers.fusion import rag_fusion_retrieve
from app.chains.qa import build_qa_chain
from app.config import settings

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="⚡ Advanced RAG Assistant",
    layout="wide",
    page_icon="🔎",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Sidebar (Branding & Settings)
# ---------------------------
with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=150)
    st.title("⚡ RAG Assistant")
    st.caption("Next-Gen Retrieval Augmented Generation")

    mode = st.radio("📌 Retrieval Mode", ["Simple (k)", "RAG-Fusion (multi-query)"])
    answer_style = st.selectbox("✍️ Answer Style", ["Concise", "Detailed", "Bullet Points"])
    show_confidence = st.checkbox("Show confidence score", True)

    if st.button("🧹 Clear Chat"):
        st.session_state.history = []

    st.markdown("---")
    st.caption("Made with ❤️ using Streamlit & LangChain")

# ---------------------------
# Main UI
# ---------------------------
st.title("🔎 Advanced RAG Assistant")
st.caption("Ask questions from your documents like a pro!")

# Vectorstore
vs = load_vectorstore()
if not vs:
    st.error("❌ Vector store not found. Run ingestion first: `python -m scripts.ingest`")
    st.stop()

# Session State for history
if "history" not in st.session_state:
    st.session_state.history = []

# User Input
question = st.text_input("💬 Ask a question")
ask = st.button("🚀 Ask")

# ---------------------------
# Helper: Typing Animation
# ---------------------------
def render_answer(answer: str):
    placeholder = st.empty()
    output = ""
    for ch in answer:
        output += ch
        placeholder.markdown(f"**Assistant:** {output}▌")
        time.sleep(0.01)
    placeholder.markdown(f"**Assistant:** {output}")

# ---------------------------
# Processing Question
# ---------------------------
if ask and question.strip():
    with st.spinner("🔍 Retrieving answer..."):
        if mode.startswith("Simple"):
            qa = build_qa_chain(get_retriever(vs))
            res = qa({"query": question})
            answer = res.get("result", "")
            sources = [d.metadata.get("source", "unknown") for d in res.get("source_documents", [])]
        else:
            docs = rag_fusion_retrieve(vs, question)
            qa = build_qa_chain(vs.as_retriever(search_kwargs={"k": settings.top_k}))
            context = "\n\n".join([d.page_content for d in docs])
            res = qa.combine_documents_chain.run(input_documents=docs, question=question)
            answer = res
            sources = [d.metadata.get("source", "unknown") for d in docs]

        # Confidence score (dummy example: length-based)
        confidence = min(100, len(answer) // 5) if show_confidence else None

        # Adjust answer style
        if answer_style == "Bullet Points":
            answer = "\n".join([f"- {line}" for line in answer.split(".") if line.strip()])
        elif answer_style == "Concise":
            answer = answer.split(".")[0] + "."

        st.session_state.history.append((question, answer, sources, confidence))

# ---------------------------
# Display Chat History
# ---------------------------
for q, a, s, conf in st.session_state.history[::-1]:
    st.markdown(f"**🧑 You:** {q}")
    render_answer(a)

    if conf:
        st.progress(conf / 100)
        st.caption(f"Confidence: {conf}%")

    if s:
        with st.expander("📂 Sources"):
            for i, src in enumerate(s, 1):
                st.info(f"{i}. {src}")
    st.markdown("---")

# ---------------------------
# Download Chat Option
# ---------------------------
if st.session_state.history:
    import pandas as pd
    df = pd.DataFrame(st.session_state.history, columns=["Question", "Answer", "Sources", "Confidence"])
    st.download_button("📥 Download Chat (CSV)", df.to_csv(index=False), "chat_history.csv", "text/csv")
