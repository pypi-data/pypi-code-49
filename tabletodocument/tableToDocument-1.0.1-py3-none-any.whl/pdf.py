import tableToDocument.toDoc as toDoc
import PyPDF2

def write(toPdf):
    with open(toPdf.path,"rb") as p:
        pread = PyPDF2.PdfFileReader(p)
        txt = pread.getPage(5)
        txt.extractText()
