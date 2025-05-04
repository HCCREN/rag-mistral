# README.md（根據最新版 Python 程式碼同步）

<p align="center">
  <img src="https://raw.githubusercontent.com/HCCREN/rag-mistral-cli/main/banner1.png" alt="RAG Mistral CLI Banner" width="100%">
</p>

<h1 align="center">📚 RAG-Mistral-CLI | 高效離線文件問答系統</h1>

<p align="center">
  支援 PDF/TXT 文件，具備摘要處理、頁面標註、快速搜尋與本地化推論功能
</p>

---

## 🚀 功能總覽 | Features

- 🧠 Mistral 7B (Q6_K, GGUF) 本地 LLM via `llama-cpp-python`
- 🧾 PDF 多頁處理 + chunk 切割（使用 LangChain `RecursiveCharacterTextSplitter`）
- 📝 長段落自動摘要（`distilbart`）提升效率與準確性
- 🔍 內建 FAISS 向量資料庫支援 `top_k` 向量檢索
- 📌 每段回答皆附帶原始 PDF 頁碼來源
- 💻 離線運行、無需 GPU、支援 Windows（含安裝教學）

---

## 🧰 環境需求 | Requirements

- ✅ Python 3.10（強烈建議）
- ✅ CMake
- ✅ Visual Studio Build Tools 2022：
  - Windows 11 SDK
  - MSVC v143
  - Visual C++ 與 Visual Basic Build Tools

---

## 📦 安裝步驟 | Installation

```bash
# 建立虛擬環境
python -m venv env
env\Scripts\activate  # Windows

# 安裝套件
pip install -r requirements.txt
```

> 若安裝 `llama-cpp-python` 失敗，請使用「x64 Native Tools Command Prompt for VS 2022」執行。

---

## 🧠 模型下載 | Download Mistral Model

```bash
pip install huggingface_hub
huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.2-GGUF \
  mistral-7b-instruct-v0.2.Q6_K.gguf --local-dir ./models
```

---

## 🏃 使用方式 | How to Use

```bash
python rag_mistral.py
```

選單顯示如下：
```
====== RAG CLI System (Mistral 7B Q6_K + FAISS) ======
1. Upload document (.txt/.pdf)
2. Ask a question
3. Exit
```

---

## 📥 文件上傳與提問 | Upload & Ask

1. 輸入 PDF 或 TXT 檔路徑（自動切段/摘要/index）
2. 提問自然語言問題 → 回傳最佳答案段落 + 頁碼

---

## 🔧 進階技巧 | Advanced Tips

- `RecursiveCharacterTextSplitter` 用於安全分段，支援段落重疊
- 對長段落自動摘要，可提升回覆精度（避免稀釋向量）
- 向量編碼內容包括 chunk + metadata（如 page info）
- 向量搜尋支援 top_k=5~10 彈性設定

---

## 📝 requirements.txt 建議內容

```txt
faiss-cpu
PyMuPDF
langchain
sentence-transformers
transformers
llama-cpp-python
```

---

## ⚠️ 注意事項

- `.gitignore` 建議排除：
```txt
docs.index
docs.txt
models/
```
- 請勿上傳機密或個資

---

## 🧭 後續規劃 | Roadmap

- ✅ CLI 簡化流程與輸出排版
- 📊 支援 CSV 輸出問答記錄
- 📄 支援網頁前端版本（待開發）
- 📷 支援圖像 PDF 或 OCR（將採用 VDR）

---

## 📄 License
Apache 2.0

---

## 🙌 貢獻者
Made with ❤️ by [@HCCREN](https://github.com/HCCREN)
