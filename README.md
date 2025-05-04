# README.md（根據最新版 Python 程式碼同步）

<p align="center">
  <img src="https://raw.githubusercontent.com/HCCREN/rag-mistral/main/banner1.png" alt="RAG Mistral CLI Banner" width="100%">
</p>

<h1 align="center">📚 RAG-Mistral-CLI | 高效離線文件問答系統</h1>

<p align="center">
  支援 PDF/TXT 文件，具備摘要處理、頁面標註、快速搜尋與本地化推論功能
</p>

---

## 🚀 Features | 功能特色

- 🧠 Mistral 7B (Q6_K, GGUF) with `llama-cpp-python`
- 🧾 Multi-page PDF reader + chunk splitter (`LangChain` `RecursiveCharacterTextSplitter`)
- 📝 Automatic summarization for long passages using `distilbart`
- 🔍 Vector search via FAISS with metadata-enhanced retrieval
- 📌 Answer includes source page numbers
- 💻 CPU only, fully offline, Windows compatible (Visual Studio required)

---

## 🧰 Requirements | 環境需求

- ✅ Python 3.10 (strongly recommended)
- ✅ CMake
- ✅ Visual Studio Build Tools 2022：
  - Windows 11 SDK
  - MSVC v143
  - Visual C++ and Visual Basic Build Tools

---

## 📦 Installation | 安裝

```bash
# Create venv
python -m venv env
env\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

> If `llama-cpp-python` build fails, use “x64 Native Tools Command Prompt for VS 2022”.

> 若安裝失敗，請改用「x64 Native Tools Command Prompt for VS 2022」。

---

## 🧠 Download the Model | 模型下載

```bash
pip install huggingface_hub
huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.2-GGUF \
  mistral-7b-instruct-v0.2.Q6_K.gguf --local-dir ./models
```

---

## 🏃 How to Use | 使用方式

```bash
python rag_mistral.py
```

Prompt menu:
```
====== RAG CLI System (Mistral 7B Q6_K + FAISS) ======
1. Upload document (.txt/.pdf)
2. Ask a question
3. Exit
```

---

## 📥 Upload & Ask | 上傳與提問

1. Upload your `.pdf` or `.txt` file — system will chunk + summarize + index
2. Ask natural language questions — you get relevant answers with page numbers

---

## 🔧 Advanced Tips | 進階技巧

- Use `RecursiveCharacterTextSplitter` for safe chunking with overlap
- Long paragraphs are auto-summarized before vectorizing
- FAISS vectors include `chunk + metadata (e.g. page info)`
- Top-k vector search for relevant context retrieval

---

## 📝 requirements.txt

```txt
faiss-cpu
PyMuPDF
langchain
sentence-transformers
transformers
llama-cpp-python
```

---

## ⚠️ Notes | 注意事項

- `.gitignore` 建議排除：
```txt
docs.index
docs.txt
models/
```
- Do not upload private or sensitive data
- 請勿上傳機密文件或個資

---

## 🧭 Roadmap | 開發規劃

- ✅ Improved CLI flow with page-tagged answers
- 📊 CSV export for Q&A history (TBD)
- 🌐 Web frontend (in progress)
- 🖼️ OCR/Visual PDF support via VDR (future)

---

## 📄 License
Apache 2.0

---

## 🙌 貢獻者
Made with ❤️ by [@HCCREN](https://github.com/HCCREN)
