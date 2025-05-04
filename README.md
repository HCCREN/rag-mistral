# rag_mistral.py
# Full English version of a Python RAG CLI system using Mistral 7B Q6_K and FAISS

<p align="center">
  <img src="https://raw.githubusercontent.com/HCCREN/rag-mistral-cli/main/banner.png" alt="RAG Mistral CLI Banner" width="100%">
</p>

<h1 align="center">🔍 RAG-Mistral-CLI | 文檔問答系統 (Mistral 7B + FAISS)</h1>

<p align="center">
  <b>Offline RAG-powered chatbot for PDFs and text documents, built with FAISS + Mistral 7B</b><br>
  離線文件問答系統，支援 PDF 與 TXT 文件，使用 FAISS + Mistral 7B GGUF 模型。
</p>

---

## 📦 Features | 功能特色

- 🧠 Powered by `Mistral 7B (GGUF Q6_K)` via `llama-cpp-python`
- 🔍 SentenceTransformer (`GTE-small`) embedding
- 💾 FAISS 向量搜尋資料庫
- 📄 支援 `.txt` 與 `.pdf` 文件上傳
- 💻 純 CPU 運行，完全離線，無需 GPU

---

## 🧰 Requirements | 環境需求

- Python 3.10+
- 安裝所需套件：

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use | 執行方式

```bash
python rag_mistral.py
```

執行後會看到 CLI 選單如下：

```
====== RAG CLI System (Mistral 7B Q6_K + FAISS) ======
1. Upload document (.txt/.pdf)
2. Ask a question
3. Exit
```

- 選 `1` 上傳 `.txt` 或 `.pdf` 文件
- 選 `2` 提問，系統會自動從資料中擷取內容作答

---

## 📥 Download Model | 模型下載

```bash
pip install huggingface_hub

huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.2-GGUF \
  mistral-7b-instruct-v0.2.Q6_K.gguf --local-dir ./models
```

> ✅ 模型請放入 `./models` 目錄，與 `rag_mistral.py` 同層。

---

## 🧪 Example | 使用範例

1. 上傳一份 PDF 或 TXT 文件（如 `manual.pdf`）
2. 提問：

```
What is the purpose of this document?
```

系統將擷取最相關段落並由 Mistral 模型回覆。

---

## ⚠️ Notes | 注意事項

- 請將以下檔案加入 `.gitignore` 避免洩露私密資料：

```
docs.index
docs.txt
models/
```

- 請勿上傳個資或機密資料文件

---

## 📄 License

Apache 2.0 License

---

## 🙌 Feedback | 回饋建議

If you like this project, ⭐ star it, fork it, or open an issue!

➡️ [Back to GitHub Repository](https://github.com/HCCREN/rag-mistral-cli)
