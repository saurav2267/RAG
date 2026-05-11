from src.load_document import load_pdfs_from_folder
from src.chunk_text import chunk_documents
from src.create_embeddings import create_embeddings, model
from src.vector_store import create_vector_store
from src.retriever import retrieve_chunks
from src.llm_generator import generate_response


documents = load_pdfs_from_folder("data/papers")

chunks = chunk_documents(documents)

print(f"\nTotal chunks created: {len(chunks)}")

embeddings = create_embeddings(chunks)

index = create_vector_store(embeddings)

query = input("\nAsk a question about your research papers: ")

retrieved_chunks = retrieve_chunks(
    query=query,
    model=model,
    index=index,
    chunks=chunks,
    top_k=8
)

answer = generate_response(query, retrieved_chunks)

print("\n" + "=" * 80)
print("USER QUERY")
print("=" * 80)
print(query)

print("\n" + "=" * 80)
print("GENERATED ANSWER")
print("=" * 80)
print(answer)

print("\n" + "=" * 80)
print("SOURCES USED")
print("=" * 80)

for i, chunk in enumerate(retrieved_chunks, start=1):
    print(f"{i}. {chunk['source']} | Page {chunk['page']} | Distance: {chunk['distance']:.4f}")