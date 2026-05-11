# 📚 Basic RAG Pipeline

A lightweight Retrieval-Augmented Generation (RAG) system that lets you ask natural language questions about your own research papers (PDFs).

---

## 🧠 How It Works

1. **Load** — Reads all PDFs from the `data/papers/` folder
2. **Chunk** — Splits documents into overlapping text chunks
3. **Embed** — Converts chunks into vector embeddings
4. **Index** — Stores embeddings in a FAISS vector store
5. **Retrieve** — Finds the most relevant chunks for your query
6. **Generate** — Passes retrieved context to an LLM to produce an answer

---

## 🗂️ Project Structure

```
rag-pipeline/
├── data/
│   └── papers/          # Place your PDF files here
├── src/
│   ├── load_document.py     # PDF loading logic
│   ├── chunk_text.py        # Text chunking
│   ├── create_embeddings.py # Embedding model + vector creation
│   ├── vector_store.py      # FAISS index creation
│   ├── retriever.py         # Similarity search
│   └── llm_generator.py     # LLM response generation
├── main.py                  # Entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-pipeline.git
cd rag-pipeline
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your PDFs

Drop your research paper PDFs into the `data/papers/` folder.

---

## 🚀 Usage

```bash
python main.py
```

You'll be prompted to enter a question:

```
Ask a question about your research papers: What are the main findings on transformer attention?
```

The system will return a generated answer along with the source chunks and page numbers used.

---

## 📄 Sample Output

```
================================================================================
USER QUERY
================================================================================
What are the main findings on transformer attention?

================================================================================
GENERATED ANSWER
================================================================================
According to the retrieved papers, transformer attention mechanisms...

================================================================================
SOURCES USED
================================================================================
1. paper1.pdf | Page 4 | Distance: 0.1823
2. paper2.pdf | Page 11 | Distance: 0.2041
```

---

## 🛠️ Configuration

| Parameter | Location | Default | Description |
|-----------|----------|---------|-------------|
| `top_k` | `main.py` | `8` | Number of chunks retrieved per query |
| Chunk size | `src/chunk_text.py` | — | Controls chunk length |
| Embedding model | `src/create_embeddings.py` | — | Model used for embeddings |

---

## 📦 Requirements

See `requirements.txt` for the full list. Key dependencies:
- `faiss-cpu` — Vector similarity search
- `sentence-transformers` or similar — Embedding model
- `PyMuPDF` / `pdfplumber` — PDF loading
- `openai` / `anthropic` / `ollama` — LLM backend

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📝 License

[MIT](https://choosealicense.com/licenses/mit/)
