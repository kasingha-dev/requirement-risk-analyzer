import pdfplumber


class FileProcessor:

    @staticmethod
    def extract_text(uploaded_file):
        filename = uploaded_file.filename.lower()

        if filename.endswith(".txt"):
            return uploaded_file.file.read().decode("utf-8")

        if filename.endswith(".pdf"):
            text = ""

            with pdfplumber.open(uploaded_file.file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

            return text

        return ""

    @staticmethod
    def merge_documents(documents):
        return "\n\n".join(documents) 