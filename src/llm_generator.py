import requests


def generate_response(query, retrieved_chunks):
    context_blocks = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        context_blocks.append(
            f"[Source {i}]\n"
            f"Paper: {chunk['source']}\n"
            f"Page: {chunk['page']}\n"
            f"Text: {chunk['text']}"
        )

    context = "\n\n".join(context_blocks)

    prompt = f"""
You are a research assistant.

Answer the user's question using ONLY the provided context.

Rules:
- Be concise.
- Do not invent information.
- If the context does not contain enough information, say so.
- When listing datasets, group them by paper when possible.
- Include source paper name and page number.

Context:
{context}

Question:
{query}

Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]