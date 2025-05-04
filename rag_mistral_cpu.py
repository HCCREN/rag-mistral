# rag_mistral.py (code version)
# 強化版：RecursiveChunk + Summary + Metadata Embedding

import os
import fitz  # PyMuPDF
import faiss
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from llama_cpp import Llama

# Load components
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")  # lightweight summarizer
llm = Llama(model_path="C://Ren//python//env//huggingface_LLM_Model//models//mistral-7b-instruct-v0.2.Q6_K.gguf", n_ctx=2048)

# FAISS index init
embedding_size = 384  # dimension of MiniLM
index = faiss.IndexFlatL2(embedding_size)
documents = []

# === Load PDF & Chunk with Metadata + Optional Summarization ===
def add_document(path):
    global documents
    with fitz.open(path) as pdf:
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text = page.get_text()
            # Chunking
            splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            chunks = splitter.split_text(text)

            for chunk in chunks:
                if len(chunk) > 600:
                    chunk = summarizer(chunk, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
                metadata = f"[Page {page_num+1}]"
                documents.append((chunk, metadata))

    # Embed & index
    vectors = [embedder.encode(chunk + " " + meta) for chunk, meta in documents]
    index.add(np.array(vectors))


# === Search + Prompt Mistral ===
def ask_question(question, top_k=5):
    q_embedding = embedder.encode(question)
    D, I = index.search(np.array([q_embedding]), top_k)

    context = ""
    for idx in I[0]:
        chunk, meta = documents[idx]
        context += f"{meta}\n{chunk}\n\n"

    prompt = f"### Instruction:\nUse the context to answer the question.\n\n### Context:\n{context}\n\n### Question:\n{question}\n\n### Answer:\n"
    output = llm(prompt, max_tokens=512, stop=["###"])
    print("\n\033[92mAnswer:\033[0m", output["choices"][0]["text"].strip())


# === CLI ===
def main():
    while True:
        print("\n====== RAG CLI System (Mistral 7B Q6_K + FAISS) ======")
        print("1. Upload document (.txt/.pdf)")
        print("2. Ask a question")
        print("3. Exit")
        choice = input("Please select: ")

        if choice == '1':
            path = input("Enter path to document: ")
            if os.path.isfile(path):
                add_document(path)
                print("Document added successfully.")
            else:
                print("File not found.")

        elif choice == '2':
            if not documents:
                print("Please upload document first.")
                continue
            q = input("Ask your question: ")
            ask_question(q)

        elif choice == '3':
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
