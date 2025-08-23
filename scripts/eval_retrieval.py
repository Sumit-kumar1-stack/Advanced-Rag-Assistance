from app.utils.eval import evaluate_retrieval
if __name__ == "__main__":
    m = evaluate_retrieval("data/eval/qas.jsonl", k=4)
    print(m)