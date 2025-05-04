# 🔍 RAG-Mistral-CLI | 文檔問答系統 (Mistral 7B + FAISS)

A simple RAG (Retrieval-Augmented Generation) CLI chatbot built with:
- 🔎 SentenceTransformer for document embedding
- 💾 FAISS for vector search
- 🤖 Mistral 7B (GGUF Q6_K) via llama-cpp-python
- 📝 Supports `.txt` and `.pdf` documents

一個使用 Mistral 7B 模型與 FAISS 的文件問答系統，支援 CLI 操作與文件上傳。

---

## 🧰 Requirements | 環境需求

- Python 3.10
- CPU-only (no GPU required)
- `pip install -r requirements.txt`

需安裝 Python 3.10，並使用以下指令安裝套件：

```bash
pip install -r requirements.txt
