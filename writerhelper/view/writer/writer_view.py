# -*- coding: utf-8 -*-
from django.shortcuts import render
from wirtermodels.models import Book

def saveBook(request):
    book = Book (name="《三体》")
    book.save()
    content = {}
    content['hello'] = "欢迎光临"
    content['message'] = "数据添加成功!"
    return render(request,"hellow.html" ,content)