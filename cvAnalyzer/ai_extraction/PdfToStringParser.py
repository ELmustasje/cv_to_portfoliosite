import PyPDF2


def extract_text(pdf_file_path):
    """
    Extract text from a PDF file.
    """
    text = ""

    with open(pdf_file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
            text += "\n"

    return text
