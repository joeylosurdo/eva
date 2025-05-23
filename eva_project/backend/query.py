# 📁 eva/backend/query.py
import openai
from backend.config import OPENAI_API_KEY, PINECONE_API_KEY, PINECONE_ENV, PINECONE_INDEX
import pinecone

openai.api_key = OPENAI_API_KEY
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
index = pinecone.Index(PINECONE_INDEX)

def embed_query(query):
    result = openai.Embedding.create(input=query, model="text-embedding-3-large")
    return result["data"][0]["embedding"]

def search_index(query, top_k=5, filters=None):
    vector = embed_query(query)
    results = index.query(vector=vector, top_k=top_k, include_metadata=True, filter=filters)
    return results

def summarize_with_gpt(query, matches):
    context = "\n\n---\n\n".join([f"{m['metadata']['content']}" for m in matches])
    prompt = f"""You are Embark's assistant. Based on the internal knowledge below, answer the user's question.

User: {query}

Knowledge:
{context}

Answer:"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response["choices"][0]["message"]["content"]# Dummy content for query.py
