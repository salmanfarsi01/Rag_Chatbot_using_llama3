from ingest import ingest_documents
from chat import chat_with_llama

def main():
    # STEP 1: Build the FAISS vector DB from your PDF
    ingest_documents()  # <-- run this ONLY ONCE

    # STEP 2: Ask a question
    query = input("Ask something: ")
    answer = chat_with_llama(query)
    print("\n💬 Answer:\n", answer)

if __name__ == "__main__":
    main()
