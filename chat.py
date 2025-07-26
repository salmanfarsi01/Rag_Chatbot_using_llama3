# chat.py

from retriever import get_relevant_chunks
from model import call_ollama

def chat_with_llama(query):
    context = get_relevant_chunks(query)
    prompt = f"""You are a helpful assistant. Use the context below to answer the question.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"""
    
    response = call_ollama(prompt)
    return response
