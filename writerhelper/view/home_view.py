# -*- coding: utf-8 -*-
from bson import json_util
from django.http import HttpResponse
from django.shortcuts import render
from wirtermodels.models import Book

import json



from django.views.decorators.csrf import csrf_exempt


def index(request):
    context ={}
    context['title'] = '首页'
    context['section_title'] = '欢迎使用写作助手！'
    return render(request, 'home.html', context)


# 获取书籍列表
@csrf_exempt
def query_book_List(request):
    book_list = query_books_from_db(request.POST)
    returnData = {}
    returnData["rows"] = []
    returnData["total"] = book_list.count()
    for book in book_list:
        dict = book.toDict()
        dict['create_time'] = book.create_time.strftime("%Y-%m-%d %H:%M")
        dict['modify_time'] = book.modify_time.strftime("%Y-%m-%d %H:%M")
        returnData["rows"].append(dict)
    return HttpResponse(json.dumps(returnData, default=json_util.default))


def query_books_from_db(params):
    limit = params.get('limit')
    offset = params.get('offset')
    order = params.get('order')
    ordername = params.get('ordername')
    bookname = params.get('bookname')
    author = params.get('author')
    starttime = params.get('starttime')
    endtime = params.get('endtime')
    result = Book.objects.filter()
    if bookname:
        result = result.filter(name__contains=bookname)
    if author:
        result = result.filter(authors__contains=author)
    if starttime:
        result = result.filter(create_time__gte= starttime)
    if endtime:
        result = result.filter(create_time__gte= starttime)

    if ordername:
        if order == 'desc':
            ordername = "-" + ordername
        result = result.order_by(ordername)
    return result[offset:offset+limit]