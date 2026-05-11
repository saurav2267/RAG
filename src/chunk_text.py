# def chunk_text(text):
#     chunks = text.split("\n")
#     chunks = [chunk for chunk in chunks if chunk.strip() != ""]
#     return chunks


def chunk_documents(documents, chunk_size=500, overlap=100):
    chunks = []

    for doc in documents:
        words = doc["text"].split()
        start = 0

        while start < len(words):
            end = start + chunk_size
            chunk_text = " ".join(words[start:end])

            chunks.append({
                "source": doc["source"],
                "page": doc["page"],
                "text": chunk_text
            })

            start += chunk_size - overlap

    return chunks