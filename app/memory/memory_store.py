import chromadb

# initialize chroma client
client = chromadb.Client()

collection = client.get_or_create_collection(name="coach_memory")


def store_message(session_id, message, response):
    
    text = f"User: {message}\nAgent: {response}"

    collection.add(
        documents=[text],
        ids=[f"{session_id}-{hash(text)}"]
    )


def retrieve_memory(session_id, query):

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    docs = results.get("documents", [])

    if docs:
        return "\n".join(docs[0])

    return ""