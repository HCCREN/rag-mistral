# rag_mistral.py
# Full English version of a Python RAG CLI system using Mistral 7B Q6_K and FAISS

import os
import faiss
import time
import fitz  # PyMuPDF, used for PDF parsing
import numpy as np
from pathlib import Path
from llama_cpp import Llama
from sentence_transformers import SentenceTransformer

# Parameters
EMBED_MODEL_NAME = "thenlper/gte-small"  # Embedding model
GGUF_MODEL_PATH = "./models/mistral-7b-instruct-v0.2.Q6_K.gguf"  # Path to GGUF model
VECTOR_DIM = 384  # Embedding dimension (gte-small)
INDEX_PATH = "docs.index"

# Load embedding model
print("[1/5] Loading embedding model...")
embedder = SentenceTransformer(EMBED_MODEL_NAME)

# Initialize or load vector database
if os.path.exists(INDEX_PATH):
    print("[2/5] Loading vector database...")
    index = faiss.read_index(INDEX_PATH)
    with open("docs.txt", "r", encoding="utf-8") as f:
        doc_list = f.read().split("\n")
else:
    print("[2/5] Creating new vector database...")
    index = faiss.IndexFlatIP(VECTOR_DIM)
    doc_list = []

# Load the LLaMA model
print("[3/5] Launching LLaMA model...")
llm = Llama(model_path=GGUF_MODEL_PATH, n_ctx=4096, n_threads=16)

# Add document and index it
def add_document(file_path):
    print(f"[+] Adding document: {file_path}")

    if file_path.lower().endswith(".pdf"):
        print("[*] PDF detected. Parsing with PyMuPDF...")
        doc = fitz.open(file_path)
        content = ""
        for page in doc:
            content += page.get_text()
    else:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

    paragraphs = [p.strip() for p in content.split("\n") if len(p.strip()) > 30]

    if len(paragraphs) == 0:
        print("⚠️ The file does not contain any paragraph longer than 30 characters. Skipped.")
        return

    vectors = embedder.encode(paragraphs, normalize_embeddings=True)
    index.add(np.array(vectors))
    doc_list.extend(paragraphs)
    faiss.write_index(index, INDEX_PATH)
    with open("docs.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(doc_list))
    print(f"[+] Added {len(paragraphs)} new paragraphs to the vector DB.\n")

# Ask a question and get answer from LLM
def ask_question(query, top_k=3):
    q_embed = embedder.encode([query], normalize_embeddings=True)
    D, I = index.search(np.array(q_embed), top_k)
    related = [doc_list[i] for i in I[0]]
    context = "\n".join(related)
    prompt = f"The following context was retrieved:\n{context}\n\nBased on the above, answer the question: {query}"
    print("[4/5] LLM is thinking...")
    response = llm(prompt, max_tokens=512, stop=["</s>"])
    print("\n[Answer]", response["choices"][0]["text"].strip())

# CLI Interface
if __name__ == "__main__":
    while True:
        print("\n====== RAG CLI System (Mistral 7B Q6_K + FAISS) ======")
        print("1. Upload document (.txt/.pdf)")
        print("2. Ask a question")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            path = input("Enter .txt or .pdf file path: ").strip()
            if os.path.exists(path):
                add_document(path)
            else:
                print("File not found!")
        elif choice == "2":
            q = input("Enter your question: ")
            ask_question(q)
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")
