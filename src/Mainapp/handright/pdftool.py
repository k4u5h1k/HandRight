#!/usr/bin/python3
import cairosvg
import copy
import math
from PyPDF2 import PdfFileReader, PdfFileWriter
# cairosvg.svg2pdf(url='./img/all_star.svg', write_to='my_pdf8.pdf')

class PdfTool():
    def __init__(self,svg,pdf_src,pdf_dst,split_dst):
        self.svg_src = svg
        self.pdf_src = pdf_src
        self.pdf_dst = pdf_dst
        self.split_dst = split_dst

    def parse_input(self):
        pdf_fileobj = open(self.pdf_src, 'rb')
        pdf_read = PdfFileReader(pdf_fileobj)
        no_of_pages = pdf_read.getNumPages()
        lines = ""

        for page_no in range(no_of_pages):
            pageobj = pdf_read.getPage(page_no)
            text = pageobj.extractText() 
            text = text.split('\n')
            for line in text:
                    count = 1 
                    while len(line) > 75*count:
                        line = line[:75*count] + "\n" + line[75*count:]
                        count += 1 
                    lines += '\n' + line
                
        return lines


    def svg_to_pdf(self):
        cairosvg.svg2pdf(url = self.svg_src, write_to = self.pdf_dst)

    def split_pages(self):
        src_f = open(self.pdf_dst, 'r+b')
        dst_f = open(self.split_dst, 'w+b')

        inp = PdfFileReader(src_f)
        output = PdfFileWriter()
        has_not_ran_once = True

        while has_not_ran_once or x4 > x3*1.41:
            pp = inp.getPage(0) if output.getNumPages() == 0 else q
            p = copy.copy(pp)
            q = copy.copy(pp)

            # the new media boxes are the previous crop boxes
            p.mediaBox = copy.copy(p.cropBox)
            q.mediaBox = copy.copy(p.cropBox)

            x1, x2 = pp.mediaBox.lowerLeft
            x3, x4 = pp.mediaBox.upperRight

            x1, x2 = math.floor(x1), math.floor(x2)
            x3, x4 = math.floor(x3), math.floor(x4)
            x5 = math.floor(x4-math.floor(x3*1.41))

            p.mediaBox.upperRight = (x3, x4)
            p.mediaBox.lowerLeft = (x1, x5)

            q.mediaBox.upperRight = (x3, x5)
            q.mediaBox.lowerLeft = (x1, x2)

            p.artBox = p.mediaBox
            p.bleedBox = p.mediaBox
            p.cropBox = p.mediaBox

            q.artBox = q.mediaBox
            q.bleedBox = q.mediaBox
            q.cropBox = q.mediaBox

            if has_not_ran_once:
                output.addPage(p)
                output.addPage(q)
                has_not_ran_once = False 
            else:
                new_output = PdfFileWriter()
                for i in range(output.getNumPages()-1):
                    new_output.addPage(output.getPage(i))
              
                new_output.addPage(p)
                if q.getContents() is not None:
                    new_output.addPage(q)
                output = new_output
             


        output.write(dst_f)
        src_f.close()
        dst_f.close()

