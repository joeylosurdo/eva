# 📁 eva/scripts/bootstrap_index.py
from backend.ingest.drive_ingest import list_drive_files, download_file
from backend.ingest.extract_text import extract_text_from_file
from backend.ingest.chunker import chunk_text
from backend.ingest.embedder import upsert_chunks
import os

def run_index():
    files = list_drive_files()
    for file in files:
        name = file["name"]
        file_id = file["id"]
        ext = os.path.splitext(name)[-1].lower()
        if ext not in [".pdf", ".docx", ".txt"]:
            continue
        download_file(file_id, name)
        text = extract_text_from_file(name)
        chunks = chunk_text(text)
        metadata = {"document_title": name, "document_type": ext.lstrip("."), "source": "GDrive"}
        upsert_chunks(chunks, metadata)
        os.remove(name)

if __name__ == "__main__":
    run_index()# Dummy content for bootstrap_index.py
