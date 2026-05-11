import numpy as np


def retrieve_chunks(query, model, index, chunks, top_k=8):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for distance, idx in zip(distances[0], indices[0]):
        results.append({
            "source": chunks[idx]["source"],
            "page": chunks[idx]["page"],
            "text": chunks[idx]["text"],
            "distance": float(distance)
        })

    return results