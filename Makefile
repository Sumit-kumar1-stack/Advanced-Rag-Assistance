.PHONY: venv install ingest chat ui api docker up

venv:
	python -m venv .venv

install:
	pip install -r requirements.txt

ingest:
	python -m scripts.ingest

chat:
	python -m scripts.chat_cli

ui:
	streamlit run ui/streamlit_app.py

api:
	uvicorn app.server.api:app --reload

docker:
	docker build -t rag-assistant .

up:
	docker-compose up --build