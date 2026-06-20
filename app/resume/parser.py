import pdfplumber

from docx import Document


class ResumeParser:

    @staticmethod
    def parse_pdf(
        file_path: str
    ) -> str:

        text = ""

        with pdfplumber.open(
            file_path
        ) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text + "\n"

        return text

    @staticmethod
    def parse_docx(
        file_path: str
    ) -> str:

        document = Document(
            file_path
        )

        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

        return text