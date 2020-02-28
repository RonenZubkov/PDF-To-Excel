from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
import struct


def pdf_to_text(path):
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)
    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)
        text = retstr.getvalue()
        filepath.close()
        device.close()
        retstr.close()
    return text


def convertToFloat(line):
    return float(line.decode('utf-8', 'strict').replace(',', ''))

def init():
    text = pdf_to_text("pdfFiles/515813277_DOCUMENT_7_9290.pdf")
    text = text.splitlines()

    # Both Params Needed #
    afterTaxSum = ""
    orderNumber = ""

    for num, line in enumerate(text):
        # print('number of line:',num,'line is:',line.decode())
        if (line == b'\xd7\x9e"\xd7\xa2\xd7\x9e'):
            beforeTax = convertToFloat(text[num + 18])

        if (b':\xd7\xa8\xd7\xa4\xd7\xa1\xd7\x9e' in line):
            line = line.decode('utf-8').split(" ")
            orderNumber = line[0]

if __name__ == "__main__":
    init()


