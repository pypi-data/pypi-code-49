from PyPDF2 import PdfFileReader
from PyPDF2.utils import PdfReadError


class PDFReader:
    def run(self, file):
        input1 = PdfFileReader(file)
        try:
            num_pages = input1.getNumPages()
        except PdfReadError as err:
            raise PdfReadError(f"O arquivo {file} está protegido com senha. \n {err}")

        pages = ''
        for i in range(0, num_pages):
            page = input1.getPage(i)
            page_text = page.extractText()
            pages += page_text

        return pages
