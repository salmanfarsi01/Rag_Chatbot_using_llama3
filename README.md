# 🧠 RAG Chatbot with Ollama (LLaMA 3), FAISS & HuggingFace

This project implements a lightweight **Retrieval-Augmented Generation (RAG)** chatbot using the `llama3` model via [Ollama](https://ollama.com/), `FAISS` for vector search, and `HuggingFaceEmbeddings` for semantic search — all powered locally.

## 📦 Features

- Offline-capable chatbot using **LLaMA 3 via Ollama**
- PDF ingestion and semantic chunking
- **FAISS** vector store for fast similarity search
- `all-MiniLM-L6-v2` embeddings for efficient query matching
- Lightweight and modular — ideal for local RAG prototyping

## 📁 Project Structure

.
├── chat.py # Builds the prompt with relevant context
├── config.py # Global configs and paths
├── ingest.py # PDF ingestion & vector DB generation
├── retriever.py # Semantic retrieval using FAISS
├── model.py # Calls the Ollama LLaMA 3 model
├── main.py # Entry point for CLI interaction
├── requirements.txt # Dependencies
└── data/
└── ai.pdf # Your source document

## 🚀 Getting Started

### 1. Install Dependencies

pip install -r requirements.txt
2. Run Ollama (LLaMA 3)
Install Ollama and start the LLaMA 3 model:

bash
Copy
Edit
ollama run llama3
This will expose a local API at http://localhost:11434.

3. Ingest PDF
Make sure your ./data/ai.pdf file is in place, then:

bash
Copy
Edit
python main.py
This will:

Parse the PDF

Split it into chunks

Embed it using all-MiniLM-L6-v2

Save vectors to local FAISS DB

Launch a CLI prompt for questions

🧠 How It Works
ingest.py reads and splits the PDF.

Chunks are embedded using HuggingFaceEmbeddings and stored in FAISS.

When you ask a question:

Top-k relevant chunks are retrieved.

These are formatted with your query and sent to LLaMA 3 via Ollama.

The model returns an answer grounded in your PDF context.

⚙️ Configuration
All settings live in config.py:

python
Copy
Edit
PDF_PATH = "./data/ai.pdf"
DB_FAISS_PATH = "./vectorstore/db"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3"
🧪 Example
bash
Copy
Edit
Ask something: What are the main challenges in artificial intelligence?
💬 Answer (from LLaMA 3): "...based on the document, the main challenges are..."

📝 Requirements
See requirements.txt. Key libraries:

langchain

faiss-cpu

sentence-transformers

transformers

torch

pypdf

🛠️ Notes
⚠️ ingest_documents() should only be run once unless the source PDF changes.

Use allow_dangerous_deserialization=True cautiously — only for trusted sources.

You can replace the embedding model or vector store as needed.
