from ingest import ingest_documents
from chat import chat_with_llama
import os

def main():
    # STEP 1: Build the FAISS vector DB (only if it doesn't exist)
    if not os.path.exists("vectorstore/db/index.faiss"):
        print("[INFO] Vector DB not found. Ingesting PDF...")
        ingest_documents()
    else:
        print("[INFO] Vector DB already exists. Skipping ingestion.")

    # STEP 2: Chat loop
    print("\n🔁 You can now chat with your LLaMA3 chatbot.")
    print("💡 Type 'exit' or 'quit' to stop.\n")

    while True:
        query = input("🧠 You: ").strip()
        if query.lower() in ["exit", "quit"]:
            print("👋 Exiting. Goodbye!")
            break

        answer = chat_with_llama(query)
        print(f"🤖 Bot: {answer}\n")

if __name__ == "__main__":
    main()
