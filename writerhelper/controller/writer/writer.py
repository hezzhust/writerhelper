# -*- coding: utf-8 -*-
from django.shortcuts import render
from wirtermodels.models import BookInfo

def saveBook(request):
    book = BookInfo (name="《三体》")
    book.save()
    content = {}
    content['hello'] = "欢迎光临"
    content['message'] = "数据添加成功!"
    return render(request,"hellow.html" ,content)