from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from PyPDF2 import PdfFileReader
from .handright.main import *
import os
import time
from atlas import settings

def home(request):
    return render(request,"index.html",{})

def forminput(request):
    if request.method=='POST':
        dic = dict(request.POST)
        fl = request.FILES['pdf']
        filename = settings.BASE_DIR +'/Mainapp/handright/pdf/upload.pdf'
        with open(filename,'wb+') as handle:
            for chunk in fl.chunks():
                handle.write(chunk)
        # print(settings.pdf_file['pdf'].read())
        request.session['writing_style'] =[int(dic['style'][0]), dic['color'][0]] 
        return render(request, "loading.html", {'load' : True})
    return render(request,"index.html",{})

def ML(request):
    data = request.session.get('writing_style')
    style = data[0]
    color = data[1]
    # fl = settings.pdf_file['pdf']
    # print(fl.read())
    lets_go(style, color)
    return render(request, "loaded.html", {})
