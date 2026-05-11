# def load_document(file_path):
#     with open(file_path, "r", encoding="utf-8") as file:
#         return file.read()

import os
import re
import fitz  # PyMuPDF


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"Downloaded.*?Restrictions apply\.", "", text)
    text = re.sub(r"Authorized licensed use.*?", "", text)
    return text.strip()


def load_pdfs_from_folder(folder_path):
    documents = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            print(f"Loading PDF: {filename}")

            pdf = fitz.open(file_path)

            for page_number, page in enumerate(pdf, start=1):
                page_text = clean_text(page.get_text())

                if page_text:
                    documents.append({
                        "source": filename,
                        "page": page_number,
                        "text": page_text
                    })

            pdf.close()

    return documents
