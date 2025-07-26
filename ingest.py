# ingest.py

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
from config import PDF_PATH, DB_FAISS_PATH, CHUNK_SIZE, CHUNK_OVERLAP

def ingest_documents():
    loader = PyPDFLoader(PDF_PATH)
    pages = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    docs = splitter.split_documents(pages)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)

    os.makedirs(DB_FAISS_PATH, exist_ok=True)
    vectorstore.save_local(DB_FAISS_PATH)
    print("[INFO] Vector DB created and saved.")
