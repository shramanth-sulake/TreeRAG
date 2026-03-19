import fitz  # pymupdf

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []

    for i, page in enumerate(doc):
        text = page.get_text("text")

        pages.append({
            "page_number": i + 1,
            "text": text
        })

    return pages