# -*- coding: utf-8 -*-
import datetime
import uuid

from bson import json_util
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from wirtermodels.models import Book

import pytz
import json


tzone = pytz.timezone(settings.TIME_ZONE)


def index(request):
    context ={}
    context['title'] = '首页'
    context['section_title'] = '欢迎使用写作助手！'
    return render(request, 'home.html', context)

@csrf_exempt
def batch_delete_book(request):
    ids = request.POST.getlist('ids[]')
    if ids:
        Book.objects.filter(id__in=ids).update(status = -1)
    return HttpResponse(json.dumps({"msg": '删除成功!',"code": 1}))

@csrf_exempt
def delete_book(request):
    id = request.POST.get('id')
    if id:
        book = Book.objects.get(id=id)
        book.status = -1
        book.save()
    return HttpResponse(json.dumps({"msg": '删除成功',"code": 1}))


@csrf_exempt
def get_book_detail(request):
    id = request.POST.get('id')
    if id:
        book = Book.objects.get(id = id)
        if book:
            dict = book.toDict()
            # dict['id'] = str(book.id)
            if book.create_time:
                dict['create_time'] = book.create_time.strftime("%Y-%m-%d %H:%M %Z")
            if book.modify_time:
                dict['modify_time'] = book.modify_time.strftime("%Y-%m-%d %H:%M %Z")
            return HttpResponse(json.dumps({"msg": '查询成功','data':dict, "code": 1}))
    return HttpResponse(json.dumps({"msg": '查询失败',"code": -1}))
    pass


@csrf_exempt
def save_book(request):
    args = request.POST
    id = args.get('id')
    authors = args.get('authors')
    chapter_count = args.get('chapter_count')
    name = args.get('name')
    if id:
        book = Book.objects.get(id = id)
    else:
        book = Book()
        book.create_time = timezone.now()

    book.authors = authors
    book.chapter_count = chapter_count
    book.modify_time = timezone.now()
    book.name = name
    book.save()
    book.refresh_from_db()
    return HttpResponse(json.dumps({"msg": '保存成功','id':str(book.id), "code": 1}))



# 获取书籍列表
@csrf_exempt
def query_book_list(request):
    returnData = {}
    returnData["rows"] = []
    book_list, returnData["total"] = query_books_from_db(request.POST)
    for book in book_list:
        dict = book.toDict()
        # dict['id'] = str(book.id)
        if book.create_time:
            dict['create_time'] = book.create_time.astimezone(tzone).strftime("%Y-%m-%d %H:%M %Z")
        if book.modify_time:
            dict['modify_time'] = book.modify_time.astimezone(tzone).strftime("%Y-%m-%d %H:%M %Z")
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
    result = result.filter(status__gt=-1)
    count = result.count()
    if ordername:
        if order == 'desc':
            ordername = "-" + ordername
        result = result.order_by(ordername)
    return result[offset:offset+limit],count