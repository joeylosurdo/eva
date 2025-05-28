import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "").strip()
PINECONE_ENV = os.getenv("PINECONE_ENV", "").strip()
PINECONE_INDEX = os.getenv("PINECONE_INDEX", "").strip()

print(f"[CONFIG] PINECONE_ENV: {repr(PINECONE_ENV)}")
print(f"[CONFIG] PINECONE_INDEX: {repr(PINECONE_INDEX)}")

# --- Re-add search_index and summarize_with_gpt for test_query.py ---
from openai import OpenAI
from pinecone import Pinecone

client = OpenAI(api_key=OPENAI_API_KEY)
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)

def search_index(query, top_k=5, filters=None):
    embedding = client.embeddings.create(input=query, model="text-embedding-3-large")
    vector = embedding.data[0].embedding
    results = index.query(vector=vector, top_k=top_k, include_metadata=True, filter=filters)
    return results

def summarize_with_gpt(query, matches):
    context = "\n\n---\n\n".join([m['metadata']['content'] for m in matches])
    prompt = f"""You are Embark's internal AI assistant. Answer the question below using the following internal knowledge context.

    Question: {query}

    Context:
    {context}

    Answer:"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content
