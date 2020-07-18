#!/usr/bin/python3
import time
import os
from .hand import Hand
from .pdftool import PdfTool
from . import lyrics
import random
from atlas import settings

def lets_go(style, color):
    this_dir = settings.BASE_DIR +'/Mainapp/handright'
    print('imported necessary modules')
    svg_dst = this_dir+"/img/handright.svg"
    pdf_dst = this_dir+"/pdf/to_split.pdf"
    pdf_src = this_dir+"/pdf/upload.pdf"
    split_dst = settings.BASE_DIR + '/static/doc/to_serve.pdf'

    my_hand = Hand()
    pdfutil = PdfTool(svg_dst, pdf_src, pdf_dst, split_dst)

    lines = pdfutil.parse_input().split('\n')
    new_lines = []
    for line in lines:
        if line == ' ':
            new_lines.append('')
        else:
            new_lines.append(line)

    print(new_lines)

    colours = { 'Bl' : 'blue',
                'Bk' : 'black',
                'Rd' : 'red',
                'Gr' : 'green' }

    biases = [2.4 for i in lines]
    # styles = [1,3,5,7,8,9,10,12]
    styles = [style for i in lines]
    # stroke_widths = [1 for i in lines]
    # stroke_widths = [random.choice([1.0,1.2,1.1,1.3,1.4,1.5]) for i in lines]
    stroke_widths = [random.choice([1.0,1.2,1.1,1.3,1.4,1.5]) for i in lines]
    stroke_colors = [colours[color] for i in lines]
    # styles = np.cumsum(np.array([len(i) for i in lines]) == 0).astype(int)

    print("writing by hand")

    my_hand.write(
        filename = svg_dst,
        lines = new_lines,
        biases = biases,
        styles = styles,
        stroke_colors = stroke_colors,
        stroke_widths = stroke_widths
    )

    print("done writing, cutting into A4 sheets")

    pdfutil.svg_to_pdf()
    pdfutil.split_pages()


