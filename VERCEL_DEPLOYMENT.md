# Vercel Deployment

The repository now exposes the existing FastAPI application through `api/index.py`.

## Project configuration

- Repository: `Advanced-Rag-Assistance`
- Root Directory: `./`
- Framework: Python / FastAPI
- Production branch: `main`

## Recommended environment variables

```env
LLM_PROVIDER=openai
LLM_MODEL=gpt-4o-mini
EMBEDDINGS_PROVIDER=openai
OPENAI_API_KEY=<secret>
OPENAI_EMBEDDINGS_MODEL=text-embedding-3-small
VECTORSTORE_BACKEND=faiss
TOP_K=4
```

The current project stores its vector index on the local filesystem. That is fine for local development, but a production RAG deployment should use a durable external vector store or package a read-only index into the deployment artifact.

For a lightweight showcase deployment, the health endpoint can run even when no vector store is loaded. The question-answering endpoint will report that ingestion is required until a usable index is available.

## Verify

1. `/health` responds successfully.
2. Secrets are stored only in Vercel environment variables.
3. Cold starts are acceptable for the selected embedding provider.
4. The vector-store strategy is durable before enabling real production ingestion.
5. `/ask` returns a controlled error when no index is available.
