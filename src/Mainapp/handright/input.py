from PyPDF2 import PdfFileReader
pdf_fileobj = open('./pdf/STM.pdf', 'rb')
pdf_read = PdfFileReader(pdf_fileobj)
no_of_pages = pdf_read.getNumPages()
lines = ""
counter = 1
for page_no in range(no_of_pages):
    pageobj = pdf_read.getPage(page_no)
    text = pageobj.extractText() 
    text = text.split("\n")
    for line in text:
            count = 1 
            while len(line) > 75*count:
                line = line[:75*count] + "\n" + line[75*count:]
                count += 1 
            lines += '\n' + line
            counter += 1

print(lines)
