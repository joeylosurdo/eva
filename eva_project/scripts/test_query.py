# 📁 eva/scripts/test_query.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.query import search_index, summarize_with_gpt

if __name__ == "__main__":
    q = input("Ask EVA: ")
    results = search_index(q)
    print("\nTop Results:\n")
    for match in results["matches"]:
        print(f"- {match['metadata']['document_title']}\n{match['metadata']['content'][:300]}\n")
    print("\nAnswer:\n")
    print(summarize_with_gpt(q, results["matches"]))# Dummy content for test_query.py
