# rag_mistral.py
# Bilingual (EN + 中文) README for a Python RAG CLI system using Mistral 7B Q6_K and FAISS

<p align="center">
  <img src="https://raw.githubusercontent.com/HCCREN/rag-mistral-cli/main/banner.png" alt="RAG Mistral CLI Banner" width="100%">
</p>

<h1 align="center">🔍 RAG-Mistral-CLI | Document Q&A System (Mistral 7B + FAISS) | 文檔問答系統</h1>

<p align="center">
  <b>Offline RAG-powered chatbot for PDFs and text documents, built with FAISS + Mistral 7B</b><br>
  離線文件問答系統，支援 PDF 與 TXT 文件，使用 FAISS 與 Mistral 7B GGUF 模型。
</p>

---

## 📦 Features | 功能特色

- 🧠 Mistral 7B (GGUF Q6_K) via `llama-cpp-python`
- 🔍 Embedding with `SentenceTransformer (GTE-small)`
- 💾 Vector search with FAISS
- 📄 Supports `.txt` and `.pdf` documents
- 💻 CPU-only, runs fully offline

---

## 🧰 Requirements | 環境需求

- ✅ Python 3.10 (strongly recommended)
- ✅ CMake
- ✅ Visual Studio Build Tools 2022 with:
  - ✅ Windows 11 SDK (10.0.22000.0 or higher 可接受)
  - ✅ MSVC v143 - VS 2022 C++ x64/x86 build tools
  - ✅ **Visual C++ tools** and **Visual Basic build tools** (必要！)

- 安裝所需套件：

```bash
pip install -r requirements.txt
```

---

## 🛠 llama-cpp-python Installation (Windows 安裝指引 / English + 中文)

If you get build errors while installing `llama-cpp-python`, follow these steps:
若你在安裝 `llama-cpp-python` 遇到錯誤，請依下列步驟安裝：

```bash
# Create Python 3.10 virtual environment / 建立 Python 虛擬環境
python -m venv env
env\Scripts\activate

# Upgrade pip and install cmake / 更新 pip 並安裝 cmake
python -m pip install --upgrade pip
pip install cmake

# ✅ Install Visual Studio Build Tools (via installer)
# 必選項目：
# - ✅ Windows 10 或 Windows 11 SDK (>= 10.0.22000.0)
# - ✅ MSVC v143 (VS 2022 C++ x64/x86 build tools)
# - ✅ Visual C++ tools
# - ✅ Visual Basic build tools

# Run inside x64 Native Tools Command Prompt for VS 2022
# 使用「x64 Native Tools Command Prompt for VS 2022」執行下列：
pip install llama-cpp-python
```

> If you see `cl not found` or `CMake failed`, double-check you’re in the right build prompt.
> 若出現 `cl` 或 `cmake configuration failed` 錯誤，請確認你是用正確的命令列工具。

---

## 🚀 How to Use | 執行方式

```bash
python rag_mistral.py
```

You will see the CLI menu / 執行後會看到 CLI 選單：

```
====== RAG CLI System (Mistral 7B Q6_K + FAISS) ======
1. Upload document (.txt/.pdf)
2. Ask a question
3. Exit
```

- Option 1 上傳 `.txt` 或 `.pdf`
- Option 2 提問，系統會從文件中取出段落作答

---

## 📥 Download Model | 模型下載

```bash
pip install huggingface_hub

huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.2-GGUF \
  mistral-7b-instruct-v0.2.Q6_K.gguf --local-dir ./models
```

> ✅ Place the GGUF file in `./models` next to your script
> ✅ 模型請放入 `./models` 資料夾，與主程式同層

---

## 🧪 Example | 使用範例

1. Upload a document (e.g. `manual.pdf`)
2. Ask a question:

```
What is the purpose of this document?
```

System will retrieve the best-matching paragraph and generate an answer using Mistral.
系統會擷取段落並使用 LLM 回答

---

## ⚠️ Notes | 注意事項

- Add the following files to `.gitignore`:

```
docs.index
docs.txt
models/
```

- Avoid uploading sensitive or personal data
- 請勿上傳機密或個資

---

## 📄 License

Apache 2.0 License

---

## 🙌 Feedback | 回饋建議

If you like this project, ⭐ star it, fork it, or open an issue!
如果你喜歡這個專案，歡迎按星星、複製、提出建議！

➡️ [GitHub Repository](https://github.com/HCCREN/rag-mistral)
