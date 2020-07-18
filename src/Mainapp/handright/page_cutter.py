#!/usr/bin/python3
import copy
import math
from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pages2(src, dst):
    src_f = open(src, 'r+b')
    dst_f = open(dst, 'w+b')

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
            print(p.getContents())
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

if __name__=="__main__":
    split_pages2("./pdf/to_split.pdf","./new_split.pdf")
