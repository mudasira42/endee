from sentence_transformers import SentenceTransformer
from endee_vector_store import EndeeVectorStore

# Initialize embedding model and Endee vector database
model = SentenceTransformer("all-MiniLM-L6-v2")
db = EndeeVectorStore()

# Knowledge base (documents)
documents = [
    # --- Endee ---
    "Endee is a high-performance vector database written in C++.",
    "Endee is designed to store vector embeddings and perform fast similarity search.",
    "Endee acts as the vector database layer in AI applications such as RAG systems.",

    # --- Vector Databases ---
    "Vector databases store numerical embeddings instead of traditional rows and columns.",
    "Vector similarity search compares embeddings using metrics like cosine similarity.",
    "Vector databases enable semantic retrieval rather than keyword-based search.",

    # --- Semantic Search ---
    "Semantic search retrieves documents based on contextual meaning.",
    "Embeddings capture semantic relationships between words and sentences.",

    # --- RAG ---
    "RAG stands for Retrieval Augmented Generation.",
    "RAG systems retrieve relevant context before generating responses."
]

# Store documents as vectors in Endee
for doc in documents:
    db.insert(model.encode(doc), doc)

print("🤖 Endee RAG Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    # 🔹 RETRIEVAL STEP (vector search)
    query_vector = model.encode(user_input)
    retrieved = db.search(query_vector, top_k=2)

    retrieved_texts = [text for _, text in retrieved]

    # 🔹 GENERATION STEP (simple but valid)
    answer = " ".join(retrieved_texts)

    print("\nBot (RAG response):")
    print(answer)
    print()
