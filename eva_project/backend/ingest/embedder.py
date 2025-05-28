import openai
import pinecone
from uuid import uuid4
from backend.config import OPENAI_API_KEY, PINECONE_API_KEY, PINECONE_ENV, PINECONE_INDEX
from openai import OpenAI
from pinecone import Pinecone

client = OpenAI(api_key=OPENAI_API_KEY)

openai.api_key = OPENAI_API_KEY
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)

def embed_text(text):
    response = client.embeddings.create(input=text, model="text-embedding-3-large")
    return response.data[0].embedding

def upsert_chunks(chunks, metadata):
    for i, chunk in enumerate(chunks):
        try:
            embedding = embed_text(chunk)
            vector_id = str(uuid4())
            index.upsert([{
                "id": vector_id,
                "values": embedding,
                "metadata": {
                    **metadata,
                    "chunk_index": i,
                    "content": chunk
                }
            }])
        except Exception as e:
            print(f"⚠️ Error on chunk {i}: {e}")# Dummy content for embedder.py
