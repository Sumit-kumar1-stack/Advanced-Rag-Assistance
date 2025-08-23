import sys
from rich.console import Console
from rich.panel import Panel
from app.vectorstores.factory import load_vectorstore
from app.retrievers.simple import get_retriever
from app.chains.qa import build_qa_chain

console = Console()

def main():
    vs = load_vectorstore()
    if not vs:
        console.print("[red]Index not found. Run: python -m scripts.ingest[/red]")
        sys.exit(1)
    qa = build_qa_chain(get_retriever(vs))
    console.print(Panel.fit("Advanced RAG — type 'exit' to quit", title="Module 1+"))
    while True:
        q = console.input("[bold cyan]> [/bold cyan]").strip()
        if q.lower() in {"exit","quit","q"}:
            break
        res = qa({"query": q})
        console.print("\n[bold]Answer:[/bold]")
        console.print(res.get("result",""))
        srcs = res.get("source_documents", [])
        if srcs:
            console.print("\n[bold]Sources:[/bold]")
            for i, d in enumerate(srcs, 1):
                console.print(f"{i}. {d.metadata.get('source','unknown')}")
        console.print()

if __name__ == "__main__":
    main()